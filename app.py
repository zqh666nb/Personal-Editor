from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import io
import matplotlib.pyplot as plt
import base64
from collections import defaultdict
from datetime import datetime


app = Flask(__name__)
filename = 'expenses.json'

# 加载数据
def load_data():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

# 保存数据
def save_data(data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_record', methods=['POST'])
def add_record():
    date = request.form['date']
    amount = float(request.form['amount'])
    record_type = request.form['type']  # 获取用户选择的类型

    # 根据类型调整金额的正负
    if record_type == 'expense':
        amount = -abs(amount)  # 将支出金额设置为负值

    category = request.form['category']
    note = request.form['note']
    
    data = load_data()
    record = {
        'date': date,
        'amount': amount,
        'category': category,
        'note': note
    }
    data.append(record)
    save_data(data)
    
    return redirect(url_for('view_records'))


@app.route('/view_records')
def view_records():
    data = load_data()
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
    return render_template('records.html', records=sorted_data)

@app.route('/monthly_statistics')
def monthly_statistics():
    data = load_data()
    monthly_stats = defaultdict(lambda: {'income': 0, 'expenses': 0})

    for record in data:
        date = record['date']
        amount = record['amount']
        month = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m')  # 获取月份字符串

        if amount > 0:
            monthly_stats[month]['income'] += amount
        else:
            monthly_stats[month]['expenses'] += abs(amount)  # 记录为正值
     # 对monthly_stats进行排序，确保按月份顺序显示
    sorted_monthly_stats = dict(sorted(monthly_stats.items(), key=lambda item: datetime.strptime(item[0], '%Y-%m')))
    # 将排序后的结果传递给模板
    return render_template('monthly_statistics.html', stats=sorted_monthly_stats)

@app.route('/statistics')
def statistics():
    data = load_data()
    income = sum(record['amount'] for record in data if record['amount'] > 0)
    expenses = sum(record['amount'] for record in data if record['amount'] < 0)
    return jsonify({'total_income': income, 'total_expenses': expenses})
@app.route('/line_chart')
def generate_line_chart():
    data = load_data()
    if not data:
        return render_template('line_chart.html', chart_url=None)

    monthly_stats = defaultdict(lambda: {'income': 0, 'expenses': 0, 'profit': 0})

    for record in data:
        date = record['date']
        amount = record['amount']
        month = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m')  # 获取月份字符串

        if amount > 0:
            monthly_stats[month]['income'] += amount
        else:
            monthly_stats[month]['expenses'] += abs(amount)  # 记录为正值
        monthly_stats[month]['profit'] = monthly_stats[month]['income'] - monthly_stats[month]['expenses']

    months = list(monthly_stats.keys())
    incomes = [monthly_stats[month]['income'] for month in months]
    expenses = [monthly_stats[month]['expenses'] for month in months]
    profits = [monthly_stats[month]['profit'] for month in months]

    plt.figure(figsize=(10, 6))
    plt.plot(months, incomes, label='Total Income', marker='o')
    plt.plot(months, expenses, label='Total Expenses', marker='o')
    plt.plot(months, profits, label='Profit', marker='o')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Monthly Statistics')
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    return render_template('line_chart.html', chart_url=chart_url)


if __name__ == "__main__":
    app.run(debug=True)

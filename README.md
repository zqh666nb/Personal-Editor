# 个人记账本应用

## 简介

个人记账本应用是一款简单易用的网页记账工具，用户可以记录和管理自己的收入与支出。该应用通过 Flask 框架构建后端，使用 HTML、CSS 和 JavaScript 实现前端界面，并能够将数据以 JSON 格式保存到本地文件中，便于后续查看和统计。

## 特性

- **基础记账**：记录每笔支出和收入，包括日期、金额、类别和备注。
- **查看数据**：用户可以查看最近的几笔记录。
- **收支统计**：根据日期、类别和金额查看总支出和收入情况。
- **用户友好型界面**：简洁直观的用户界面，易于操作。
- **数据保存**：使用 JSON 文件保存用户数据，支持数据持久化。
- **简单图表展示**（可选）：提供基本的图表功能，帮助用户直观地了解财务状况。

## 技术栈

- **后端**：Python（Flask 框架）
- **前端**：HTML、CSS 和 JavaScript
- **数据存储**：JSON 文件

## 文件结构

- project/
- │
- ├── app.py                 # Flask 应用的主文件
- ├── expenses.json          # 数据存储文件
- ├── requirements.txt       # Python 依赖库列表
- └── templates/             # 存放 HTML 模板的文件夹
- ├── index.html        # 主页面模板
- ├── records.html      # 记录页面模板
- └── monthly_statistics.html # 月度统计页面模板

## 安装

### 先决条件

- Python 3.x
- pip（Python 包管理工具）

### 克隆项目

```bash
git clone https://github.com/zqh666nb/Personal-Editor
cd bookkeeping

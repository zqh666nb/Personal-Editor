# 个人记账本应用

## 简介

个人记账本应用是一款简单易用的网页记账工具，用户可以记录和管理自己的收入与支出。该应用通过 Flask 框架构建后端，使用 HTML、CSS 实现前端界面，并能够将数据以 JSON 格式保存到本地文件中，便于后续查看和统计。

## 特性

- **基础记账**：记录每笔支出和收入，包括日期、金额、类别和备注。
- **查看数据**：用户可以查看最近的几笔记录。
- **收支统计**：根据日期、类别和金额查看总支出和收入情况。
- **用户友好型界面**：简洁直观的用户界面，易于操作。
- **数据保存**：使用 JSON 文件保存用户数据，支持数据持久化。
- **简单图表展示**（可选）：提供基本的图表功能，帮助用户直观地了解财务状况。

## 技术栈

- **后端**：Python（Flask 框架）
- **前端**：HTML、CSS 
- **数据存储**：JSON 文件

## 文件结构
project/
│
├── app.py                   # Flask 应用的主文件
├── expenses.json            # 数据存储文件
├── requirements.txt         # Python 依赖库列表
│
├── static/                  # 存放静态文件的文件夹
│   ├── index2.css           # 主页面的样式文件
│   ├── line_chart.css       # 折线图页面的样式文件
│   └── style.css            # 通用样式文件
│
└── templates/               # 存放 HTML 模板的文件夹
    ├── index.html           # 主页面模板
    ├── line_chart.html      # 折线图页面模板
    ├── monthly_statistics.html # 月度统计页面模板
    └── records.html         # 记录页面模板

##程序运行环境

### 1. 安装 Python

确保你已经在系统上安装了 Python 3.x。可以在 [Python 官方网站](https://www.python.org/downloads/) 下载适合你操作系统的安装包。

#### 检查 Python 安装

在终端或命令提示符中输入以下命令，检查 Python 是否已安装：


python --version

或

python3 --version


如果没有安装，你可以按照说明进行安装。

### 2. 安装 pip

pip 是 Python 的包管理工具，通常在安装 Python 时会自动安装。你可以通过以下命令检查 pip 是否已安装：

pip --version

如果未安装，可以通过以下方式安装：


python -m ensurepip --upgrade



### 4. 安装项目
克隆github项目<https://github.com/zqh666nb/Personal-Editor>


### 5. 运行 Flask 应用
在编译器（推荐vscode）中打开该项目文件，根据requirements.txt中的要求安装好相应的库，然后可以在终端中打开文件运行app.py

### 6. 访问应用

打开浏览器，访问 `http://localhost:5000` 查看应用。

### 总结
通过上述步骤，你可以成功设置一个 Python 程序的运行环境。根据项目需求，可以添加其他库和工具。确保在开发过程中保持虚拟环境的激活状态，以便使用正确的依赖库。
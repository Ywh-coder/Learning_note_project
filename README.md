# Learning Notes

一个基于 Django 的学习笔记管理应用，帮助用户按主题分类记录和管理学习笔记。支持用户注册、登录、注销，以及对学习主题和条目的增删改查。

## 功能特性

- **用户认证**：注册 / 登录 / 注销（基于 Django 内置 auth 系统）
- **主题管理**：创建、查看学习主题列表，每个主题独立归属
- **条目管理**：在主题下添加、编辑学习笔记条目
- **权限控制**：只能查看和操作自己的内容
- **响应式 UI**：基于 Bootstrap 5 样式

## 技术栈

| 项 | 版本 |
|---|---|
| Python | 3.13.5 |
| Django | 6.1.1 |
| django-bootstrap5 | 26.3 |
| 数据库 | SQLite（内置，无需额外配置） |

## 项目结构

\`\`\`
learning_note/
├── ll_project/          # Django 项目配置
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── learning_notes/      # 核心应用：主题与条目管理
│   ├── models.py        # Topic、Entry 模型
│   ├── views.py         # 首页、主题、条目 CRUD 视图
│   ├── forms.py         # TopicForm、EntryForm
│   └── templates/
│       └── learning_notes/
│           ├── base.html
│           ├── index.html
│           ├── topics.html
│           ├── topic.html
│           ├── new_topic.html
│           ├── new_entry.html
│           └── edit_entry.html
├── accounts/            # 认证应用
│   ├── views.py         # 注册视图
│   ├── urls.py          # 包含 django.contrib.auth.urls
│   └── templates/
│       └── registration/
│           ├── login.html
│           └── register.html
└── manage.py
\`\`\`

## 快速开始

### 1. 创建并激活虚拟环境

\`\`\`bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
# 或
source .venv/Scripts/activate   # macOS / Linux
\`\`\`

### 2. 安装依赖

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. 数据迁移

\`\`\`bash
python manage.py migrate
\`\`\`

### 4. 创建超级用户（可选，用于访问后台管理）

\`\`\`bash
python manage.py createsuperuser
\`\`\`

### 5. 启动开发服务器

\`\`\`bash
python manage.py runserver
\`\`\`

访问 http://127.0.0.1:8000/ 即可使用。

## 使用说明

1. **注册**：点击首页 "Register(注册)" 创建账号
2. **登录**：登录后可以创建主题、添加条目
3. **注销**：右上角 "Log out" 按钮退出登录
4. **管理后台**：访问 /admin/ 使用超级用户管理数据

## URL 路由

| 路径 | 视图名 | 说明 |
|---|---|---|
| \`/\` | \`index\` | 欢迎首页 |
| \`/topics/\` | \`topics\` | 所有主题列表 |
| \`/topic<id>/\` | \`topic\` | 单个主题及条目 |
| \`/new_topic/\` | \`new_topic\` | 新建主题 |
| \`/new_entry/<topic_id>/\` | \`new_entry\` | 添加条目 |
| \`/edit_entry/<entry_id>/\` | \`edit_entry\` | 编辑条目 |
| \`/login/\` | \`LoginView\` | 登录 |
| \`/logout/\` | \`LogoutView\` | 注销 |
| \`/register/\` | \`register\` | 注册 |
| \`/admin/\` | Django Admin | 管理后台 |

## License

MIT

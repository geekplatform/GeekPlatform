# Geek Platform For Syclover

---
## 概述
#### 环境
- Python 3.7.x
- Django 2.1.5
- Mysql（必须5.6版本以上）
    - 端口：3306
    - 帐号：root
    - 密码：root
- pymysql
#### 准备
- 开发前先在你的mysql下创建一个名为Geek的数据库，这是Django基本库。然后使用以下命令迁移即可正常启动开发
```python
python manage.py makemigrations
python manage.py migrate
```
- **管理员帐号密码都是admin**
#### APP
目前创建了两个app
- account
    - 登录
    - 注册
    - 信息修改
    - 队伍
    - 密码修改
- challenge

---

## 更新
#### 2019-07-15

已配置好所有准备环境


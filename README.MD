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
#### 2019-07-15（9：00）

- 已配置好所有准备环境

#### 2019-07-15（21：00）

- 已该公共部分
    - Geek的urls.py填加了accountsApp的路由

- 目前已创建数据库
    - Teams(记录队伍信息数据库)
- 目前已实现功能
    - 队伍登录
    - 队伍注册
    - 队伍信息
---


#### 2019-07-16 (21:55)

- 公共部分
    - Geek下的setting.py增加了LOGIN_URL参数
- 增加表
    - author(出题人),challenge(问题及相关信息),Category(该题分类)
- 目前已实现功能
    - 题目相关处理
    
---
### 2019-07-19
- 创建一个文件，forms.py，用来自定义表单。
    - 扩展创建用户表单
    - 扩展修改信息表单
- 目前已实现功能
    - 队伍登录
    - 队伍注册
    - 队伍信息
    - 队伍信息修改
---

### 2019-7-22
- 没写视图的公告     (数据库又崩了)


---

### 2019-7-24
- 那个公告我只写了model,不用再开一个app吧
- flag的提交
- scoreborad的在各种分类下的呈现
    - 请确保先在category中建一个所有种类的数据，并确保其id为1


### 2019-7-25
- 已经做好主页的效果
- base.html也做好了,想要加路由按照里面的格式加就可以了。
    - 在accounts/templates/base.html
- 创建一个static文件夹，用来存储静态文件，如css，js
- 登录和注册的前端写好例框架，细节没处理，如错误提示，细节美化没做。

---
### 2019-7-26
- 公告的完善(支持markdown，由于我的环境没切，所有请先 pip install markdown 再更新下 pip freeze > requirements.txt)
- 那些队伍完成的具体情况
- 增加了文件上传模块


### 2019-7-26
- 前端做好页面
    - 主页
    - 登录(细节待完善)
    - 注册(细节待完善)
    - 修改队伍信息(细节待完善)
    - 修改密码(细节待完善)

### 2019-7-26
- 改变了scoreboard为路由式 /scoreboard/1/SECRET
    - 1-all
    - 2-web
    - 3-...
    - secret对了才能显示新生

 

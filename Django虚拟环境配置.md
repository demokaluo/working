## Django

谈谈pythonweb框架: 

​	--Django,大而全,重武器,内部提供:ORM,Admin,中间件,Form,MOdelFrom,Session,缓存,信号,CSRF

```
安装虚拟环境:pip install virtualenv
虚拟环境包管理工具:pip install virtualenvwrapper-win
```

#### `virtualenvwrapper`基本使用：

1. 创建虚拟环境：

   ```
    mkvirtualenv my_env  这个是按照默认python版本创建的   
    如果想 创建 python2.7版本的  
    
    mkvirtualenv --python==c:\Python27\python.exe 虚拟环境的名字
   ```

   那么会在你当前用户下创建一个`Env`的文件夹，然后将这个虚拟环境安装到这个目录下。 如果你电脑中安装了`python2`和`python3`，并且两个版本中都安装了`virtualenvwrapper`，那么将会使用环境变量中第一个出现的`Python`版本来作为这个虚拟环境的`Python`解释器。

2. 切换到某个虚拟环境：

   ```
    workon my_env
   ```

3. 退出当前虚拟环境：

   ```
    deactivate
   ```

4. 删除某个虚拟环境：

   ```
    rmvirtualenv my_env
   ```

5. 列出所有虚拟环境：

   ```
    lsvirtualenv
   ```

6. 进入到虚拟环境所在的目录：

   ```
    首先切换到该虚拟环境
    cdvirtualenv
   ```

## 创建第一个项目

使用 django-admin.py 来创建 HelloWorld 项目：

```
django-admin.py startproject HelloWorld
```

创建完成后我们可以查看下项目的目录结构：

```
$ cd HelloWorld/
$ tree
.
|-- HelloWorld
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

目录说明：

- **HelloWorld:** 项目的容器。
- **manage.py:** 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
- **HelloWorld/__init__.py:** 一个空文件，告诉 Python 该目录是一个 Python 包。
- **HelloWorld/asgi.py:** 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目。
- **HelloWorld/settings.py:** 该 Django 项目的设置/配置。
- **HelloWorld/urls.py:** 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
- **HelloWorld/wsgi.py:** 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

接下来我们进入 HelloWorld 目录输入以下命令，启动服务器：

```
python3 manage.py runserver 0.0.0.0:8000
```

0.0.0.0 让其它电脑可连接到开发服务器，8000 为端口号。如果不说明，那么端口号默认为 8000。


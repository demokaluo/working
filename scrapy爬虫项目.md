#### scrapy爬虫框架

### 一. 新建项目(scrapy startproject)

在开始爬取之前，必须创建一个新的Scrapy项目。进入自定义的项目目录中，运行下列命令：

```
scrapy startproject mySpider
```

其中， mySpider 为项目名称，可以看到将会创建一个 mySpider 文件夹，目录结构大致如下：

下面来简单介绍一下各个主要文件的作用：

```
mySpider/
    scrapy.cfg
    mySpider/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            ...
```

这些文件分别是:

- scrapy.cfg: 项目的配置文件。
- mySpider/: 项目的Python模块，将会从这里引用代码。
- mySpider/items.py: 项目的目标文件。
- mySpider/pipelines.py: 项目的管道文件。
- mySpider/settings.py: 项目的设置文件。
- mySpider/spiders/: 存储爬虫代码目录。

##### 在当前目录下输入命令，将在mySpider/spider目录下创建一个名为itcast的爬虫，并指定爬取域的范围：

```
scrapy genspider itcast "itcast.cn"
```

- 运行爬虫

```

scrapy crawl itcast
```

#### scrapy爬虫框架

- 创建一个scrapy项目

  scrapy     startproject  mySpider

- 生成一个爬虫

  scrapy   genspider   itcast   "itcast.cn"

- 提取数据

  完善spider,使用xpath等方法

- 保存数据

  pipeline 中保存数据

  
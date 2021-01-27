



## ajax  

​		生活中 同步： 国家富强 人民生活水平提高   多件事情一起做   

​		技术上同步 ：正好跟生活相反  事情一件件做  得排队     打电话   挂掉一个才能下一个  

​	   生活中的异步:  你做你的 我做我的    事情一件件做  得排队  

​		技术上的异步: 多件事情一起做        发微博  （九宫格图片发送中 ）我们可以浏览其它微博至于什么时候发送成功不用管  肯定会返回一个状态 早晚的事情 

​		原生js ajax 步骤 : 

​		生活中                        							原生js

​	1.先有个手机             								 1.ajax对象

​    2.拨通对方手机号      								2.连接服务器 

​    3.你先说话 :"我是社会源，你过来啊" 	 3.发送你的请求  

​    4.等待对方的回复    								  4.接收返回数据 



ajax  在项目中 应用 : 

​	1.前后端交互 前台提交数据 后台返回数据 

​	2.股票 每秒变化  异步 无刷新  

​	3.天气预报  不用刷新  实时显示  

​	4.表单验证  你继续往下写  同时 字段到服务器验证 到最后 提交的都是没问题     

​	 局部更新  不需要刷新页面

## json  

```
var box={
	name:"test",   对象
}


{
	"name":"test",  //json
}

[{'name':'a'},{'age':18}]  //数组  js类型   单引号 

{
    "city": "北京",
    "pm25": "26",
    "weather": [
        {
            "date": "周四 08月15日",
            "icon1": "day/leizhenyu",
            "icon2": "night/zhongyu",
            "weather": "雷阵雨转中雨",
            "wind": "西南风微风",
            "temp": "32 ~ 22℃"
        },
        {
            "date": "周五",
            "icon1": "day/qing",
            "icon2": "night/qing",
            "weather": "晴",
            "wind": "西北风3-4级",
            "temp": "31 ~ 22℃"
        },
        {
            "date": "周六",
            "icon1": "day/qing",
            "icon2": "night/qing",
            "weather": "晴",
            "wind": "西北风微风",
            "temp": "31 ~ 20℃"
        },
        {
            "date": "周日",
            "icon1": "day/qing",
            "icon2": "night/qing",
            "weather": "晴",
            "wind": "北风微风",
            "temp": "31 ~ 21℃"
        }
    ],
    "date": "2019-08-15",
    "id": "101010100",
    "t": 1565798400
}     //json 



```

## json  js原生类型相互转化  

* 原生js->json      JSON.stringify(变量)

```
var shehuiyuan= [{'name':'a','age':18},{'name':'b','age':19}];
var test = JSON.stringify(shehuiyuan); //单引号 自动转化为双引号  
document.write(test);
```

* json ->原生js    JSON.parse()

  ```
  var box = '[{"name": "a","age": 18},{"name": "b","age": 19}]';
  var test = JSON.parse(box);
  alert(test);
  ```

  


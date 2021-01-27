
function  ajax(){
	//1.ajax对象     得烤炉浏览器的兼容性
	//W3c浏览器  ie浏览器  不一样
	alert(window.XMLHttprRequest);
	if(window.XMLHttpRequest){

	var ajax = new XMLHttpRequest();    //这是w3c  浏览器支持的
	}else{	
	var  ajax = new  ActiveObject("Microsft.XMLHTTp");  //这是ie浏览器支持的
	}
	//2.连接服务器
	//open(method,url,是否是异步)
	//method  get  post
	//true  表示异步   false  同步
	aJax.open("GET",url,true);
	
	
	//3.发送请求
	ajax.send();
	
	
	//4.等待服务器返回
	//接收服务器返回的数据   需要监听XMLHttprequest的状态
	//当状态发生改变  会发生一个事件  onreadystatechange
	//onreadystatechange   5个状态  0 1 2 3 4
	//0  请求没有初始化  
	//1  连接已经建立
	//2 请求已经接收
	//3 请求处理中
	//4 请求完成，开始响应
	ajax.onreadystatechange = function(){
		if(ajax.readyState==4){
			// 为4  说明 到了商店了  还需要取决于商店有没有卖给他
			if(ajax.status==200){    //两百条卖给他
				alert('成功')
//				funcsuccess()			
			}else{
				alert('失败');
			}
		}
	}

}
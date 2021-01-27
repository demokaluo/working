//先获取元素  

//1.获取div标签  根据id 
var box = document.getElementById('box');
var span = box.getElementsByTagName('span') //多个span 所以 别忘了 s 
//alert(span.length);


//创建一个容器 用来 存放产生的红球 6个

var redBall = [];


for(var i=0;i<6;i++){
	//产生随机数   
	var rand = Math.floor(Math.random()*33+1);
	if(redBall.indexOf(rand) == -1){
		redBall.push(rand);
	}else{
		i--; //如果有重复的 该次作废  次数恢复一个
	}
	
}

for(var i=0;i<redBall.length;i++){
	//跟下一个球进行比较 并调换
	for(var j=i+1;j<redBall.length;j++){
		if(redBall[i]>redBall[j]){
			var temp = redBall[i];
			redBall[i] = redBall[j];
			redBall[j] = temp;
		}
	}
}

var blueBall = Math.floor(Math.random()*16+1);

redBall.push(blueBall);
for(var i=0;i<span.length;i++){
	span[i].innerHTML = redBall[i];
}



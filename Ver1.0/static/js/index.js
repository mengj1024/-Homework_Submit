// 获取画布信息

// 重置画布背景
// resetCanvas();

// 设置默认样式和全局样式
var colorLine,lineWidth=4,move = false,imgData,r;
drawBrush();

// 保存
save.onclick=function(){
	// chose();
	// this.setAttribute('class','on');
	// 保存画布信息
	var imgdata = canvas.toDataURL();
	// 调用保存函数
	
	// 创建一个新的img元素，将其放入底部
	var newImg = document.createElement('img');
	var footer = document.getElementById('footer');
	// 把canvas信息传递给img
	thumb = document.getElementById("thumb");
	newImg.setAttribute('src',imgdata);
	newImg.style.width = '200px';
	footer.appendChild(newImg);
	thumb.value=canvas.toDataURL("image/png")
	// document.write(imgdata);
	// 把canvas信息传递给img
	resetCanvas();
}

// 清空画布
clear.onclick=function(){
	// chose();
	// 清空画布
	this.setAttribute('class','on');
	resetCanvas();
}

// 选择绘制工具
brush.onclick=function(){
    // 获取对应id属性值
    var gjID = this.getAttribute('id');
    this.setAttribute('class','on');
    // 执行相应操作
    switch(gjID){
        // 画笔工具
        case 'brush':{
            drawBrush();
            break;
        }
    }
}
text.onclick=function(){
    // 获取对应id属性值
    var gjID = this.getAttribute('id');
    this.setAttribute('class','on');
    // 执行相应操作
    switch(gjID){
        // 文字输入工具
        case 'text':{
            drawText();
            break;
        }
    }
}
red.onclick = function(){
    // 清除所有样式
    // for (var i = 0; i < ele.length; i++) {
    //     ele[i].removeAttribute('class');
    // }
    // 给点击元素添加样式并获取其值
    // this.setAttribute('class','colorOn');
    // 获取对应的id值
    colorLine = this.getAttribute('id');
    // 设置填充和绘制样式
    ctx.strokeStyle = colorLine;
    ctx.fillStyle = colorLine;
}
function saveTu(){
	var saveImage = canvas.toDataURL('image/png');
	var b64 = saveImage.substring(22);
	
	
	$.ajax({
	url: "http://localhost:8080/jiemian/saveImg",
	type:'post',
	data: { pp: b64},
	success:function ()  
	        {  
	        alert('保存成功');  
	        }  
	});  
}

// 画笔工具函数
function drawBrush(){
	canvas.onmousedown=function(evt){
		// 兼容事件
		var e = window.event||evt;
		// 获取坐标
		x1 = e.pageX - this.offsetLeft;
		y1 = e.pageY - this.offsetTop;
		// 表示可以移动
		move = true;
		// 开始绘制
		ctx.closePath();
		ctx.beginPath();
		ctx.moveTo(x1,y1);
	}
	canvas.onmousemove=function(evt){
		var e = window.event||evt;
		x2 = e.pageX - this.offsetLeft;
		y2 = e.pageY - this.offsetTop; 
		// 移动绘制
		if(move){
			ctx.lineTo(x2,y2);
			ctx.stroke();
		 }
	}
	// 关闭可以移动的开关
	canvas.onmouseup=function(){
			move=false;
	}
	canvas.onmouseout=function(){
			move=false;
	}
}


// 文字输入工具
function drawText(){
	canvas.onmousedown=function(evt){
		var e =window.event||evt;
		X = e.pageX - this.offsetLeft;
		Y = e.pageY - this.offsetTop; 
		var word=window.prompt('输入文本','例如:你好！');
		// 如果有输入内容 则显示
		if(word){
			// 设置字体大小
			var fontSize = (lineWidth*lineWidth+12)+'px';
			ctx.font = ''+fontSize+' 微软雅黑';
			ctx.fillText(word,X,Y);
		}
		
	}
}

// 保存图片函数 (图像信息)
function Download(imgdata){
	// 确定图片的类型 
	var type ='png';
	// 将mime-type改为image/octet-stream,强制让浏览器下载
	var fixtype=function(type){
	    type=type.toLocaleLowerCase().replace(/jpg/i,'jpeg');
	    var r=type.match(/png|jpeg|bmp|gif/)[0];
	    return 'image/'+r;
	};
	imgdata=imgdata.replace(fixtype(type),'image/octet-stream');
	// 将图片保存到本地
	var savaFile=function(data,filename){
	    var save_link=document.createElementNS('http://www.w3.org/1999/xhtml', 'a');
	    save_link.href=data;
	    save_link.download=filename;
	    var event=document.createEvent('MouseEvents');
	    event.initMouseEvent('click',true,false,window,0,0,0,0,0,false,false,false,false,0,null);
	    save_link.dispatchEvent(event);
	};
	var filename=''+new Date().getDate()+'.'+type;  
	// 设置文件名
	savaFile(imgdata,filename);
}


// 重置画布信息
function resetCanvas(){
	ctx.clearRect(0,0,1080,720);
	ctx.fillStyle = '#fff';
	ctx.fillRect(0,0,1080,720);
	ctx.fillStyle = colorLine||'#000';
}
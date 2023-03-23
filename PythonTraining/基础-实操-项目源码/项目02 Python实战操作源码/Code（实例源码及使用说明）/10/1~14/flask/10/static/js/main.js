// 查照URL
function UrlSearch() {
   var data = new Array();   // 初始化数组
   var name,value;           // 初始化 key ,value
   var str=location.href;     //取得当前整个地址栏
   var num=str.indexOf("?");  // 查找是否包含"?"
   str=str.substr(num+1); // 取得所有参数   stringvar.substr(start [, length ]
   var arr=str.split("&"); // 各个参数放到数组里
   for(var i=0;i < arr.length;i++){
        num=arr[i].indexOf("=");
        if(num>0){
             name=arr[i].substring(0,num);      // 获取key
             value=arr[i].substr(num+1); // 获取value
             data[name]=value;                  // 写入数组
        }
   }
   return data
}


// 拼接参数
function param(data){
   var url= '';
   for(var k in data){
     //去掉undefined
    var value=data[k] !== undefined ? data[k] :'';
    url =url+'&'+k+'='+ value;
    }
  return url ? url.substring(1) : '';
}

 function urlContact(url){
  //增加？url.indexOf('?')<0  ? '?': '&'
  return  url =url+(url.indexOf('?')<0  ? '?': '&')+param(data);
}

// 匹配URL地址
function matchUrl(key,value){
    data = UrlSearch();
    data[key] = value;
    url=urlContact(window.location.pathname);
    window.location.href = url
}

(function(){
    let headerCache = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function(key, value) {
        console.log("hook set header %s=>%s", key, value);
        if(key=== "X-Dgi-Req-Signature"){
            debugger;
        }
        return headerCache.apply(this, arguments); // 调用原始方法
    };
})()
// console.log(lrc)
/**
 * 解析歌词字符串
 * 得到一个歌词对象的数组
 * 每个歌词对象：
 * {time:开始时间，words:歌词内容}
 */
function parseLrc() {
    // console.log(lrc)
    var lines = lrc.split('\n');
    var result = []; //歌词对象数组
    for (var i = 0; i < lines.length; i++) {
        var str = lines[i];
        var parts = str.split(']');
        var timeStr = parts[0].substring(1)
        // console.log(parts);
        var obj = {
            time: parseTime(timeStr),
            words: parts[1]
        };
        result.push(obj)
    }
    return result
}
/**
 * 将一个时间字符串解析为数字(秒)
 * @param {*} timeStr  时间字符串
 * @returns 
 */
function parseTime(timeStr) {
    // console.log('timStr:'+timeStr)

    var parts = timeStr.split(':');
    // console.log('parts:'+parts)
    // console.log('result:'+parts[0] * 60 + parts[1])
    
    return +parts[0] * 60 + +parts[1]
}

var lrcData = parseLrc();
// console.log(lrcData)

var doms = {
    audio: document.querySelector('audio'),
    ul: document.querySelector('.container ul'),
    container: document.querySelector('.container')
};

/**
 * 计算出，在当前播放器播放到第几秒的情况下
 * lrcData数组中，应该搞了显示歌词的下标
 * 如果没有任何一句歌词需要显示，则得到-1
 */
function findIndex() {
    //播放器当前时间
    var curTime = doms.audio.currentTime;
    console.log('curTime:'+curTime)

    for (var i = 0; i < lrcData.length; i++) {
        if (curTime < lrcData[i].time) {
            return i - 1;
        }
    }
    //找遍了都没有找到，说明播放器到最后一句
    return lrcData.length - 1;
}
//界面
/**
 * 创建歌词元素 li
 */
function createLrcElements() {
    //文档片段
    var frag = document.createDocumentFragment();
    for (var i = 0; i < lrcData.length; i++) {
        var li = document.createElement('li');
        li.textContent = lrcData[i].words;
        frag.appendChild(li);
    }
    doms.ul.appendChild(frag);

}
createLrcElements();

//容器高度
var containerHeight = doms.container.clientHeight;
//每个li高度
var liHeight = doms.ul.children[0].clientHeight;
//最大偏移量
var maxOffset = doms.ul.clientHeight -containerHeight;
/**
 * 设置ul元素的偏移量
 */
function setOffset() {
    var index = findIndex();
    console.log("index:"+index)
    var offset = liHeight * index + liHeight / 2 - containerHeight / 2;

    if (offset<0){
        offset = 0;
    }

    if(offset>maxOffset){
        offset = maxOffset;
    }
    doms.ul.style.transform = `translateY(-${offset}px`;
    //去掉之前的active样式
    var li = doms.ul.querySelector('.active');
    if (li){
        li.classList.remove('active');
    }
    var li = doms.ul.children[index];
    if (li){
        li.classList.add('active')
    }
   console.log(offset)
}

doms.audio.addEventListener('timeupdate',setOffset);
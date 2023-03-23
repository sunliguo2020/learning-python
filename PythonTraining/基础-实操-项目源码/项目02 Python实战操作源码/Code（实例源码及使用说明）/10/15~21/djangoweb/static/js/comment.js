
/* 
parentcontent  //父容器
boxcontent   // 评论区图片展示区域
*/
function commentMove(parentcontent, boxcontent) {
    this.obj = {
        activeClass: 'tm-current',
        nextButton: '.tm-m-photo-viewer-navright',
        prevButton: '.tm-m-photo-viewer-navleft',
    }
    this.parentcontent = parentcontent;
    this.boxcontent = boxcontent;

}
commentMove.prototype = {
    init: function () {
        var that = this;
        that.start();
        this.lefthover();
        this.righthover();
        this.leftclick();
        this.rightclick();
    },
    start: function () {
        var that = this;
        $(that.parentcontent + ' li').click(function () {

            $(this).toggleClass(that.obj.activeClass).siblings().removeClass(that.obj.activeClass);
            var src = $('.' + that.obj.activeClass).attr('data-src');

            var img = new Image();
            img.src = src;
            img.onload = function () {
                var imageWidth = img.width;
                var imageHeight = img.height;
                $(that.boxcontent).css({ "width": imageWidth, "height": imageHeight })
                $(that.obj.prevButton).css({ "width": imageWidth / 3, "height": imageHeight })
                $(that.obj.prevButton).children().css({ "top": imageHeight / 2 - 10 + 'px' })
                $(that.obj.nextButton).children().css({ "top": imageHeight / 2 - 10 + 'px' })

            }
            if (!src) {
                $(that.boxcontent).css({ "width": 0, "height": 0 });
            } else {
                $(that.boxcontent + " img").attr('src', src);
            }
        })
    },
    lefthover: function () {
        var that = this;
        $(that.obj.prevButton).hover(function () {
            var index = $(that.parentcontent + ' li').index($(that.parentcontent + ' li.' + that.obj.activeClass));
            if (index < 1) {
                $(this).children().css("display", "none");
            } else {
                $(this).children().css({ "display": "inline" });
            }
        }, function () {
            $(this).children().css({ "display": "none" });
        })
    },
    righthover: function () {
        var that = this;

        $(that.obj.nextButton).hover(function () {
            var index = $(that.parentcontent + ' li').index($(that.parentcontent + ' li.' + that.obj.activeClass));
            if (index >= $(that.parentcontent + ' li').length - 1) {
                $(this).children().css("display", "none");
            } else {
                $(this).children().css({ "display": "inline" });
            }
        }, function () {
            $(this).children().css({ "display": "none" });
        })
    },
    leftclick: function () {
        var that = this;
        $(that.obj.prevButton).click(function () {
            var index = $(that.parentcontent + ' li').index($(that.parentcontent + ' li.' + that.obj.activeClass));

            index--;
            if (index >= 0) {
                $(that.parentcontent + ' li').eq(index).toggleClass(that.obj.activeClass).siblings().removeClass(that.obj.activeClass)
                $(that.boxcontent + " img").attr("src", $(that.arentcontent + ' li').eq(index).attr('data-src'))
            }
            if (index < 1) {
                index = 0;
                $(this).children().css({ "display": "none" });
                return;
            }
        })
    },
    rightclick: function () {
        var that = this;
        $(that.obj.nextButton).click(function () {
            var index = $(that.parentcontent + ' li').index($(that.parentcontent + ' li.' + that.obj.activeClass));
            index++;
            $(that.boxcontent + " img").attr("src", $(that.parentcontent + ' li').eq(index).attr('data-src'))

            $(that.parentcontent + ' li').eq(index).toggleClass(that.obj.activeClass).siblings().removeClass(that.obj.activeClass);
            if (index >= $(that.parentcontent + ' li').length - 1) {
                $(this).children().css({ "display": "none" });
            }
        })
    }
}



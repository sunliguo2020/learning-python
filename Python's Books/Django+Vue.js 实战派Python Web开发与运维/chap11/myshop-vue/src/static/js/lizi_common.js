/**
 * 产品名称: Ecshop生鲜蔬菜商城模板 
 * 使用版本：Ecshop v2.7.3版
 * 出品单位: O菜龙工作室出品
 * 设计者网址：http://www.ocailong.com/
 * 设计者QQ：763191200（o菜龙）
*/
$(function(){
	/*收藏夹功能*/
	$("#favorite_wb").click(function() {
		var h = "http://"+location.hostname;
		var j = location.title;
		try {
			window.external.addFavorite(h, j);
		} catch (i) {
			try {
				window.sidebar.addPanel(j, h, "");
			} catch (i) {
				alert("对不起，您的浏览器不支持此操作！\n请您使用菜单栏或Ctrl+D收藏本站。");
			}
     	}
	})
	
	/*回到顶部效果 start*/
	$("a.back2top").click(function(){	
		$("body,html").animate({
                    scrollTop: 0
		}, 500);
	})
	/*回到顶部效果 end*/
	
	/*头部下拉菜单 start*/
	$("#userinfo-bar li.more-menu").mouseenter(function(){
		$(this).animate(300,function(){
			$(this).addClass("hover");
		})
	})
	
	$("#userinfo-bar li.more-menu").mouseleave(function(){
		$(this).animate(300,function(){
			$(this).removeClass("hover");
		})
	})
	/*头部下拉菜单 end*/
	
	/*购物车鼠标移入效果 start*/
	$("#ECS_CARTINFO").on("mouseenter", function() {
		$("#ECS_CARTINFO").animate(200,function(){
			$("#ECS_CARTINFO").addClass("hd_cart_hover");
			$("p.fail").show();
		})
	}).on("mouseleave", function() {
		$("#ECS_CARTINFO").animate(200,function(){
			$("#ECS_CARTINFO").removeClass("hd_cart_hover");
			$("p.fail").hide();
		})
	});
	/*购物车鼠标移入效果 end*/
	
	/*分类导航鼠标移入效果 start*/	
	h = this;
	b = $("#J_mainCata");
	e = $("#J_subCata");
	i = $("#main_nav");
	l = null;
	k = null;
	d = false;
	g = false;
	f = false;
			
	i.on("mouseenter", function() {
		var m = $(this);
		if (l !== null) {
			clearTimeout(l);
		}
		if (f) {
			return;
		}
		l = setTimeout(function() {
			m.addClass("main_nav_hover");
			b.stop().show().animate({
					opacity: 1
			}, 300);
		}, 200);		
	}).on("mouseleave", function() {
		if (l !== null) {
			clearTimeout(l);
		}
		l = setTimeout(function() {
			e.css({
				opacity: 0,
				left: "100px"
			}).find(".J_subView").hide();
			b.hide();
			g = false;
			if (!f) {
				b.stop().delay(200).animate({
					opacity: 0
				}, 300, function() {
					i.removeClass("main_nav_hover");
					b.hide().find("li").removeClass("current");
				});
			} else {
				b.find("li").removeClass("current");
			}
        }, 200);
	});
			
			
	$("#J_mainCata li").mouseenter(function(){
		m = $(this);
		n = $("#J_mainCata li").index($(this));
				
		/*
		if (n > 4) {
			m.addClass("current").siblings("li").removeClass("current");
			e.find(".J_subView").hide();
			return false;
		}
		*/
		if (n > 1) {
			subView_h = (e.find(".J_subView").eq(n).height());
			b_h = b.height();
			m_h = m.height();
			m_p = m.position();
			

			x = b_h-subView_h;
			x = (x/2);
			
			v = parseInt(m_p.top)+m_h;
			
			
			if(parseInt(subView_h+x) > v)
			{
				x+=35;
				e.css({
					top: x
				});	
			}
			else
			{
				
				s = v - x - subView_h;
				x += s;
				x += 35;
				
				e.css({
					top: x
				});	
				
			}

			
		} else {
			e.css({
			top: "35px"
			});
		} 
		
		if (g) {					
			m.addClass("current").siblings("li").removeClass("current");
			e.find(".J_subView").hide().eq(n).show();
		} else {
			if (k !== null) {
				clearTimeout(k);
			}
			k = setTimeout(function() {
					m.addClass("current").siblings("li").removeClass("current");
					g = true;
					if (d) {
						e.css({
							opacity: 1,
							left: "213px"
						}).find(".J_subView").eq(n).show();
					} else {
						c(n);
                    }
			}, 200);
		}
	})
			
	function c(m) {
		e.css({
			opacity: 1,
			left: "213px"
		}).find(".J_subView").eq(m).show();
			d = true;
	}
	/*分类导航鼠标移入效果 end*/	
	
	$("#h_box h3").click(function(){
		var i = $("#h_box h3").index($(this));
		
		if($("#h_box ul").eq(i).is(":hidden"))
		{
			$(this).addClass("h3_all");
			$("#h_box ul").eq(i).show();
		}
		else
		{
			$(this).removeClass("h3_all");
			$("#h_box ul").eq(i).hide();
		}
	})
})


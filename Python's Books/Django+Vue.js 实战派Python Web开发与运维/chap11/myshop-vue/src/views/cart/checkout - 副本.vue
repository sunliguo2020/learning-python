<template>
<div>

<link href="../../static/css/cart2.css" rel="stylesheet" type="text/css">

<div class="cle cart_main">
  <div class="flowBox_cart">
    <h6><span style="padding-left:0px;">确认订单信息页面</span></h6>
    <div class="flowBox_in">
      <form action="flow.php" method="post" name="theForm" id="theForm" onsubmit="return checkOrderForm(this)">

        <div class="flowBox">
          <h6><span>商品列表</span><a href="flow.php" class="f16">返回修改购物车</a></h6>
          <table width="99%" align="center" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
            <tr>
              <th bgcolor="#f5f5f5">商品名称</th>
              <th bgcolor="#f5f5f5">属性</th>
                            <th bgcolor="#f5f5f5">原价</th>
                            <th bgcolor="#f5f5f5">本店价</th>
              <th bgcolor="#f5f5f5">购买数量</th>
              <th bgcolor="#f5f5f5">小计</th>
            </tr>
                        <tr>
              <td bgcolor="#ffffff"> 
                <a href="goods.php?id=7" target="_blank" class="f6">酣畅家庭菲力牛排10片澳洲生鲜牛肉团购套餐</a> 
                 
                 
                </td>
              <td bgcolor="#ffffff"></td>
                            <td align="right" bgcolor="#ffffff">￥285.59元</td>
                            <td bgcolor="#ffffff" align="right">￥190.40元</td>
              <td bgcolor="#ffffff" align="right">1</td>
              <td bgcolor="#ffffff" align="right">￥190.40元</td>
            </tr>
                        <tr>
              <td bgcolor="#ffffff"> 
                <a href="goods.php?id=2" target="_blank" class="f6">田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛</a> 
                 
                 
                (<span style="color:#FF0000">免运费商品</span>)</td>
              <td bgcolor="#ffffff"></td>
                            <td align="right" bgcolor="#ffffff">￥105.60元</td>
                            <td bgcolor="#ffffff" align="right">￥70.40元</td>
              <td bgcolor="#ffffff" align="right">2</td>
              <td bgcolor="#ffffff" align="right">￥140.80元</td>
            </tr>
             
                        <tr>
              <td bgcolor="#ffffff" colspan="7"> 
                购物金额小计 ￥331.20元，比市场价 ￥496.79元 节省了 ￥165.59元 (33%)</td>
            </tr>
                      </table>
        </div>
        <div class="blank"></div>
        <div class="flowBox">
          <h6><span>收货人信息</span><a href="flow.php?step=consignee" class="f16">返回修改收货地址</a></h6>
          <table width="99%" align="center" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
            <tr>
              <td bgcolor="#f5f5f5">收货人姓名:</td>
              <td bgcolor="#ffffff">2222</td>
			  <td bgcolor="#f5f5f5">详细地址:</td>
              <td bgcolor="#ffffff">2222222222222222222222222 </td>
            </tr>
            <tr>
              <td bgcolor="#f5f5f5">手机:</td>
              <td bgcolor="#ffffff">13999869743</td>
			  <td bgcolor="#f5f5f5">备用电话:</td>
              <td bgcolor="#ffffff"> </td>
            </tr>
          </table>
        </div>
        <div class="blank"></div>
                <div class="flowBox">
          <h6><span>配送方式</span></h6>
          <table width="99%" align="center" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd" id="shippingTable">
            <tr>
              <th bgcolor="#f5f5f5" width="5%">&nbsp;</th>
              <th bgcolor="#f5f5f5" width="25%">名称</th>
              <th bgcolor="#f5f5f5">订购描述</th>
              <th bgcolor="#f5f5f5" width="15%">费用</th>
              <th bgcolor="#f5f5f5" width="15%">免费额度</th>
              <th bgcolor="#f5f5f5" width="15%">保价费用</th>
            </tr>
                        <tr>
              <td bgcolor="#ffffff" align="center"><input name="shipping" type="radio" value="1" checked="true" supportCod="1" insure="0" onclick="selectShipping(this)" /></td>
              <td bgcolor="#ffffff"><strong>上门取货</strong></td>
              <td bgcolor="#ffffff" valign="top">买家自己到商家指定地点取货</td>
              <td bgcolor="#ffffff" align="right" valign="top">￥0.00元</td>
              <td bgcolor="#ffffff" align="right" valign="top">￥0.00元</td>
              <td bgcolor="#ffffff" align="right" valign="top">不支持保价</td>
            </tr>
                        <tr>
              <td bgcolor="#ffffff" align="center"><input name="shipping" type="radio" value="2"  supportCod="0" insure="0" onclick="selectShipping(this)" /></td>
              <td bgcolor="#ffffff"><strong>运费到付</strong></td>
              <td bgcolor="#ffffff" valign="top">所购商品到达即付运费</td>
              <td bgcolor="#ffffff" align="right" valign="top">￥0.00元</td>
              <td bgcolor="#ffffff" align="right" valign="top">￥0.00元</td>
              <td bgcolor="#ffffff" align="right" valign="top">不支持保价</td>
            </tr>
                        <tr>
              <td bgcolor="#ffffff" align="center"><input name="shipping" type="radio" value="3"  supportCod="0" insure="0" onclick="selectShipping(this)" /></td>
              <td bgcolor="#ffffff"><strong>顺丰速运</strong></td>
              <td bgcolor="#ffffff" valign="top">江、浙、沪地区首重15元/KG，续重2元/KG，其余城市首重20元/KG</td>
              <td bgcolor="#ffffff" align="right" valign="top">￥15.00元</td>
              <td bgcolor="#ffffff" align="right" valign="top">￥0.00元</td>
              <td bgcolor="#ffffff" align="right" valign="top">不支持保价</td>
            </tr>
                        <tr>
              <td bgcolor="#ffffff" align="center"><input name="shipping" type="radio" value="4"  supportCod="1" insure="0" onclick="selectShipping(this)" /></td>
              <td bgcolor="#ffffff"><strong>圆通速递</strong></td>
              <td bgcolor="#ffffff" valign="top">上海圆通物流（速递）有限公司经过多年的网络快速发展，在中国速递行业中一直处于领先地位。为了能更好的发展国际快件市场，加快与国际市场的接轨，强化圆通的整体实力，圆通已在东南亚、欧美、中东、北美洲、非洲等许多城市运作国际快件业务</td>
              <td bgcolor="#ffffff" align="right" valign="top">￥5.00元</td>
              <td bgcolor="#ffffff" align="right" valign="top">￥0.00元</td>
              <td bgcolor="#ffffff" align="right" valign="top">不支持保价</td>
            </tr>
                        <tr>
              <td colspan="6" bgcolor="#ffffff" align="right"><label for="ECS_NEEDINSURE">
                  <input name="need_insure" id="ECS_NEEDINSURE" type="checkbox"  onclick="selectInsure(this.checked)" value="1"  disabled="true"  />
                  配送是否需要保价 </label></td>
            </tr>
          </table>
        </div>
        <div class="blank"></div>
         
                <div class="flowBox">
          <h6><span>支付方式</span></h6>
          <table width="99%" align="center" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd" id="paymentTable">
            <tr>
              <th width="5%" bgcolor="#ffff99">&nbsp;</th>
              <th width="20%" bgcolor="#ffff99">名称</th>
              <th bgcolor="#ffff99">订购描述</th>
              <th bgcolor="#ffff99" width="15%">手续费</th>
            </tr>
             
            
            <tr>
              <td bgcolor="#ffffff"><input type="radio" name="payment" value="1" id="pay_check_value_1" checked isCod="0" onclick="selectPayment(this)" /></td>
              <td bgcolor="#ffffff"><label class="pay_label" for="pay_check_value_1">支付宝</label></td>
              <td valign="top" bgcolor="#ffffff">支付宝网站(www.alipay.com) 是国内先进的网上支付平台。<br/>支付宝收款接口：在线即可开通，<font color="red"><b>零预付，免年费</b></font>，单笔阶梯费率，无流量限制。<br/><a href="http://cloud.ecshop.com/payment_apply.php?mod=alipay" target="_blank"><font color="red">立即在线申请</font></a></td>
              <td align="right" bgcolor="#ffffff" valign="top">￥0.00元</td>
            </tr>
             
            
            <tr>
              <td bgcolor="#ffffff"><input type="radio" name="payment" value="2" id="pay_check_value_2"  isCod="0" onclick="selectPayment(this)" /></td>
              <td bgcolor="#ffffff"><label class="pay_label" for="pay_check_value_2">余额支付</label></td>
              <td valign="top" bgcolor="#ffffff">使用帐户余额支付。只有会员才能使用，通过设置信用额度，可以透支。</td>
              <td align="right" bgcolor="#ffffff" valign="top">￥0.00元</td>
            </tr>
             
            
            <tr>
              <td bgcolor="#ffffff"><input type="radio" name="payment" value="3" id="pay_check_value_3"  isCod="0" onclick="selectPayment(this)" /></td>
              <td bgcolor="#ffffff"><label class="pay_label" for="pay_check_value_3">银行汇款/转帐</label></td>
              <td valign="top" bgcolor="#ffffff">银行名称
收款人信息：全称 ××× ；帐号或地址 ××× ；开户行 ×××。
注意事项：办理电汇时，请在电汇单“汇款用途”一栏处注明您的订单号。</td>
              <td align="right" bgcolor="#ffffff" valign="top">￥0.00元</td>
            </tr>
             
            
            <tr>
              <td bgcolor="#ffffff"><input type="radio" name="payment" value="4" id="pay_check_value_4"  isCod="1" onclick="selectPayment(this)" /></td>
              <td bgcolor="#ffffff"><label class="pay_label" for="pay_check_value_4">货到付款</label></td>
              <td valign="top" bgcolor="#ffffff">开通城市：×××
货到付款区域：×××</td>
              <td align="right" bgcolor="#ffffff" valign="top"><span id="ECS_CODFEE">￥0.00元</span></td>
            </tr>
                      </table>
        </div>
                <div class="blank"></div>
         
        
                
        <div class="flowBox">
          <h6><span>其它信息</span></h6>
          <table width="99%" align="center" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
             
             
                        <tr>
              <td bgcolor="#ffffff"><strong>使用红包:</strong></td>
              <td bgcolor="#ffffff"> 选择已有红包                <select name="bonus" onchange="changeBonus(this.value)" id="ECS_BONUS" style="border:1px solid #ccc;">
                  <option value="0" selected>请选择</option>
                                  </select>
                或者输入红包序列号                <input name="bonus_sn" type="text" class="inputBg" size="15" value="" />
                <input name="validate_bonus" type="button" class="bnt_blue_1" value="验证红包" onclick="validateBonus(document.forms['theForm'].elements['bonus_sn'].value)" style="vertical-align:middle;" /></td>
            </tr>
             
                        <tr>
              <td valign="top" bgcolor="#f5f5f5"><strong>订单附言:</strong></td>
              <td bgcolor="#ffffff"><textarea name="postscript" cols="80" rows="3" id="postscript" style="border:1px solid #ccc;"></textarea></td>
            </tr>
                        <tr>
              <td bgcolor="#ffffff"><strong>缺货处理:</strong></td>
              <td bgcolor="#ffffff">                
                <label>
                  <input name="how_oos" type="radio" value="0" checked onclick="changeOOS(this)" />
                  等待所有商品备齐后再发</label>
                
                                
                <label>
                  <input name="how_oos" type="radio" value="1"  onclick="changeOOS(this)" />
                  取消订单</label>
                
                                
                <label>
                  <input name="how_oos" type="radio" value="2"  onclick="changeOOS(this)" />
                  与店主协商</label>
                
                </td>
            </tr>
                      </table>
        </div>
        <div class="blank"></div>
        <div class="flowBox">
          <h6><span>费用总计</span></h6>
          <div id="ECS_ORDERTOTAL">
<table width="99%" align="center" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
    <tr>
    <td align="right" bgcolor="#f5f5f5">
    该订单完成后，您将获得 
            <font class="f4_b">331</font> 积分            ，以及价值               <font class="f4_b">￥0.00元</font>的红包。
          </td>
  </tr>
    <tr>
    <td align="right" bgcolor="#f5f5f5" style="color:#666666;">
      商品总价: <font class="f4_b">￥331.20元</font>
                                              </td>
  </tr>
    <tr>
    <td align="right" bgcolor="#ffffff"> 应付款金额: <font class="f4_b">￥331.20元</font>
    	</td>
  </tr>
</table>
</div>          <div align="center" style="margin:8px auto;">
            <input type="image" src="themes/lizi/images/bnt_subOrder.gif" />
            <input type="hidden" name="step" value="done" />
          </div>
        </div>
      </form>
    </div>
  </div>
</div>

</div>
</template>
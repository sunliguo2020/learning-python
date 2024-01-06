<template>
  <div class="w-max ct mb30 clearfix">
    <div class="surprise-tit clearfix">
      <div class="fl sur-titimg overflow">
        <img src="../../static/images/day_surprises.jpg" />
      </div>
    </div>
    <div class="surprise-con clearfix bgwhite border-eee">
      <div class="day-surimg fl" id="day-surimg">
        <a href="#"
          ><img src="../../static/images/bg.jpg" width="222" height="380"
        /></a>
      </div>
      <div class="fr surprise-list ovh">
        <ul class="clearfix" style="text-align: center">
          <li v-for="item in lists">
            <div class="sur-hear p25">
              <a href="#" class="imgBox ftc"
                ><img :src="item.main_img" class="zom"
              /></a>
              <h1 class="overflow mt">
                <router-link :to="'/detail/' + item.id" class="ft12 c333">{{  item.name }}</router-link>
              </h1>
            </div>
            <div class="sur-price clearfix">
              <div class="fl sur-numbox overflow">
                <div class="sur-num bold">￥{{ item.price }}元</div>
                <p class="c999">
                  <del>原价:￥{{ item.market_price }}元</del>
                </p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
import { getGoods } from "@/api/goods";
export default {
  data() {
    return {
      lists: [],
    };
  },
  methods: {
    getRecommendGoods() {
      getGoods({ is_recommend: "true" }).then((response) => {
        console.log(response.data.data);
        this.lists = response.data.data;
      });
    },
  },
  created() {
    this.getRecommendGoods();
  },
};
</script>

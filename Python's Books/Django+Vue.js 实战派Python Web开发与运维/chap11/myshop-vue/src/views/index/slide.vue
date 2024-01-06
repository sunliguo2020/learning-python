<template>
  <div class="app-container">
    <div class="swiper">
      <swiper ref="mySwiper" :options="swiperOptions">
        <swiper-slide v-for="(item, index) in lists" :key="index">
          <router-link :to="'/detail/' + item.goods" target="_blank">
            <img :src="item.images" alt=""
          /></router-link>
        </swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
      </swiper>
    </div>
  </div>
</template>
<script>
import { swiper, swiperSlide } from "vue-awesome-swiper";
import { getSlide } from "@/api/goods"; //引入api里面定义的方法
import "swiper/dist/css/swiper.css";
export default {
  name: "default",
  data() {
    return {
      swiperOptions: {
        loop: true,
        autoplay: {
          delay: 3000,
          stopOnLastSlide: false,
        },
        pagination: {
          el: ".swiper-pagination", //与slot="pagination"处 class 一致
          clickable: true, //轮播按钮支持点击
          autoplay: true,
        },
      },
      lists: [],
    };
  },
  components: {
    swiper,
    swiperSlide,
  },
  methods: {
    getData() {
      getSlide()
        .then((response) => {
          //console.log(response.data);
          this.lists = response.data.data;
          console.log("slide " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  created() {
    this.getData();
  },
};
</script>

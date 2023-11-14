<template>
  <div class="series_list">
    <div class="series_box cle" v-for="(item, index) in lists">
      <div class="series_info">
        <div class="series_name name_hufu">
          <h2>{{ item.name }}</h2>
        </div>

        <div class="brand_cata">
          <div v-for="iteminfo in item.sub_cat">
            <router-link :to="'/list/' + iteminfo.id">{{
              iteminfo.name
            }}</router-link>
          </div>
        </div>
        <div>
          <img :src="item.logo" style="width: 200px; height: 200px" />
        </div>
      </div>

      <div class="pro_list">
        <ul class="cle">
          <li v-for="good in item.goods">
            <router-link :to="'/detail/' + good.id">
              <p class="pic">
                <img :src="good.main_img" style="display: inline" />
              </p>
              <h3 style="text-align: center">{{ good.name }}</h3>
              <p class="price" style="text-align: center">
                ￥{{ good.price }}元
              </p>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
import { getCategoryGoods } from "@/api/goods";
export default {
  data() {
    return {
      lists: [],
    };
  },
  methods: {
    getData() {
      getCategoryGoods().then((response) => {
        console.log(response.data.data);
        this.lists = response.data.data;
      });
    },
  },
  created() {
    this.getData();
  },
};
</script>

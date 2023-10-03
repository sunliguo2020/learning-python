<template>
    <h3>条件渲染</h3>
    <div v-if="flag">你能看见我吗？</div>
    <div v-else>那你还是看看我吧</div>
</template>
<script>
export default{
    data(){
        return {
            flag:false,
        }
    }
}
</script>

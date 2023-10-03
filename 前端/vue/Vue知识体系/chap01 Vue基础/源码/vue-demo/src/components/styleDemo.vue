<template>
    <p :style="{class:'red'}">style绑定1</p>
    <p :style="{class:activeColor}">style绑定2</p>
    <p :style="styleObject">style绑定3</p>

    
</template>
<script>
export default {
    data(){
        return {
            activeColor:'green',
            fontSize:30,
            styleObject:{
                color:'red',
                fontSize:'30px'
            }

        }
    }
}
</script>
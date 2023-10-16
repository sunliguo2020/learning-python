<template>
    <h3>prop传递数据</h3>
    <p>{{ title }}</p>
    <p>{{ age }}</p>
</template>
<script>
export default {
    name: "myComponents",
    props: {
        title: {
            type: String,
            default: ''
        },
        age: {
            type: Number,
            default: 2
        }

    }
}
</script>
<style scoped></style>
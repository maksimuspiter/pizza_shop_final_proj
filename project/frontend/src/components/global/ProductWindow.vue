<script setup>

const props = defineProps({
    data: Object,
    close_window: Function,
})

const product_name = props.data.product_name

</script>

<template>
    <ModalWindow width_window="750" height_window="750" :close_window="close_window">

        <ProductWindowPizza 
        v-if="product_name === 'Pizza'" 
        :data="data"
        :close_window="close_window" />

        <ProductWindowSimple 
        v-else 
        :data="data"
        :close_window="close_window" />

    </ModalWindow>
</template>

<style scoped></style>
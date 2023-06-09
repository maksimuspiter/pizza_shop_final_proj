<script setup>

const props = defineProps({
    data: Object,
    close_window: Function,
})

const product_name = props.data.product_name

</script>

<template>
    <div>
        <ModalWindow v-if="product_name === 'Pizza'" 
        width_window="750" 
        height_window="750" 
        :close_window="close_window">
            <ProductWindowPizza 
            :data="data" 
            :close_window="close_window" />

        </ModalWindow>

        <ModalWindow  v-if="product_name === 'Desert'"
        width_window="750" 
        height_window="400" 
        :close_window="close_window">

            <ProductWindowSimple 
            :data="data" 
            :close_window="close_window" />
        </ModalWindow>


        <ModalWindow  v-if="product_name === 'Drink'"
        width_window="750" 
        height_window="400" 
        :close_window="close_window">

            <ProductWindowSimple 
            :data="data" 
            :close_window="close_window" />
        </ModalWindow>

        <ModalWindow  v-if="product_name === 'Other'"
        width_window="750" 
        height_window="400" 
        :close_window="close_window">

            <ProductWindowSimple 
            :data="data" 
            :close_window="close_window" />
        </ModalWindow>
        <ModalWindow  v-if="product_name === 'Snack'"
        width_window="750" 
        height_window="400" 
        :close_window="close_window">

            <ProductWindowSimple 
            :data="data" 
            :close_window="close_window" />
        </ModalWindow>
    </div>
</template>

<style scoped></style>
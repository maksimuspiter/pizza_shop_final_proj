<script setup>

import { useCartStore } from '@/stores/cart'

const cart = useCartStore()

const props = defineProps({
    product_slug: String,
    quantity: Number,
})


</script>
<template>
    <div class="product_quantity_group_button row">
        <button class="col m-0 p-0 btn btn-sm" @click="cart.cart_product_decrement(product_slug)">
            <svg width="10" height="10" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg" class="icon">
                <rect fill="#454B54" y="4" width="10" height="2" rx="1"></rect>
            </svg>
        </button>
        <div class="col m-0 p-0">{{ quantity }}</div>
        <button class="col m-0 p-0 btn btn-sm" @click="cart.cart_product_increment(product_slug)">
            <svg width="10" height="10" viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg" class="icon">
                <g fill="#454B54">
                    <rect x="4" width="2" height="10" ry="1"></rect>
                    <rect y="4" width="10" height="2" rx="1"></rect>
                </g>
            </svg>
        </button>
    </div>
</template>

<style>
.product_quantity_group_button {
    margin: 0;
    padding-top: 4px;
    padding-bottom: 4px;
    width: 100px;
    border: 2px solid;
    border-color: #0d6efd;
    text-align: center;
    border-radius: 9999px;
}
</style>
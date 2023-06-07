<script setup>
import { useCartStore } from '@/stores/cart'
import { computed, ref } from "vue";

const cart = useCartStore()
const products_with_choose = ["Pizza"]

const { product, open_window } = defineProps({
    product: {
        id: Number,
        slug: String,
        product_name: String,
        title: String,
        description: String,
        image_url: String,
        min_price: Number,
    },
    button_title: String,
    open_window:Function,
})
const check_btn = () => {
    return cart.check_product_in_cart(product.slug)===true ? 'btn-primary': 'btn-outline-primary'
}
const product_with_options = ["Pizza"]
const is_Product_with_options = () => {
    return product_with_options.includes(product.product_name)
}
const product_quantity = computed(() =>{
    return cart.get_product_quantity(product.slug)
})
function to_cart() {
    if(products_with_choose.includes(product.product_name)){
        open_window(product)
    } else {
        cart.add_to_cart(product.id, product.product_name, product.slug, product.min_price, product)
    }
}
function open_product_window(){
    open_window(product)
}

</script>

<template>
    <div class="product-card d-flex flex-column p-2">
        <div class="p-1">
            <img class="product-img img-fluid"
                :src="product.image_url" alt=""
                @click="open_product_window">
        </div>
        <div class="m-1">
            <h4 class="text-center">{{ product.title }}</h4>
        </div>

        <div class="m-2 text-secondary ">
            <p>{{ product.description }}</p>
        </div>
        <div class="mt-auto ms-2 me-2">
            <div class="d-flex justify-content-between align-items-center">
                <div>
                    <span>{{ Math.round(product.min_price) }} ₽</span>
                </div>
                <div v-if="is_Product_with_options() || product_quantity === 0">
                    <button 
                    v-bind:class="['btn',' btn-sm', check_btn() ] " @click="to_cart">
                        {{ button_title }}
                    </button>
                </div>
                <div v-else>
                    <IncrementDecrement 
                    :product_slug="product.slug"
                    :quantity="product_quantity"
                    />                
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.product-card {
    max-width: 250px;
    max-height: 5000px;
}
</style>

<script setup>
import { reactive } from "vue"
import { useCartStore } from '@/stores/cart'

const { data, close_window } = defineProps({
    data: {
        id: Number,
        slug: String,
        product_name:String,
        title: String,
        description: String,
        min_price: Number,
        image_url: String,
        weight: Number,

    },
    close_window: Function,

})
const cart = useCartStore()
function to_cart() {
    const product = data
    cart.add_to_cart(product.id, product.product_name, product.slug, product.min_price, data)
    close_window()
}

</script>

<template>
    <div class="row">
        <div class="col-5 mt-5" id="window-main-img">
            <img class="img-fluid" :src="data.image_url" alt="img" />
        </div>

        <div class="col-7 d-flex align-items-center flex-column">
            <div class="mb-2">
                <div class="row">
                    <h3 class="col-10 text-center p-2">{{ data.title }}</h3>
                    <div class="col-2">
                        <button type="button" class="btn btn-outline-secondary">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd"
                                    d="M12 20a8 8 0 100-16 8 8 0 000 16zm0 2c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"
                                    fill="#000"></path>
                                <path fill-rule="evenodd" clip-rule="evenodd"
                                    d="M12 11a1 1 0 011 1v5a1 1 0 11-2 0v-5a1 1 0 011-1z" fill="#000"></path>
                                <path d="M13.5 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z" fill="#000"></path>
                            </svg>
                        </button>
                    </div>
                </div>
                <div class="ms-2 me-2 mt-5">
                    <p>{{ data.description }}</p>
                </div>

            </div>
            <div class="mt-auto text-center mb-3">
                <button class="btn btn-outline-success" @click="to_cart">
                    Добавить в корзину за {{ data.min_price }}
                </button>
            </div>
        </div>

    </div>
</template>

<style scoped></style>
<script setup>
import { useCartStore } from '@/stores/cart'
import { reactive, ref, computed } from "vue"
import router from '../../router'

const cart = useCartStore()

const props = defineProps({
    close_window: Function,
})
const getProductInCartSuffix = cart.getProductInCartSuffix
// const getProductInCartSuffix = () => {
//     const quantity_last_number = String(cart.cart_length).split('').pop();
//     if (quantity_last_number === '1') {
//         return "товар"
//     } else if (['2', '3', '4'].includes(quantity_last_number)) {
//         return "товара"
//     } else return "товаров"
// }
function to_order(){
    props.close_window()
    router.push({ name: 'order-create' })
}
</script>

<template>
    <ModalWindow width_window="500" height_window="800" :close_window="close_window">
        <div class="cart-wrapper d-flex flex-column" v-if="cart.cart_length > 0">
            <div class="cart-header">
                <h4 class="text-center mb-3">{{ cart.cart_length }} {{ getProductInCartSuffix() }} на {{
                    cart.total_price }}₽</h4>
                <h6 v-if="cart.get_minimum_amount_diference_for_free_delivery() > 0">До минимальной суммы на доставку —
                    {{ cart.get_minimum_amount_diference_for_free_delivery() }} ₽</h6>
                <hr>
            </div>
            <div class="cart-body">
                <div class="cart-product m-1" v-for="[slug, product] of Object.entries(cart.products_in_cart)">
                    <div class="row">
                        <div class="col-2"><img :src="product.data.image_url" width="50"></div>
                        <div class="col-8">
                            <h6>{{ product.data.title }}</h6>
                            <p>{{ product.data.description }}</p>
                        </div>
                        <div class="col-1 m-0 p-0">
                            <button @click="cart.delete_product_from_cart(slug)"
                                class="btn btn-outline-secondary btn-sm">X</button>
                        </div>
                    </div>
                    <div class="d-flex justify-content-between">
                        <div>{{ product.quantity * product.price }} ₽</div>
                        <div>
                            <IncrementDecrement 
                            :product_slug="slug" 
                            :quantity="product.quantity" />
                        </div>
                    </div>
                    <hr>
                </div>
            </div>
            <hr>
            <div class="cart-footer">
                <div class="d-flex justify-content-between">
                    <div><span>{{ cart.cart_length }} {{ getProductInCartSuffix() }}</span></div>
                    <div><span>{{ cart.total_price }}₽</span></div>
                </div>
                <hr>
                <div class="d-flex justify-content-between">
                    <div><span>Начислим бонусов</span></div>
                    <div><span>мало </span></div>
                </div>
                <hr>
            </div>
            <div class="cart-create_order text-center mt-auto">
                <button @click="to_order"
                 class="btn btn-success btn-lg">К оформлению заказа</button>
            </div>
        </div>
        <div v-else class="cart-empty-wrapper">
            <div class="cart-empty-content">
                <h4 class="mb-3 text-center">Ой, пусто!</h4>
                <p>Ваша корзина пуста, откройте «Меню» и выберите понравившийся товар. Мы доставим ваш заказ из
                    последних сил
                </p>
            </div>
        </div>
    </ModalWindow>
</template>

<style scoped>
.cart-empty-wrapper {
    position: absolute;
    margin: 0;
    padding: 0;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 10px;
}
.cart-empty-content {
    margin: 20px;
}
.cart-wrapper {
    margin: 10px;
    padding: 10px;
    min-height: 700px;
}

.cart-body {
    width: auto;
    overflow: scroll;
    overflow-x: hidden;
    margin: 10px;
    height: 400px;
}
.product_quantity_group_button {
    margin: 0;
    padding: 0;
    width: 100px;
    background-color: bisque;
    text-align: center;
    border-radius: 9999px;
}
</style>
<script setup>
import axios from "axios"
import router from '../router'
import { useCuctomerStore } from '@/stores/customer'
import { useCartStore } from '@/stores/cart'
import { ref, reactive, computed } from "vue"

const customer = useCuctomerStore()
const cart = useCartStore()

const auth = customer.check_auth()
const cart_length = cart.cart_length
const total_price = cart.total_price
const create_order_url = customer.get_url("create_order")

const getProductInCartSuffix = cart.getProductInCartSuffix

const user_data = customer.get_user_data()
const payment_option = [
    {name: "Картой на сайте"},
    {name: "Наличными"},
    {name: "SberPay"},
]
const order = reactive({
    name: user_data.nickname ? user_data.nickname : "",
    phone_number: user_data.phone_number ? user_data.phone_number : "",
    address: user_data.last_address ? user_data.last_address : "",
    token: user_data.user_token,
    promocode: '',
})
const order_items = reactive({})
const order_result = reactive({
    active: false,
    message: '',
})
function create_order(){
    const goods = cart.get_goods_to_order()
    const data = {
        "address": order.address,
        "goods": goods
    }
    const config = customer.get_config_to_order()

    axios.post(create_order_url, data, config)
    .then((res) => {
        console.log(res)
        customer.add_data_to_local_storage_after_order(order.name, order.phone_number, order.address)
        
        const order_items = cart.products_in_cart
        order_result.active = true
        cart.delete_cart()
    }).catch((err) => {
    console.log(err)
    })
}
function validate_data(){
    if(!order.name || !order.phone_number || !order.address ){
        return false
    } return true
}
const create_order_button_active = computed(() => {
    return validate_data()
})
</script>
<template>
    <div class="ms-4 me-4">
        <div v-if="cart_length > 0">
            <h1 class="text-center mb-4">Заказ на доставку</h1>
            <div class="row m-2">

                <div class="col-7">
                    <div class="row mt-1 mb-2">
                        <div class="col-4">
                            <h6>Имя</h6>
                        </div>
                        <div class="col-8">
                            <input 
                            v-model="order.name"
                            type="text" 
                            class="form-control" 
                            placeholder="Ваше имя">
                        </div>
                    </div>
                    <div class="row mt-1 mb-2">
                        <div class="col-4 mb-1">
                            <h6>Номер телефона</h6>
                        </div>
                        <div class="col-8">
                            <input 
                            v-model="order.phone_number"
                            type="tel" 
                            class="form-control" 
                            placeholder="Номер телефона">
                        </div>
                    </div>
                    <div class="row mt-1 mb-2">
                        <div class="col-4">
                            <h6>Адрес доставки</h6>
                        </div>
                        <div class="col-8">
                            <textarea 
                            v-model="order.address"
                            class="form-control" 
                            placeholder="Адрес доставки"
                            rows="4">
                                </textarea>
                        </div>
                    </div>
                    <div class="mt-3 promocode">
                        <h2 class="mb-3">Промокод</h2>
                        <div class="input-group">
                            <input type="text-aria" class="form-control" placeholder="Промокод" aria-label="Username"
                                aria-describedby="basic-addon1">
                            <button class="btn btn-outline-primary">Применить</button>
                        </div>
                    </div>
                    <div class="payment">
                        <h1>Способы оплаты</h1>


                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="payment" id="payment1">
                            <label class="form-check-label" for="payment1">
                                <h4>Картой на сайте</h4>
                            </label>
                        </div>

                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="payment" id="cash" checked>
                            <label class="form-check-label" for="cash">
                                <h4>Наличными</h4>
                            </label>
                        </div>

                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="payment" id="sberpay">
                            <label class="form-check-label" for="sberpay">
                                <h4>SberPay</h4>
                            </label>
                        </div>

                    </div>
                    <div class="d-flex justify-content-between mt-3 ps-1 pe-1">
                        <button 
                        class="btn btn-sm btn-outline-primary"
                        @click="router.push({name: 'home'})">Вернуться к меню</button>
                        <button 
                        :class="[{'disabled' : !create_order_button_active}, 'btn', 'btn-sm', 'btn-outline-success']"

                        @click="create_order">Оформить заказ на {{ total_price }} ₽</button>
                    </div>


                </div>

                <div class="col-5 ps-5">

                    <h3 class="text-center mb-3">
                        <span  v-if="order_result.active"
                        class="text-success">{{ order_result.message }}</span>
                        <span  v-else> Состав заказа</span>
        
                    </h3>
                    <div 
                    v-if="order_result.active" 
                    class="p-2 mb-4 d-flex flex-wrap justify-content-between border border-success rounded">
                        <div v-for="product in order_items">
                            <div><img :src="product.product_data.image_url" alt="" width="75"></div>
                            
                        </div>
                    </div>
                        <div class="order-items mt-1 mb-1 p-2 border" v-for="product in cart.products_in_cart">
                            <div class="row ">
                                <div class="col"><span>{{ product.data.title }}</span></div>
                                <div class="col d-flex align-items-center justify-content-end me-2">
                                    <span v-if="product.quantity > 1">{{ product.quantity }} × </span>
                                    <span >{{ product.price }} ₽</span></div>
                            </div>
                        </div>

                        <hr>
                        <div v-if="!order_result.active">
                            <div class="d-flex justify-content-between">
                                <div><span>{{ cart_length}} {{ getProductInCartSuffix() }}</span></div>
                                <div><span>{{ total_price }} ₽</span></div>
                            </div>
                            <div class="d-flex justify-content-between">
                                <div><span>Начислим бонусов</span></div>
                                <div><span>мало</span></div>
                            </div>
                            <div class="d-flex justify-content-between">
                                <div><span>Доставка</span></div>
                                <div><span>Бесплатно</span></div>
                            </div>
                        </div>
                        <hr>
                        <div class="d-flex justify-content-between">
                            <div>
                                <h5>Сумма заказа</h5>
                            </div>
                            <div>
                                <h5>{{ total_price }} ₽</h5>
                            </div>
                        </div>


                </div>
            </div>

        </div>
        <div v-else>
            <h1 class="text-center mb-4">Ваша карзина пуста =(</h1>
        </div>
    </div>
</template>
  
<style>
.promocode {
    max-width: 350px;
}

.payment {
    margin-top: 20px;
    background-color: rgba(148, 143, 143, 0.389);
    padding: 20px;
    border-radius: 25px;
}
</style>
  
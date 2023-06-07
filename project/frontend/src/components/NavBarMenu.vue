<script setup>
import router from '../router'
import { RouterLink } from 'vue-router'
import { useCuctomerStore } from '@/stores/customer'
import { ref, computed } from "vue";

const customer = useCuctomerStore()
const main_img = customer.get_url("main_img_url")
const auth = computed(() => {
    return customer.check_auth()
})
const cart_window_activ = ref(false)
const open_cart = () => {
    cart_window_activ.value = true
}
const close_cart = () => {
    cart_window_activ.value = false
}
</script>

<template>
    <div class="navbar-container  m-4">
        <CartWindow 
            v-if="cart_window_activ"
            :close_window="close_cart"
            />
        <div class="row">
            <div class="col-2">
                <img :src="main_img" alt="pizza-ava" width="100">
            </div>
            <div class="col-4">
                <h5>Noname Pissa Store </h5>
                <span>Сеть пиццерий № 99 в России</span>
            </div>
            <div class="col-4">
                <p>Доставка пиццы от 90 минут</p>
                <p>Если опоздаем, пицца за ваш счет</p>
            </div>
            <div class="col-2 nav-main-buttons d-flex flex-column">

                <button class="btn btn-outline-success btn-sm mb-1"
                @click="open_cart">Корзина</button>
                <button v-if="auth" class="btn btn-outline-success btn-sm mb-1" 
                @click="router.push({name: 'protfolio'})">Кабинет</button>
                <button v-if="auth" class="btn btn-outline-primary btn-sm mb-1" 
                @click="customer.logout()">Выйти</button>
                <button v-else class="btn btn-outline-success btn-sm mb-1" 
                @click="router.push({name: 'login'})">Войти</button>

            </div>
        </div>
        <div>
            <div class="d-flex flex-wrap justify-content-around m-2">
                
            <button class="btn btn-outline-secondary btn-sm mb-1" @click="router.push({name: 'home'})">Пицца</button>
            <button class="btn btn-outline-secondary btn-sm mb-1">Закуски</button>
            <button class="btn btn-outline-secondary btn-sm mb-1">Десерты</button>
            <button class="btn btn-outline-secondary btn-sm mb-1">Напитки</button>
            <button class="btn btn-outline-secondary btn-sm mb-1">Другие товары</button>
            <button class="btn btn-outline-secondary btn-sm mb-1">Акции</button>
            <button class="btn btn-outline-secondary btn-sm mb-1">Контакты</button>
            <button class="btn btn-outline-secondary btn-sm mb-1">О нас</button>

            </div>
        </div>
    </div>
</template>

<style scoped>
.nav-main-buttons button {
    width: 80px;
    padding: 0;
    margin: 0;
}
</style>

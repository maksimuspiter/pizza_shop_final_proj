<script setup>
import axios from "axios"
import router from '../router'

import { useCuctomerStore } from '@/stores/customer'
import { reactive, ref, onMounted } from "vue";

const customer = useCuctomerStore()
const login_url = customer.get_url("login")

const form_data = reactive({
  email: null,
  password: null,
  errors: [],
})

function login() {
  form_data.errors = []
  if (!form_data.email || !form_data.password) {
    form_data.errors.push("Заполните все поля формы")
    return false
  }
  axios.post(login_url, {
    "username": form_data.email,
    "password": form_data.password,
  }).then((res) => {

    customer.save_data_after_login(form_data.email, res.data.token)

    router.push({ name: 'home' })

  }).catch((err) => {
    console.log(err)
    form_data.errors = ["Непрвилная почта или пароль"]
  })
}
</script>

<template>
  <main class="content">
    <form @submit.prevent="login">

      <h4 class="text-center mb-4">Вход на сайт</h4>
      <div class="text-center text-danger">
        <h5 v-for="error in form_data.errors">{{ error }}</h5>
      </div>
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Почта</label>
        <input type="email" class="form-control" v-model="form_data.email">
      </div>

      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Пароль</label>
        <input type="password" class="form-control" v-model="form_data.password">
      </div>

      <div class="d-flex justify-content-center mt-3 mb-3">
        <button type="submit" class="btn btn-outline-primary">Войти</button>
      </div>

      <div class="text-center mt-5">
        <p>Если у вас еще нет аккаута, вы можете <a class="fs-5 text-success"
            @click="router.push({ name: 'register' })">зарегистрироваться</a></p>
      </div>
    </form>
  </main>
</template>

<style>
.content {
  margin-top: 40px;
  margin-left: 100px;
  margin-right: 100px;
  padding: 20px;
  border:  dashed rgb(1, 127, 20);
  border-radius: 90;
}
</style>

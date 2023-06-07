<script setup>
import axios from "axios"
import router from '../router'

import { useCuctomerStore } from '@/stores/customer'
import { reactive, ref, onMounted } from "vue";

const customer = useCuctomerStore()
const registr_url = customer.get_url("registr")

const form_data = reactive({
  email: null,
  password: null,
  password2: null,
  nickname: null,

  errors: [],
})
function validator(email, password, password2) {
  console.log('valid')

  if (!email || !password) {
    return ["Заполните все поля формы"]
  }
  if (password !== password2) {
    return ["Пароли не совпадают"]
  }
  if (password.length < 8) {
    return ["Пароль должен быть длиннее 8 символов"]
  } return null
}
function registration() {
  console.log('reg')
  form_data.errors = validator(form_data.email, form_data.password, form_data.password2)
  console.log(form_data.errors)

  if (!form_data.errors) {
    const nickname = form_data.nickname ? form_data.nickname : "Anonymous";
    console.log(nickname)

    axios.post(registr_url, {
      "email": form_data.email,
      "password": form_data.password,
      "password2": form_data.password2,
      "nickname": nickname
    })
      .then((res) => {
        if (res.data.create == true) {
          customer.save_data_after_registration(res.data.email, res.data.nickname, res.data.token)
          router.push({ name: 'home' })
        }
      }).catch((err) => {
        console.log(err)
        if (err.response.status == 304) {
          form_data.errors = ["Такой пользователь уже существует"]
        }
      })
  }
}

</script>

<template>
  <main class="content">
      <form @submit.prevent="registration">

        <h4 class="text-center mb-4">Регистрация</h4>
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

        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Пароль повторите</label>
          <input type="password" class="form-control" v-model="form_data.password2">
        </div>

        <div class="mb-3">
          <label class="form-label">НикНейм</label>
          <input type="text" class="form-control" v-model="form_data.nickname">
        </div>

        <div class="d-flex justify-content-center mt-3 mb-3">
          <button type="submit" class="btn btn-outline-primary">Регистрация</button>
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

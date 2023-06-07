<script setup>
import { useCuctomerStore } from '@/stores/customer'
import { reactive } from "vue";

const customer = useCuctomerStore()
const user_data = customer.get_user_data()

const form_data = reactive({
  name: user_data.nickname !== "null" ? user_data.nickname : "",
  email: user_data.email,
  phone_number: user_data.phone_number !== "null" ? user_data.phone_number : "",
  birthday: user_data.birthday !== "null" ? user_data.birthday : "",
})

function change_portfolio_data() {
  console.log('change')
}



</script>

<template>
  <main class="m-5">
    <div v-if="user_data.auth === true">
      <h1 class="text-center">Личные данные</h1>
      <div class="d-flex justify-content-center">
        <div>

        </div>
        <form class="portfolio-form " @submit.prevent="change_portfolio_data">

          <div class="mb-3">
            <label for="disabledTextInput" class="form-label">Имя</label>
            <input type="text" class="form-control" v-model="form_data.name">
          </div>

        <div class="mb-3">
          <label class="form-label">День рождения</label>
          <input type="date" class="form-control" v-model="form_data.birthday">
        </div>

        <div class="mb-3">
          <label class="form-label">Номер телефона</label>
          <input type="tel" class="form-control" v-model="form_data.phone_number">
        </div>

        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Эл. почта</label>
          <input type="email" class="form-control" v-model="form_data.email">
          </div>
        </form>

      </div>

      <!-- <div>
          <form @submit.prevent="change_portfolio_data">
            <div class="d-flex form-field">
              <div class="mb-3 col-10">
                <select id="disabledSelect" class="form-select form-sm">
                  <option>Disabled select</option>
                </select>
              </div>
              <div class="col-2">
                <button type="submit" class="btn btn-primary">Submit</button>
              </div>
            </div>
          </form>
        </div> -->
    </div>
    <div v-else>
      <h1 class="text-center">Вы еще не авторизованы!!!</h1>
    </div>
  </main>
</template>

<style>
.portfolio-form {

  max-width: 400px;
  margin-top: 10px;
  padding: 20px;
  border: 2px solid;
  border-color: #0d6efd;
  border-radius: 10px;
}

.form-field {
  max-width: 100px;
}</style>
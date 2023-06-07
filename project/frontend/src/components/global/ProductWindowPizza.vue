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
    image_url: String,
    min_price: Number,
    base_toppings: Array,
    options: Array
  },
  close_window: Function,
})

const size_options_button = reactive([
    { name: "Маленькая", value: "S", active: false },
    { name: "Средняя", value: "M", active: true },
    { name: "Большая", value: "L", active: false },
  ])

const category_options_button = reactive([
  { name: "Традиционное", value: 1, active: true, isDisabled: false },
  { name: "Тонкое", value: 2, active: false, isDisabled: false }
])

const middle_pizza = data.options.filter(
  (p) => p.category.id === 2 && p.size === "M" )[0]

const chosen_pizza = reactive({
  id: middle_pizza.id,
  category: middle_pizza.category,
  price: middle_pizza.price,
  size: middle_pizza.size,
  slug: middle_pizza.slug,
})

function change_pizza(chosen_pizza, new_pizza) {
  chosen_pizza.id = new_pizza.id
  chosen_pizza.category = new_pizza.category
  chosen_pizza.price = new_pizza.price
  chosen_pizza.size = new_pizza.size
  chosen_pizza.slug = new_pizza.slug
}

function change_button(arr, button) {
  arr.forEach((btn) => {
    btn == button ? btn.active = true : btn.active = false
  })
}

function change_pizza_size(size) {
  // Small pizza don't have a category.id=1 ("тонкое тесто")
  let new_pizza;
  if (size == "S") {
    category_options_button[1].isDisabled = true
    category_options_button[1].active = false
    category_options_button[0].active = true
    new_pizza = data.options.filter((p) => p.size == size && p.category.id == 1)[0]
  } else {
    category_options_button[1].isDisabled = false
    new_pizza = data.options.filter((p) => p.size == size && p.category.id === chosen_pizza.category.id)[0]
  }
  change_pizza(chosen_pizza, new_pizza)
}

function change_pizza_category(category_id) {
  const new_pizza = data.options.filter(
    (p) => p.category.id == category_id && p.size == chosen_pizza.size)[0]
  change_pizza(chosen_pizza, new_pizza)
}

const cart = useCartStore()
function to_cart() {
    const product = data
    const product_data = {title:product.title, description:product.description, image_url:product.image_url}
    cart.add_to_cart(chosen_pizza.id, product.product_name, product.slug, chosen_pizza.price, product_data)
    close_window()
}

</script>


<template>
<div class="pizza-window row">
      <div class="col mt-5" id="window-main-img">
        <img class="img-fluid" :src="data.image_url" alt="img" />
      </div>
      <div class="col d-flex align-items-center flex-column">
        <div class="mb-2">
          <div class="row">
            <h3 class="col-10 text-center p-2">{{ data.title }}</h3>
            <div class="col-2">
              <button type="button" class="btn btn-outline-secondary">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M12 20a8 8 0 100-16 8 8 0 000 16zm0 2c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"
                    fill="#000"></path>
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12 11a1 1 0 011 1v5a1 1 0 11-2 0v-5a1 1 0 011-1z"
                    fill="#000"></path>
                  <path d="M13.5 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z" fill="#000"></path>
                </svg>
              </button>
            </div>
          </div>
          <div class="p-1 mb-2">
            <span class="ms-1 me-1 badge rounded-pill bg-info text-dark" v-for="topping in data.base_toppings">
              {{ topping.title }}
            </span>
          </div>
        </div>
        <div class="mb-2 d-flex justify-content-center rounded-pill">
          <button v-for="button in size_options_button"
            :class="['btn', button.active ? 'btn-secondary' : 'btn-outline-secondary']"
            @click="change_pizza_size(button.value), change_button(size_options_button, button)">
            {{ button.name }}</button>
        </div>
        <div class="mt-2 mb-2 d-flex justify-content-center rounded-pill">
          <button v-for="button in category_options_button"
            :class="['btn', button.active ? 'btn-info' : 'btn-outline-info']" :disabled="button.isDisabled"
            @click="change_pizza_category(button.value), change_button(category_options_button, button)">
            {{ button.name }}</button>
        </div>
        <div class="d-flex flex-column">
          <h5>Тесто: {{ chosen_pizza.category.title }}</h5>
          <h5>Размер: {{ chosen_pizza.size }}</h5>
        </div>
      </div>
      <div class="mt-auto text-center">
        <button class="btn btn-outline-success" @click="to_cart">
          Добавить в корзину за {{ chosen_pizza.price }}
        </button>
      </div>

    </div> 
</template>

<style scoped></style>
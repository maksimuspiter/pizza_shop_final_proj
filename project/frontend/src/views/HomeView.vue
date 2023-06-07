<script setup>
import axios from "axios"

import { useProductListStore } from '@/stores/product_list'
import { onBeforeMount, ref, reactive } from "vue"

const product_list = useProductListStore()

const products = reactive({})
const products_title = product_list.get_all_products_title()
const products_url = product_list.get_all_products_url()

const product_window_activ = ref(false)
const product_window_data = ref(null)

const close_window = () => {
  product_window_activ.value = false
}
function product_window_close(){
  setTimeout(close_window, 200)
}
function product_window_open(data){
  product_window_data.value = data
  product_window_activ.value = true
} 

function get_products_data_from_server_or_pinia() {

  products_title.forEach(title => {
    const product = product_list.get_products_by_title(title)
    if (product) {
      products[title] = product
    } else {
      const url = products_url[title]
      axios.get(url)
        .then(response => {
          products[title] = response.data
          product_list.save_product_by_title(title, response.data)
        })
    }
  }
  )
}

onBeforeMount(() => {
  get_products_data_from_server_or_pinia()
})


</script>

<template>
  <main>
    <ProductWindow 
    v-if="product_window_activ"
    :data="product_window_data"
    :close_window="product_window_close"
    />

    <div class="product-list d-flex justify-content-around flex-wrap">
      <ProductCard 
      v-for="product in products.pizzas" 
      :product="product" 
      :open_window="product_window_open"
      button_title="Подробнее" />
    </div>

    <div class="product-list d-flex justify-content-around flex-wrap">
      <ProductCard 
      v-for="product in products.deserts" 
      :product="product" 
      :open_window="product_window_open"
      button_title="В корзину " />
    </div>
  </main>
</template>

<style scoped></style>

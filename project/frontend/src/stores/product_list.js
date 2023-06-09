import { reactive, computed } from "vue"
import { defineStore } from "pinia"

import axios from "axios"
import { useCuctomerStore } from "./customer"

export const useProductListStore = defineStore("product_list", () => {

  const customer = useCuctomerStore()
  const main_api_url = customer.get_url("main")
  const products_title = ["pizzas", "deserts"];

  const products_urls = {
    pizzas: main_api_url + "api-pizza/pizzas/",
    deserts: main_api_url + "api-pizza/desert/",

    drink: main_api_url + "api-pizza/drink/",
    other: main_api_url + "api-pizza/other/",
    snack: main_api_url + "api-pizza/snack/",

  }

  const products = reactive({});

  function get_products_by_title(product_title){
    console.log("get_products_by_title", product_title)

    return products[product_title]
  }
  const get_all_products_title = () => {
    return products_title
  }
  const get_all_products_url = () => {
    return products_urls
  }
  function save_product_by_title(title, data){
    console.log("save_product_by_title")
    products[title] = data
  }

  return {
    products,
    get_products_by_title,
    get_all_products_title,
    get_all_products_url,
    save_product_by_title
  };
});

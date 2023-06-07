import { reactive, ref, computed } from "vue";
import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", () => {
  const price_for_free_delivery = Number(600);
  const products_in_cart = reactive({});
  const cart_length = computed(() => {
    return _get_length(products_in_cart);
  });
  const total_price = computed(() => {
    return _get_total_price(products_in_cart);
  });

  function _get_total_price(products) {
    let total_price = 0;
    for (const key in products) {
      total_price +=
        Number(products[key].quantity) * Number(products[key].price);
    }
    return total_price;
  }

  function _get_length(products) {
    let length = 0;
    for (const key in products) {
      length += Number(products[key].quantity);
    }
    return length;
  }
// data = [title, description, image_url]
  function add_to_cart(
    id,
    content_type,
    slug,
    price,
    data,
    quantity = 1
  ) {
    if (products_in_cart[slug]) {
      products_in_cart[slug]["quantity"] += Number(quantity);
    } else {
      products_in_cart[slug] = {
        id: id,
        content_type: content_type,
        data: data,
        quantity: Number(quantity),
        price: Number(price),
      };
    }
  }
  function cart_product_decrement(slug) {
    if (products_in_cart[slug].quantity > 1) {
      products_in_cart[slug].quantity--;
    } else {
      delete products_in_cart[slug];
    }
  }
  function cart_product_increment(slug) {
    if (products_in_cart[slug]) {
      products_in_cart[slug].quantity++;
    }
  }
  function delete_product_from_cart(slug) {
    if (products_in_cart[slug]) {
      delete products_in_cart[slug];
    }
  }
  function delete_cart() {
    for (const key in products_in_cart) {
      delete products_in_cart[key];
    }
  }
  function get_minimum_amount_diference_for_free_delivery() {
    const dif = price_for_free_delivery - total_price;
    if (dif > 0) {
      return dif;
    }
    return 0;
  }
  function check_product_in_cart(slug) {
    if (products_in_cart[slug]) {
      return true;
    }
    return false;
  }
  function get_product_quantity(slug) {
    if (products_in_cart[slug]) {
      console.log(products_in_cart[slug].quantity);
      return products_in_cart[slug].quantity;
    }
    return 0;
  }
  const getProductInCartSuffix = () => {
    const quantity_last_number = String(cart_length.value).split('').pop();
    if (quantity_last_number === '1') {
        return "товар"
    } else if (['2', '3', '4'].includes(quantity_last_number)) {
        return "товара"
    } else return "товаров"
}
function get_goods_to_order(){
  const goods = [];
  for(const [slug, product] of Object.entries(products_in_cart)){

    goods.push({
          "content_type": product.content_type, 
          "object_id": product.id,
          "quantity": product.quantity } )
  }
  return goods
}

  return {
    products_in_cart,
    total_price,
    cart_length,
    add_to_cart,
    cart_product_increment,
    cart_product_decrement,
    delete_product_from_cart,
    delete_cart,
    get_minimum_amount_diference_for_free_delivery,
    check_product_in_cart,
    get_product_quantity,
    getProductInCartSuffix,
    get_goods_to_order,
  };
});

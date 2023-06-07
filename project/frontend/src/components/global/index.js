import ModalWindow from "./ModalWindow.vue";
import ProductCard from "./ProductCard.vue";
import ProductWindow from "./ProductWindow.vue";
import ProductWindowPizza from "./ProductWindowPizza.vue";
import ProductWindowSimple from "./ProductWindowSimple.vue";
import IncrementDecrement from "./IncrementDecrement.vue";
import CartWindow from "./CartWindow.vue";


const components = [
  { name: "ModalWindow", component: ModalWindow },
  { name: "ProductCard", component: ProductCard },
  { name: "ProductWindow", component: ProductWindow },
  { name: "CartWindow", component: CartWindow },


  { name: "ProductWindowPizza", component: ProductWindowPizza },
  { name: "ProductWindowSimple", component: ProductWindowSimple },
  { name: "IncrementDecrement", component: IncrementDecrement },
];

export default {
  install(app) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};

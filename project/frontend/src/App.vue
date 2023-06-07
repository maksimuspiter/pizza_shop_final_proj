<script setup>
import { RouterView } from 'vue-router'
import { onMounted } from "vue"
import { useCuctomerStore } from '@/stores/customer'

import NavBarMenu from './components/NavBarMenu.vue'
import FooterMenu from './components/FooterMenu.vue'

const customer = useCuctomerStore()
onMounted(() => {
  customer.load_user_data_from_local_storege()
})
</script>

<template>
  <NavBarMenu />
  <RouterView />
  <FooterMenu />
</template>

<style scoped></style>

<script setup>
import router from '../../router';

const props = defineProps({
    width_window: String,
    height_window: String,
    close_window: Function,
})

</script>

<template>
    <div class="modal-mask">
        <div class="modal-wrapper">
            <div class="modal-container" v-click-away="close_window" 
            :style="{width: width_window + 'px', height:height_window+'px'}">
                <slot />
            </div>
        </div>
    </div>
</template>

<style scoped>
.modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.62);
    display: table;
    transition: opacity 0.3s ease;
}

.modal-wrapper {
    display: table-cell;
    vertical-align: middle;
}

.modal-container {

    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 25px;
    box-shadow: 0 2px 8px rgba(82, 82, 82, 0.33);
    transition: all 0.3s ease;
}
</style>
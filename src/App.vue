<script setup>
import { RouterView } from 'vue-router'
import ToastNotification from '@/components/ToastNotification.vue';
</script>

<template>
  <div class="app-wrapper">
    <RouterView v-slot="{ Component }">
      <transition name="slide-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </RouterView>
    <ToastNotification />
  </div>
</template>

<style>
/* ... tus estilos globales o css imports ... */
</style>
<script setup>
import { RouterView } from 'vue-router';
</script>

<template>
  <transition name="slide-fade" mode="out-in">
    <RouterView />
  </transition>
</template>

<style scoped></style>

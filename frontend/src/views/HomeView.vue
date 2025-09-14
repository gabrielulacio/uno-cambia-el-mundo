<template>
  <div class="home-container">
    <NavigationBar />
    <HeroSection /> 
    <InfoCard />
  </div>
</template>

<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import HeroSection from '@/components/HeroSection.vue';
import ObjectiveSection from '@/components/ObjectiveSection.vue';
import InfoCard from '@/components/InfoCard.vue';
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background-color: var(--background-color);
}
</style>
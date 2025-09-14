<template>
  <div class="home-container">
    <NavigationBar />
    <HeroSection /> 
    <InfoCard />
    <FeatureCards />
    <CallToActionSection />
    <FooterSection />
  </div>
</template>

<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import HeroSection from '@/components/HeroSection.vue';
import InfoCard from '@/components/InfoCard.vue';
import FeatureCards from '@/components/FeatureCards.vue';
import CallToActionSection from '@/components/CallToActionSection.vue';
import FooterSection from '@/components/FooterSection.vue';
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background-color: var(--background-color);
}
</style>
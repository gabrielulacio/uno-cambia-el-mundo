<template>
  <div class="home-container">
    <NavigationBar />
    <HeroSection /> 
    <BrandIntro />
    <FeaturedProjects />
    <ImpactMetrics />
    <FooterSection />
  </div>
</template>

<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import HeroSection from '@/components/HeroSection.vue';
import BrandIntro from '@/components/BrandIntro.vue';
import FeaturedProjects from '@/components/FeaturedProjects.vue';
import ImpactMetrics from '@/components/ImpactMetrics.vue';
import FooterSection from '@/components/FooterSection.vue';
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
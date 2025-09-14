<template>
  <div class="about-container">
    <NavigationBar />

    <main class="about-content">
      <!-- Contenido a agregar próximamente -->
      <section class="about-hero">
        <h1 class="about-title">Acerca de</h1>
        <p class="about-subtitle">Esta página contendrá información sobre la campaña y el equipo.</p>
      </section>
    </main>

    <FooterSection />
  </div>
</template>

<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import FooterSection from '@/components/FooterSection.vue';
</script>

<style scoped>
.about-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--background-color);
}

.about-content {
  flex: 1 1 auto;
  background-color: #ffffff; /* fondo blanco para el contenido */
}

.about-hero {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.about-title {
  margin: 0 0 8px 0;
}

.about-subtitle {
  margin: 0;
}
</style>

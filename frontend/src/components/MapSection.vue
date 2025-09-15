<template>
  <section class="map-sponsors-section">
    <div class="map-container">
      <!-- Reemplaza el src con la ubicación real de tu centro -->
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3953.239252233995!2d-72.21757248044014!3d7.764433104542299!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e666d219d861935%3A0xe9dba25322c511b5!2sLaboratorio%20de%20la%20Fundaci%C3%B3n%20Centro%20M%C3%A9dico%20Rotario%20Dr.%20Pablo%20Puky!5e0!3m2!1ses!2sve!4v1757908670705!5m2!1ses!2sve"
        width="100%"
        height="250"
        style="border:0;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
    </div>
    <div class="sponsors-container">
      <img src="/images/hero-bg.jpg" alt="Patrocinadores" class="sponsors-placeholder" />
      <p class="sponsors-text">Foto del centro médico</p>
    </div>
  </section>
</template>

<script setup>
// No necesitas lógica por ahora
</script>

<style scoped>
.map-sponsors-section {
  display: flex;
  gap: 2rem;
  margin: 3rem 0;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.map-container,
.sponsors-container {
  flex: 1 1 300px;
  max-width: 500px;
  min-width: 250px;
}

.sponsors-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sponsors-placeholder {
  width: 100%;
  height: 250px;
  object-fit: cover;
  border-radius: 8px;
  background: #eee;
}

.sponsors-text {
  text-align: center;
  margin-top: 0.5rem;
  color: #888;
}
</style>
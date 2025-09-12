<template>
  <section class="objective-section">
    <div class="objective-container">
      <h2 class="objective-title">Nuestro Objetivo</h2>
      
      <div class="progress-wrapper">
        <DonationProgressBar :goal="goal" :current="current" />
        <p class="progress-description">
          Cada aporte, grande o pequeño, es un paso hacia un mejor centro médico.
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DonationProgressBar from '@/components/DonationProgressBar.vue';
import { getDonationStatus } from '@/services/api.js';

// Estados reactivos
const goal = ref(100000);
const current = ref(100000); // 100% como se ve en la imagen
const loading = ref(true);
const error = ref(null);

// Intentar cargar datos reales de la API
onMounted(async () => {
  try {
    // Descomenta esto cuando la API esté lista
    // const data = await getDonationStatus();
    // goal.value = data.goal;
    // current.value = data.current;
    
    // Por ahora usamos datos mock que muestran 100%
    loading.value = false;
  } catch (err) {
    console.error('Error loading donation status:', err);
    // Mantener valores por defecto en caso de error
    loading.value = false;
  }
});
</script>

<style scoped>
.objective-section {
  background: linear-gradient(135deg, var(--rotary-blue) 0%, #1e5aa8 100%);
  padding: 80px 0;
  position: relative;
}

.objective-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  text-align: center;
}

.objective-title {
  color: var(--rotary-gold);
  font-size: 2.5rem;
  font-weight: 600;
  margin-bottom: 50px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.progress-wrapper {
  max-width: 600px;
  margin: 0 auto;
}

.progress-description {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.2rem;
  margin-top: 30px;
  font-weight: 400;
  line-height: 1.6;
}

/* Responsive */
@media (max-width: 768px) {
  .objective-section {
    padding: 60px 0;
  }
  
  .objective-title {
    font-size: 2rem;
    margin-bottom: 40px;
  }
  
  .progress-description {
    font-size: 1.1rem;
    margin-top: 25px;
  }
}

@media (max-width: 480px) {
  .objective-title {
    font-size: 1.7rem;
  }
  
  .progress-description {
    font-size: 1rem;
  }
}</style>
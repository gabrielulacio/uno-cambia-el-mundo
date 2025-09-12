<template>
  <div class="donation-container">
    <div v-if="loading" class="loading-message">
      Cargando datos de la donación...
    </div>
    
    <div v-if="error" class="error-message">
      <p>Error al cargar los datos. Por favor, intenta de nuevo más tarde.</p>
      <p>Detalle: {{ error }}</p>
    </div>

    <!-- La tarjeta principal ahora tiene el fondo azul y texto blanco -->
    <div v-if="!loading && !error" class="progress-section">
      <h1>Nuestra Meta</h1>
      <p>Tu donación nos acerca a nuestro objetivo.</p>
      
      <DonationProgressBar :goal="donationStatus.goal" :current="donationStatus.current" />
      
      <div class="donation-summary">
        <p><strong>Meta:</strong> ${{ donationStatus.goal.toLocaleString() }}</p>
        <p><strong>Recaudado:</strong> ${{ donationStatus.current.toLocaleString() }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DonationProgressBar from '@/components/DonationProgressBar.vue';
import { getDonationStatus } from '@/services/api.js';

const donationStatus = ref({
  goal: 10000,
  current: 10000,
});
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    //const data = await getDonationStatus();
    //donationStatus.value = data;
  } catch (err) {
    error.value = err.message || 'Error desconocido';
    console.error('Error fetching donation status:', err);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
:root {
  --rotary-blue: #17458f;
}

.donation-container {
  font-family: 'Inter', sans-serif;
  color: #333;
  text-align: center;
  padding: 20px;
  background-color: #f0f4f8;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.progress-section {
  /* Cambio de color de la tarjeta a azul */
  background-color: var(--rotary-blue);
  color: white; /* Cambio de color del texto para contraste */
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 500px;
}

h1 {
  color: white;
}

p {
    color: rgba(255, 255, 255, 0.85);
}

.donation-summary {
  margin-top: 20px;
  font-size: 1.2rem;
}

.donation-summary p {
    color: white;
}

.loading-message, .error-message {
    margin-top: 20px;
    font-size: 1.1rem;
    color: #555;
}

.error-message {
    color: #d9534f;
    background-color: #f2dede;
    border: 1px solid #ebccd1;
    padding: 15px;
    border-radius: 8px;
}
</style>


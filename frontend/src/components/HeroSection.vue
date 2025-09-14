<template>
  <section class="hero-section">
    <div class="hero-container">
      <div class="hero-content">
        <div class="hero-logo">
          <img src="/images/unocambiaelmundo-logo.png" alt="Logo de Uno Cambia el Mundo" />
          <p class="hero-subtitle">
            Alimentar, Educar y Sanar. Todo empieza con un gesto.
          </p>
        </div>

        <div class="meta">
          <p class="title-meta">Nuestra Meta</p>
          <DonationProgressBar :goal="goal" :current="current" />
          <p class="subtitle-meta">Cada aporte, grande o pequeño, es un paso hacia un mejor centro médico.</p>
        </div>
      </div>

      
    
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DonationProgressBar from '@/components/DonationProgressBar.vue';
import { getDonationStatus } from '@/services/api.js';

// Estados reactivos
const goal = ref(100);
const current = ref(20); // 100% como se ve en la imagen
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

<style scoped lang="scss">

.title-meta {
  @include heading-2;
  color: var(--rotary-gold);
}

.subtitle-meta {
  @include paragraph-semibold;
  color: var(--white);
}

.hero-section {
  /* Degradado vertical: Rotary Blue (arriba) -> Azure (abajo, 80%-100%) */
  background: linear-gradient(to bottom, var(--rotary-blue) 0%, var(--azure) 80%, var(--azure) 100%);
  min-height: 60vh;
  display: flex;
  justify-content: center;
  position: relative;
  overflow: hidden;
  padding: 96px 0;
}

.hero-section::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: url('/images/hero-bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.2; 
  pointer-events: none;
  z-index: 1;
}

.hero-container {
  
  max-width: 1200px;
  margin: 0 auto;
  
  padding: 60px 20px;
  text-align: center;
  position: relative;
  z-index: 2; /* sobre la imagen */
  
  
}

.hero-content {
  max-width: 800px;
  gap: 64px;
  display: flex;
  flex-direction: column;
}

.hero-subtitle {
  @include heading-3;
  color: var(--white);
  margin: 0;
}


.floating-circle {
  position: absolute;
  border-radius: 50%;
  background: rgba(247, 168, 27, 0.1);
  animation: float 6s ease-in-out infinite;
}

/* Animaciones */
@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes float {
  0%, 100% { 
    transform: translateY(0px) scale(1);
    opacity: 0.3;
  }
  50% { 
    transform: translateY(-20px) scale(1.1);
    opacity: 0.6;
  }
}

/* Responsive */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .uno {
    font-size: 3rem;
  }
  
  .globe {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.1rem;
  }
  
  .hero-container {
    padding: 40px 20px;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 2rem;
  }
  
  .uno {
    font-size: 2.5rem;
  }
  
  .globe {
    font-size: 2rem;
  }
}</style>
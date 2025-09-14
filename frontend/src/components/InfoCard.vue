<template>
  <section class="info-section">
    <div class="info-container">
      <div class="info-card">
        <div class="card-image">
          <!-- Placeholder para la imagen médica -->
          <div class="image-placeholder">
            <img v-if="imageUrl" :src="imageUrl" alt="Imagen informativa" class="image-fill" />
            <div v-else class="stethoscope-icon">🩺</div>
          </div>
        </div>
        
        <div class="card-content">
          <div class="card-text">
            <p class="card-paragraph">
              Atendemos a <strong>27 mil personas</strong> al año, pero nuestros equipos ya no responden como deberían. Con <strong>tu ayuda</strong>, podemos cambiarlos y <strong>marcar la diferencia</strong> entre la esperanza y la incertidumbre.
            </p>
          </div>
        </div>
        
      </div>
    </div>
  </section>
</template>

<script setup>
const imageUrl = '/images/tarjeta-1.png';
</script>

<style scoped lang="scss">
.info-section {
  background-color: var(--background-color);
  padding: 80px 0;
}

.info-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.info-card {
  background-color: white;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  display: flex;
  align-items: center;
  max-width: 900px;
  margin: 0 auto;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.info-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.card-image {
  flex: 0 0 300px;
  height: 250px;
  position: relative;
  overflow: hidden;
}

.image-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #f0f4f8 0%, #e2e8f0 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

/* La imagen llena el placeholder manteniendo proporción */
.image-fill {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover; /* usa 'contain' si prefieres ver la imagen completa sin recorte */
}

.stethoscope-icon {
  font-size: 4rem;
  opacity: 0.6;
  z-index: 1;
  position: relative;
}

.card-content {
  flex: 1;
  padding: 40px;
}

.card-text {
  color: var(--black);
  line-height: 1.7;
}

.card-paragraph {
  @include heading-4;
  margin-bottom: 20px;
  text-align: justify;
}

.card-paragraph:last-child {
  margin-bottom: 0;
  color: var(--black);
}

/* Responsive */
@media (max-width: 768px) {
  .info-card {
    flex-direction: column;
    text-align: center;
  }
  
  .card-image {
    flex: none;
    width: 100%;
    height: 200px;
  }
  
  .card-content {
    padding: 30px 25px;
  }
  
  .card-paragraph {
    font-size: 1rem;
    text-align: left;
  }
}

@media (max-width: 480px) {
  .info-section {
    padding: 50px 0;
  }
  
  .card-content {
    padding: 25px 20px;
  }
  
  .card-paragraph {
    font-size: 0.95rem;
    margin-bottom: 15px;
  }
}</style>
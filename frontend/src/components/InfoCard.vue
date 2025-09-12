<template>
  <section class="info-section">
    <div class="info-container">
      <div class="info-card">
        <div class="card-image">
          <!-- Placeholder para la imagen médica -->
          <div class="image-placeholder">
            <div class="stethoscope-icon">🩺</div>
          </div>
        </div>
        
        <div class="card-content">
          <div class="card-text">
            <p class="card-paragraph">
              En la Fundación Centro Médico Rotario Dr Pablo Puky atendemos a cientos de 
              personas cada mes. Sin embargo, nuestros equipos ya no responden como 
              deberían, lo que limita nuestra capacidad de salvar vidas. Hoy tenemos la 
              oportunidad de cambiar esta realidad.
            </p>
            
            <p class="card-paragraph">
              Con tu ayuda, podemos dotar al centro con nuevos equipos que marcarán la 
              diferencia entre la esperanza y la incertidumbre.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// No props needed for this static component
</script>

<style scoped>
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

/* Efecto de imagen médica simulada */
.image-placeholder::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 30% 30%, rgba(23, 69, 143, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 70% 70%, rgba(247, 168, 27, 0.1) 0%, transparent 50%);
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
  color: var(--text-color);
  line-height: 1.7;
}

.card-paragraph {
  font-size: 1.1rem;
  margin-bottom: 20px;
  text-align: justify;
}

.card-paragraph:last-child {
  margin-bottom: 0;
  font-weight: 500;
  color: var(--rotary-blue);
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
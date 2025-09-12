<template>
  <section class="hero-section">
    <div class="hero-container">
      <div class="hero-content">
        <h1 class="hero-title">
          <span class="uno">Uno</span><br>
          <span class="cambia">cambia el mund</span><span class="globe">🌍</span>
        </h1>
        
        <p class="hero-subtitle">
          Alimentar, Educar y Sanar. Todo empieza con un gesto.
        </p>
      </div>
      
      <!-- Elementos decorativos de fondo -->
      <div class="hero-decoration">
        <div class="floating-circle circle-1"></div>
        <div class="floating-circle circle-2"></div>
        <div class="floating-circle circle-3"></div>
      </div>
    </div>
  </section>
</template>

<script setup>
// No props needed
</script>

<style scoped>
.hero-section {
  background: linear-gradient(135deg, var(--rotary-blue) 0%, #1e5aa8 100%);
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 20px;
  text-align: center;
  position: relative;
  z-index: 2;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero-title {
  font-size: 4rem;
  font-weight: 300;
  color: white;
  margin-bottom: 30px;
  line-height: 1.1;
}

.uno {
  font-style: italic;
  font-weight: 300;
  font-size: 4.5rem;
}

.cambia {
  font-weight: 400;
}

.globe {
  font-size: 3.5rem;
  margin-left: 10px;
  display: inline-block;
  animation: rotate 6s linear infinite;
}

.hero-subtitle {
  font-size: 1.4rem;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 400;
  margin: 0;
  letter-spacing: 0.5px;
}

/* Elementos decorativos flotantes */
.hero-decoration {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.floating-circle {
  position: absolute;
  border-radius: 50%;
  background: rgba(247, 168, 27, 0.1);
  animation: float 6s ease-in-out infinite;
}

.circle-1 {
  width: 200px;
  height: 200px;
  top: 10%;
  left: 5%;
  animation-delay: 0s;
}

.circle-2 {
  width: 150px;
  height: 150px;
  top: 60%;
  right: 10%;
  animation-delay: 2s;
}

.circle-3 {
  width: 100px;
  height: 100px;
  bottom: 20%;
  left: 15%;
  animation-delay: 4s;
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
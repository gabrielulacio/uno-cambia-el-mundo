<template>
  <section class="cta-section">
    <div class="cta-container">
      <div class="cta-content">
        <div class="cta-text-wrapper">
          <p class="cta-main-text">La salud no puede esperar.</p>
          <p class="cta-main-text">Súmate a esta campaña y ayúdanos a lograrlo.</p>
        </div>

        <div class="cta-button-wrapper">
          <router-link to="/donar" class="cta-donate-button">
            Dona ahora 💛
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// No props needed for static CTA
</script>

<style scoped lang="scss">

.cta-section {
  background-color: #f0f4f9;
  padding: 32px;
  text-align: center;
}

.cta-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px;
}

.cta-content {
  display: flex;
  flex-direction: row;            
  justify-content: space-between; 
  align-items: center;
  gap: 20px;
}

.cta-text-wrapper {
  text-align: left; /* Alinea el texto a la izquierda dentro de su contenedor */
  padding: 24px 0;
}

.cta-main-text {
    @include heading-3; 
    color: var(--black);
    margin: 0 0 4px 0; 
    font-style: italic;
    font-weight: 600; 
    font-family: 'Open Sans', Arial, sans-serif;
    text-align: center;
}

/* Nueva clase para el texto secundario */
.cta-sub-text {
  @include paragraph-regular;
  color: var(--black);
  margin: 0;
  font-family: 'Open Sans', Arial, sans-serif;
}

.cta-button-wrapper {
  margin-top: 0; /* Ya no se necesita el margen superior */
}

.cta-donate-button {
  @include paragraph-bold;
  background-color: #0066cc; /* Color azul sólido como en la imagen */
  color: var(--white);
  padding: 16px 36px;
  border-radius: 50px;
  text-decoration: none;
  font-size: 1.13rem;
  font-weight: 700;
  box-shadow: 0 4px 15px rgba(0, 102, 204, 0.3);
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.cta-donate-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 102, 204, 0.4);
  background-color: #0052a3;
}

@media (max-width: 768px) {
  .cta-section {
    padding: 40px 0;
  }
  
  .cta-content {
    flex-direction: column; 
    text-align: center;
    gap: 24px;
  }
  
  .cta-text-wrapper {
    text-align: center;
  }

  .cta-main-text {
    font-size: 1.5rem;
  }

  .cta-sub-text {
    font-size: 1rem;
  }
}
</style>
<template>
  <section class="hero-section">
    <div class="hero-background">
      <div class="overlay"></div>
      <!-- Action Ticker moving inside background to avoid layout issues -->
      <div class="action-ticker">
        <div class="ticker-content">
          <span>{{ $t('hero.ticker_text') }}</span>
          <span>{{ $t('hero.ticker_text') }}</span>
        </div>
      </div>
    </div>

    <div class="hero-content">
      <div class="rotary-badge">
        <span class="badge-text">{{ $t('hero.rotary_initiative') }} <strong>{{ $t('hero.rotary_name') }}</strong></span>
      </div>

      <div class="brand-logo-container">
        <img 
          src="@/assets/images/unocambiaelmundo-logo.png" 
          alt="Uno Cambia el Mundo" 
          class="hero-brand-logo"
        />
      </div>

      <p class="hero-subtitle" v-html="$t('hero.subtitle')"></p>

      <div class="cta-group">
        <router-link to="/donar" class="btn btn-primary">
          {{ $t('hero.cta_donate') }}
        </router-link>
        <router-link to="/proyectos" class="btn btn-outline">
          {{ $t('hero.cta_projects') }}
        </router-link>
      </div>
    </div>
  </section>
</template>

<style scoped lang="scss">
.hero-section {
  position: relative;
  height: 90vh; /* Un poco más alto para que quepa todo bien */
  min-height: 650px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  color: var(--white);
  padding: 0 20px;
  /* Compensamos la altura del header fijo para que quede centrado visualmente */
  padding-top: 100px; 
}

/* Fondo */
.hero-background {
  position: absolute;
  inset: 0;
  z-index: 0;
  background-image: url('@/assets/images/hero-bg.png');
  background-size: cover;
  background-position: center;
}

.overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(23, 69, 143, 0.5) 0%,
    rgba(0, 0, 0, 0.85) 100%
  );
}

/* Contenido */
.hero-content {
  position: relative;
  z-index: 1;
  max-width: 800px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 28px; /* Espacio entre elementos */
  animation: fadeUp 1s ease-out;
}

/* Badge Rotary */
.rotary-badge {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  padding: 6px 14px;
  border-radius: 50px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  margin-bottom: 8px;
}
.badge-text {
  font-size: 0.85rem;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

/* LOGO */
.hero-brand-logo {
  width: 100%;
  max-width: 450px; /* Tamaño máximo controlado */
  height: auto;
  filter: drop-shadow(0 4px 10px rgba(0,0,0,0.3)); /* Sombra para que flote */
}

/* Subtítulo */
.hero-subtitle {
  font-size: 1.35rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.95);
  font-weight: 400;
  max-width: 600px;
  margin: 0;
}

/* Botones */
.cta-group {
  display: flex;
  gap: 16px;
  margin-top: 8px;
}

.btn {
  padding: 14px 32px;
  border-radius: 50px; /* Botones redondos se ven más modernos */
  font-weight: 700;
  font-size: 1rem;
  text-decoration: none;
  transition: all 0.3s ease;
}

.btn-primary {
  background-color: var(--rotary-gold);
  color: var(--rotary-blue);
  box-shadow: 0 4px 15px rgba(247, 168, 27, 0.4); /* Glow dorado */
  
  &:hover {
    transform: translateY(-2px);
    background-color: #ffb84d;
  }
}

.btn-outline {
  background: rgba(255,255,255,0.1);
  color: var(--white);
  border: 1px solid rgba(255,255,255,0.4);
  backdrop-filter: blur(4px);
  
  &:hover {
    background-color: var(--white);
    color: var(--rotary-blue);
  }
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Action Ticker Styles */
.action-ticker {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: var(--rotary-gold);
  color: var(--rotary-blue);
  padding: 8px 0; /* Un poco mas pequeño */
  overflow: hidden;
  z-index: 5; /* Por encima del overlay pero puede estar bajo el contenido si se solapan */
  border-top: 1px solid rgba(255, 255, 255, 0.3);
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.85rem; /* Ajuste tamaño */
  letter-spacing: 1px;
}

.ticker-content {
  display: flex;
  white-space: nowrap;
  animation: ticker-animation 30s linear infinite;
  gap: 0;
}

.ticker-content span {
  display: inline-block;
  padding-right: 20px; /* Space between repeated text */
}

@keyframes ticker-animation {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* Responsive */
@media (max-width: 768px) {
  .hero-brand-logo { max-width: 280px; } /* Más pequeño en celular */
  .hero-subtitle { font-size: 1.1rem; }
  .cta-group { flex-direction: column; width: 100%; max-width: 300px; }
  .btn { width: 100%; text-align: center; }
  
  .action-ticker {
    font-size: 0.75rem;
    padding: 8px 0;
  }
}
</style>
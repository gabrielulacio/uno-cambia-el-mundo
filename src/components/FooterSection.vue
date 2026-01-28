<template>
  <footer class="footer-section">
    <div class="footer-container">
      
      <div class="footer-col brand-col">
        <img src="@/assets/images/unocambiaelmundo-logo.png" alt="Logo" class="footer-logo" />
        <p class="footer-desc" v-html="$t('footer.desc')"></p>
      </div>

      <div class="footer-col links-col">
        <h4>{{ $t('footer.explore') }}</h4>
        <nav class="footer-nav">
          <router-link to="/">{{ $t('nav.start') }}</router-link>
          <router-link to="/proyectos">{{ $t('nav.projects') }}</router-link>
          <router-link to="/donar">{{ $t('footer.how_to_donate') }}</router-link>
        </nav>
      </div>

      <div class="footer-col contact-col">
        <h4>{{ $t('footer.contact') }}</h4>
        <p>San Cristóbal, Táchira.</p>
        <a href="mailto:rotarysc@gmail.com" class="contact-link">rotarysc@gmail.com</a>
        <div class="footer-social">
          <a href="https://www.instagram.com/rotary_sc/" target="_blank" class="social-link" :aria-label="$t('nav.instagram_aria')">
            <InstagramIcon :size="18" />
            <span>@rotary_sc</span>
          </a>
        </div>
      </div>
    </div>
    
    <div class="dev-credits">
      <p class="credits-label" v-html="$t('footer.dev_credits')"></p>
      <div v-if="$tm('footer.devs')" class="dev-names">
        <template v-for="(dev, index) in $tm('footer.devs')" :key="index">
          <a :href="$rt(dev.url)" target="_blank" class="dev-name">{{ $rt(dev.name) }}</a>
          <span v-if="index < $tm('footer.devs').length - 1" class="separator">•</span>
        </template>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; {{ new Date().getFullYear() }} Uno Cambia el Mundo. {{ $t('footer.all_rights') }}</p>
    </div>
  </footer>
</template>

<script setup>
import InstagramIcon from '@/components/icons/InstagramIcon.vue'
</script>

<style scoped lang="scss">
.footer-section {
  background-color: var(--rotary-blue); /* Azul oscuro corporativo */
  color: var(--white);
  padding-top: 64px; /* Espacio arriba */
  font-size: 0.95rem;
  /* El padding bottom se maneja en los hijos para que queden pegados al borde */
}

/* --- ESTRUCTURA PRINCIPAL (GRID) --- */
.footer-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr; /* La primera columna es más ancha */
  gap: 60px;
  margin-bottom: 48px;

  @media (max-width: 768px) {
    grid-template-columns: 1fr; /* En móvil, una sola columna */
    gap: 40px;
    text-align: center;
  }
}

/* --- ESTILOS DE COLUMNAS --- */
.footer-logo {
  max-width: 180px; /* Controla el tamaño del logo */
  width: 100%;      /* Asegura que sea responsive */
  margin-bottom: 16px;
  /* Nota: Sin filtro invertido para respetar colores amarillo/blanco */
}

.footer-desc {
  line-height: 1.6;
  opacity: 0.8;
  max-width: 300px;
  /* Centrar texto en móvil si es necesario */
  @media (max-width: 768px) { margin: 0 auto; }
}

h4 {
  font-size: 1.1rem;
  margin-bottom: 20px;
  color: var(--rotary-gold);
  font-weight: 700;
}

.footer-nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-nav a, .contact-link {
  color: var(--white);
  text-decoration: none;
  opacity: 0.8;
  transition: opacity 0.2s;

  &:hover { opacity: 1; color: var(--rotary-gold); }
}

.footer-social {
  margin-top: 20px;
  
  @media (max-width: 768px) {
    display: flex;
    justify-content: center;
  }
}

.social-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--white);
  text-decoration: none;
  background: rgba(255, 255, 255, 0.1);
  padding: 8px 16px;
  border-radius: 50px;
  font-size: 0.9rem;
  transition: all 0.3s ease;

  &:hover {
    background: var(--rotary-gold);
    color: var(--rotary-blue);
    transform: translateY(-2px);
  }

  svg {
    stroke-width: 2.5px;
  }
}

/* --- ESTILOS NUEVOS PARA CRÉDITOS --- */
.dev-credits {
  background: rgba(0, 0, 0, 0.2); /* Fondo ligeramente más oscuro */
  padding: 24px 20px;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.credits-label {
  margin: 0 0 8px;
  font-size: 0.9rem;
  opacity: 0.9;
  
  strong {
    color: var(--rotary-gold);
  }
}

.dev-names {
  display: flex;
  justify-content: center;
  gap: 12px;
  flex-wrap: wrap;
  font-size: 0.9rem;
  font-weight: 600;
  color: #fff;
}

.separator {
  color: var(--rotary-gold);
  opacity: 0.6;
}

.dev-name {
  color: var(--white);
  text-decoration: none;
  transition: all 0.2s;
  opacity: 0.85;

  &:hover {
    opacity: 1;
    color: var(--rotary-gold);
    text-decoration: underline;
  }
}

/* --- COPYRIGHT FINAL --- */
.footer-bottom {
  background: rgba(0, 0, 0, 0.4); /* Fondo más oscuro para el cierre */
  padding: 16px;
  text-align: center;
  font-size: 0.8rem;
  opacity: 0.6;
}
</style>
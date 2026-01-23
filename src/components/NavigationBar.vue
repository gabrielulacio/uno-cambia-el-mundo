<template>
  <nav class="navbar" :class="{ 'navbar-solid': isSolid }">
    <div class="navbar-container">
      <router-link to="/" class="rotary-logo" :aria-label="$t('nav.home_aria')">
        <img src="@/assets/images/logo-rotary.png" alt="Rotary Logo" class="nav-logo-img" />
      </router-link>
      
      <div class="navbar-menu">
        <router-link to="/" class="navbar-link">{{ $t('nav.start') }}</router-link>
        <router-link to="/proyectos" class="navbar-link">{{ $t('nav.projects') }}</router-link>
        
        <!-- Selector de Idioma -->
        <button @click="toggleLanguage" class="navbar-link lang-switcher" aria-label="Cambiar idioma">
          {{ currentLanguage }}
        </button>

        <a href="https://www.instagram.com/rotary_sc/" target="_blank" class="navbar-link instagram-icon" :aria-label="$t('nav.instagram_aria')">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <router-link to="/donar" class="navbar-link donate-btn">
          {{ $t('nav.donate') }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { computed } from 'vue';
import { useI18n } from 'vue-i18n';

const { locale } = useI18n();

defineProps({
  isSolid: {
    type: Boolean,
    default: false
  }
});

const currentLanguage = computed(() => locale.value.toUpperCase());

const toggleLanguage = () => {
  locale.value = locale.value === 'es' ? 'en' : 'es';
};
</script>

<style scoped lang="scss">
.navbar {
  position: absolute; /* Clave: Flota sobre el contenido */
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100; /* Asegura que esté encima de la foto */
  padding: 24px 0 32px; /* Más padding, especialmente abajo */
  background: linear-gradient(to bottom, rgba(0,0,0,0.6) 0%, transparent 100%); /* Sombra suave para leer */
  transition: background-color 0.3s ease;
}

.navbar-solid {
  background: var(--rotary-blue) !important;
  position: relative;
  padding: 16px 0; /* Un poco más compacta si es sólida */
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
}

.nav-logo-img {
  height: 50px; /* Controlamos la altura para que no se vea gigante */
  width: auto;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: 40px;
}

.navbar-link {
  color: var(--white); /* Texto blanco para resaltar sobre foto oscura */
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  transition: opacity 0.3s ease;
  text-shadow: 0 2px 4px rgba(0,0,0,0.3);
  background: none;
  border: none;
  cursor: pointer;
  font-family: inherit;

  &:hover {
    opacity: 0.8;
  }
}

.lang-switcher {
  border: 1px solid rgba(255, 255, 255, 0.4);
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  min-width: 38px;
  text-align: center;
  
  &:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: var(--white);
  }
}

.instagram-icon {
  display: flex;
  align-items: center;
  padding: 5px;
  
  svg {
    transition: transform 0.2s ease;
  }
  
  &:hover svg {
    transform: scale(1.1);
  }
}

/* Botón de Donar Estilizado en el Menú */
.donate-btn {
  background: var(--rotary-gold);
  color: var(--rotary-blue);
  padding: 10px 24px;
  border-radius: 50px;
  font-weight: 700;
  text-shadow: none;
  transition: transform 0.2s ease;

  &:hover {
    transform: scale(1.05);
    opacity: 1;
  }
}

@media (max-width: 768px) {
  .navbar-menu { gap: 15px; }
  .navbar-link:not(.donate-btn):not(.instagram-icon) { display: none; } /* En móvil a veces ocultamos enlaces y dejamos solo Donar o Menú Hambuguesa */
}
</style>
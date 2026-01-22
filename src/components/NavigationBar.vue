<template>
  <nav class="navbar">
    <div class="navbar-container">
      <router-link to="/" class="rotary-logo" :aria-label="$t('nav.home_aria')">
        <img src="/images/logo-rotary.png" alt="Rotary Logo" class="nav-logo-img" />
      </router-link>
      
      <div class="navbar-menu">
        <router-link to="/" class="navbar-link">{{ $t('nav.start') }}</router-link>
        <router-link to="/proyectos" class="navbar-link">{{ $t('nav.projects') }}</router-link>
        <router-link to="/donar" class="navbar-link donate-btn">
          {{ $t('nav.donate') }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<style scoped lang="scss">
.navbar {
  position: absolute; /* Clave: Flota sobre el contenido */
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100; /* Asegura que esté encima de la foto */
  padding: 20px 0;
  background: linear-gradient(to bottom, rgba(0,0,0,0.6) 0%, transparent 100%); /* Sombra suave para leer */
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

  &:hover {
    opacity: 0.8;
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
  .navbar-menu { gap: 20px; }
  .navbar-link:not(.donate-btn) { display: none; } /* En móvil a veces ocultamos enlaces y dejamos solo Donar o Menú Hambuguesa */
}
</style>
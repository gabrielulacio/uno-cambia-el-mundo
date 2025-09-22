<template>
  <nav class="navbar">
    <div class="navbar-container">
      <router-link to="/" class="rotary-logo" aria-label="Ir al inicio">
        <img src="/images/logo-rotary.png" alt="Rotary Logo" />
      </router-link>
      <!-- Menú de navegación -->
      <div class="navbar-menu">
        <router-link to="/" class="navbar-link">Inicio</router-link>
        <router-link to="/acerca" class="navbar-link">Acerca de</router-link>
        <router-link to="/donar" class="navbar-link donate-link">
          Donar 💛
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script setup>
// No props needed for now
</script>

<style scoped lang="scss">
.navbar {
  background-color: var(--rotary-blue);
  padding: 8px 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: 64px;
}

.navbar-link {
  color: var(--white);
  text-decoration: none;
  transition: opacity 0.3s ease;
  cursor: pointer;
  @include paragraph-regular;
}

.donate-link {
  @include paragraph-bold;
}

@media (max-width: 768px) {
  .navbar-container {
    flex-direction: column;
    gap: 15px;
  }

  .navbar-menu {
    gap: 15px;
  }

  .brand-text .rotary-text {
    font-size: 1.2rem;
  }
}
</style>
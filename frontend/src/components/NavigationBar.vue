<template>
  <nav class="navbar">
    <div class="navbar-container">
      <!-- Logo y texto del distrito -->
      <div class="navbar-brand">
        <div class="rotary-logo">
          <svg width="40" height="40" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Logo simplificado de Rotary -->
            <circle cx="100" cy="100" r="95" fill="#17458f" stroke="#f7a81b" stroke-width="10"/>
            <circle cx="100" cy="50" r="20" fill="#f7a81b"/>
            <circle cx="150" cy="100" r="20" fill="#f7a81b"/>
            <circle cx="100" cy="150" r="20" fill="#f7a81b"/>
            <circle cx="50" cy="100" r="20" fill="#f7a81b"/>
            <circle cx="130" cy="70" r="15" fill="#f7a81b"/>
            <circle cx="130" cy="130" r="15" fill="#f7a81b"/>
            <circle cx="70" cy="130" r="15" fill="#f7a81b"/>
            <circle cx="70" cy="70" r="15" fill="#f7a81b"/>
            <circle cx="100" cy="100" r="15" fill="#f7a81b"/>
          </svg>
        </div>
        <div class="brand-text">
          <div class="district">Distrito 4380</div>
          <div class="rotary-text">Rotary</div>
          <div class="location">San Cristóbal</div>
        </div>
      </div>

      <!-- Menú de navegación -->
      <div class="navbar-menu">
        <router-link to="/" class="navbar-link">Inicio</router-link>
        <router-link to="/donar" class="navbar-link donate-link">
          Donar 💛
        </router-link>
        <div class="navbar-link">Acerca de</div>
      </div>
    </div>
  </nav>
</template>

<script setup>
// No props needed for now
</script>

<style scoped>
.navbar {
  background-color: var(--rotary-blue);
  padding: 15px 0;
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

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 15px;
}

.rotary-logo {
  flex-shrink: 0;
}

.brand-text {
  color: white;
}

.district {
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: 2px;
}

.rotary-text {
  font-size: 1.4rem;
  font-weight: 800;
  line-height: 1;
  margin-bottom: 2px;
}

.location {
  font-size: 0.9rem;
  font-weight: 400;
  opacity: 0.9;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: 30px;
}

.navbar-link {
  color: white;
  text-decoration: none;
  font-weight: 500;
  font-size: 1.1rem;
  transition: opacity 0.3s ease;
  cursor: pointer;
}

.navbar-link:hover {
  opacity: 0.8;
}

.donate-link {
  background-color: var(--rotary-gold);
  color: var(--rotary-blue);
  padding: 10px 20px;
  border-radius: 25px;
  font-weight: 700;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.donate-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(247, 168, 27, 0.4);
  opacity: 1;
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
}</style>
<template>
  <div class="thank-you-page">
    <NavigationBar />
    
    <main class="content">
      <div class="card">
        <div class="icon-wrapper">
          <div class="heart-icon">💙</div>
        </div>

        <h1>{{ $t('thank_you.title') }}</h1>
        
        <p class="message" v-html="$t('thank_you.message')"></p>

        <div class="info-box">
          <p><strong>{{ $t('thank_you.next_steps_title') }}</strong></p>
          <p>{{ $t('thank_you.next_steps_text') }}</p>
        </div>

        <div class="actions">
          <router-link to="/" class="btn-primary">{{ $t('thank_you.back_home') }}</router-link>
          </div>
      </div>
    </main>

    <FooterSection />
  </div>
</template>

<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import FooterSection from '@/components/FooterSection.vue';
import { onMounted } from 'vue';
import confetti from 'canvas-confetti'; // Efecto opcional de confeti

onMounted(() => {
  // Disparar confeti al cargar (requiere: npm install canvas-confetti)
  // Si no quieres instalarlo, simplemente borra estas líneas y el import
  confetti({
    particleCount: 100,
    spread: 70,
    origin: { y: 0.6 },
    colors: ['#17458f', '#f7a81b', '#ffffff'] // Colores Rotary
  });
});
</script>

<style scoped lang="scss">
.thank-you-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f4f6f9;
}

.content {
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 120px 20px 60px; /* Padding top alto por el navbar flotante */
}

.card {
  background: white;
  padding: 48px;
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.08);
  max-width: 600px;
  width: 100%;
  text-align: center;
  animation: slideUp 0.8s ease-out;
}

.icon-wrapper {
  margin-bottom: 24px;
}

.heart-icon {
  font-size: 5rem;
  animation: pulse 2s infinite;
}

h1 {
  color: var(--rotary-blue);
  font-size: 2.5rem;
  margin-bottom: 16px;
  line-height: 1.2;
}

.message {
  font-size: 1.1rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 32px;
}

.info-box {
  background: #f9fcff;
  border: 1px solid #eef2f7;
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 32px;
  font-size: 0.95rem;
  color: #555;
  
  strong { color: var(--rotary-blue); display: block; margin-bottom: 4px; }
}

.btn-primary {
  display: inline-block;
  background: var(--rotary-gold);
  color: var(--rotary-blue);
  padding: 14px 32px;
  border-radius: 50px;
  font-weight: 700;
  text-decoration: none;
  transition: transform 0.2s;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(247, 168, 27, 0.4);
  }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

@media(max-width: 600px) {
  .card { padding: 32px 20px; }
  h1 { font-size: 2rem; }
}
</style>
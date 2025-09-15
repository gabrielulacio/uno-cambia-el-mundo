<template>
  <div class="about-container">
    <NavigationBar />

    <main class="about-content">
      <!-- Contenido a agregar próximamente -->
      <section class="about-hero">
        <h1 class="about-title">Acerca de</h1>
        <p class="about-subtitle">Conoce más sobre quiénes somos y cómo esta campaña transformará vidas.</p>
      </section>

      <!-- FAQs / Acordeón -->
      <section class="faq-section">
        <div class="faq-container">
          <h2 class="faq-title">Preguntas frecuentes</h2>

          <details class="faq-item" v-for="(item, idx) in faqs" :key="idx">
            <summary class="faq-question">
              {{ item.q }}
            </summary>
            <div class="faq-answer">
              <p>{{ item.a }}</p>
            </div>
          </details>
        </div>
      </section>
    </main>

    <FooterSection />
  </div>
</template>

<script setup>
import NavigationBar from '@/components/NavigationBar.vue';
import FooterSection from '@/components/FooterSection.vue';

// Contenido inicial de ejemplo (podés editarlo libremente)
const faqs = [
  {
    q: '¿Quién es Rotary San Cristóbal?',
    a: 'Rotary San Cristóbal es un club rotario local comprometido con el servicio y el desarrollo de la comunidad. Trabajamos en proyectos de salud, educación y bienestar, articulando esfuerzos con instituciones públicas y privadas para generar un impacto positivo y sostenible.',
  },
  {
    q: '¿Qué es la Fundación Centro Médico Dr. Pablo Puky?',
    a: 'La Fundación Centro Médico Dr. Pablo Puky es una organización sin fines de lucro dedicada a brindar atención médica de calidad y programas de prevención a personas y familias que más lo necesitan. Esta campaña busca fortalecer su equipamiento e infraestructura para mejorar la atención.',
  },
  {
    q: '¿Cómo se usarán los fondos recaudados?',
    a: 'Los fondos se destinarán a la adquisición y renovación de equipos médicos prioritarios y a mejoras en la capacidad de atención del centro. Publicaremos avances y resultados para asegurar transparencia en cada etapa.',
  },
  {
    q: '¿Cómo puedo donar?',
    a: 'Podés realizar tu aporte desde la página Donar, eligiendo el monto que prefieras. Cada contribución, grande o pequeña, nos acerca a la meta y tiene un impacto directo en la atención médica de la comunidad.',
  },
];
</script>

<style scoped>
.about-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--background-color);
}

.about-content {
  flex: 1 1 auto;
  background-color: #ffffff; /* fondo blanco para el contenido */
}

.about-hero {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.about-title {
  margin: 0 0 8px 0;
}

.about-subtitle {
  margin: 0;
}

/* FAQ styles */
.faq-section {
  padding: 10px 0 40px;
}

.faq-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px;
}

.faq-title {
  margin: 0 0 16px 0;
}

details.faq-item {
  background: #fff;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 12px;
  box-shadow: 0 4px 18px rgba(0,0,0,0.06);
  margin: 12px 0;
  overflow: hidden;
}

summary.faq-question {
  cursor: pointer;
  position: relative;
  list-style: none; /* oculta el marcador por defecto */
  padding: 16px 56px 16px 20px;
  font-weight: 700;
}

/* Ocultar el triángulo nativo */
summary::-webkit-details-marker {
  display: none;
}

/* Chevron personalizado */
summary.faq-question::after {
  content: '▾';
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%) rotate(0deg);
  transition: transform 0.2s ease;
  font-size: 1.1rem;
}

details[open] > summary.faq-question::after {
  transform: translateY(-50%) rotate(180deg);
}

.faq-answer {
  padding: 0 20px 16px 20px;
  color: var(--text-color);
}

.faq-answer p {
  margin: 10px 0 0 0;
}

@media (max-width: 768px) {
  .about-hero {
    padding: 28px 16px;
  }
  .faq-container {
    padding: 0 16px;
  }
  summary.faq-question {
    padding: 14px 52px 14px 16px;
  }
  summary.faq-question::after {
    right: 16px;
  }
}
</style>

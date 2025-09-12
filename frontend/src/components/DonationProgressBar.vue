<template>
  <div class="progress-bar-container">
    <div class="progress-bar-wrapper">
      <div class="progress-bar">
        <div class="progress-bar-fill" :style="{ width: percentage + '%' }" :class="colorClass">
          <!-- La animación de onda ahora está en los pseudo-elementos del fill -->
          <span v-if="!isLabelOutside" class="progress-label">
            {{ roundedPercentage }}%
          </span>
        </div>
      </div>
      <span v-if="isLabelOutside" class="progress-label label-outside">
        {{ roundedPercentage }}%
      </span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  goal: {
    type: Number,
    required: true,
    default: 10000,
  },
  current: {
    type: Number,
    required: true,
    default: 0,
  },
});

const percentage = computed(() => {
  if (props.goal <= 0) return 0;
  return Math.min((props.current / props.goal) * 100, 100);
});

const roundedPercentage = computed(() => Math.round(percentage.value));

const colorClass = computed(() => {
  const p = roundedPercentage.value;
  if (p < 20) return 'level-red';
  if (p < 40) return 'level-orange';
  if (p < 60) return 'level-yellow';
  if (p < 80) return 'level-green';
  if (p < 100) return 'level-blue';
  return 'level-navy';
});

const isLabelOutside = computed(() => roundedPercentage.value < 15);
</script>

<style scoped>
.progress-bar-container {
  width: 100%;
  max-width: 500px;
  margin: 20px auto;
  text-align: center;
}

.progress-bar-wrapper {
  width: 100%;
  position: relative;
  padding-bottom: 30px;
}

.progress-bar {
  width: 100%;
  height: 40px;
  /* 3. El fondo de la barra (track) ahora es un tono oscuro traslúcido */
  background-color: rgba(0, 0, 0, 0.2);
  /* 2. El borde ahora es blanco */
  border: 3px solid var(--white);
  border-radius: 20px;
  box-sizing: border-box;
  /* 2. Se añade el espaciado interior */
  padding: 4px;
  position: relative;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  border-radius: 16px; /* Radio interno para encajar en el padding */
  transition: width 0.7s cubic-bezier(0.4, 0, 0.2, 1); /* La transición de color ya no es necesaria aquí */
  display: flex;
  align-items: center;
  justify-content: center;
  /* Clave para la animación: debe ser un contenedor de posicionamiento */
  position: relative;
  overflow: hidden;
  /* La magia: el color de fondo se aplica aquí */
  background-color: transparent; /* El div en sí es transparente */
}

/* Colores corregidos y usando variables globales */
.level-red { background: linear-gradient(to right, #ff7e5f, #ff5f5f); }
.level-orange { background: linear-gradient(to right, #ffb75f, #ff9933); }
.level-yellow { background: linear-gradient(to right, #f9d423, var(--rotary-gold)); }
.level-green { background: linear-gradient(to right, #69f0ae, #00e676); }
.level-blue { background: linear-gradient(to right, #89f7fe, var(--azure)); }
.level-navy { background: linear-gradient(to right, var(--azure), var(--rotary-blue)); }

.progress-label {
  font-size: 1.5rem;
  font-weight: 900;
  white-space: nowrap;
  /* Posicionamiento relativo para que esté por encima de la animación */
  position: relative;
  z-index: 10;
}

.progress-bar-fill .progress-label {
  color: white;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);
}

.label-outside {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  color: white;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
  font-size: 1rem;
  font-weight: bold;
}

/* 1. Animación de líquido corregida */
@keyframes wave {
  0% { transform: translateX(0) translateZ(0) scaleY(1); }
  50% { transform: translateX(-25%) translateZ(0) scaleY(0.55); }
  100% { transform: translateX(-50%) translateZ(0) scaleY(1); }
}

.progress-bar-fill::before,
.progress-bar-fill::after {
  content: "";
  position: absolute;
  z-index: 1; /* Por debajo del texto (z-index: 10) */
  width: 200%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: rgba(255, 255, 255, 0.2);
  animation: wave 2.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
  transform-origin: center bottom;
}

.progress-bar-fill::before {
  border-radius: 45%;
}

.progress-bar-fill::after {
  border-radius: 40%;
  opacity: 0.7;
  animation-delay: -1.2s;
}
</style>


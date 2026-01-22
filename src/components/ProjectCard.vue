<template>
  <div class="project-card">
    <div class="card-image-wrapper">
      <img :src="image" :alt="title" class="card-image" />
      <div class="category-badge">{{ category }}</div>
    </div>

    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-description">{{ description }}</p>

      <div class="progress-section">
        <div class="progress-labels">
          <span class="raised">{{ $t('projects.ui.card_raised') }}: <strong>{{ progressPercentage }}%</strong></span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" :style="{ width: progressPercentage + '%' }"></div>
        </div>
      </div>

      <router-link :to="link" class="card-btn">
        {{ $t('projects.ui.card_view_details') }} <span class="arrow">→</span>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  title: String,
  description: String,
  image: String,
  category: String,
  current: Number,
  goal: Number,
  link: String
});

const progressPercentage = computed(() => {
  if (!props.goal) return 0;
  return Math.min(Math.round((props.current / props.goal) * 100), 100);
});
</script>

<style scoped lang="scss">
.project-card {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(23, 69, 143, 0.15);
  }
}

.card-image-wrapper {
  position: relative;
  height: 220px;
  overflow: hidden;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.project-card:hover .card-image {
  transform: scale(1.05);
}

.category-badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background: rgba(255, 255, 255, 0.95);
  color: var(--rotary-blue);
  padding: 6px 12px;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.card-content {
  padding: 24px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.card-title {
  font-size: 1.25rem;
  color: var(--rotary-blue);
  margin-bottom: 12px;
  font-weight: 700;
}

.card-description {
  font-size: 0.95rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 24px;
  flex-grow: 1;
}

/* Barra de Progreso */
.progress-section {
  margin-bottom: 24px;
}

.progress-labels {
  display: flex;
  justify-content: space-between;
  font-size: 0.85rem;
  margin-bottom: 8px;
  color: #555;
}

.progress-track {
  background: #f0f0f0;
  height: 8px;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  background: var(--rotary-gold);
  height: 100%;
  border-radius: 4px;
  transition: width 1s ease-out;
}

/* Botón */
.card-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  padding: 12px;
  background: #f4f6f9;
  color: var(--rotary-blue);
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s ease;

  &:hover {
    background: var(--rotary-blue);
    color: white;
  }
}
</style>
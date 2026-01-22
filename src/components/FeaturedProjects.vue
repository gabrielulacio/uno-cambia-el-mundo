<template>
  <section class="featured-section">
    <div class="container">
      <div class="section-header">
        <h2>{{ $t('featured_projects.title') }}</h2>
        <p>{{ $t('featured_projects.subtitle') }}</p>
      </div>

      <div class="projects-grid">
        <ProjectCard
          v-for="project in featuredProjects"
          :key="project.slug"
          :title="project.title"
          :description="project.description"
          :category="project.category"
          :image="PROJECTS_CONFIG[project.slug]?.image || 'hero-bg.png'"
          :link="`/proyectos/${project.slug}`"
          :goal="PROJECTS_CONFIG[project.slug]?.goal || 5000"
          :current="PROJECTS_CONFIG[project.slug]?.current || 1200"
        />
      </div>

      <div class="view-all-wrapper">
        <router-link to="/proyectos" class="view-all-btn">
          {{ $t('featured_projects.view_all') }}
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue';
import { useI18n } from 'vue-i18n';
import ProjectCard from './ProjectCard.vue';
import { PROJECTS_CONFIG } from '@/constants/projects';

const { tm } = useI18n();

const featuredProjects = computed(() => {
  const allProjects = tm('projects.list');
  // Return first 3 projects
  return Object.values(allProjects).slice(0, 3);
});
</script>

<style scoped lang="scss">
.featured-section {
  padding: 80px 0;
  background-color: #fff;
}

.section-header {
  text-align: center;
  margin-bottom: 50px;

  h2 {
    color: var(--rotary-blue);
    font-size: 2.5rem;
    margin-bottom: 15px;
  }

  p {
    color: #666;
    font-size: 1.1rem;
    max-width: 600px;
    margin: 0 auto;
  }
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
  margin-bottom: 50px;
}

.view-all-wrapper {
  text-align: center;
}

.view-all-btn {
  display: inline-block;
  padding: 12px 30px;
  background-color: var(--rotary-blue);
  color: white;
  border-radius: 30px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;

  &:hover {
    background-color: #1a4a8e;
    transform: translateY(-2px);
  }
}

@media (max-width: 768px) {
  .featured-section {
    padding: 60px 0;
  }
}
</style>
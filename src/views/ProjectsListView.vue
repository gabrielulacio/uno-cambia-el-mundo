<template>
  <div class="projects-page">
    <NavigationBar />

    <header class="page-header">
      <div class="header-content">
        <h1>{{ $t('projects.title') }}</h1>
        <p>{{ $t('projects.subtitle') }}</p>
      </div>
    </header>

    <main class="container">
      <div class="projects-grid">
        
        <ProjectCard 
          v-for="proj in projectList"
          :key="proj.slug"
          :title="proj.title"
          :description="proj.description"
          :category="proj.category"
          :image="proj.image"
          :current="proj.current"
          :goal="proj.goal"
          :link="`/proyectos/${proj.slug}`"
        />

        <div class="coming-soon-card">
          <span class="icon">✨</span>
          <h3>{{ $t('projects.coming_soon') }}</h3>
          <p>{{ $t('projects.coming_soon_desc') }}</p>
        </div>

      </div>
    </main>

    <FooterSection />
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import NavigationBar from '@/components/NavigationBar.vue';
import ProjectCard from '@/components/ProjectCard.vue';
import FooterSection from '@/components/FooterSection.vue';
import { useDonationStatus } from '@/store/useDonationStatus';

const { tm, rt } = useI18n();
const { projects, loadDonationStatus } = useDonationStatus();

onMounted(() => {
  loadDonationStatus();
});

const projectList = computed(() => {
  const all = tm('projects.list');
  return Object.entries(all).map(([slug, content]) => {
    const status = projects.value.find(p => p.id === slug);
    return {
      slug,
      title: rt(content.title),
      description: rt(content.description),
      category: rt(content.category),
      image: status?.image || 'hero-bg.png',
      goal: status?.goal || 5000,
      current: status?.current || 0
    };
  });
});
</script>

<style scoped lang="scss">
.projects-page {
  background-color: #f8f9fa;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Cabecera compacta (Diferente al Hero del Home) */
.page-header {
  background: var(--rotary-blue);
  color: white;
  padding: 120px 20px 60px; /* Padding top alto para compensar el Navbar flotante */
  text-align: center;
}

.header-content h1 {
  font-size: 2.5rem;
  margin-bottom: 12px;
  color: var(--rotary-gold);
}

.header-content p {
  opacity: 0.9;
  font-size: 1.1rem;
  max-width: 600px;
  margin: 0 auto;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 20px;
  flex-grow: 1;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 32px;
}

/* Tarjeta "Próximamente" */
.coming-soon-card {
  border: 2px dashed #ddd;
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 40px;
  color: #888;
  background: rgba(0,0,0,0.02);

  .icon {
    font-size: 3rem;
    margin-bottom: 16px;
    opacity: 0.5;
  }
  
  h3 { margin-bottom: 8px; color: #666; }
}

@media (max-width: 768px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>
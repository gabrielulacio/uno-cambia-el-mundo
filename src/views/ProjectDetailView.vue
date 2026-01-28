<template>
  <div class="project-detail-page">
    <NavigationBar />

    <div v-if="project" class="detail-container">
      
      <header class="project-header" :style="{ backgroundImage: `url(${getImageUrl(projectStatus.image)})` }">
        <div class="overlay"></div>
        <div class="header-content">
          <div class="badge">{{ $rt(project.category) }}</div>
          <h1>{{ $rt(project.title) }}</h1>
          
          <div class="big-progress-wrapper">
            <div class="stats-row">
              <div class="stat">
                <span class="label">{{ $t('project_detail.raised') }}</span>
                <span class="value">{{ progressPercentage }}%</span>
              </div>
            </div>
            <div class="progress-track">
              <div class="progress-fill" :style="{ width: progressPercentage + '%' }"></div>
            </div>
          </div>
        </div>
      </header>

      <main class="content-wrapper">
        <div class="grid-layout">
          
          <div class="story-column">
            <h2>{{ $t('project_detail.about_title') }}</h2>
            <div class="rich-text" v-html="$rt(project.long_description)"></div>
          </div>

          <aside class="sidebar-column">
            <div class="donate-card">
              <h3>{{ $t('project_detail.cta_title') }}</h3>
              <p>{{ $t('project_detail.cta_desc') }}</p>
              
              <div class="impact-list">
                <div class="impact-item">
                  <span class="check">✓</span> {{ $t('project_detail.impact_transparency') }}
                </div>
                <div class="impact-item">
                  <span class="check">✓</span> {{ $t('project_detail.impact_report') }}
                </div>
              </div>

              <router-link :to="{ path: '/donar', query: { project: slug } }" class="btn-donate-big">
                {{ $t('project_detail.donate_btn') }}
              </router-link>
            </div>
          </aside>

        </div>
      </main>

    </div>

    <div v-else class="not-found">
      <h2>{{ $t('project_detail.not_found') }}</h2>
      <router-link to="/proyectos" class="btn-back">{{ $t('project_detail.back_to_catalog') }}</router-link>
    </div>

    <FooterSection />
  </div>
</template>

<script setup>
import { computed, ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useI18n } from 'vue-i18n';
import NavigationBar from '@/components/NavigationBar.vue';
import FooterSection from '@/components/FooterSection.vue';
import { useDonationStatus } from '@/store/useDonationStatus';
import { getImageUrl } from '@/utils/images';

const { tm, rt } = useI18n();
const route = useRoute();
const slug = computed(() => route.params.slug);
const project = ref(null);
const { projects, loadDonationStatus } = useDonationStatus();

// Obtener datos dinámicos del proyecto desde el store
const projectStatus = computed(() => {
  return projects.value.find(p => p.id === slug.value) || { current: 0, goal: 5000, image: 'hero-bg.png' };
});

const progressPercentage = computed(() => {
  if (!projectStatus.value) return 0;
  return Math.min(Math.round((projectStatus.value.current / projectStatus.value.goal) * 100), 100);
});

const loadProject = () => {
  loadDonationStatus();
  const allProjects = tm('projects.list');
  if (allProjects[slug.value]) {
    project.value = allProjects[slug.value];
    window.scrollTo(0, 0);
  } else {
    project.value = null;
  }
};

onMounted(loadProject);
watch(slug, loadProject);
</script>

<style scoped lang="scss">
.project-detail-page {
  background-color: #f9f9f9;
  min-height: 100vh;
}

/* HEADER GRANDE */
.project-header {
  position: relative;
  height: 60vh;
  min-height: 500px;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: flex-end;
  color: white;
  padding-bottom: 60px;
}

.overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(23,69,143,0.4) 100%);
}

.header-content {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
}

.badge {
  background: var(--rotary-gold);
  color: var(--rotary-blue);
  display: inline-block;
  padding: 6px 12px;
  border-radius: 4px;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 16px;
  font-size: 0.85rem;
}

h1 {
  font-size: 3rem;
  margin: 0 0 32px 0;
  line-height: 1.1;
  text-shadow: 0 4px 10px rgba(0,0,0,0.3);
  
  @media(max-width: 768px) { font-size: 2rem; }
}

/* Barra de Progreso Header */
.big-progress-wrapper {
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(10px);
  padding: 24px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,0.2);
}

.stats-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
  font-family: monospace; /* Look técnico */
}

.stat {
  display: flex;
  flex-direction: column;
}

.label { font-size: 0.8rem; text-transform: uppercase; opacity: 0.8; }
.value { font-size: 1.5rem; font-weight: 700; color: var(--rotary-gold); }

.progress-track {
  height: 12px;
  background: rgba(255,255,255,0.2);
  border-radius: 6px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: var(--rotary-gold);
  border-radius: 6px;
  transition: width 1.5s ease-out;
}

/* CONTENIDO PRINCIPAL */
.content-wrapper {
  max-width: 1000px;
  margin: 0 auto;
  padding: 60px 20px;
}

.grid-layout {
  display: grid;
  grid-template-columns: 1fr 350px; /* Contenido ancho | Sidebar fija */
  gap: 60px;

  @media(max-width: 900px) {
    grid-template-columns: 1fr;
  }
}

/* Columna Historia */
.story-column h2 {
  color: var(--rotary-blue);
  font-size: 2rem;
  margin-bottom: 24px;
}

.rich-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #444;
  
  :deep(h3) { margin-top: 30px; color: var(--rotary-blue); }
  :deep(li) { margin-bottom: 8px; }
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-top: 40px;
  
  img {
    width: 100%;
    border-radius: 8px;
    height: 200px;
    object-fit: cover;
  }
}

/* Columna Sidebar (Donar) */
.donate-card {
  background: white;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  position: sticky;
  top: 100px; /* Se queda pegado al hacer scroll */
  border-top: 5px solid var(--rotary-gold);
  text-align: center;
}

.donate-card h3 {
  margin-top: 0;
  color: var(--rotary-blue);
}

.impact-list {
  text-align: left;
  margin: 24px 0;
  color: #666;
}

.impact-item {
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.check { color: var(--rotary-gold); font-weight: bold; }

.btn-donate-big {
  display: block;
  width: 100%;
  padding: 16px;
  background: var(--rotary-gold);
  color: var(--rotary-blue);
  font-weight: 800;
  text-decoration: none;
  border-radius: 8px;
  font-size: 1.1rem;
  transition: transform 0.2s;
  box-shadow: 0 4px 15px rgba(247, 168, 27, 0.3);

  &:hover {
    transform: translateY(-3px);
  }
}

/* Not Found */
.not-found {
  text-align: center;
  padding: 100px 20px;
}
</style>
/* Archivo: src/router/index.js */
import { createRouter, createWebHistory } from 'vue-router';

// Vistas Principales
import HomeView from '../views/HomeView.vue'; 
import ProjectsListView from '../views/ProjectsListView.vue'; // Nuevo
import ProjectDetailView from '../views/ProjectDetailView.vue'; // Nuevo
import DonationView from '../views/DonationView.vue';
import AboutView from '../views/AboutView.vue';
import ThankYouView from '../views/ThankYouView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    // Esto hace que al cambiar de página, el scroll suba arriba de todo (muy profesional)
    return { top: 0 };
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView, // Ahora será la "Home Institucional"
    },
    {
      path: '/proyectos',
      name: 'projects-list',
      component: ProjectsListView,
    },
    {
      // Ruta dinámica: :slug permitirá cargar distintos proyectos con la misma plantilla
      // Ejemplo: /proyectos/centro-medico o /proyectos/gym-abuelos
      path: '/proyectos/:slug', 
      name: 'project-detail',
      component: ProjectDetailView,
      props: true 
    },
    {
      path: '/donar',
      name: 'donate',
      component: DonationView,
    },
    {
      path: '/acerca',
      name: 'about',
      component: AboutView,
    },
    {
      path: '/gracias',
      name: 'thank-you',
      component: ThankYouView,
    },
  ],
});

export default router;
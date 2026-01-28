/* Archivo: src/router/index.js */
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(_to, _from, _savedPosition) {
    // Esto hace que al cambiar de página, el scroll suba arriba de todo (muy profesional)
    return { top: 0 };
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'), // Lazy loading para la Home
    },
    {
      path: '/proyectos',
      name: 'projects-list',
      component: () => import('../views/ProjectsListView.vue'), // Lazy loading
    },
    {
      // Ruta dinámica: :slug permitirá cargar distintos proyectos con la misma plantilla
      path: '/proyectos/:slug', 
      name: 'project-detail',
      component: () => import('../views/ProjectDetailView.vue'), // Lazy loading
      props: true 
    },
    {
      path: '/donar',
      name: 'donate',
      component: () => import('../views/DonationView.vue'), // Lazy loading
    },
    {
      path: '/acerca',
      name: 'about',
      component: () => import('../views/AboutView.vue'), // Lazy loading
    },
    {
      path: '/gracias',
      name: 'thank-you',
      component: () => import('../views/ThankYouView.vue'), // Lazy loading
    },
  ],
});

export default router;
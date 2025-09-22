import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue'; // Nueva vista del home
import HelloWorldView from '../views/HelloWorldView.vue';
import DonationView from '../views/DonationView.vue';
import ShowcaseView from '../views/ShowcaseView.vue';
import AboutView from '../views/AboutView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView, // Ahora la ruta principal es el HomeView
    },
    {
      path: '/hello',
      name: 'hello-world',
      component: HelloWorldView,
    },
    {
      path: '/donar',
      name: 'donar',
      component: DonationView,
    },
    {
      path: '/showcase',
      name: 'showcase',
      component: ShowcaseView,
    },
    {
      path: '/acerca',
      name: 'about',
      component: AboutView,
    },
  ],
});

export default router;
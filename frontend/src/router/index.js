import { createRouter, createWebHistory } from 'vue-router';
import HelloWorldView from '../views/HelloWorldView.vue';
import DonationView from '../views/DonationView.vue'; // <-- Importar la nueva vista

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'hello-world',
      component: HelloWorldView,
    },
    { // <-- Añadir nueva ruta
      path: '/donar',
      name: 'donar',
      component: DonationView,
    },
  ],
});

export default router;

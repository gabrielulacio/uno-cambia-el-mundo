import './assets/main.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; 
import i18n from './i18n'; // Importa i18n

const app = createApp(App);

app.use(router); 
app.use(i18n); // Registra i18n
app.mount('#app');

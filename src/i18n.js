import { createI18n } from 'vue-i18n';
import es from './locales/es.json';

const i18n = createI18n({
  legacy: false, // Usar Composition API
  locale: 'es',
  fallbackLocale: 'es',
  warnHtmlInMessage: false,
  warnHtmlMessage: false,
  messages: {
    es
  }
});

export default i18n;

import { ref } from 'vue';
import { getDonationStatus } from '@/services/api.js';

// Fuente única de estado para la donación (meta y recaudado)
const totalGoal = ref(100);
const totalCurrent = ref(0);
const projects = ref([]);
const loading = ref(false);
const error = ref(null);
let loadedOnce = false;

/**
 * @typedef {Object} ProjectStatus
 * @property {string} id - Slug del proyecto
 * @property {string} name - Nombre del proyecto
 * @property {number} goal - Meta en USD
 * @property {number} current - Monto recaudado en USD
 * @property {string} image - Nombre o URL de la imagen
 * @property {number} percentage - Porcentaje de avance
 */

/**
 * Store para gestionar el estado de las donaciones y proyectos.
 * @returns {Object}
 */
export function useDonationStatus() {
  /**
   * Carga el estado de donación desde la API.
   * @param {boolean} [force=false] - Si es true, ignora el cache y recarga los datos.
   */
  async function loadDonationStatus(force = false) {
    if (loadedOnce && !force) return;
    loading.value = true;
    try {
      const data = await getDonationStatus();
      if (typeof data?.total_goal === 'number') totalGoal.value = data.total_goal;
      if (typeof data?.total_current === 'number') totalCurrent.value = data.total_current;
      /** @type {ProjectStatus[]} */
      if (Array.isArray(data?.projects)) projects.value = data.projects;
      
      error.value = null;
      loadedOnce = true;
    } catch (e) {
      // Mantener valores por defecto si falla
      error.value = e?.message || 'Error al cargar estado de donación';
      console.error('useDonationStatus error:', e);
    } finally {
      loading.value = false;
    }
  }

  /**
   * Fuerza la recarga de los datos.
   */
  function refreshDonationStatus() {
    return loadDonationStatus(true);
  }

  return {
    totalGoal,
    totalCurrent,
    /** @type {import('vue').Ref<ProjectStatus[]>} */
    projects,
    loading,
    error,
    loadDonationStatus,
    refreshDonationStatus,
  };
}

import { ref } from 'vue';
import { getDonationStatus } from '@/services/api.js';

// Fuente única de estado para la donación (meta y recaudado)
const goal = ref(100);
const current = ref(20);
const loading = ref(false);
const error = ref(null);
let loadedOnce = false;

export function useDonationStatus() {
  async function loadDonationStatus(force = false) {
    if (loadedOnce && !force) return;
    loading.value = true;
    try {
      const data = await getDonationStatus();
      if (typeof data?.goal === 'number') goal.value = data.goal;
      if (typeof data?.current === 'number') current.value = data.current;
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

  function refreshDonationStatus() {
    return loadDonationStatus(true);
  }

  return {
    goal,
    current,
    loading,
    error,
    loadDonationStatus,
    refreshDonationStatus,
  };
}

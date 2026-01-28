import { useNotifications } from '@/store/useNotifications';

/**
 * Composable para copiar texto al portapapeles con notificación opcional.
 * @returns {Object} { copy }
 */
export function useClipboard() {
  const { showToast } = useNotifications();

  /**
   * Copia el texto al portapapeles.
   * @param {string} text - El texto a copiar.
   * @param {string} successMessage - Mensaje opcional para el brindis (toast).
   */
  async function copy(text, successMessage = null) {
    try {
      await navigator.clipboard.writeText(text);
      if (successMessage) {
        showToast(successMessage, 'info');
      }
    } catch (err) {
      console.error('Error al copiar al portapapeles:', err);
      showToast('No se pudo copiar el texto', 'error');
    }
  }

  return { copy };
}

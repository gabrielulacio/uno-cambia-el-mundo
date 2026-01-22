import axios from 'axios';

// La URL base ahora apunta a /api en producción.
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api'
});

export const getDonationStatus = async () => {
  try {
    const response = await api.get('/donation-status');
    return response.data;
  } catch (error) {
    console.error('Error fetching donation status:', error);
    throw error;
  }
};

export const getPaymentMethods = async () => {
  try {
    const response = await api.get('/payment-methods');
    return response.data;
  } catch (error) {
    console.error('Error fetching payment methods:', error);
    throw error;
  }
};


/**
 * Registra un nuevo reporte de pago
 * @param {Object} paymentData - Datos del formulario de donación
 */
export const reportPayment = async (paymentData) => {
  try {
    const response = await api.post('/report-payment', paymentData);
    return response.data;
  } catch (error) {
    console.error('Error reporting payment:', error);
    throw error;
  }
};

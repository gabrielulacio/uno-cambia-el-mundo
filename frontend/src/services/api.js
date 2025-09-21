import axios from 'axios';

// La URL base ahora apunta a /api en producción.
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api'
});


// --- Tu código existente (no necesita cambios) ---

export const getHelloWorld = async () => {
  try {
    const response = await api.get('/hello');
    return response.data;
  } catch (error) {
    console.error('Error fetching Hello World:', error);
    throw error;
  }
};

export const getDonationStatus = async () => {
  try {
    // Esta llamada ahora irá a -> tunombrededominio.com/api/donation-status
    const response = await api.get('/donation-status');
    return response.data;
  } catch (error) {
    console.error('Error fetching donation status:', error);
    throw error;
  }
};

export const getPaymentMethods = async () => {
  try {
    // Esta llamada ahora irá a -> tunombrededominio.com/api/payment-methods
    const response = await api.get('/payment-methods');
    return response.data;
  } catch (error) {
    console.error('Error fetching payment methods:', error);
    throw error;
  }
};
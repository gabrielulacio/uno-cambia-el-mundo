import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000'
});

export const getHelloWorld = async () => {
  try {
    const response = await api.get('/hello');
    return response.data;
  } catch (error) {
    console.error('Error fetching Hello World:', error);
    throw error;
  }
};

// --- NUEVA FUNCIÓN ---
export const getDonationStatus = async () => {
  try {
    const response = await api.get('/donation-status');
    return response.data;
  } catch (error) {
    console.error('Error fetching donation status:', error);
    throw error;
  }
};

// Obtener métodos de pago (para no exponer datos sensibles en el frontend)
export const getPaymentMethods = async () => {
  try {
    const response = await api.get('/payment-methods');
    return response.data; // Se espera un array de métodos { id, name, logo, description, fields: [{label, valueMasked, copyValue?}] }
  } catch (error) {
    console.error('Error fetching payment methods:', error);
    throw error;
  }
};

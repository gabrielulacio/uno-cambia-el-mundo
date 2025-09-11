import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL
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
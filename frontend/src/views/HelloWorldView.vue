<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import { getHelloWorld } from '../services/api';

export default {
  data() {
    return {
      message: '',
    };
  },
  async created() {
    try {
      const data = await getHelloWorld();
      this.message = data.message;
    } catch (error) {
      console.error('Error fetching message:', error);
    }
  },
};
</script>
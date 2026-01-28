import { reactive } from 'vue';

const state = reactive({
  toast: {
    show: false,
    message: '',
    type: 'success' // 'success', 'error', 'info'
  }
});

export const useNotifications = () => {
  const showToast = (message, type = 'success', duration = 3000) => {
    state.toast.message = message;
    state.toast.type = type;
    state.toast.show = true;

    setTimeout(() => {
      state.toast.show = false;
    }, duration);
  };

  return {
    state,
    showToast
  };
};

<template>
  <Transition name="toast">
    <div v-if="state.toast.show" :class="['toast-notification', state.toast.type]">
      <div class="toast-content">
        <span class="icon" v-if="state.toast.type === 'success'">✅</span>
        <span class="icon" v-if="state.toast.type === 'error'">❌</span>
        <span class="icon" v-if="state.toast.type === 'info'">ℹ️</span>
        <p>{{ state.toast.message }}</p>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { useNotifications } from '@/store/useNotifications';

const { state } = useNotifications();
</script>

<style scoped lang="scss">
.toast-notification {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 9999;
  min-width: 280px;
  padding: 16px 24px;
  border-radius: 12px;
  color: white;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;

  &.success {
    background: #10b981;
  }
  &.error {
    background: #ef4444;
  }
  &.info {
    background: var(--rotary-gold, #f7a81b);
    color: var(--rotary-blue, #17458f);
  }
}

.toast-content {
  display: flex;
  align-items: center;
  gap: 12px;
  
  p {
    margin: 0;
    font-weight: 600;
    font-size: 0.95rem;
  }
}

.toast-enter-active,
.toast-leave-active {
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateX(100px);
}
</style>

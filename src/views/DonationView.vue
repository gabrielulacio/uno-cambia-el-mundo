<template>
  <div class="donation-page">
    <NavigationBar />

    <div class="header-spacer"></div>

    <main class="container py-5">
      <div class="donation-layout">
        
        <section class="payment-methods-col">
          <h1 class="page-title">{{ $t('donations.title') }}</h1>
          <p class="subtitle">
            {{ $t('donations.subtitle') }}
          </p>

          <div class="steps">
            <div class="step-item">
              <div class="step-number">1</div>
              <div class="step-content">
                <h3>{{ $t('donations.step1_title') }}</h3>
                <p>{{ $t('donations.step1_desc') }}</p>
              </div>
            </div>

            <div class="methods-accordion">
              <div 
                v-for="method in paymentMethods" 
                :key="method.id"
                class="method-card" 
                :class="{ active: activeMethod === method.id }" 
                @click="activeMethod = method.id"
              >
                <div class="method-header">
                  <span class="method-icon">{{ method.icon }}</span>
                  <span class="method-name">{{ method.name }}</span>
                  <span class="arrow-icon">▼</span>
                </div>
                <div class="method-details" v-if="activeMethod === method.id">
                  <div v-for="(detail, index) in method.details" :key="index" class="detail-row">
                    <span class="label">{{ te(detail.label) ? t(detail.label) : detail.label }}</span>
                    <span 
                      class="value" 
                      :class="{ copyable: detail.copyable }"
                      @click="detail.copyable ? copy(detail.value) : null"
                    >
                      {{ detail.value }} {{ detail.copyable ? '📋' : '' }}
                    </span>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </section>

        <section class="report-form-col">
          <div class="form-card">
            <div class="step-item">
              <div class="step-number">2</div>
              <div class="step-content">
                <h3>{{ $t('donations.step2_title') }}</h3>
                <p>{{ $t('donations.step2_desc') }}</p>
              </div>
            </div>

            <form @submit.prevent="submitReport" class="donation-form">
              <div class="form-group">
                <label>{{ $t('donations.form.project_label') }}</label>
                <select v-model="form.project" required>
                  <option value="" disabled>{{ $t('donations.form.project_placeholder') }}</option>
                  <option value="fondo-general">{{ $t('donations.form.project_general') }}</option>
                  <option v-for="(proj, slug) in $tm('projects.list')" :key="slug" :value="slug">
                    {{ $rt(proj.title) }}
                  </option>
                </select>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>{{ $t('donations.form.name_label') }}</label>
                  <input type="text" v-model="form.name" required />
                </div>
                <div class="form-group">
                  <label>{{ $t('donations.form.email_label') }}</label>
                  <input type="email" v-model="form.email" required />
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label>{{ $t('donations.form.amount_label') }}</label>
                  <input type="number" step="0.01" v-model="form.amount" required />
                </div>
                <div class="form-group">
                  <label>{{ $t('donations.form.currency_label') }}</label>
                  <select v-model="form.currency" required>
                    <option value="USD">USD ($)</option>
                    <option value="VES">Bolívares (Bs.)</option>
                    <option value="USDT">USDT</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label>{{ $t('donations.form.reference_label') }}</label>
                <input type="text" v-model="form.reference" :placeholder="$t('donations.form.reference_placeholder')" required />
              </div>

              <div class="form-group checkbox-group">
                <label>
                  <input type="checkbox" v-model="form.anonymous" />
                  {{ $t('donations.form.anonymous_label') }}
                </label>
              </div>

                            <button type="submit" class="btn-submit" :disabled="loading">
                <span v-if="!loading">{{ $t('donations.form.submit_btn') }}</span>
                <span v-else>{{ $t('donations.form.loading') }}</span>
              </button>
            </form>
          </div>
        </section>

      </div>
    </main>
    
    <FooterSection />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { reportPayment, getPaymentMethods } from '@/services/api';
import { useNotifications } from '@/store/useNotifications';
import { useClipboard } from '@/composables/useClipboard';
import NavigationBar from '@/components/NavigationBar.vue';
import FooterSection from '@/components/FooterSection.vue';

const route = useRoute();
const router = useRouter();
const { t, te } = useI18n();
const { showToast } = useNotifications();
const { copy } = useClipboard();

const activeMethod = ref('zelle'); 
const loading = ref(false);
const paymentMethods = ref([]);

const form = ref({
  project: '',
  name: '',
  email: '',
  amount: '',
  currency: 'USD',
  reference: '',
  anonymous: false
});

// Al cargar, revisar si venimos de un proyecto específico
onMounted(async () => {
  if (route.query.project) {
    form.value.project = route.query.project;
  } else {
    form.value.project = 'fondo-general';
  }

  try {
    const data = await getPaymentMethods();
    if (data?.methods) {
      paymentMethods.value = data.methods;
    }
  } catch (error) {
    console.error("Error cargando métodos:", error);
    // Fallback local robusto por si el API falla (offline o error servidor)
    paymentMethods.value = [
      {
        id: "zelle",
        name: "Zelle",
        icon: "🇺🇸",
        details: [
          { label: "donations.methods.email", value: "zelle@rotarysc.org", copyable: true },
          { label: "donations.methods.holder", value: "Rotary San Cristóbal", copyable: false }
        ]
      },
      {
        id: "pagomovil",
        name: "Pago Móvil",
        icon: "⿽",
        details: [
          { label: "donations.methods.bank", value: "Bancamiga (0172)", copyable: false },
          { label: "donations.methods.phone", value: "04141234567", copyable: true },
          { label: "donations.methods.rif", value: "J-123456789", copyable: true }
        ]
      }
    ];
  }
});


// Función simple de copiar
// Usamos el composable useClipboard importado arriba
const submitReport = async () => {
  loading.value = true;
  
  try {
    await reportPayment(form.value);
    
    // Si todo sale bien:
    setTimeout(() => {
      loading.value = false;
      router.push('/gracias'); 
    }, 500);

  } catch (error) {
    console.error("Error enviando reporte:", error);
    loading.value = false;
    showToast("Hubo un error enviando el reporte. Por favor intenta de nuevo.", "error");
  }
};
</script>


<style scoped lang="scss">
.donation-page {
  background-color: #f4f6f9;
  min-height: 100vh;
}

.header-spacer {
  height: 110px; /* Aumentado de 80px para dar espacio al nuevo padding del Navbar */
  background: var(--rotary-blue);
}

.page-title {
  color: var(--rotary-blue);
  font-size: 2.5rem;
  margin-bottom: 8px;
}

.subtitle {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 40px;
}

.donation-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;

  @media(max-width: 900px) {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

/* Pasos */
.step-item {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}

.step-number {
  background: var(--rotary-gold);
  color: var(--rotary-blue);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1.2rem;
  flex-shrink: 0;
}

.step-content h3 { margin: 0 0 4px 0; color: var(--rotary-blue); }
.step-content p { margin: 0; color: #666; font-size: 0.95rem; }

/* Acordeón de Métodos */
.methods-accordion {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.method-card {
  background: white;
  border: 1px solid #ddd;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.2s;

  &.active {
    border-color: var(--rotary-blue);
    box-shadow: 0 4px 12px rgba(23,69,143,0.1);
  }
}

.method-header {
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 600;
  color: #333;
}

.method-icon { font-size: 1.5rem; }
.arrow-icon { margin-left: auto; font-size: 0.8rem; color: #999; }

.method-details {
  background: #f9fcff;
  padding: 16px;
  border-top: 1px solid #eee;
  font-size: 0.95rem;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  
  &:last-child { margin-bottom: 0; }
}

.label { color: #666; }
.value { font-family: monospace; font-weight: 600; color: #333; }
.copyable { cursor: pointer; color: var(--rotary-blue); }

/* Formulario */
.form-card {
  background: white;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

.donation-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 24px;
}

.form-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 8px;
  font-size: 0.9rem;
  color: #444;
}

.form-group input, .form-group select {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.2s;

  &:focus {
    outline: none;
    border-color: var(--rotary-blue);
  }
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.checkbox-group {
  display: flex;
  align-items: center;
  gap: 10px;
  
  input { width: auto; }
  label { margin: 0; font-weight: 400; font-size: 0.9rem; }
}

.btn-submit {
  background: var(--rotary-blue);
  color: white;
  padding: 16px;
  border: none;
  border-radius: 8px;
  font-weight: 700;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background 0.2s;

  &:hover {
    background: #123670;
  }
  
  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
}
</style>
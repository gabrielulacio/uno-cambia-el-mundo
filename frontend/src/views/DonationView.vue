<template>
  <div class="donation-page">
    <NavigationBar />

    <main class="donation-content">
      <div class="container">
        <div v-if="loading" class="loading-message">
          Cargando datos...
        </div>

        <div v-if="error" class="error-message">
          <p>Error al cargar los datos. Por favor, intenta de nuevo más tarde.</p>
          <p>Detalle: {{ error }}</p>
        </div>

        <section v-if="!loading && !error" class="progress-section">
          <h1>Nuestra Meta</h1>
          <p>Tu donación nos acerca a nuestro objetivo.</p>
          <DonationProgressBar :goal="donationStatus.goal" :current="donationStatus.current" />
        </section>

        <section v-if="!loading && !error" class="methods-section">
          <h2 class="methods-title">Métodos de pago</h2>
          <div class="methods-grid">
            <button v-for="m in paymentMethods" :key="m.id" class="method-card" @click="openMethod(m)">
              <img v-if="m.logo" :src="m.logo" :alt="m.name" class="method-logo" />
              <span class="method-name">{{ m.name }}</span>
            </button>
          </div>
        </section>
      </div>
    </main>

    <FooterSection />

    <!-- Modal de detalles del método -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <header class="modal-header">
          <h3>{{ selectedMethod?.name }}</h3>
          <button class="modal-close" @click="closeModal" aria-label="Cerrar">✕</button>
        </header>
        <div class="modal-body">
          <p v-if="selectedMethod?.description" class="modal-description">{{ selectedMethod.description }}</p>
          <ul class="fields-list" v-if="selectedMethod?.fields?.length">
            <li v-for="(f, idx) in selectedMethod.fields" :key="idx" class="field-row">
              <span class="field-label">{{ f.label }}</span>
              <span class="field-value">{{ f.valueMasked || '********' }}</span>
              <button v-if="f.copyValue" class="copy-btn" @click="copyToClipboard(f.copyValue)">Copiar</button>
            </li>
          </ul>
          <p v-else>No hay datos disponibles para este método.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import NavigationBar from '@/components/NavigationBar.vue';
import FooterSection from '@/components/FooterSection.vue';
import DonationProgressBar from '@/components/DonationProgressBar.vue';
import { getDonationStatus, getPaymentMethods } from '@/services/api.js';
import { useDonationStatus } from '@/store/useDonationStatus.js';

const { goal, current, loading: loadingDonation, error: errorDonation, loadDonationStatus } = useDonationStatus();
const donationStatus = ref({ goal: 10000, current: 10000 });
const paymentMethods = ref([]);
const loading = ref(true);
const error = ref(null);

const showModal = ref(false);
const selectedMethod = ref(null);

function openMethod(method) {
  selectedMethod.value = method;
  showModal.value = true;
}

function closeModal() {
  showModal.value = false;
  selectedMethod.value = null;
}

async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    // Opcional: mostrar feedback al usuario
  } catch (e) {
    console.error('No se pudo copiar al portapapeles', e);
  }
}

onMounted(async () => {
  try {
    // Cargar estado de donación compartido
    await loadDonationStatus();
    donationStatus.value = { goal: goal.value, current: current.value };
    // Obtener métodos de pago desde backend para no exponer datos sensibles
    // const methods = await getPaymentMethods();
    // paymentMethods.value = methods;
    // Mock temporal si backend aún no está listo:
    paymentMethods.value = [
      {
        id: 'pagomovil',
        name: 'Pago Movil (QR)',
        logo: '/icons/pagomovil.png',
        description: 'Realiza el pago movil desde cualquier banco nacional',
        fields: [
          { label: 'Banco', valueMasked: 'Banco Mercantil'},
          { label: 'Telefono', valueMasked: '04241234567', copyValue: '04241234567' },
          { label: 'Cédula', valueMasked: 'V-123456789', copyValue: 'V-123456789' },
        ],
      },
      {
        id: 'binancepay',
        name: 'Binance Pay',
        logo: '/icons/binancepay.png',
        description: 'Realiza una transferencia de USDT o cualquier criptomoneda via Binance Pay.',
        fields: [
          { label: 'Correo', valueMasked: 'prueba@rotarysc.org', copyValue: 'prueba@rotarysc.org' },
        ],
      },
      {
        id: 'Zelle',
        name: 'Zelle',
        logo: '/icons/zelle.png',
        description: 'Podés acercarte al centro médico para realizar tu aporte.',
        fields: [],
      },
      {
        id: 'Zelle2',
        name: 'Zelle',
        logo: '/icons/zelle.png',
        description: 'Podés acercarte al centro médico para realizar tu aporte.',
        fields: [],
      },
    ];
  } catch (err) {
    error.value = err.message || 'Error desconocido';
    console.error('Error fetching data:', err);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.donation-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--background-color);
}

.donation-content {
  flex: 1 1 auto;
  background: #fff;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 20px 48px;
}

.progress-section {
  background-color: var(--rotary-blue);
  color: #fff;
  padding: 28px;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  width: 100%;
  max-width: 720px;
  margin: 0 auto 24px;
  text-align: center;
}

.progress-section h1 { color: #fff; margin: 0 0 8px 0; }
.progress-section p { color: rgba(255,255,255,0.9); margin: 0 0 12px 0; }

.donation-summary { margin-top: 16px; font-size: 1.05rem; }
.donation-summary p { color: #fff; }

.methods-section { margin-top: 12px; }
.methods-title { text-align: center; margin: 0 0 16px 0; }
.methods-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.method-card {
  background: #fff;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  transition: transform .15s ease, box-shadow .15s ease;
}
.method-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.08); }
.method-logo { width: 48px; height: 48px; object-fit: contain; }
.method-name { font-weight: 700; }

/* Modal */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  z-index: 1000;
}
.modal-content {
  background: #fff;
  width: 100%;
  max-width: 560px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}
.modal-header { display: flex; justify-content: space-between; align-items: center; padding: 14px 16px; border-bottom: 1px solid rgba(0,0,0,0.08); }
.modal-close { background: transparent; border: none; font-size: 1.25rem; cursor: pointer; }
.modal-body { padding: 16px; }
.modal-description { margin: 0 0 10px 0; }
.fields-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; }
.field-row { display: grid; grid-template-columns: 1fr auto auto; align-items: center; gap: 8px; }
.field-label { font-weight: 600; }
.field-value { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace; }
.copy-btn { padding: 6px 10px; border: 1px solid rgba(0,0,0,0.12); border-radius: 8px; background: #f7f7f7; cursor: pointer; }

/* Responsive */
@media (max-width: 900px) {
  .methods-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 600px) {
  .methods-grid { grid-template-columns: 1fr; }
  .progress-section { padding: 20px; }
}

.loading-message, .error-message {
  margin: 14px 0; text-align: center;
}

.error-message {
  color: #d9534f; background: #f2dede; border: 1px solid #ebccd1; padding: 12px; border-radius: 8px;
}
</style>


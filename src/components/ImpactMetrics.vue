<template>
  <section class="impact-section">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">{{ $t('impact.eyebrow') }}</span>
        <h2>{{ $t('impact.title') }}</h2>
        <p>{{ $t('impact.subtitle') }}</p>
      </div>

      <div class="metrics-grid">
        <div class="metric-card">
          <div class="icon-wrapper">🍲</div>
          <div class="metric-content">
            <span class="number">+1,200</span>
            <span class="label">{{ $t('impact.lunches.label') }}</span>
            <p class="detail">{{ $t('impact.lunches.detail') }}</p>
          </div>
        </div>

        <div class="metric-card">
          <div class="icon-wrapper">💊</div>
          <div class="metric-content">
            <span class="number">+350</span>
            <span class="label">{{ $t('impact.patients.label') }}</span>
            <p class="detail">{{ $t('impact.patients.detail') }}</p>
          </div>
        </div>

        <div class="metric-card">
          <div class="icon-wrapper">📚</div>
          <div class="metric-content">
            <span class="number">85</span>
            <span class="label">{{ $t('impact.scholarships.label') }}</span>
            <p class="detail">{{ $t('impact.scholarships.detail') }}</p>
          </div>
        </div>
      </div>

      <div class="transparency-banner">
        <div class="t-icon">🔒</div>
        <div class="t-text">
          <strong>{{ $t('impact.transparency_title') }}</strong>
          {{ $t('impact.transparency_text') }}
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped lang="scss">
.impact-section {
  padding: 80px 20px;
  background-color: #f4f6f9; /* Un gris muy suave para diferenciar del blanco */
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 60px;

  .eyebrow {
    color: var(--rotary-gold);
    font-weight: 700;
    text-transform: uppercase;
    font-size: 0.9rem;
    letter-spacing: 1px;
  }

  h2 {
    font-size: 2.5rem;
    color: var(--rotary-blue);
    margin: 10px 0 16px;
  }

  p {
    color: #666;
    max-width: 600px;
    margin: 0 auto;
    font-size: 1.1rem;
  }
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 60px;
}

.metric-card {
  background: white;
  padding: 32px;
  border-radius: 16px;
  text-align: center;
  transition: transform 0.3s ease;
  border: 1px solid rgba(0,0,0,0.05);
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(23, 69, 143, 0.1);
  }
}

.icon-wrapper {
  font-size: 3rem;
  margin-bottom: 16px;
  background: rgba(247, 168, 27, 0.1);
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  margin: 0 auto 24px;
}

.number {
  display: block;
  font-size: 3rem;
  font-weight: 800;
  color: var(--rotary-blue);
  line-height: 1;
  margin-bottom: 8px;
}

.label {
  display: block;
  font-size: 1.1rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 8px;
  text-transform: uppercase;
}

.detail {
  font-size: 0.95rem;
  color: #777;
  line-height: 1.5;
}

/* Banner Transparencia */
.transparency-banner {
  background: var(--rotary-blue);
  color: white;
  padding: 24px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 20px;
  max-width: 800px;
  margin: 0 auto;
  box-shadow: 0 10px 30px rgba(23, 69, 143, 0.25);

  .t-icon {
    font-size: 2rem;
  }

  .t-text {
    font-size: 1rem;
    line-height: 1.5;
  }

  @media(max-width: 600px) {
    flex-direction: column;
    text-align: center;
  }
}
</style>
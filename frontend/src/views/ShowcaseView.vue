<template>
  <div class="showcase">
    <h1>Showcase: Variables y Colores</h1>

    <section>
      <h2>Colores</h2>
      <div class="color" v-for="(color, name) in colors" :key="name">
        <div :style="{ backgroundColor: `var(${color})` }" class="color-box"></div>
        <p>{{ name }}: {{ color }}</p>
      </div>
    </section>

    <section>
      <h2>Fuentes</h2>
      <p class= "text-regular">Texto regular</p>
      <p class="text-semibold">Texto semibold</p>
      <p class= "text-bold">Texto bold</p>
      <p class= "text-small">Texto small</p>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      colors: {
        'Rotary Blue': '--rotary-blue',
        'Rotary Gold': '--rotary-gold',
        'Azure': '--azure',
        'White': '--white',
        'Black': '--black',
        'Background Color': '--background-color',
        'Shadow Light': '--shadow-light',
        'Shadow Medium': '--shadow-medium',
      },
    };
  },
};
</script>

<style scoped lang="scss">
@use '@/assets/styles/_typography' as *;

.color {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.color-box {
  width: 50px;
  height: 50px;
  margin-right: 1rem;
  border: 1px solid #ccc;
}

.text-semibold {
  @include paragraph-semibold;
}

.text-regular {
  @include paragraph-regular;
}

.text-bold {
  @include paragraph-bold;
}



</style>
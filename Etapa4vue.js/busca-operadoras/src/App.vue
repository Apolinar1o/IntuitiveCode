<template>
  <div>
    <input v-model="query" placeholder="Buscar operadora" />
    <button @click="buscar">Buscar</button>
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.id">{{ operadora.nome }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return { query: '', operadoras: [] };
  },
  methods: {
    async buscar() {
      const { data } = await axios.get(`http://127.0.0.1:8000/buscar?q=${this.query}`);
      this.operadoras = data;
    }
  }
};
</script>
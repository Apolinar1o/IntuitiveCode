<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4 text-primary fw-bold">📡 Busca de Operadoras</h1>

    <div class="input-group mb-4">
      <input 
        v-model="query" 
        class="form-control rounded-start border-primary"
        placeholder="🔍 Digite o nome da operadora..."
      />
      <button @click="buscarOperadora" class="btn btn-primary px-4">🔎 Buscar</button>
    </div>

    <div v-if="errorMessage" class="alert alert-danger text-center">
      {{ errorMessage }}
    </div>

    <div v-if="resultados.length">
      <h2 class="text-center mt-4 text-success fw-bold">Resultados encontrados ✅</h2>
      
      <div v-for="(operadora, index) in resultados" :key="index" class="card p-3 shadow-lg border-0 mb-4">
        <div class="card-body">
          <h4 class="fw-bold text-primary">{{ operadora.Nome_Fantasia }}</h4>
          <p><strong>Razão Social:</strong> {{ operadora.Razao_Social }}</p>
          <p><strong>Modalidade:</strong> {{ operadora.Modalidade }}</p>

          <div class="row">
            <div class="col-md-6">
              <p><strong>Endereço:</strong> {{ operadora.Logradouro }}, {{ operadora.Numero }}</p>
              <p><strong>Complemento:</strong> {{ operadora.Complemento || "N/A" }}</p>
              <p><strong>Bairro:</strong> {{ operadora.Bairro }}</p>
            </div>
            <div class="col-md-6">
              <p><strong>Cidade:</strong> {{ operadora.Cidade }} - {{ operadora.UF }}</p>
              <p><strong>CEP:</strong> {{ operadora.CEP }}</p>
              <p><strong>DDD:</strong> {{ operadora.DDD }} | 📞 <strong>Telefone:</strong> {{ operadora.Telefone }}</p>
            </div>
          </div>

          <hr />
          <p><strong>Representante:</strong> {{ operadora.Representante }} ({{ operadora.Cargo_Representante }})</p>
          <p><strong>E-mail:</strong> 📧 {{ operadora.Endereco_eletronico }}</p>
          <p><strong>Região de Comercialização:</strong> 🌍 {{ operadora.Regiao_de_Comercializacao }}</p>
          <p><strong>Data de Registro ANS:</strong> 🗓️ {{ operadora.Data_Registro_ANS }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: "",
      resultados: [],
      errorMessage: "",
    };
  },
  methods: {
    async buscarOperadora() {
      this.errorMessage = "";
      this.resultados = [];

      try {
        const response = await axios.get(`http://127.0.0.1:8080/buscar?q=${this.query}`);
        if (response.data.length > 0) {
          this.resultados = response.data;
        } else {
          this.errorMessage = "Nenhuma operadora encontrada.";
        }
      } catch (error) {
        this.errorMessage = "Erro ao buscar operadora.";
        console.error("Erro na requisição:", error);
      }
    },
  },
};
</script>
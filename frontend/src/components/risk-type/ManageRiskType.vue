<template>
  <div class="">
    <h1>Manage the Risk Types</h1>
    <div class="container">
      <table class="table">
        <thead>
          <th><a href="#">Name</a></th>
          <th><a href="#">Description</a></th>
        </thead>
        <tbody>
          <tr v-for="risk in risk_types" :key="risk.id">
            <td>{{ risk.name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ManageRiskType',
  data () {
    return {
      selected: '',
      risk_types: []
    }
  },
  mounted () {
    this.$http.get('http://localhost:8000/risk-types/api/v1/risk-types/')
      .then((req) => (this.risk_types = req.data))
  }
}
</script>

<style scoped>
  .container {
    display: flex;
    justify-content: center;
  }
</style>

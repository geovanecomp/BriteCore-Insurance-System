<style src="./Datefield.scss" lang="scss" scoped></style>
<template lang="html">
  <div class="datefield">
    <label :for="lblName">{{label}}</label>
    <input type="date" v-model="valueDate" />    
  </div>
</template>

<script>
export default {
  name: 'Datefield',
  props: {
    value: {
      default: ''
    },
    label: {
      default: 'Text'
    },
    lblName: {
      default: ''
    }
  },
  data () {
    return {
      valueDate: ''
    }
  },
  mounted () {
    this.valueDate = this.value
  },
  watch: {
    value (pVal) {
      this.valueDate = pVal
    },
    valueDate (pValDate) {
      this.$emit('input', pValDate)
    }
  }
}
</script>

<style src="./Combofield.scss" lang="scss" scoped></style>
<template lang="html">
  <div class="combofield">
    <label :for="lblName">{{label}} <sup v-if="isRequired" class="asterisk">*</sup></label>
    <select
    :name="lblName"
    v-model="selectedValue"
    :options="content"
    :disabled="isDisabled"
    :class="requiredRule"
    @blur="isSelected"
    @change="selected">
    <option v-for="item in content" :key='item.id' :value="item.id" >{{ item.name }}</option>
  </select>
</div>
</template>

<script>
export default {
  name: 'Combofield',
  props: {
    value: {
      default: ''
    },
    lblName: {
      default: 'Text'
    },
    content: {
      default () { return [] }
    },
    label: {
      default: 'Text'
    },
    isDisabled: {
      deafult: false
    },
    isRequired: {
      default: false
    }
  },
  data () {
    return {
      selection: {},
      ifDisabled: '',
      selectedValue: '',
      requiredRule: ''
    }
  },
  watch: {
    value (pVal, pValOld) {
      this.selectedValue = this.value
      if (this.value) {
        this.$emit('rule', this.label, false)
      }
    },
    selectedValue (pVal, pValOld) {
      this.$emit('input', this.selectedValue)
    }
  },
  computed: {
    isValid () {
      return this.selectedValue
    }
  },
  mounted () {
    this.verifyRules()
    this.selectedValue = this.value || null
  },
  methods: {
    selected () {
      const selected = this.selectedValue
      if (selected) {
        this.$emit('input', selected)
        this.$emit('change', selected)
        this.$emit('rule', this.label, false)
        this.requiredRule = ''
        return false
      } else {

      }
    },
    verifyRules () {
      if (this.isRequired) {
        this.$emit('rule', this.label, true)
      }
    },
    isSelected () {
      if (!this.selectedValue && this.isRequired) {
        this.requiredRule = 'error'
      }
    }
  }
}
</script>

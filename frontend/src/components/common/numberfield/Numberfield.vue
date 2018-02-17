<style src="./Numberfield.scss" lang="scss" scoped></style>
<template lang="html">
  <div class="textfield">
    <label :for="lblName" :class="selected">{{label}} <sup v-if="isRequired" class="asterisk">*</sup></label>
    <input type="text"
    :name="lblName"
    :id="lblName"
    @focus="upLabel"
    @blur="removeFloating"
    v-model="inputValue"
    :class="requiredRule"
    :disabled="isDisabled"/>
  </div>
</template>

<script>
export default {
  name: 'Numberfield',
  props: {
    value: {
      default: ''
    },
    label: {
      default: 'Text'
    },
    lblName: {
      default: ''
    },
    isRequired: {
      default: false
    },
    defineMask: {
      default: ''
    },
    isDisabled: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      selected: '',
      inputValue: '',
      requiredRule: ''
    }
  },
  watch: {
    value (pVal, pValOld) {
      this.inputValue = this.value
      if (this.value) {
        this.$emit('rule', this.label, false)
      }
      if (this.inputValue) {
        this.selected = 'focused'
      }
      if (this.isRequired && this.value.length === 0) {
        this.$emit('rule', this.label, true)
      }
    },
    inputValue (pVal, pValOld) {
      this.$emit('input', this.inputValue)
    },
    isRequired (pVal, pOldVal) {
      this.verifyRules()
    }
  },
  mounted () {
    this.inputValue = this.value
    if (this.inputValue) {
      this.selected = 'focused'
    }
    this.verifyRules()
  },
  methods: {
    upLabel () {
      this.selected = 'focused'
    },
    removeFloating () {
      if (!this.inputValue) {
        if (this.isRequired) {
          this.requiredRule = 'error'
        }
        this.selected = ''
      } else {
        this.requiredRule = ''
        this.$emit('input', this.inputValue)
        this.$emit('rule', this.label, false)
      }
    },
    verifyRules () {
      if (this.isRequired) {
        this.$emit('rule', this.label, true)
      }
    }
  }
}
</script>

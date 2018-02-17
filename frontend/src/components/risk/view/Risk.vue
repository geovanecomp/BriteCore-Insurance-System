<style src="./Risk.scss" lang="scss" scoped></style>
<template>
  <section class="risk">
    <h1>Select the risk</h1>
    <div class="risk--type-content row">
      <combobox v-model="form.risk_type" :content="riskTypes" label="risk type" class="col-6"/>
      <combobox v-model="form.risk" :content="risks" label="risk" class="col-6"/>
    </div>

    <div class="risk--content row">
      <h3>Add the risk fields</h3>
      <form @submit.stop.prevent="handleNewField(form)" class="risk--content-fields row">
        <combobox v-model="form.fieldType" :content="fieldTypes" label="field type" class="col-4"/>
        <textbox v-model="form.fieldLabel" label="field label" class="col-6" :is-required="true"/>
        <button class="risk--action-new col-2">+</button>
      </form>

      <div class="risk--content-header">
        <li>
          <ul class="row">
            <li class="col-4">Field Type</li>
            <li class="col-6">Field Label</li>
            <li class="col-2"></li>
          </ul>
        </li>
      </div>
      <div class="risk--list">
        <li v-for="(field, idx) in fields" :key='idx'>
          <ul class="row">
            <li class="col-4">{{ field.fieldType | fieldTypeFilter(fieldTypes)}}</li>
            <li class="col-6">{{ field.fieldLabel }}</li>
            <li class="col-2"><span @click="removeField(idx)"><icon-garbage class="icon-garbage"/></span></li>
          </ul>
        </li>
      </div>
    </div>

    <div class="actions col-12">
      <button class="button--save col-4" disabled @click="registerNewFieldsByRisk(fields)">Save</button>
    </div>
  </section>
</template>

<script>
import ManageRiskTypeModel from '@/components/risk-type/model/ManageRiskTypeModel'
import ManageRiskModel from '../model/ManageRiskModel'
import RiskModel from '../model/RiskModel'
import Textbox from '@/components/common/textbox/Textbox'
import Combobox from '@/components/common/combobox/Combobox'
import { IconEdit, IconGarbage } from '@/components/common/icon'

export default {
  name: 'Risk',
  components: {
    Textbox,
    Combobox,
    IconEdit,
    IconGarbage
  },
  data () {
    return {
      manageRiskTypeModel: null,
      manageRiskModel: null,
      riskModel: null,
      riskTypes: [],
      risks: [],
      fieldTypes: [],
      fields: [],
      form: {
        risk_type: '',
        field_type: '',
        field_label: ''
      }
    }
  },
  mounted () {
    this.manageRiskModel = ManageRiskModel
    this.manageRiskTypeModel = ManageRiskTypeModel
    this.riskModel = RiskModel
    this.setContentType()
  },
  filters: {
    fieldTypeFilter (pParam, pFieldTypes) {
      return pFieldTypes.filter(item => item.id === pParam)[0].name
    }
  },
  watch: {
    'form.risk_type' (pRiskType) {
      console.log('selecionei!')
      console.log(pRiskType)
      if (pRiskType) {
        this.setRisks(pRiskType)
      }
    }
  },
  methods: {
    handleNewField (pForm) {
      if (pForm) {
        let field = {
          fieldLabel: pForm.fieldLabel,
          fieldType: pForm.fieldType
        }

        this.fields.push(field)
        this.cleanFields()
      }
    },
    registerNewFieldsByRisk (pRisks) {
      // To be created
    },
    cleanFields () {
      this.form.fieldType = ''
      this.form.fieldLabel = ''
    },
    setContentType () {
      this.setAllRiskTypes()
      this.setAllFieldTypes()
    },
    setAllRiskTypes () {
      this.manageRiskTypeModel.getAllRiskTypes()
        .then(res => (this.riskTypes = res.data))
        .catch(error => console.error(error))
    },
    setAllFieldTypes () {
      this.manageRiskModel.getAllFieldTypes()
        .then(res => (this.fieldTypes = res.data))
        .catch(error => console.error(error))
    },
    setRisks (pRiskTypeId) {
      this.riskModel.getRisksByRiskType(pRiskTypeId)
        .then(res => (this.risks = res.data))
        .catch(error => console.error(error))
    }
  }
}
</script>

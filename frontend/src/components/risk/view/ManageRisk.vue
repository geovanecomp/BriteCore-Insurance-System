<style src="./ManageRisk.scss" lang="scss" scoped></style>
<template>
  <section class="manage-risk">
    <h1>Manage the Risks</h1>
    <div class="manage-risk--type-content row">
      <combofield v-model="form.risk_type" :content="riskTypes" label="risk type" class="col-6"/>
      <textfield v-model="form.name" label="name" class="col-6" :is-required="true"/>
    </div>

    <div class="manage-risk--content row">
      <h3>Add the risk fields</h3>
      <form @submit.stop.prevent="handleNewField(form)" class="manage-risk--content-fields row">
        <combofield v-model="form.fieldType" :content="fieldTypes" label="field type" class="col-4"/>
        <textfield v-model="form.fieldLabel" label="field label" class="col-6" :is-required="true"/>
        <button class="manage-risk--action-new col-2">+</button>
      </form>

      <div class="manage-risk--content-header">
        <li>
          <ul class="row">
            <li class="col-4">Field Type</li>
            <li class="col-6">Field Label</li>
            <li class="col-2"></li>
          </ul>
        </li>
      </div>
      <div class="manage-risk--list">
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
import Textfield from '@/components/common/textfield/Textfield'
import Combofield from '@/components/common/combofield/Combofield'
import { IconEdit, IconGarbage } from '@/components/common/icon'

export default {
  name: 'ManageRisk',
  components: {
    Textfield,
    Combofield,
    IconEdit,
    IconGarbage
  },
  data () {
    return {
      manageRiskTypeModel: null,
      manageRiskModel: null,
      riskTypes: [],
      fieldTypes: [],
      fields: [],
      form: {
        name: '',
        riskType: '',
        fieldType: '',
        fieldLabel: ''
      }
    }
  },
  filters: {
    fieldTypeFilter (pParam, pFieldTypes) {
      return pFieldTypes.filter(item => item.id === pParam)[0].name
    }
  },
  mounted () {
    this.manageRiskModel = ManageRiskModel
    this.manageRiskTypeModel = ManageRiskTypeModel
    this.setContentType()
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
      this.fieldTypes = this.setAllFieldTypes()
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
    }
  }
}
</script>

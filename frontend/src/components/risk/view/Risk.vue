<style src="./Risk.scss" lang="scss" scoped></style>
<template>
  <section class="risk">
    <h1>Select the risk</h1>
    <div class="risk--type-content row">
      <combofield v-model="form.risk_type" :content="riskTypes" label="risk type" class="col-6"/>
      <combofield v-model="form.risk" :content="risks" label="risk" class="col-6"/>
    </div>

    <div class="risk--content row">
      <h3 v-if="fieldsByRisk.length">Risk fields / information</h3>

      <component class="fields-by-risk-elements"
        v-for="(fieldByRisk, idx) in fieldsByRisk" :key='idx'
        :is="mapFieldsId[fieldByRisk.field.id]"
        :label="fieldByRisk.field.label"
        v-model="fieldsByRisk[idx].value"
        :content="fieldsByRisk[idx].value"
      >
      </component>
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
import Textfield from '@/components/common/textfield/Textfield'
import Numberfield from '@/components/common/numberfield/Numberfield'
import Datefield from '@/components/common/datefield/Datefield'
import Combofield from '@/components/common/combofield/Combofield'
import { IconEdit, IconGarbage } from '@/components/common/icon'

export default {
  name: 'Risk',
  components: {
    Textfield,
    Numberfield,
    Combofield,
    Datefield,
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
      mapFieldsId: [
        '',
        'Textfield',
        'Numberfield',
        'Datefield',
        'Combofield'
      ],
      fieldsByRisk: [],
      form: {
        risk_type: '',
        field_type: '',
        field_label: '',
        risk: ''
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
      if (pRiskType) {
        this.setRisks(pRiskType)
      }
    },
    'form.risk' (pRisk) {
      if (pRisk) {
        this.setFieldsByRisk(pRisk)
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
    },
    setFieldsByRisk (pRiskId) {
      this.riskModel.getFieldsByRisk(pRiskId)
        .then(res => (this.fieldsByRisk = res.data))
        .catch(error => console.error(error))
    }
  }
}
</script>

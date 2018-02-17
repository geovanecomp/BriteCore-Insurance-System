<style src="./ManageRisk.scss" lang="scss" scoped></style>
<template>
  <section class="manage-risk">
    <h1>Manage the Risks</h1>
    <div class="manage-risk--type-content row">
      <textbox v-model="form.riskName" label="name" class="col-6" :is-required="true"/>
      <combobox v-model="form.riskType" :content="riskTypes" label="risk type" class="col-6"/>
    </div>

    <div class="manage-risk--content row">
      <h3>Add the risk fields</h3>
      <form @submit.stop.prevent="handleNewField(form)" class="manage-risk--content-fields row">
        <combobox v-model="form.fieldType" :content="fieldTypes" label="field type" class="col-4"/>
        <textbox v-model="form.fieldName" label="field label" class="col-6" :is-required="true"/>
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
        <li v-for="(field, idx) in risks" :key='idx'>
          <ul class="row">
            <li class="col-4">{{ field.fieldType | fieldTypeFilter(fieldTypes)}}</li>
            <li class="col-6">{{ field.fieldName }}</li>
            <li class="col-2"><span @click="deleteRisk(risk, idx)"><icon-garbage class="icon-garbage"/></span></li>
          </ul>
        </li>
      </div>
    </div>

    <div class="actions col-12">
      <button class="button--save col-4" @click="registerNewFieldsByRisk(risks)">Save</button>
    </div>
  </section>
</template>

<script>
import ManageRiskTypeModel from '@/components/risk-type/model/ManageRiskTypeModel'
import ManageRiskModel from '../model/ManageRiskModel'
import Textbox from '@/components/common/textbox/Textbox'
import Combobox from '@/components/common/combobox/Combobox'
import { toast } from '@/components/common/alert'
import { IconEdit, IconGarbage } from '@/components/common/icon'

export default {
  name: 'ManageRisk',
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
      riskTypes: [],
      fieldTypes: [],
      risks: [],
      form: {
        riskName: '',
        riskType: '',
        fieldType: '',
        fieldName: ''
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
    this.getContentType()
  },
  methods: {
    handleNewField (pForm) {
      if (pForm) {
        let tempObj = {
          name: pForm.fieldName,
          description: pForm.fieldName,
          field_type: pForm.fieldType,
          required: false
        }
        this.manageRiskModel.createField(tempObj).then((res) => {
          this.risks.push({...res.data})
          this.cleanFields()
        })
      }
    },
    registerNewFieldsByRisk (pRisks) {
      if (this.risks.length > 0) {
        let riskObj = {
          name: this.form.riskName,
          risk_type: this.form.riskType
        }
        this.manageRiskModel.createRisk(riskObj)
          .then((res) => {
            this.manageRiskModel.createFieldsByRisk(res.data.id, pRisks)
              .then((res) => {
                this.cleanFields()
                toast.success('Fields by risk created', 'Success!')
              })
          })
          .catch((error) => {
            console.error(error)
            toast.error('Server internal error', 'Error!')
          })
      } else {
        toast.error('A field by risk is required', 'Field Required')
      }
    },
    updateRisk (pRisk) {
      this.manageRiskModel.updateRisk(pRisk.id, pRisk)
        .then((res) => {
          this.cleanFields()
          toast.success('Risk updated', 'Success!')
        })
        .catch((error) => {
          console.error(error)
          toast.error('Server internal error', 'Error!')
        })
    },
    deleteRisk (pRisk, index) {
      this.manageRiskModel.deleteRisk(pRisk.id)
        .then((res) => {
          this.risks.splice(-1, index)
          toast.success('Risk removed', 'Success!')
        })
        .catch((error) => {
          console.error(error)
          toast.error('Server internal error', 'Error!')
        })
    },
    editRisk (pRisk) {
      this.updateRisk = true
      this.form = pRisk
    },
    cleanFields () {
      this.form.fieldType = ''
      this.form.fieldName = ''
    },
    getContentType () {
      this.manageRiskTypeModel.getAllRiskTypes()
        .then((res) => {
          this.riskTypes = res.data
        })
        .catch((error) => {
          console.error(error)
        })

      this.manageRiskModel.getAllFieldTypes()
        .then((res) => {
          this.fieldTypes = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>

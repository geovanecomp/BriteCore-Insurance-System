<style src="./ManageRiskType.scss" lang="scss" scoped></style>
<template>
  <section class="manage-risk-type">
    <h1>Manage the Risk Types</h1>
    <div class="manage-risk-type--content row">
      <form @submit.stop.prevent="handleAction(form)" class="manage-risk-type--content-fields row">
        <textfield v-model="form.name" label="name" class="col-4" :is-required="true"/>
        <textfield v-model="form.description" label="description" class="col-6"/>
        <button class="manage-risk-type--action-new col-2" v-if="!updateRisk">Register</button>
        <button class="manage-risk-type--action-new col-2" v-if="updateRisk">Update</button>
      </form>

      <div class="manage-risk-type--content-header">
        <li>
          <ul class="row">
            <li class="col-4">Name</li>
            <li class="col-6">Description</li>
            <li class="col-1"></li>
            <li class="col-1"></li>
          </ul>
        </li>
      </div>
      <div class="manage-risk-type--list">
        <li v-for="(risk, idx) in riskTypes" :key='idx'>
          <ul class="row">
            <li class="col-4">{{ risk.name }}</li>
            <li class="col-6">{{ risk.description }}</li>
            <li class="col-1"><span @click="deleteRiskType(risk, idx)"><icon-garbage class="icon-garbage"/></span></li>
            <li class="col-1"><span @click="editRiskType(risk)"><icon-edit class="icon-edit"/></span></li>
          </ul>
        </li>
      </div>
    </div>
  </section>
</template>

<script>
import ManageRiskTypeModel from '../model/ManageRiskTypeModel'
import Textfield from '@/components/common/textfield/Textfield'
import { toast } from '@/components/common/alert'
import { IconEdit, IconGarbage } from '@/components/common/icon'

export default {
  name: 'ManageRiskType',
  components: {
    Textfield,
    IconEdit,
    IconGarbage
  },
  data () {
    return {
      manageRiskTypeModel: null,
      riskTypes: [],
      errors: [],
      form: {
        name: '',
        description: ''
      },
      updateRisk: false
    }
  },
  mounted () {
    this.manageRiskTypeModel = ManageRiskTypeModel
    this.getAllRiskTypes()
  },
  methods: {
    handleAction (pForm) {
      if (!this.updateRisk) {
        this.registerNewRiskType(pForm)
      } else {
        this.updateRiskType(pForm)
      }
    },
    registerNewRiskType (pForm) {
      if (pForm.name) {
        this.manageRiskTypeModel.createRiskType(pForm)
          .then((res) => {
            this.cleanFields()
            this.getAllRiskTypes()
            toast.success('Risk type created', 'Success!')
          })
          .catch((error) => {
            console.error(error)
            toast.error('Server internal error', 'Error!')
          })
      } else {
        toast.error('Name is required', 'Field Required')
      }
    },
    updateRiskType (pRisk) {
      this.manageRiskTypeModel.updateRiskType(pRisk.id, pRisk)
        .then((res) => {
          this.cleanFields()
          toast.success('Risk type updated', 'Success!')
        })
        .catch((error) => {
          console.error(error)
          toast.error('Server internal error', 'Error!')
        })
    },
    deleteRiskType (pRisk, index) {
      this.manageRiskTypeModel.deleteRiskType(pRisk.id)
        .then((res) => {
          this.riskTypes.splice(-1, index)
          toast.success('Risk type removed', 'Success!')
        })
        .catch((error) => {
          console.error(error)
          toast.error('Server internal error', 'Error!')
        })
    },
    editRiskType (pRiskType) {
      this.updateRisk = true
      this.form = pRiskType
    },
    cleanFields () {
      this.form = {
        name: '',
        description: ''
      }
    },
    getAllRiskTypes () {
      this.manageRiskTypeModel.getAllRiskTypes()
        .then((res) => {
          this.riskTypes = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>

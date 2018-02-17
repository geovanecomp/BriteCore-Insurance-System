import Vue from 'vue'
import Router from 'vue-router'
import MainHeader from '@/components/common/MainHeader'
import MainFooter from '@/components/common/MainFooter'
import WelcomePage from '@/components/WelcomePage'
import ManageRiskType from '@/components/risk-type/view/ManageRiskType'
import ManageRisk from '@/components/risk/view/ManageRisk'
import Risk from '@/components/risk/view/Risk'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'WelcomePage',
      components: {
        default: WelcomePage,
        header: MainHeader,
        footer: MainFooter
      }
    },
    {
      path: '/risk-type',
      name: 'ManageRiskType',
      components: {
        default: ManageRiskType,
        header: MainHeader,
        footer: MainFooter
      }
    },
    {
      path: '/manage-risk',
      name: 'ManageRisk',
      components: {
        default: ManageRisk,
        header: MainHeader,
        footer: MainFooter
      }
    },
    {
      path: '/risk',
      name: 'Risk',
      components: {
        default: Risk,
        header: MainHeader,
        footer: MainFooter
      }
    }
  ]
})

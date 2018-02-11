import Vue from 'vue'
import Router from 'vue-router'
import WelcomePage from '@/components/WelcomePage'
import MainHeader from '@/components/common/MainHeader'
import MainFooter from '@/components/common/MainFooter'

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
    }
  ]
})

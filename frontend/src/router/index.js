import Vue from 'vue'
import Router from 'vue-router'
import HelloBriteCore from '@/components/HelloBriteCore'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloBriteCore',
      component: HelloBriteCore
    }
  ]
})

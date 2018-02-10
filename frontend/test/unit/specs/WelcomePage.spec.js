import Vue from 'vue'
import WelcomePage from '@/components/WelcomePage'

describe('WelcomePage.vue', () => {
  it('Should render the correct welcome message', () => {
    const Constructor = Vue.extend(WelcomePage)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.hello h1').textContent)
      .to.equal('Welcome to BriteCore Insurance Administration System')
  })
})

<style src="./style/index.scss" lang="scss"></style>
<template lang="html">
  <div id="app">
    <link rel="shortcut icon" type="image/x-icon" href="../static/images/favicon.ico">
    <router-view name="header">
      <main-header class="header"/>
    </router-view>

    <router-view/>

    <router-view name="footer">
      <main-footer class="footer"/>
    </router-view>
  </div>
</template>

<script>
import MainHeader from '@/components/common/MainHeader'
import MainFooter from '@/components/common/MainFooter'

export default {
  name: 'App',
  components: {
    MainHeader,
    MainFooter
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

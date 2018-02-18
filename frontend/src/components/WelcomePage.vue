<style src="./WelcomePage.scss" lang="scss" scoped></style>
<template>
  <div class="hello">
    <div class="header-content">
      <img src="/static/images/britecore_logo.png" class="logo-resize">
      <h1>{{ welcomeMessage }}</h1>
    </div>
    <div class="body-content">
      <h2>Risk Management</h2>
      <ul>
        <li>
          <router-link class="button" to="/risk-type">Create the risk types</router-link>
        </li>
        <li>
          <router-link class="button" to="/manage-risk">Manage them</router-link>
        </li>
        <li>
          <router-link class="button" to="/risk">Risks</router-link>
        </li>
        <li>
          <a class="button" href="https://github.com/geovanecomp/BriteCore-Insurance-System" target="_blank">
            About the project
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>

export default {
  name: 'WelcomePage',
  data () {
    return {
      welcomeMessage: 'Welcome to BriteCore Insurance Administration System'
    }
  }
}
</script>

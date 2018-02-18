<style src="./MainHeader.scss" lang="scss" scoped></style>
<template>
  <header class="header">
    <img src="/static/images/britecore_logo_header.png" class="logo-resize">
    <div class="information">
      <router-link to="/">Home</router-link>
      <a href="https://www.britecore.com/">Oficial Website</a>
    </div>
  </header>
</template>

<script>
export default {
  name: 'MainHeader'
}
</script>

<template>
  <header class="header">
    <img src="../../assets/britecore_logo_header.png" class="logo-resize">
    <div class="information">
      <router-link to="/">Home</router-link>
      <a href="https://www.britecore.com/">Oficial Website</a>
    </div>
  </header>
</template>

<script>
export default {
  name: 'MainHeader',
  data () {
    return {

    }
  }
}
</script>

<style scoped>
h2 {
  font-weight: normal;
  margin: 0;
}

ul {
  list-style-type: none;
  padding: 0;
  margin-top: 0;
}
li {
  display: inline-block;
  margin: 2px, 5px;
}
a {
  color: #0290a9;
  font-weight: bold;
}

.header {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  /*text-align: center;*/
  /*background-color: red;*/
  margin: 10px;
}

.header .information {
  float: right;
  margin-right: 20px;
}

.information a {
  margin-right: 10px;
}

.logo-resize {
  float: left;
  max-width: 10%;
  height: auto;
}
</style>

<template>
  <div class="hello">
    <img src="../assets/britecore_logo.png" class="logo-resize">
    <h1>{{ welcomeMessage }}</h1>
    <h2>Risk Management</h2>
    <ul>
      <li>
        <a href="#" target="_blank">
          Create the risk types
        </a>
      </li>
      <li>
        <a href="#" target="_blank">
          Manage them
        </a>
      </li>
      <li>
        <a href="#" target="_blank">
          About the project
        </a>
      </li>
    </ul>
    <div class="contact-information">
      <h2>Geovane Pacheco</h2>
      <ul>
        <li>
          <a href="https://www.linkedin.com/in/geovane-pacheco/?locale=en_US" target="_blank">
            LinkedIn
          </a>
        </li>
        <li>
          <a href="https://github.com/geovanecomp" target="_blank">
            GitHub
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloBriteCore',
  data () {
    return {
      welcomeMessage: 'Welcome to BriteCore Insurance Administration System'
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}

h1 {
  font-weight: bold;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #0290a9;
  font-weight: bold;
}

.logo-resize {
  max-width: 40%;
  height: auto;
}

.contact-information > h2 {
  margin-top: 10%;
  height: 10px;
}
</style>

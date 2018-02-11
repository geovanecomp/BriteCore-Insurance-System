<template>
  <footer class='footer'>
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
  </footer>
</template>

<script>
export default {
  name: 'MainFooter',
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

.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  text-align: center;
}
</style>

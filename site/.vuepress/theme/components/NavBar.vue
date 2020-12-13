<template>
  <div class="nav-bar">
    <ul>
      <li class="logo-holder"><img src="logo.png" class="logo" alt="game tree of connect four" /></li>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/team/">Team</router-link></li>
      <li><router-link to="/connect-four/">Connect Four</router-link></li>
      <li><router-link to="/mcts/">MCTS</router-link></li>
      <li><router-link to="/minimax/">Minimax</router-link></li>
      <li><router-link to="/performance/">Performance</router-link></li>
      <li><router-link to="/discussion/">Discussion</router-link></li>
      <li><router-link to="/bibliography/">Bibliography</router-link></li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "NavBar",
    data() {
      return {};
    },
    props: {}
  };
</script>

<style scoped>
 .nav-bar ul {
     font-size: 1.2rem;
     list-style-type: none;
 }
 .nav-bar li {
     padding: 0.3rem;
 }
 .logo {
     width: 100%;
     max-width: 300px;
     min-width: 200px;
 }
 .logo-holder {
     list-style-type: none;
 }
</style>

<template>
  <div class="nav-bar">
    <ul>
      <router-link to="/"><li class="logo-holder"><img src="logo.png" class="logo" alt="game tree of connect four" /></li></router-link>
      <router-link to="/"><li>Home</li></router-link>
      <router-link to="/demo"><li>Demo</li></router-link>
      <router-link to="/team/"><li>Team</li></router-link>
      <router-link to="/connect-four/"><li>Connect Four</li></router-link>
      <router-link to="/mcts/"><li>Monte Carlo Tree Search</li></router-link>
      <router-link to="/minimax/"><li>Minimax</li></router-link>
      <router-link to="/performance/"><li>Performance</li></router-link>
      <router-link to="/bibliography/"><li>Bibliography</li></router-link>
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

<style lang="scss" scoped>
 .nav-bar ul {
     font-size: 1.2rem;
     list-style-type: none;
 }
 .nav-bar li {
     padding: 0.5rem;
 }
 .logo {
     width: 100%;
     width: 200px;
 }
 .logo-holder {
     list-style-type: none;
 }
</style>

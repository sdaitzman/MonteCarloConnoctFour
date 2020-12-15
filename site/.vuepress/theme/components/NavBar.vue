<template>
  <div class="nav-bar">
    <ul>
      <router-link to="/"><li class="logo-holder"><img src="/logo.png" class="logo no-medium-zoom" alt="game tree of connect four" /></li></router-link>
      <router-link class="home-link" to="/"><li><i class="fas fa-home"></i>Home</li></router-link>
      <router-link class="demo-link" to="/demo"><li><i class="fas fa-laptop-code"></i>Demo</li></router-link>
      <router-link class="team-link" to="/team/"><li><i class="fas fa-users"></i>Team</li></router-link>
      <router-link class="conn-link" to="/connect-four/"><li><i class="fas fa-chess-board"></i>Connect Four</li></router-link>
      <router-link class="mcts-link" to="/mcts/"><li><i class="fas fa-tree"></i>Monte Carlo Tree Search</li></router-link>
      <router-link class="mnmx-link" to="/minimax/"><li><i class="fas fa-chart-area"></i>Minimax</li></router-link>
      <router-link class="perf-link" to="/performance/"><li><i class="fas fa-bolt"></i>Performance</li></router-link>
      <router-link class="bibl-link" to="/bibliography/"><li><i class="fas fa-book"></i>Bibliography</li></router-link>
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
    a { text-decoration: none }
 }
 .nav-bar li {
    padding: 0.5rem;
    font-weight: 500;
    i { padding-right: 10px }
 }
 .logo {
     width: 100%;
     width: 200px;
 }
 .logo-holder {
     list-style-type: none;
 }
</style>

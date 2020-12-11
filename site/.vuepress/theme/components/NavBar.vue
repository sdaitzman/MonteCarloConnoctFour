<template>
  <div class="photo-holder">
    <ul>
      <li><router-link to="/connect-four/">Connect Four</router-link></li>
      <li><router-link to="/mcts/">MCTS</router-link></li>
      <li><router-link to="/heuristics/">Heuristics</router-link></li>
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

</style>
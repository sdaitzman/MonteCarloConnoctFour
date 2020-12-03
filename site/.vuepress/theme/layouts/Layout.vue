<template>
  <div class="all-container" :class="$page.title.toLowerCase()">
  <link rel="preconnect" href="https://fonts.gstatic.com"> 
  <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">

    <div class="body-container">
      <div class="body-content">
        <Content />
      </div>
    </div>
  </div>
</template>

<style lang="scss">
@import '../styles/base.scss';

</style>

<style scoped lang="scss">
// @import '../styles/variables';
</style>

<script>
// import Nav from '@theme/components/Nav'
import 'normalize.css'
// import "fontsource-libre-baskerville"

export default {
  components: {
    // Nav
  }
}
</script>

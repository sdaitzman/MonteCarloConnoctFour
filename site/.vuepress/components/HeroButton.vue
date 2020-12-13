<template>
<div>
    <router-link :to="to">
        <button class="hero-button">
            <slot></slot>
        </button>
    </router-link>
</div>
</template>

<script>
/**
  * A hero button for placing in text
  */
// import moment from "moment"
export default {
		name: "HeroButton",
		data() {
            console.log(this)
           return {};
		},
		props: ['to']
};

</script>

<style scoped>

button::after { content: ' →' }

.hero-button {
    padding: 20px;
    margin-bottom: 35px;
    border: 3px solid black;
}
</style>
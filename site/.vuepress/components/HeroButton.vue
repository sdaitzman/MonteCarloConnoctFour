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

<style lang="scss" scoped>

button::after { content: ' →' }

.hero-button {
    transition: background 0.16s ease, color 0.16s ease, border 0.16s ease;
    box-sizing: border-box;
    cursor: pointer;
    padding: 12px 25px;
    margin-bottom: 35px;
    border: 3px solid black;
    outline: none;
    color: black;
    background: white;
    border-radius: 8px;
    &:hover {
        background: lighten(black, 20%);
        border-color: lighten(black, 20%);
        color: white;
    }
    &:active {
        transition: none;
        background: lighten(black, 50%);
        border-color: lighten(black, 50%);
        color: rgba(white, 0.75);
    }
}
</style>
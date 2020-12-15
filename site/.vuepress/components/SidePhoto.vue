<template>
<div class="photo-holder">
  <slot></slot>
</div>
</template>

<script>
/**
  * A, "not so bad" way to put a photo to the left or right of
  * a paragraph in markdown. Just add markdown and an img into the slot
  * of this component
  *
  * TODO: add left and right props
  */
import moment from "moment"
import mediumZoom from 'medium-zoom'


export default {
		name: "SidePhoto",
		data() {
				return {};
		},
    props: {},
    mounted() {
      mediumZoom(document.querySelectorAll('img:not(.logo)'))
    },
    updated() {
      mediumZoom(document.querySelectorAll('img:not(.logo)'))
    }
};
</script>

<style lang="scss" scoped>
.photo-holder {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: row;
  justify-content: space-between;
  img {
    width: 50%;
    align-self: flex-start;
  }
}
.photo-holder p {
  margin: 0;
}

@media (max-width: 825px) {
  .photo-holder {
    flex-direction: column;
    img { width: 100% }
  }
  .photo-holder p {
     margin-top: 1em;
     margin-bottom: 1em;
  }
}
</style>

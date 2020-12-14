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
export default {
		name: "SidePhoto",
		data() {
				return {};
		},
		props: {}
};
</script>

<style scoped>
.photo-holder {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: row;
  justify-content: space-between;
}
.photo-holder p {
  margin: 0;
}
img {
    height: 100%
}
@media (max-width: 750px) {
  .photo-holder {
    flex-direction: column;
  }
  .photo-holder p {
     margin-top: 1em;
     margin-bottom: 1em;
  }
}
</style>

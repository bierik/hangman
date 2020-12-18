<template>
  <div class="scene d-flex justify-center flex-column align-center">
    <GameDialog />
    <GuessField text="putzstein" />
    <GuessTimer />
    <v-spacer />
    <Gallows />
    <Keys />
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  fetch() {
    this.init()
  },
  methods: {
    ...mapActions('game', ['init']),
    ...mapMutations('game', ['stop', 'reset']),
  },
  beforeRouteLeave(to, from, next) {
    next()
    this.stop()
    this.reset()
  },
}
</script>
<style>
.scene {
  background-image: url('~assets/images/scene-background.jpeg');
  background-size: cover;
  height: 100%;
}
</style>

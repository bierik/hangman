<template>
  <div class="scene d-flex justify-center flex-column align-center">
    <GameDialog />
    <GuessField />
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
    ...mapMutations('timer', ['resetValue']),
  },
  beforeRouteLeave(to, from, next) {
    next()
    this.stop()
    this.reset()
    this.resetValue()
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

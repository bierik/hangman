<template>
  <div class="scene d-flex justify-center flex-column align-center">
    <GameDialog />
    <GuessField />
    <GuessTimer />
    <Gallows class="my-2" />
    <Keys />
    <v-spacer />
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  beforeRouteLeave(to, from, next) {
    next()
    this.stop()
    this.reset()
    this.resetValue()
  },
  fetch() {
    this.init()
  },
  head() {
    return {
      title: 'Spiel',
    }
  },
  methods: {
    ...mapActions('game', ['init', 'stop']),
    ...mapMutations('game', ['reset']),
    ...mapMutations('timer', ['resetValue']),
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

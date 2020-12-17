<template>
  <v-progress-linear color="black" :value="value" />
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
  computed: {
    ...mapState('game', ['started']),
    ...mapState('timer', ['value']),
  },
  watch: {
    started: {
      handler(started) {
        if (started) {
          this.startTimer()
        } else {
          this.stopTimer()
        }
      },
      immediate: true,
    },
  },
  methods: {
    ...mapMutations('game', ['increaseStage']),
    ...mapMutations('timer', ['startTimer', 'stopTimer']),
  },
}
</script>

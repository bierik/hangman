<template>
  <div class="d-flex flex-wrap justify-center px-4">
    <v-btn
      v-for="key in keys"
      :key="key.char"
      :disabled="key.isGuessed"
      class="key pa-1"
      small
      @click="makeGuess(key.char)"
      >{{ key.char }}</v-btn
    >
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import debounce from 'lodash/debounce'

export default {
  computed: {
    ...mapGetters('game', ['keys']),
  },
  methods: {
    ...mapMutations('game', ['guessChar']),
    makeGuess: debounce(function makeGuess(char) {
      this.guessChar(char)
    }, 200),
  },
}
</script>
<style scoped>
.key {
  min-width: 0 !important;
  width: 35px !important;
  height: 35px !important;
  border-radius: 0;
  margin: 2px;
}

.theme--light.v-btn:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined).key:disabled {
  background-color: rgba(39, 39, 39, 0.8) !important;
  color: rgba(255, 255, 255, 0.4) !important;
}
</style>

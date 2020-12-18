<template>
  <div class="d-flex flex-wrap justify-center my-2 px-4">
    <v-btn
      v-for="key in keys"
      :key="key.char"
      :disabled="key.isGuessed"
      class="key pa-1"
      small
      dark
      @click="guessChar(key.char)"
      >{{ key.char }}</v-btn
    >
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
  computed: {
    ...mapGetters('game', ['keys']),
  },
  methods: {
    ...mapMutations('game', ['guessChar']),
  },
}
</script>
<style scoped>
.key {
  min-width: 0 !important;
  width: 30px !important;
  height: 30px !important;
  border-radius: 0;
  margin: 2px;
}

.theme--dark.v-btn:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined).key:disabled {
  background-color: rgba(39, 39, 39, 0.8) !important;
  color: rgba(255, 255, 255, 0.4) !important;
}
</style>

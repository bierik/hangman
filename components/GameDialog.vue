<template>
  <v-overlay :value="!started" class="game-dialog">
    <v-card width="80vw">
      <v-card-title class="d-flex justify-center">
        <transition name="fade-in" mode="out-in">
          <span :key="readyText">{{ readyText }}</span>
        </transition>
      </v-card-title>
      <v-divider />
      <v-card-text class="d-flex flex-column align-center py-10">
        <transition name="fade-in" mode="out-in">
          <v-progress-circular v-if="!initialized" indeterminate color="primary" size="40" width="2" />
          <v-icon v-else x-large>mdi-party-popper</v-icon>
        </transition>
      </v-card-text>
      <v-divider />
      <v-card-actions class="d-flex justify-center py-4">
        <v-btn tile block depressed :disabled="!initialized" color="primary" @click="start">Starten</v-btn>
      </v-card-actions>
    </v-card>
  </v-overlay>
</template>

<script>
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {
  data() {
    return {
      loading: true,
    }
  },
  computed: {
    ...mapState('game', ['started']),
    ...mapGetters('game', ['initialized']),
    readyText() {
      return this.initialized ? 'Bereit' : 'Wird geladen...'
    },
  },
  methods: {
    ...mapMutations('game', ['start']),
  },
}
</script>
<style>
.game-dialog {
  max-height: calc(100vh - 56px);
}
</style>

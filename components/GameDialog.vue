<template>
  <v-overlay :value="showOverlay" class="game-dialog" z-index="10">
    <v-card width="80vw">
      <v-card-title class="d-flex flex-column align-center">
        <transition name="fade-in" mode="out-in">
          <span :key="message">{{ message }}</span>
        </transition>
        <transition name="fade-in" mode="out-in">
          <span :key="submessage" class="body-2">{{ submessage }}</span>
        </transition>
      </v-card-title>
      <v-divider />
      <v-card-text class="d-flex flex-column align-center py-10">
        <transition name="fade-in" mode="out-in">
          <v-progress-circular v-if="!initialized" indeterminate color="primary" size="40" width="2" />
          <v-icon v-else :key="icon" x-large>{{ icon }}</v-icon>
        </transition>
      </v-card-text>
      <v-divider />
      <v-card-actions class="d-flex justify-center py-4">
        <v-btn
          v-if="!hasFailed && !isWordGuessed && available"
          tile
          block
          depressed
          :disabled="!initialized"
          color="primary"
          @click="start"
          >Starten</v-btn
        >
        <v-btn v-else tile block depressed color="primary" @click="close">Schliessen</v-btn>
      </v-card-actions>
    </v-card>
  </v-overlay>
</template>

<script>
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {
  computed: {
    ...mapState('game', ['started', 'available', 'initialized']),
    ...mapGetters('game', ['isWordGuessed', 'hasFailed', 'word']),
    message() {
      if (!this.initialized && !this.hasFailed && !this.isWordGuessed) {
        return 'Wird geladen…'
      } else if (this.initialized && !this.available) {
        return 'Awww!'
      } else if (this.initialized && !this.hasFailed && !this.isWordGuessed) {
        return 'Bereit'
      } else if (this.hasFailed && !this.isWordGuessed) {
        return 'Schade!'
      } else if (this.isWordGuessed && !this.hasFailed) {
        return 'Juhuuu! Geschafft!'
      }
      return ''
    },
    submessage() {
      if (this.initialized) {
        if (this.initialized && !this.available) {
          return 'Du hast heute schon gespielt.'
        } else if (this.initialized && !this.hasFailed && !this.isWordGuessed) {
          return 'Los gehts!'
        } else if (this.hasFailed && !this.isWordGuessed) {
          return `Richtig wäre "${this.word}"`
        } else if (this.isWordGuessed && !this.hasFailed) {
          return 'Viel Spass mit den Preisen'
        }
      }
      return ''
    },
    icon() {
      if (this.initialized) {
        if (!this.available) {
          return 'mdi-emoticon-cry-outline'
        } else if (!this.hasFailed && !this.isWordGuessed) {
          return 'mdi-emoticon-excited-outline'
        } else if (this.isWordGuessed && !this.hasFailed) {
          return 'mdi-party-popper'
        } else if (!this.isWordGuessed && this.hasFailed) {
          return 'mdi-emoticon-dead-outline'
        }
      }
      return ''
    },
    showOverlay() {
      return !this.started || this.isWordGuessed || this.hasFailed || !this.available
    },
  },
  methods: {
    ...mapMutations('game', ['start', 'reset']),
    close() {
      this.$router.push('/')
      this.reset()
    },
  },
}
</script>
<style>
.game-dialog {
  max-height: calc(100vh - 56px);
}
</style>

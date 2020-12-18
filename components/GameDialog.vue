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
          v-if="!hasFailed && !isTextGuessed"
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
    ...mapState('game', ['started', 'text']),
    ...mapGetters('game', ['initialized', 'isTextGuessed', 'hasFailed']),
    message() {
      if (!this.initialized && !this.hasFailed && !this.isTextGuessed) {
        return 'Wird geladen…'
      } else if (this.initialized && !this.hasFailed && !this.isTextGuessed) {
        return 'Bereit'
      } else if (this.hasFailed && !this.isTextGuessed) {
        return 'Schade!'
      } else if (this.isTextGuessed && !this.hasFailed) {
        return 'Juhuuu! Geschafft!'
      }
      return ''
    },
    submessage() {
      if (this.initialized) {
        if (this.initialized && !this.hasFailed && !this.isTextGuessed) {
          return 'Los gehts!'
        } else if (this.hasFailed && !this.isTextGuessed) {
          return `Richtig wäre "${this.text}"`
        } else if (this.isTextGuessed && !this.hasFailed) {
          return 'Viel Spass mit den Preisen'
        }
      }
      return ''
    },
    icon() {
      if (this.initialized) {
        if (!this.hasFailed && !this.isTextGuessed) {
          return 'mdi-check-circle-outline'
        } else if (this.isTextGuessed && !this.hasFailed) {
          return 'mdi-party-popper'
        } else if (!this.isTextGuessed && this.hasFailed) {
          return 'mdi-emoticon-dead-outline'
        }
      }
      return ''
    },
    showOverlay() {
      return !this.started || this.isTextGuessed || this.hasFailed
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

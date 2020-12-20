<template>
  <v-sheet class="d-flex justify-center py-2" width="100%" height="40px">
    <span v-for="(char, index) in guessedWord" :key="`char-${index}`" class="guess-field-char">{{ char }}</span>
  </v-sheet>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters('game', ['guessedWord']),
  },
}
</script>
<style>
.guess-field-char {
  padding: 0 5px;
}
</style>

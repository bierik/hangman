<template>
  <ToolbarLayout>
    <template #toolbar>
      <v-icon class="mr-1">mdi-trophy</v-icon>
      <span class="title">Preise</span>
    </template>
    <v-card tile dark class="mb-3">
      <v-img class="white--text align-end" height="200px" src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
        <v-card-title>Massage</v-card-title>
      </v-img>
      <v-card-text>Gönn dir von mir eine sinnliche Massage</v-card-text>
      <v-divider />
      <v-card-actions>
        <v-btn depressed tile color="orange" text>
          <v-icon small class="mr-1">mdi-gift</v-icon>
          <span>Einlösen</span>
        </v-btn>
      </v-card-actions>
    </v-card>
    <v-card tile dark href="https://open.spotify.com/track/21jGcNKet2qwijlDFuPiPb?si=dW5pY3vGT62Gif94ZipohQ">
      <v-img
        gradient="180deg, rgba(0,0,0,.1) 0%, rgba(0,0,0,.8) 100%"
        class="white--text"
        height="200px"
        :src="require('~/assets/images/music.jpg')"
      >
        <div class="d-flex fill-height flex-column">
          <div class="d-flex align-items justify-center flex-grow-1">
            <v-icon x-large>mdi-play</v-icon>
          </div>
          <v-card-title>Post Malone - Circle</v-card-title>
        </div>
      </v-img>
      <v-card-text>Lehn dich zurück und geniesse einen von deinen Lieblingssongs</v-card-text>
    </v-card>
  </ToolbarLayout>
</template>
<script>
import { mapState } from 'vuex'

export default {
  fetch({ store }) {
    store.dispatch('trophy/fetch')
  },
  computed: {
    ...mapState('trophy', ['trophies']),
  },
}
</script>

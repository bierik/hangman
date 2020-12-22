<template>
  <v-card tile :href="trophy.link" class="mb-3" outlined>
    <v-img
      gradient="180deg, rgba(0,0,0,.1) 0%, rgba(0,0,0,.8) 100%"
      class="white--text"
      height="200px"
      :src="trophy.preview"
      v-on="{
        ...(trophy.expandable ? { click: () => openPhotoswipe(trophy) } : {}),
      }"
    >
      <div v-if="trophy.is_consumed" class="consumed-indicator">
        <v-icon>mdi-gift-outline</v-icon>
      </div>
      <div class="d-flex fill-height flex-column">
        <div class="d-flex align-items justify-center flex-grow-1">
          <v-icon v-if="trophy.link" x-large>mdi-play</v-icon>
        </div>
        <v-card-title>{{ trophy.title }}</v-card-title>
      </div>
    </v-img>
    <v-card-text>{{ trophy.subtitle }}</v-card-text>
    <v-card-actions v-if="trophy.consumable">
      <v-btn
        v-if="!trophy.is_consumed"
        depressed
        tile
        color="orange"
        text
        :loading="consuming"
        :disabled="consuming"
        @click="consumeTrophy(trophy)"
      >
        <v-icon small class="mr-1">mdi-gift</v-icon>
        <span>Einlösen</span>
      </v-btn>
      <span v-else class="caption grey--text text--darken-1">Am {{ trophy.consumed_at | dateString }} eingelöst</span>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import PhotoSwipe from 'photoswipe'
import PhotoSwipeUIDefault from 'photoswipe/dist/photoswipe-ui-default'

export default {
  props: {
    trophy: {
      type: Object,
      required: true,
    },
  },
  computed: {
    ...mapState('trophy', ['consuming']),
  },
  methods: {
    ...mapActions('trophy', ['consume']),
    openPhotoswipe(trophy) {
      const photoSwipeRoot = document.querySelector('#pswp')
      const options = {}
      const items = [
        {
          w: trophy.width,
          h: trophy.height,
          src: trophy.image,
        },
      ]
      const gallery = new PhotoSwipe(photoSwipeRoot, PhotoSwipeUIDefault, items, options)
      gallery.init()
    },
    async consumeTrophy(trophy) {
      await this.consume(trophy)
      this.$router.push({ hash: 'consumed' })
    },
  },
}
</script>
<style>
.consumed-indicator {
  position: absolute;
  top: 0;
  right: 0;
  width: 80px;
  height: 80px;
  background-color: #388e3c;
  clip-path: polygon(100% 0, 0 0, 100% 100%);
}
.consumed-indicator > i {
  position: absolute !important;
  right: 10px;
  top: 10px;
}
</style>

<template>
  <nuxt-link to="/profile">
    <v-progress-circular :value="level" size="35" width="2">
      <v-badge bottom offset-x="10" offset-y="10" :content="trophiesCount.toString()" color="grey">
        <v-avatar size="27" color="orange">
          <v-icon small>mdi-account-circle</v-icon>
        </v-avatar>
      </v-badge>
    </v-progress-circular>
  </nuxt-link>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('profile', ['level', 'trophiesCount']),
  },
}
</script>

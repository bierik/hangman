<template>
  <v-app>
    <v-main>
      <nuxt />
    </v-main>
    <v-bottom-navigation app>
      <v-btn to="/" nuxt>
        <span>Preise</span>
        <v-icon>{{ mdiTrophy }}</v-icon>
      </v-btn>
      <v-btn to="/game" nuxt>
        <span>Spiel</span>
        <v-icon>{{ mdiDice5 }}</v-icon>
      </v-btn>
      <v-btn to="/profile" nuxt>
        <span>Profil</span>
        <v-icon>{{ mdiAccount }}</v-icon>
      </v-btn>
      <v-btn to="/instructions" nuxt>
        <span>Über</span>
        <v-icon>{{ mdiFileDocumentOutline }}</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
import { mdiTrophy, mdiDice5, mdiAccount, mdiFileDocumentOutline } from '@mdi/js'

export default {
  data() {
    return {
      mdiTrophy,
      mdiDice5,
      mdiAccount,
      mdiFileDocumentOutline,
    }
  },
}
</script>

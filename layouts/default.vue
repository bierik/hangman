<template>
  <v-app dark>
    <v-main>
      <nuxt />
    </v-main>
    <v-bottom-navigation app dark>
      <v-btn to="/" nuxt>
        <span>Preise</span>
        <v-icon>mdi-trophy</v-icon>
      </v-btn>
      <v-btn to="/game" nuxt>
        <span>Spiel</span>
        <v-icon>mdi-dice-5</v-icon>
      </v-btn>
      <v-btn to="/profile" nuxt>
        <span>Profil</span>
        <v-icon>mdi-account</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
export default {}
</script>

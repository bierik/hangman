<template>
  <ToolbarLayout>
    <template #toolbar>
      <v-icon class="mr-1">mdi-trophy</v-icon>
      <span class="title">Preise</span>
    </template>
    <template #top>
      <v-tabs v-model="activeTab" grow>
        <v-tab to="#consumable"><v-badge color="error" dot :value="hasConsumables">Offen</v-badge></v-tab>
        <v-tab to="#consumed">Eingelöst</v-tab>
      </v-tabs>
    </template>
    <v-overlay :value="hasReceivedTrophy" class="trophy-dialog">
      <v-card width="80vw" light>
        <v-card-title>Gratulation!</v-card-title>
        <v-card-text>
          <p>Du hast einen Preis gewonnen</p>
          <v-divider />
          <video autoplay loop width="100%" height="100%" src="~assets/animations/party-popper.mp4" />
          <p class="mb-0 title">{{ trophyReceived && trophyReceived.title }}</p>
          <p class="mb-0">{{ trophyReceived && trophyReceived.subtitle }}</p>
        </v-card-text>
        <v-divider />
        <v-card-actions>
          <v-btn depressed color="primary" @click="claimTrophy">Preis abholen</v-btn>
        </v-card-actions>
      </v-card>
    </v-overlay>
    <v-tabs-items v-model="activeTab">
      <v-tab-item value="consumable" transition="fade-transition" reverse-transition="fade-transition">
        <TrophyCard v-for="trophy in consumable" :key="trophy.id" :trophy="trophy" />
      </v-tab-item>
      <v-tab-item value="consumed" transition="fade-transition" reverse-transition="fade-transition">
        <TrophyCard v-for="trophy in consumed" :key="trophy.id" :trophy="trophy" />
      </v-tab-item>
    </v-tabs-items>
  </ToolbarLayout>
</template>
<script>
import { mapGetters, mapMutations, mapState } from 'vuex'

export default {
  fetch({ store }) {
    store.dispatch('trophy/fetch')
  },
  data() {
    return {
      activeTab: null,
    }
  },
  computed: {
    ...mapGetters('trophy', ['consumable', 'consumed', 'hasConsumables']),
    ...mapGetters('profile', ['hasReceivedTrophy']),
    ...mapState('profile', ['trophyReceived']),
  },
  methods: {
    ...mapMutations('profile', ['claimTrophy']),
    claim() {
      this.claimTrophy()
      this.$router.replace({ path: '/', hash: '#consumable' })
    },
  },
}
</script>
<style>
.theme--dark.v-tabs-items {
  background-color: transparent;
}

.trophy-dialog {
  max-height: calc(100vh - 56px);
}
</style>

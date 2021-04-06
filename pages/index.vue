<template>
  <ToolbarLayout>
    <template #toolbar>
      <v-icon class="mr-1">{{ mdiTrophy }}</v-icon>
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
        <div v-if="loading" class="d-flex justify-center py-10">
          <v-progress-circular indeterminate width="2" color="primary" />
        </div>
        <template v-else>
          <template v-if="hasConsumables">
            <TrophyCard v-for="trophy in consumable" :key="trophy.id" :trophy="trophy" />
          </template>
          <div v-else class="d-flex flex-column empty-state">
            <v-icon class="grow" size="100">{{ mdiGamepadVariantOutline }}</v-icon>
            <span class="text-center">Du hast im Moment leider keine Preise zum öffnen. Bleib dran!</span>
          </div>
        </template>
      </v-tab-item>
      <v-tab-item value="consumed" transition="fade-transition" reverse-transition="fade-transition">
        <div v-if="loading" class="d-flex justify-center py-10">
          <v-progress-circular indeterminate width="2" color="primary" />
        </div>
        <template v-else>
          <template v-if="hasConsumed">
            <TrophyCard v-for="trophy in consumed" :key="trophy.id" :trophy="trophy" />
          </template>
          <div v-else class="d-flex flex-column empty-state">
            <v-icon class="grow" size="100">{{ mdiGiftOutline }}</v-icon>
            <span class="text-center">Du konntest leider noch keine Preise öffnen. Bleib dran!</span>
          </div>
        </template>
      </v-tab-item>
    </v-tabs-items>
    <PhotoSwipeRoot />
  </ToolbarLayout>
</template>
<script>
import { mapGetters, mapMutations, mapState } from 'vuex'
import { mdiTrophy, mdiGamepadVariantOutline, mdiGiftOutline } from '@mdi/js'

export default {
  fetch({ store }) {
    store.dispatch('trophy/fetch')
  },
  data() {
    return {
      activeTab: null,
      mdiTrophy,
      mdiGamepadVariantOutline,
      mdiGiftOutline,
    }
  },
  computed: {
    ...mapGetters('trophy', ['consumable', 'consumed', 'hasConsumables', 'hasConsumed']),
    ...mapGetters('profile', ['hasReceivedTrophy']),
    ...mapState('profile', ['trophyReceived']),
    ...mapState('trophy', ['loading']),
  },
  methods: {
    ...mapMutations('profile', ['claimTrophy']),
    claim() {
      this.claimTrophy()
      this.$router.replace({ path: '/', hash: '#consumable' })
    },
  },
  head() {
    return {
      title: 'Preise',
    }
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

.empty-state {
  height: 60vh;
}
</style>

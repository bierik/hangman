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
        <v-tab to="#unconsumable">Uneinlösbar</v-tab>
      </v-tabs>
    </template>
    <v-tabs-items v-model="activeTab">
      <v-tab-item value="consumable" transition="fade-transition" reverse-transition="fade-transition">
        <TrophyCard v-for="trophy in consumable" :key="trophy.id" :trophy="trophy" />
      </v-tab-item>
      <v-tab-item value="consumed" transition="fade-transition" reverse-transition="fade-transition">
        <TrophyCard v-for="trophy in consumed" :key="trophy.id" :trophy="trophy" />
      </v-tab-item>
      <v-tab-item value="unconsumable" transition="fade-transition" reverse-transition="fade-transition">
        <TrophyCard v-for="trophy in unconsumable" :key="trophy.id" :trophy="trophy" />
      </v-tab-item>
    </v-tabs-items>
  </ToolbarLayout>
</template>
<script>
import { mapGetters } from 'vuex'

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
    ...mapGetters('trophy', ['consumable', 'consumed', 'unconsumable', 'hasConsumables']),
  },
}
</script>
<style>
.theme--dark.v-tabs-items {
  background-color: transparent;
}
</style>

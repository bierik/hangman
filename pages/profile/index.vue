<template>
  <ToolbarLayout>
    <template #toolbar>
      <v-icon class="mr-1">mdi-account</v-icon>
      <span class="title">Profil</span>
    </template>
    <div class="d-flex align-center mb-4">
      <v-progress-circular :value="level" size="74" width="4" class="mr-6">
        <v-avatar size="62" color="orange">
          <v-icon large>mdi-account-circle</v-icon>
        </v-avatar>
      </v-progress-circular>
      <div class="d-flex flex-column">
        <span class="title"
          >Level:<span class="body-2 ml-1">{{ level }} / 100</span></span
        >
        <span class="title"
          >Preise:<span class="body-2 ml-1">{{ trophiesCount }} / {{ maxTrophiesCount }}</span></span
        >
      </div>
    </div>
    <v-divider />
  </ToolbarLayout>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('profile', ['level', 'trophiesCount', 'maxTrophiesCount']),
  },
}
</script>

<style>
.profile-badge .v-badge__badge {
  width: 30px !important;
  height: 30px !important;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

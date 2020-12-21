<template>
  <ToolbarLayout>
    <template #toolbar>
      <v-icon class="mr-1">mdi-account</v-icon>
      <span class="title">Profil</span>
    </template>
    <div class="d-flex align-center mb-4">
      <v-progress-circular :value="level" size="70" width="2" class="mr-6">
        <v-badge bottom offset-x="20" offset-y="20" content="3" color="grey" class="profile-badge">
          <v-avatar size="62" color="orange">
            <v-icon large>mdi-account-circle</v-icon>
          </v-avatar>
        </v-badge>
      </v-progress-circular>
      <div class="d-flex flex-column">
        <span class="title"
          >Level:<span class="body-2 ml-1">{{ level }} / 100</span></span
        >
        <span class="title">Preise:<span class="body-2 ml-1">3 / 24</span></span>
      </div>
    </div>
    <v-divider />
  </ToolbarLayout>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('profile', ['level']),
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

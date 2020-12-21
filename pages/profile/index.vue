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
    <v-list>
      <v-subheader>Spielverlauf</v-subheader>
      <v-list-item v-for="entry in history" :key="entry.id">
        <v-list-item-action>
          <v-icon large>{{ statusIcon(entry) }}</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>
            {{ entry.dictionary.word.toUpperCase() }}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ entry.created | dateTimeString }}
          </v-list-item-subtitle>
          <v-list-item-subtitle>
            {{ statusText(entry) }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </ToolbarLayout>
</template>

<script>
import { mapState } from 'vuex'

const STATUS_MAPPING = {
  SU: { title: 'Erfolgreich', icon: 'mdi-emoticon-happy-outline' },
  FA: { title: 'Gescheitert', icon: 'mdi-emoticon-sad-outline' },
  RU: { title: 'Nicht gemacht', icon: 'mdi-emoticon-confused-outline' },
}

export default {
  async asyncData({ $axios }) {
    const { data: history } = await $axios.get('guess/')
    return { history }
  },
  computed: {
    ...mapState('profile', ['level', 'trophiesCount', 'maxTrophiesCount']),
  },
  methods: {
    statusText(historyEntry) {
      return STATUS_MAPPING[historyEntry.status].title
    },
    statusIcon(historyEntry) {
      return STATUS_MAPPING[historyEntry.status].icon
    },
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

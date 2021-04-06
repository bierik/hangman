<template>
  <ToolbarLayout>
    <template #toolbar>
      <v-icon class="mr-1">{{ mdiAccount }}</v-icon>
      <span class="title">Profil</span>
    </template>
    <div class="d-flex align-center mb-4">
      <v-progress-circular :value="level" size="74" width="4" class="mr-6">
        <v-avatar size="62" color="orange">
          <v-icon large>{{ mdiAccountCircle }}</v-icon>
        </v-avatar>
      </v-progress-circular>
      <div class="d-flex flex-column">
        <span class="title"
          >Level:<span class="body-2 ml-1">{{ level }} / {{ achievementCost }}</span></span
        >
        <span class="title"
          >Preise:<span class="body-2 ml-1">{{ trophiesCount }} / {{ maxTrophiesCount }}</span></span
        >
      </div>
    </div>
    <v-divider />
    <v-list>
      <v-subheader>Spielverlauf</v-subheader>
      <template v-if="history.length > 0">
        <template v-for="entry in history">
          <v-list-item :key="entry.id">
            <v-list-item-action>
              <v-icon large>{{ statusIcon(entry) }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title v-if="needsCover(entry)">-</v-list-item-title>
              <v-list-item-title v-else>
                {{ entry.dictionary.word.toUpperCase() }}
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ entry.created | dateTimeString }}
              </v-list-item-subtitle>
              <v-list-item-subtitle>
                <v-chip small color="primary">{{ statusText(entry) }}</v-chip>
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-divider :key="`divider-${entry.id}`" />
        </template>
      </template>
      <v-subheader v-else>Du hast noch keine Spiele gespielt.</v-subheader>
    </v-list>
  </ToolbarLayout>
</template>

<script>
import { mapState } from 'vuex'
import {
  mdiAccount,
  mdiAccountCircle,
  mdiEmoticonHappyOutline,
  mdiEmoticonSadOutline,
  mdiEmoticonConfusedOutline,
} from '@mdi/js'

const STATUS_MAPPING = {
  SU: { title: 'Erfolgreich', icon: mdiEmoticonHappyOutline },
  FA: { title: 'Gescheitert', icon: mdiEmoticonSadOutline },
  RU: { title: 'Läuft', icon: mdiEmoticonConfusedOutline },
  CR: { title: 'Läuft', icon: mdiEmoticonConfusedOutline },
}

export default {
  async asyncData({ $axios }) {
    const { data: history } = await $axios.get('guess/')
    return { history }
  },
  data() {
    return {
      mdiAccount,
      mdiAccountCircle,
    }
  },
  computed: {
    ...mapState('profile', ['level', 'trophiesCount', 'maxTrophiesCount']),
    ...mapState('config', ['achievementCost']),
  },
  methods: {
    statusText(historyEntry) {
      return STATUS_MAPPING[historyEntry.status].title
    },
    statusIcon(historyEntry) {
      return STATUS_MAPPING[historyEntry.status].icon
    },
    needsCover(historyEntry) {
      return historyEntry.status === 'RU' || historyEntry.status === 'CR'
    },
  },
  head() {
    return {
      title: 'Profil',
    }
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

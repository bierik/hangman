function defaultState() {
  return {
    level: 0,
    trophiesCount: 0,
    maxTrophiesCount: 0,
    trophyReceived: null,
  }
}

export const state = defaultState

export const mutations = {
  updateLevel(state, level) {
    state.level = level
  },
  updateTrophiesCount(state, trophiesCount) {
    state.trophiesCount = trophiesCount
  },
  updateMaxTrophiesCount(state, maxTrophiesCount) {
    state.maxTrophiesCount = maxTrophiesCount
  },
  receiveTrophy(state, trophy) {
    state.trophyReceived = trophy
  },
  claimTrophy(state) {
    state.trophyReceived = null
  },
}

export const actions = {
  async fetch({ commit }) {
    const {
      data: { level, trophies_count: trophiesCount, max_trophies_count: maxTrophiesCount },
    } = await this.$axios.get('profile/')
    commit('updateLevel', level)
    commit('updateTrophiesCount', trophiesCount)
    commit('updateMaxTrophiesCount', maxTrophiesCount)
  },
}

export const getters = {
  hasReceivedTrophy(state) {
    return !!state.trophyReceived
  },
}

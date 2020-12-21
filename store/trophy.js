function defaultState() {
  return {
    trophies: [],
  }
}

export const state = defaultState

export const mutations = {
  updateTrophies(store, trophies) {
    store.trophies = trophies
  },
}

export const actions = {
  async fetch({ commit }) {
    const { data: trophies } = await this.$axios.get('trophy/')
    commit('updateTrophies', trophies)
  },
}

export const getters = {}

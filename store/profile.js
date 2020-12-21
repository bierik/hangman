function defaultState() {
  return {
    level: 0,
  }
}

export const state = defaultState

export const mutations = {
  updateLevel(store, level) {
    store.level = level
  },
}

export const actions = {
  async fetch({ commit }) {
    const {
      data: { level },
    } = await this.$axios.get('profile/')
    commit('updateLevel', level)
  },
}

export const getters = {}

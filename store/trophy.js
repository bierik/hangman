function defaultState() {
  return {
    trophies: {},
    loading: true,
    consuming: false,
  }
}

export const state = defaultState

export const mutations = {
  updateTrophies(store, trophies) {
    store.trophies = trophies.reduce((accum, trophy) => Object.assign(accum, { [trophy.id]: trophy }), {})
  },
  updateTrophy(state, trophy) {
    if (state.trophies[trophy.id]) {
      state.trophies[trophy.id] = trophy
    }
  },
  startLoad(state) {
    state.loading = true
  },
  endLoad(state) {
    state.loading = false
  },
  startConsume(state) {
    state.consuming = true
  },
  endConsume(state) {
    state.consuming = false
  },
}

export const actions = {
  async fetch({ commit }) {
    commit('startLoad')
    const { data: trophies } = await this.$axios.get('trophy/')
    commit('updateTrophies', trophies)
    commit('endLoad')
  },
  async consume({ commit }, trophy) {
    commit('startConsume')
    const { data } = await this.$axios.post(`trophy/${trophy.id}/consume/`)
    commit('updateTrophy', data)
    commit('endConsume')
  },
}

export const getters = {
  consumed(state) {
    return Object.values(state.trophies).filter((trophy) => trophy.is_consumed)
  },
  consumable(state) {
    return Object.values(state.trophies).filter((trophy) => !trophy.is_consumed)
  },
  hasConsumables(_, { consumable }) {
    return consumable.length > 0
  },
  hasConsumed(_, { consumed }) {
    return consumed.length > 0
  },
}

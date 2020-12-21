function defaultState() {
  return {
    trophies: {},
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
}

export const actions = {
  async fetch({ commit }) {
    const { data: trophies } = await this.$axios.get('trophy/')
    commit('updateTrophies', trophies)
  },
  async consume({ commit }, trophy) {
    const { data } = await this.$axios.post(`trophy/${trophy.id}/consume/`)
    commit('updateTrophy', data)
  },
}

export const getters = {
  consumed(state) {
    return Object.values(state.trophies).filter((trophy) => trophy.is_consumed)
  },
  consumable(state) {
    return Object.values(state.trophies).filter((trophy) => trophy.consumable && !trophy.is_consumed)
  },
  unconsumable(state) {
    return Object.values(state.trophies).filter((trophy) => !trophy.consumable)
  },
  hasConsumables(_, { consumable }) {
    return consumable.length > 0
  },
}

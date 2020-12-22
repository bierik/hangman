export const state = () => ({
  timerInterval: 50,
  achievement_cost: 100,
})

export const mutations = {
  updateConfig(state, config) {
    Object.assign(state, config)
  },
}

export const actions = {
  async fetch({ commit }) {
    const { data: config } = await this.$axios.get('config/')
    commit('updateConfig', config)
  },
}

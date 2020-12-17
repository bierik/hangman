export const state = () => ({
  timer: null,
  value: 0,
})

export const mutations = {
  increaseTimer(state) {
    state.value = Math.min(state.value + 1, 100)
    if (state.value >= 100) {
      this.commit('timer/timerRunOut')
    }
  },
  startTimer(state) {
    state.timer = setInterval(() => this.commit('timer/increaseTimer'), 200)
  },
  stopTimer(state) {
    clearInterval(state.timer)
    this.commit('timer/resetValue')
  },
  resetValue(state) {
    state.value = 0
  },
  resetTimer(_, { timerCallback = () => {} } = {}) {
    this.commit('timer/stopTimer')
    setTimeout(() => {
      timerCallback()
      this.commit('timer/resetValue')
      setTimeout(() => {
        this.commit('timer/startTimer')
      }, 200)
    }, 200)
  },
  timerRunOut() {
    this.commit('timer/resetTimer', { timerCallback: () => this.commit('game/increaseStage') })
  },
}

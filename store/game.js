import upperCase from 'lodash/upperCase'

export const state = () => ({
  stage: 0,
  text: '',
  guessedChars: [],
  started: false,
})

export const mutations = {
  increaseStage(state) {
    state.stage++
  },
  resetStage(state) {
    state.stage = 0
  },
  guessChar(state, char) {
    if (!this.getters['game/text'].includes(char)) {
      this.commit('game/increaseStage')
    } else {
      this.commit('timer/resetTimer')
    }
    state.guessedChars.push(char)
  },
  start(state) {
    state.started = true
  },
  stop(state) {
    state.started = false
    this.commit('timer/stopTimer')
  },
  init(state, { text }) {
    state.text = text
    state.guessedChars = []
  },
}

export const actions = {
  async init({ commit }) {
    const text = await new Promise((resolve) => {
      setTimeout(() => {
        resolve('Blumenstrauss')
      }, 1000)
    })
    commit('init', { text })
  },
}

export const getters = {
  guessedChars(state) {
    return state.guessedChars.map(upperCase)
  },
  text(state) {
    return upperCase(state.text)
  },
  guessedText(_, { guessedChars, text }) {
    return Array.from(text)
      .map((char) => {
        if (guessedChars.includes(char)) {
          return char
        }
        return '_'
      })
      .join('')
  },
  keys(_, { guessedChars }) {
    return new Array(26)
      .fill()
      .map((_, index) => index + 65)
      .map((key) => {
        const char = String.fromCharCode(key)
        return { char, isGuessed: guessedChars.includes(char) }
      })
  },
  initialized(state) {
    return !!state.text
  },
}

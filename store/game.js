import upperCase from 'lodash/upperCase'

const MAX_STAGE = 10
const TRY_MODE = process.env.TRY_MODE === 'true'

function defaultState() {
  return {
    stage: 0,
    text: '',
    guessedChars: [],
    started: false,
    gameAvailable: false,
    initialized: false,
  }
}

export const state = defaultState

export const mutations = {
  increaseStage(state) {
    state.stage++
    if (state.stage >= MAX_STAGE) {
      this.dispatch('game/failedGuess')
    }
  },
  resetStage(state) {
    state.stage = 0
  },
  guessChar(state, char) {
    state.guessedChars.push(char)
    if (this.getters['game/isTextGuessed']) {
      this.commit('game/stop')
    } else if (!this.getters['game/text'].includes(char)) {
      this.commit('game/increaseStage')
    } else {
      this.commit('timer/resetTimer')
    }
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
  reset(state) {
    Object.assign(state, defaultState())
  },
}

export const actions = {
  async init({ commit }) {
    const {
      data: { text },
    } = await this.$axios.get('guess_text/random/')
    commit('init', { text: TRY_MODE ? 'Aal' : text })
  },
  async successGuess({ commit }) {
    // TODO post to backend that game is over
    commit('stop')
  },
  async failedGuess({ commit }) {
    // TODO post to backend that game is over
    commit('stop')
  },
}

export const getters = {
  guessedChars(state) {
    return state.guessedChars.map(upperCase)
  },
  text(state) {
    return upperCase(state.text)
  },
  isTextGuessed(_, { guessedChars, text }) {
    if (!guessedChars.length && !text.length) {
      return false
    }
    return (
      Array.from(text).reduce((accum, char) => {
        if (guessedChars.includes(char)) {
          return accum + 1
        }
        return accum
      }, 0) === text.length
    )
  },
  hasFailed(state, { isTextGuessed }) {
    return state.stage >= MAX_STAGE && !isTextGuessed
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

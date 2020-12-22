import upperCase from 'lodash/upperCase'
import get from 'lodash/get'

const MAX_STAGE = 10
const TRY_MODE = process.env.TRY_MODE === 'true'

function defaultState() {
  return {
    stage: 0,
    guess: null,
    guessedChars: [],
    started: false,
    available: false,
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
    if (this.getters['game/isWordGuessed']) {
      this.dispatch('game/successGuess')
    } else if (!this.getters['game/word'].includes(char)) {
      this.commit('game/increaseStage')
    } else {
      this.commit('timer/resetTimer')
    }
  },
  start(state) {
    state.started = true
    this.commit('timer/startTimer')
  },
  stop(state) {
    state.started = false
    this.commit('timer/stopTimer')
  },
  init(state, { guess = null, available = false } = {}) {
    state.initialized = true
    state.available = available
    state.guess = guess
    state.guessedChars = []
  },
  reset(state) {
    Object.assign(state, defaultState())
  },
  onGuessAvailable(state) {
    state.available = false
  },
}

export const actions = {
  async init({ commit }) {
    try {
      const { data: guess } = await this.$axios.get('guess/random/')
      commit('init', { guess: TRY_MODE ? 'Aal' : guess, available: true })
    } catch (error) {
      const errorCode = get(error, 'response.data.code')
      if (errorCode === 'NO_GUESS_AVAILABLE') {
        commit('onGuessAvailable')
        commit('init', { available: false })
      }
    }
  },
  async successGuess({ commit, state }) {
    commit('stop')
    const {
      data: { received },
    } = await this.$axios.post(`guess/${state.guess.id}/success/`)
    if (received) {
      this.dispatch('trophy/fetch')
      this.commit('profile/receiveTrophy', received)
    }
  },
  async failedGuess({ commit, state }) {
    commit('stop')
    await this.$axios.post(`guess/${state.guess.id}/fail/`)
  },
  async start({ commit, state }) {
    await this.$axios.post(`guess/${state.guess.id}/start/`)
    commit('start')
  },
  async stop({ commit, state }) {
    if (state.guess) {
      await this.$axios.post(`guess/${state.guess.id}/stop/`)
    }
    commit('stop')
  },
}

export const getters = {
  guessedChars(state) {
    return state.guessedChars.map(upperCase)
  },
  word(state) {
    return upperCase(get(state, 'guess.dictionary.word', ''))
  },
  isWordGuessed(_, { guessedChars, word }) {
    if (!guessedChars.length && !word.length) {
      return false
    }
    return (
      Array.from(word).reduce((accum, char) => {
        if (guessedChars.includes(char)) {
          return accum + 1
        }
        return accum
      }, 0) === word.length
    )
  },
  hasFailed(state, { isWordGuessed }) {
    return state.stage >= MAX_STAGE && !isWordGuessed
  },
  guessedWord(_, { guessedChars, word }) {
    return Array.from(word)
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
  countGuessChars(state) {
    return get(state, 'guess.dictionary.word.length', 0)
  },
}

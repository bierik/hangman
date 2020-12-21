import Vue from 'vue'
import { DateTime } from 'luxon'

Vue.filter('dateTimeString', (value) => {
  const date = DateTime.fromISO(value)
  if (date.isValid) {
    return date.toFormat('dd.MM.yyyy, HH:mm')
  }
  return '-'
})

Vue.filter('dateString', (value) => {
  const date = DateTime.fromISO(value)
  if (date.isValid) {
    return date.toFormat('dd.MM.yyyy')
  }
  return '-'
})

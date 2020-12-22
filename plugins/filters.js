import Vue from 'vue'

Vue.filter('dateTimeString', (value) => {
  return new Intl.DateTimeFormat('de-CH', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  }).format(new Date(value))
})

Vue.filter('dateString', (value) => {
  return new Intl.DateTimeFormat('de-CH', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).format(new Date(value))
})

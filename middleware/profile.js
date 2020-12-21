export default function profile({ store }) {
  store.dispatch('profile/fetch')
}

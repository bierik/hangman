export default async function ({ store }) {
  await store.dispatch('config/fetch')
}

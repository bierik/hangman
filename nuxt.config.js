export default {
  // Disable server-side rendering (https://go.nuxtjs.dev/ssr-mode)
  ssr: false,

  // Target (https://go.nuxtjs.dev/config-target)
  target: 'static',

  loading: false,

  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    titleTemplate: '%s - hangman',
    title: 'hangman',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Play hangman and receive some nice trophies.' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
    '@/assets/styles/animations.css',
    '@/assets/styles/main.css',
    'photoswipe/dist/photoswipe.css',
    'photoswipe/dist/default-skin/default-skin.css',
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: ['~/plugins/axios', '~/plugins/filters', '~/plugins/config'],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],

  generate: {
    dir: 'staticfiles',
  },

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/proxy',
  ],

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {
    baseURL: '/api',
    headers: {
      common: {
        Accept: 'application/json',
      },
    },
  },

  proxy: ['http://localhost:8000/api'],

  router: {
    middleware: ['profile'],
  },

  // Vuetify module configuration (https://go.nuxtjs.dev/config-vuetify)
  vuetify: {
    defaultAssets: {
      icons: false,
    },
    customVariables: ['~/assets/variables.scss'],
    icons: {
      iconfont: 'mdiSvg',
    },
    theme: {
      dark: true,
    },
  },

  pwa: {
    useWebmanifestExtension: true,
    lang: 'de',
    meta: {
      nativeUI: true,
      theme_color: '#ffffff',
    },
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {},
}

<template>
  <v-progress-linear color="black" :value="value" />
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('timer', ['value']),
  },
}
</script>

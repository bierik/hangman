<template>
  <div class="my-2 px-2 d-flex align-center justify-center grow" style="width: 100%">
    <v-img :src="require('~/assets/images/gallows/frame.png')" class="frame">
      <template v-for="(bodyPart, index) in bodyParts">
        <div v-if="stage >= index + 1" :key="bodyPart" :class="`${bodyPart} hangman-part`" />
      </template>
    </v-img>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      bodyParts: [
        'noose',
        'head',
        'shirt',
        'shorts',
        'left-arm',
        'right-arm',
        'left-leg',
        'right-leg',
        'head-worried',
        'head-dead',
      ],
    }
  },
  computed: {
    ...mapState('game', ['stage']),
  },
  mounted() {
    window.addEventListener('resize', () => {
      const windowHeight = window.innerHeight
      if (windowHeight < 640) {
      }
    })
  },
}
</script>

<style>
.hangman-part {
  position: absolute;
  background-size: contain;
}

.frame {
  position: relative;
}

@media screen and (min-width: 320px) {
  .frame {
    max-height: 443px;
    max-width: 304px;
  }
}

.noose {
  background-image: url('~assets/images/gallows/noose.png');
  width: 11.147541%;
  height: 26.8623025%;
  left: 48%;
  top: 7%;
  z-index: 1;
}
.head {
  background-image: url('~assets/images/gallows/head.png');
  width: 35.1973684%;
  height: 26.8623025%;
  left: 37%;
  top: 10%;
  z-index: 4;
}
.head-dead {
  background-image: url('~assets/images/gallows/head-dead.png');
  width: 35.1973684%;
  height: 26.8623025%;
  left: 37%;
  top: 10%;
  z-index: 6;
}
.head-worried {
  background-image: url('~assets/images/gallows/head-worried.png');
  width: 35.1973684%;
  height: 26.8623025%;
  left: 37%;
  top: 10%;
  z-index: 5;
}
.shirt {
  background-image: url('~assets/images/gallows/shirt.png');
  width: 46.0526316%;
  height: 26.8623025%;
  left: 32%;
  top: 30%;
  z-index: 3;
}
.shorts {
  background-image: url('~assets/images/gallows/shorts.png');
  width: 26.6447368%;
  height: 12.1896163%;
  left: 42%;
  top: 54%;
  z-index: 3;
}

.left-arm {
  background-image: url('~assets/images/gallows/leftarm.png');
  width: 16.4473684%;
  height: 19.6388262%;
  left: 20%;
  top: 38%;
  z-index: 2;
}
.right-arm {
  background-image: url('~assets/images/gallows/rightarm.png');
  width: 18.4210526%;
  height: 20.0902935%;
  left: 73%;
  top: 38%;
  z-index: 2;
}
.left-leg {
  background-image: url('~assets/images/gallows/leftleg.png');
  width: 21.3815789%;
  height: 17.1557562%;
  left: 40%;
  top: 65%;
  z-index: 2;
}
.right-leg {
  background-image: url('~assets/images/gallows/rightleg.png');
  width: 9.2105263%;
  height: 17.1557562%;
  left: 62%;
  top: 65%;
  z-index: 2;
}
</style>

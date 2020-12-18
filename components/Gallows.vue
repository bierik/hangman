<template>
  <div class="frame">
    <template v-for="(bodyPart, index) in bodyParts">
      <div v-if="stage >= index + 1" :key="bodyPart" :class="`${bodyPart} hangman-part`" />
    </template>
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
}
</script>

<style>
.hangman-part {
  position: absolute;
}
.frame {
  background-image: url('~assets/images/gallows/frame.png');
  width: 100%;
  background-position: center;
  height: 443px;
  width: 305px;
  position: relative;
}
.noose {
  background-image: url('~assets/images/gallows/noose.png');
  width: 34px;
  height: 119px;
  left: 149px;
  top: 15px;
  z-index: 1;
}
.head {
  background-image: url('~assets/images/gallows/head.png');
  width: 107px;
  height: 119px;
  left: 113px;
  top: 42px;
  z-index: 4;
}
.head-dead {
  background-image: url('~assets/images/gallows/head-dead.png');
  width: 107px;
  height: 119px;
  left: 113px;
  top: 42px;
  z-index: 6;
}
.head-worried {
  background-image: url('~assets/images/gallows/head-worried.png');
  width: 107px;
  height: 119px;
  left: 113px;
  top: 42px;
  z-index: 5;
}
.shirt {
  background-image: url('~assets/images/gallows/shirt.png');
  width: 140px;
  height: 119px;
  left: 97px;
  top: 144px;
  z-index: 3;
}
.shorts {
  background-image: url('~assets/images/gallows/shorts.png');
  width: 81px;
  height: 54px;
  left: 128px;
  top: 253px;
  z-index: 3;
}
.left-arm {
  background-image: url('~assets/images/gallows/leftarm.png');
  width: 50px;
  height: 87px;
  left: 61px;
  top: 183px;
  z-index: 2;
}
.right-arm {
  background-image: url('~assets/images/gallows/rightarm.png');
  width: 56px;
  height: 89px;
  left: 223px;
  top: 183px;
  z-index: 2;
}
.left-leg {
  background-image: url('~assets/images/gallows/leftleg.png');
  width: 65px;
  height: 76px;
  left: 121px;
  top: 301px;
  z-index: 2;
}
.right-leg {
  background-image: url('~assets/images/gallows/rightleg.png');
  width: 28px;
  height: 76px;
  left: 188px;
  top: 301px;
  z-index: 2;
}
</style>

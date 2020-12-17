<template>
  <div class="frame">
    <div v-if="stage >= 1" class="noose hangman-part" />
    <div v-if="stage >= 5" class="left-arm hangman-part" />
    <div v-if="stage >= 6" class="right-arm hangman-part" />
    <div v-if="stage >= 7" class="left-leg hangman-part" />
    <div v-if="stage >= 8" class="right-leg hangman-part" />
    <div v-if="stage >= 4" class="shorts hangman-part" />
    <div v-if="stage >= 3" class="shirt hangman-part" />
    <div v-if="stage >= 2" class="head hangman-part" />
    <div v-if="stage >= 9" class="head-worried hangman-part" />
    <div v-if="stage >= 10" class="head-dead hangman-part" />
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
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
}
.head {
  background-image: url('~assets/images/gallows/head.png');
  width: 107px;
  height: 119px;
  left: 113px;
  top: 42px;
}
.head-dead {
  background-image: url('~assets/images/gallows/head-dead.png');
  width: 107px;
  height: 119px;
  left: 113px;
  top: 42px;
}
.head-worried {
  background-image: url('~assets/images/gallows/head-worried.png');
  width: 107px;
  height: 119px;
  left: 113px;
  top: 42px;
}
.shirt {
  background-image: url('~assets/images/gallows/shirt.png');
  width: 140px;
  height: 119px;
  left: 97px;
  top: 144px;
}
.shorts {
  background-image: url('~assets/images/gallows/shorts.png');
  width: 81px;
  height: 54px;
  left: 128px;
  top: 253px;
}
.left-arm {
  background-image: url('~assets/images/gallows/leftarm.png');
  width: 50px;
  height: 87px;
  left: 61px;
  top: 183px;
}
.right-arm {
  background-image: url('~assets/images/gallows/rightarm.png');
  width: 56px;
  height: 89px;
  left: 223px;
  top: 183px;
}
.left-leg {
  background-image: url('~assets/images/gallows/leftleg.png');
  width: 65px;
  height: 76px;
  left: 121px;
  top: 301px;
}
.right-leg {
  background-image: url('~assets/images/gallows/rightleg.png');
  width: 28px;
  height: 76px;
  left: 188px;
  top: 301px;
}
</style>

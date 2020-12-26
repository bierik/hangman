import Vue from 'vue'

Vue.directive('adjust', {
  inserted(el, { value: { width, height } = {} } = {}) {
    function resize() {
      const currentParentWidth = el.parentNode.clientWidth
      const currentParentHeight = el.parentNode.clientHeight
      const widthRatio = height / currentParentHeight
      const heightRatio = width / currentParentWidth
      debugger
      console.log(width, currentParentWidth, height, currentParentHeight)
      el.style.height = `${el.clientHeight * heightRatio}px`
      el.style.width = `${el.clientWidth * widthRatio}px`
      el.style.top = `${el.offsetTop * heightRatio}px`
      el.style.left = `${el.offsetLeft * heightRatio}px`
    }
    resize()
  },
  unbind() {},
})

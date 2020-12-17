<template>
  <v-container>
    <v-app-bar app flat dark height="65">
      <slot name="toolbar" />
      <v-spacer />
      <User />
    </v-app-bar>
    <slot />
  </v-container>
</template>

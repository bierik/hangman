<template>
  <v-container class="pa-0">
    <v-app-bar app flat>
      <slot name="toolbar" />
      <v-spacer />
      <User />
    </v-app-bar>
    <slot name="top" />
    <v-container>
      <slot />
    </v-container>
  </v-container>
</template>

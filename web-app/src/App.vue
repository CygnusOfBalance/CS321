<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase"> 
        <span class="font-weight-light">Schedules+</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
      </v-btn>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import loginPage from './views/loginPage.vue';
import createCalendar from './views/createCalendarPage.vue';

export default {
  name: 'App',
  components: {
    loginPage,
    createCalendar
  },
  data: () => ({
    //
  }),
};
</script>
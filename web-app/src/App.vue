<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">Schedules+</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn-toggle
        v-model="toggle_exclusive"
        color="black"
      >
          <v-btn
            color="orange"
            @click="darkMode"
          >
          Dark Mode
          </v-btn>
      </v-btn-toggle>
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
    toggle_exclusive: "",
  }),
  methods: {
    darkMode(){
      if(this.$vuetify.theme.dark == true){
        this.$vuetify.theme.dark = false;
      }
      else{
        this.$vuetify.theme.dark = true;
      }
1    }
  },
};
</script>

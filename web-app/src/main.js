import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import axios from 'vue-axios'
//import loginPage from './components/loginPage';

new Vue({
  axios, 
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

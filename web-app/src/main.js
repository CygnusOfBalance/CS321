import Vue from 'vue'
import loginPage from './App.vue'
import vuetify from './plugins/vuetify';
import axios from './plugins/axios';
//import loginPage from './components/loginPage';

new Vue({
  axios,
  vuetify,
  render: h => h(loginPage)
}).$mount('#app')

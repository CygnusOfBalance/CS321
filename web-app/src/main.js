import Vue from 'vue'
import loginPage from './App.vue'
import vuetify from './plugins/vuetify';
import axios from './plugins/axios';
import router from './router';
//import loginPage from './components/loginPage';



new Vue({
  axios,
  router,
  vuetify,
  render: h => h(loginPage)
}).$mount('#app')

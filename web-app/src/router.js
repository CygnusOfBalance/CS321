import Vue from 'vue'
import Router from 'vue-router'
//import Home from './views/Home.vue'
import loginPage from './components/loginPage.vue'
import createCalendar from './components/createCalendar.vue'
import userPage from './components/UserPage.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'loginPage',
      component: loginPage 
    },
    /*{
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" './views/About.vue')
    },*/
    {
      path: '/create-calendar',
      name : 'create-calendar',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: createCalendar
    },
    {
      path: '/create-user',
      name: 'create-user',
      component: userPage
    }
  ]
})

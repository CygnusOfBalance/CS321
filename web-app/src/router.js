import Vue from 'vue'
import Router from 'vue-router'
//import Home from './views/Home.vue'
import loginPage from './views/loginPage.vue'
import createCalendar from './views/createCalendarPage.vue'
import userPage from './views/UserPage.vue'
import calendarPage from './views/CalendarPage.vue'

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
    },
    {
      path: '/calendar',
      name: 'calendar',
      component: calendarPage
    }
  ]
})

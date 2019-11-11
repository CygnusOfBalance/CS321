<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  > 
   <v-col cols='30' align-self='stretch'> 
    <v-subheader>Add Event</v-subheader>

    <v-select
	v-model="year1"
        :items="years"
        :menu-props="{ maxHeight: '400' }"
        label="Select"
        hint="Select year of event"
        persistent-hint
    ></v-select>

    <v-select
	v-model="month1"
        :items="months"
        :menu-props="{ maxHeight: '400' }"
        label="Select"
        hint="Select month of event"
        persistent-hint
    ></v-select>

    <v-select
	v-model="day1"
        :items="days"
        :menu-props="{ maxHeight: '400' }"
        label="Select"
        hint="Select day of event"
        persistent-hint
    ></v-select>

    <v-text-field
      v-model="starttime"
      label="Start Time (HH:MM)"
      required
    ></v-text-field>
    
    <v-text-field
      v-model="endtime"
      label="End Time (HH:MM)"
      required
    ></v-text-field>

    <v-text-field
      v-model="name1"
      label="Event Name"
      required
    ></v-text-field>

    <v-btn
      color="success"
      class="mr-4"
      @click="addEvent"
    >
      Add Event
    </v-btn>


   </v-col>
  </v-form>
</template>
<script>
import calendar from '../views/CalendarPage'
import EventBus from '../eventBus.js'
  export default {
    data: () => ({
	year1: "",
	month1: "", 
	day1: "",
	name1: "",
	starttime: "",
	endtime: "",

	valid: true,

	years: [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012],
	days: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
		20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
	months: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
	events: [{
		name: 'Stuff',
		start: '2019-01-07 09:00',
		end: '2019-01-07 10:00'	
	}],
    }),
    methods: {
	addEvent(){
		//CALL TO DATABASE TO STORE
	} 
    }
  }
</script>

<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  > 
   <v-col cols='30' align-self='stretch'> 
    <v-subheader>Add Event</v-subheader>

    <v-select
	v-model="year"
        :items="year"
        :menu-props="{ maxHeight: '400' }"
        label="Select"
        hint="Select year of event"
        persistent-hint
    ></v-select>

    <v-select
	v-model="month"
        :items="month"
        :menu-props="{ maxHeight: '400' }"
        label="Select"
        hint="Select month of event"
        persistent-hint
    ></v-select>

    <v-select
	v-model="day"
        :items="day"
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
      v-model="name"
      label="Event Name"
      required
    ></v-text-field>

    <v-btn
      :disabled="!valid"
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
  export default {
    data: () => ({
	year: [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012],
	day: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
		20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
	month: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
	events: [],
    }),
    methods: {
	addEvent(){
		this.$refs.CalendarPage.addEvent(name, '2019-11-18 09:00', '2019-11-18 10:00');
	} 
    }
  }
</script>

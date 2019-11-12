<template>
    <v-app id="inspire">

        <v-row justify='center' align='center'>
	       <addEvent/>

                <v-sheet height="400" width="700">
		    <v-col offset="5">
		    	<p>Group 3s Calendar</p>
		    </v-col>
                    <v-calendar
                    ref="calendar"
                    :now="today"
                    :value="today"
                    :events="events"
                    color="primary"
                    type="week"
                    >
                    <!-- the events at the top (all-day) -->
                    <template v-slot:day-header="{ date }">
                        <template v-for="event in eventsMap[date]">
                        <!-- all day events don't have time -->
                        <div
                            v-if="!event.time"
                            :key="event.title"
                            class="my-event"
                            @click="open(event)"
                            v-html="event.title"
                        ></div>
                        </template>
                    </template>
                    <!-- the events at the bottom (timed) -->
                    <template v-slot:day-body="{ date, timeToY, minutesToPixels }">
                        <template v-for="event in eventsMap[date]">
                        <!-- timed events -->
                        <div
                            v-if="event.time"
                            :key="event.title"
                            :style="{ top: timeToY(event.time) + 'px', height: minutesToPixels(event.duration) + 'px' }"
                            class="my-event with-time"
                            @click="open(event)"
                            v-html="event.title"
                        ></div>
                        </template>
                    </template>
                    </v-calendar>
                </v-sheet>

        </v-row>
        <!--will change once we get api call for amount of people in calendar-->
                        <v-col cols="3" align="center" offset="5"> 
                          <p>Filter Schedules</p>
			  <v-btn-toggle
			  	v-model="toggle_exclusive"
				multiple
				color="white"
			  >
        			<v-btn
                            		v-for="n in this.users.length"
					:color="colorOrder[n-1]"
                            		:key="n"
        			>
                          		{{ users[n-1] }}
                        	</v-btn>
			  </v-btn-toggle>
                 </v-col>
    </v-app>
</template>

<script>
import UserInvite from '../components/UserInvite'
import addEvent from '../components/addEvent'
export default {
    components: {
        UserInvite,
	addEvent
    },
    data: () => ({
	name1: "",
	color1: "green",
	year1: "",
	month1: "",
	day1: "",
	starttime: "",
	endtime: "",
  	label: "key",

        today: '2019-11-18',
        events: [{
            name: 'Weekly Meeting',
            start: '2019-01-07 09:00',
            end: '2019-01-07 10:00',
        }],
	colorOrder: ["blue", "red", "orange", "green", "yellow"],
	users:["Noah", "Peter", "Holden", "Thomas"],
    }),
    methods: {
	addEvent() {
		//Constant call to database to refresh calendar events//
    	},
	dynamBtn: function(n) {
		this.label=users.slice(n, n+1);
	},
	retColor: function(n) {
		this.colorOrder=colorOrder.slice(n, n+1);
	}
   },
}
</script>

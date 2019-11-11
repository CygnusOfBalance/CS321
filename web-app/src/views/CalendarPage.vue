<template>
    <v-app id="inspire">

        <v-row justify='center' align='center'>
	   <addEvent/>

                <v-sheet height="600" width="700">
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

		<v-btn 
	  	 color="success"
	 	 class="mr-4"
		 @click="addEvent()"
		>
 		 Filter Buttons
 		</v-btn>

            

            

            
        </v-row>

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
	year1: "", 
	month1: "",
	day1: "",
	starttime: "",
	endtime: "",

        today: '2019-11-18',
        events: [{
            name: 'Weekly Meeting',
            start: '2019-01-07 09:00',
            end: '2019-01-07 10:00',
        }],
    }),
    methods: {
	addEvent() {
		//Constant call to database to refresh calendar events//
    	},
   },
}
</script>

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
                    :now="getDateNow"
                    :value="today"
                    :events="events"
                    :event-color="getEventColor"
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

		<userInvite/>
        </v-row>
        <!--will change once we get api call for amount of people in calendar-->
                        <v-col cols="12" align="center">
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
            @click="filter(users[n-1])"
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
       toggle_exclusive: undefined,
    	 name1: "",
	     color1: "green",
	     year1: "",
	     month1: "",
	     day1: "",
	     starttime: "",
	     endtime: "",
       label: "key",
       today: "",
       events: [{
        name: 'Weekly Meeting',
        start: '2019-11-13 09:00',
        end: '2019-11-13 10:00',
	      color: "blue",
       }],
        removedEvents: [],
	     colorOrder: ["blue", "red", "orange", "green", "yellow"],
	     users:["Noah", "Peter", "Holden", "Thomas"],
    }),
    methods: {
	     getEventColor(event){
        return event.color
       },

       getDateNow() {
        var d = new Date();
        this.today = d.getFullYear() + "-" + d.getMonth() + "-" + d.getDay();
        return this.today;
       },

       filter: function(name1){
        var correspondingColor = this.colorOrder[this.users.indexOf(name1)]

        

        if(this.toggle_exclusive != "0"){
          //Filter Out(Filter out via name)
          //Alg: use indexOf to find

          var takenOut = []
          for (var i = 0; i < this.events.length;  i++){
              if(this.events[i].color == correspondingColor){
                console.log("Removing color")
                takenOut.push(this.events[i])
                this.events.splice(i, 1);
              }
          }
        
          this.removedEvents = this.removedEvents.concat(takenOut)
          console.log(this.removedEvents)
        }
        else{
          //Filter In
          console.log(this.removedEvents);

          var readyToPush = [];
          for(var i = 0; i < this.removedEvents.length; i++){
              if(this.removedEvents[i].color == correspondingColor){
                  readyToPush.push(this.removedEvents[i]);
                  this.removedEvents.splice(i, 1);
              }
          }

          this.events = this.events.concat(readyToPush);
        }
       },
       //THIS FUNCTION IS FOR GETTING THE CALENDAR ON REFRESH
       /*mounted: function () {
        this.axios({
          method: 'GET',
          //url: "https://cfi7bbpmh2.execute-api.us-east-1.amazonaws.com/Production/",
        }).then(response => {console.log(response)});
      }*/
   },
}
</script>

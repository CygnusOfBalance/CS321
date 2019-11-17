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
        toggle_exclusive: "",
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
            start: '2018-11-10 09:00',
            end: '2018-11-10 10:00',
	        color: "blue",
        }],
        removedEvents: [],
        colorOrder: ["blue", "red", "orange", "green", "yellow", "purple", "cyan"],
	      users: [],
    }),

    methods: {
	    getEventColor(event){
            return event.color
      },

        //Get current date for the calendar
        getDateNow() {
            var d = new Date();
            this.today = d.getFullYear() + "-" + d.getMonth() + "-" + d.getDay();
            return this.today;
        },

        //Filters out and in the given user's schedule
        //Filter Out(Filter out via name)
        //Alg: use indexOf to find
        filter: function(name1){
            var correspondingColor = this.colorOrder[this.users.indexOf(name1)];

            //Filter out the color
            if(!this.toggle_exclusive.includes(this.users.indexOf(name1))){
                //Array of events taken out
                var takenOut = []
                for (var i = 0; i < this.events.length;  i++){
                    if(this.events[i].color == correspondingColor){
                        console.log("Removing color:" + this.events[i].color)
                        takenOut.push(this.events[i])
                        this.events.splice(i, 1);
                        //Prevent skipping when removing
                        i--
                    }
            }

            //Add towards the amount of removed events
            this.removedEvents = this.removedEvents.concat(takenOut)
            }
            //Filter in a color
            else{
                //Array of events about to be active
                var readyToPush = [];
                for(var i = 0; i < this.removedEvents.length; i++){
                    if(this.removedEvents[i].color == correspondingColor){
                        readyToPush.push(this.removedEvents[i]);
                        this.removedEvents.splice(i, 1);
                        //Prevent skipping after splice
                        i--
                    }
                }

                //Add towards the amount of events active
                this.events = this.events.concat(readyToPush);
            }
        },
    },
    //THIS FUNCTION IS FOR GETTING THE CALENDAR ON REFRESH
    mounted: function () {
      var resp
      this.axios({
        method: 'GET',
        url: "https://cfi7bbpmh2.execute-api.us-east-1.amazonaws.com/Production/getusers",
        }).then(response => {
          resp = response["data"]["body"].replace(/\"/g, '')
          resp = resp.replace(/\[/g, '')
          resp = resp.replace(/\]/g, '')
          resp = resp.split(",")
          this.users = resp;
     });

      this.axios.get(
        "https://cfi7bbpmh2.execute-api.us-east-1.amazonaws.com/Production/getschedule"
      ).then(response => {
          console.log(response)
          var i
          var x = []
          for (i in response["data"]){
            //ACTUALLY PARSE OUT THE DATA
            if(response["data"][i] != ""){
              response["data"][i]["0"]["name"] = response["data"][i]["0"]["eventName"]
              delete response["data"][i]["0"]["eventName"]
              x.push(response["data"][i])
            }
          }
          //x.push(response["data"]["Rost"])
          //alert(JSON.stringify(x[0]))
          this.events = this.events.concat(x[0]);
          /*this.events.push({name: 'Weekly Meeting',
                            start: '2019-11-10 09:00',
                            end: '2019-11-10 10:00',
                            color: "blue",});*/
         console.log(this.events)
      });
    },
}
</script>

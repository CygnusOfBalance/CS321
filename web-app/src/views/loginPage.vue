<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
   <v-col cols="4" offset="4">
    <v-subheader>Login</v-subheader>

    <v-text-field
      v-model="name"
      label="E-Mail"
      required
    ></v-text-field>

    <v-text-field
      v-model="pw"
      :rules="nameRules"
      :type="'password'"

      label="Password"
      required
    ></v-text-field>

    <v-btn
      :disabled="!valid"
      color="green"
      class="mr-4"
      @click="POST"
    >
      Login
    </v-btn>

    <v-btn
      class="mr-4"
      color="blue"
      @click="navigate"
    >
      Create User
    </v-btn>


   </v-col>
  </v-form>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      pw: '',
      nameRules: [
        v => !!v || 'Password is Required',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      checkbox: false,

      name: '',
      status: '',
    }),
    methods: {
      validate () {
        if (this.$refs.form.validate()) {
          this.snackbar = true
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },

      navigate() {
    	 this.$router.push("/create-user");
      },
      POST(){
      	// send a POST request

        //force route for now
        //this.$router.push("/calendar");

      	this.axios({
        	method: 'POST',
        	url: 'https://cfi7bbpmh2.execute-api.us-east-1.amazonaws.com/Production/login',
        	data: {
        	  name: this.name,
		        password: this.pw,
        	}
      	}).then(response => {
    	// returning the data here allows the caller to get it through another .then(...)
    	this.setStatus(JSON.stringify(response)),
      this.routerPush();
      });
    },
    setStatus: function(string){
	   this.status = string;
    },
    routerPush: function(){
      if(this.status.includes("200")){
          this.$router.push("/calendar");
      }
      else{
          window.alert("Error Username or Password Incorrect");
          alert(this.status);
      }
   }
  }
 }
</script>

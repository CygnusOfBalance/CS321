<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  > 
   <v-col cols="4" offset="4"> 
    <v-subheader>Login</v-subheader>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="email"
      required
    ></v-text-field>

    <v-text-field
      v-model="pw"
      :rules="nameRules"
      
      label="Password"
      required
      box
    ></v-text-field>

    <v-btn
      :disabled="!valid"
      color="success"
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
      Create Calendar
    </v-btn>


   </v-col>
  </v-form>
</template>

<script>
  import router from '../router.js';
  
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
    	router.push("/create-calendar");
      },
      POST(){
      	// send a POST request
      	this.axios({
        	method: 'post',
        	url: 'https://cfi7bbpmh2.execute-api.us-east-1.amazonaws.com/Production/login',
        	data: {
        	  name: this.name,
		  Password: this.Password
        	}
      	}).then(response => {
    	// returning the data here allows the caller to get it through another .then(...)
    	console.log(response)
      });
    },
  }
 }
</script>

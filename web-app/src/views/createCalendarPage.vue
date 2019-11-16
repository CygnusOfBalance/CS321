<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
   <v-col cols="4" offset="4">
    <v-subheader>Create Calendar</v-subheader>

    <v-text-field
      v-model="name"
      label="Username"
      required
    ></v-text-field>

    <v-text-field
      v-model="pw"
      :rules="nameRules"
      :type="'password'"

      label="Password"
      required
      box
    ></v-text-field>

    <v-text-field
      v-model="cname"

      label="Calendar Name"
      required
      box
    ></v-text-field>

    <v-btn
      color="blue"
      class="mr-4"
      @click="POST"
    >
      Create Calendar
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
      pw: '',
      cname: '',
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
      POST(){
      	// send a POST request
      	this.axios({
        	method: 'post',
        	url: 'https://cfi7bbpmh2.execute-api.us-east-1.amazonaws.com/Production/login',
        	data: {
        	  name: this.name,
		        Password: this.pw,
        	}
      	}).then(response => {
    	// returning the data here allows the caller to get it through another .then(...)
    	console.log(response)
      });

      this.$router.push("/calendar");
    },
  }
  }
</script>

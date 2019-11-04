<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  > 
   <v-col cols="4" offset="4"> 
    <v-subheader>Create Account</v-subheader>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"

      required
    ></v-text-field>

    <v-text-field
        v-model="password"
        :rules="passwordRules"
        :type='"password"'

        label="Password"

        required
    ></v-text-field>

    <v-text-field
        v-model="retypePassword"
        :error-messages='passwordMatch()'
        :rules="doubleCheckRules"
        :type='"password"'

        label="Retype Password"

        required
    ></v-text-field>
    

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="createUser"
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
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      password: '',
      passwordRules: [
          v => !!v || 'Password is required'
      ],
      retypePassword: '',
      doubleCheckRules: [
          v => !!v || 'Password mismatch',
      ],
    }),
    methods: {
        createUser () {
            //Validate first
            if (this.$refs.form.validate()) {
                this.snackbar = true;

                console.log("Valid and sending data...")
                this.axios({
                    method: 'post',
                    url: '',
                    data: {
                        email: this.email,
                        password: this.password
                    }
                }).then(response => console.log(response))
            }
        },
        passwordMatch() {
          return (this.password === this.retypePassword) ? '' : 'Mismatched Password';
        }


    },
  }
</script>

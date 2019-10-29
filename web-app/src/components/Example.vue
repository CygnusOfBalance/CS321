<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <v-flex xs12>
        <v-btn dark color="blue" @click.native="click" title="Login">Login</v-btn>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    username: 'hmalinch@masonlive.gmu.edu',
    password: 'CS321'
  }),
  methods: {
    click: function(){
      // send a POST request
      this.axios({
        method: 'get',
        url: 'https://cfi7bbpmh2.execute-api.us-east-1.amazonaws.com/Production/examplepost',
        data: {
          firstName: 'holden',
          lastName: 'Williams'
        }
      }).then(response => {
    // returning the data here allows the caller to get it through another .then(...)
    console.log(response)
  });
    }
  }
};
</script>

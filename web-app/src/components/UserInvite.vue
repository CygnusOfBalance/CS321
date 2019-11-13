<template>
    <v-form>
        <v-col cols="4"  offset="4">
        </v-col>
        <v-text-field>
        </v-text-field>

        Share URL: {{url}}
        <input type='hidden' id='address' :value= url>
    </v-form>
</template>

<script>
export default {
    data: () => ({
        url: "locahost:8080/create-user"
    }),
    methods: {
        copyLink () {
            text = document.querySelector('#address')

            try{
                document.execCommand('copy')
            } catch(err) {
                console.log(err)
            }
        }
    }
}
</script>
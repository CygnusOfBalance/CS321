<template>
    <v-form>
        <v-col cols="4"  justify="center" offset="2">
		<v-btn
			color=success
			class="mr-4"
			@click="copyLink"
		>
		Copy Share Link
		</v-btn>
        	<input type="hidden" id="address" :value="url">
        </v-col>

    </v-form>
</template>

<script>
export default {
    data: () => ({
        url: "localhost:8080/#/create-user",
    }),
    methods: {
        copyLink () {
            let text1 = document.querySelector('#address')
	    text1.setAttribute('type', 'text') 
	    text1.select()

            try{
                var successful = document.execCommand('copy');
		text1.setAttribute('type', 'hidden');
		alert("Share link was copied to clipboard");
            } catch(err) {
                console.log(err)
            }
        },
    }
}
</script>

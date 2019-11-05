# web-app

#### Dont remove things from .gitignore without consuilting someone, things in there are different depending on IDE's

## Project setup 
### You need npm, yarn also works but commands are different for yarn
```
npm install @vue/cli -g
```
### Once you have installed the the cli you can use the command line or you can do this: (Which I highly reccomend)
### In terminal navigate to the project folder:
```
*/CS321/web-app
```
### This is how you can make changes and see the result live locally without messing with anything else
```
vue ui
```
### If you get an error like: Local package.json exists, but node_modules missing, did you mean to install?  or something about node_modules being gone, Do:
```
npm install
```
## WARNING 
```
vue ui
```
## will defualt to the most recent git branch you are on so make sure you are on your correct branch before doing this
### This will open a webpage, Click on import, web-app.  Again if you see a warning about node modules missing go to your command line in the webapp folder do:
```
npm install
```
### This gives you a gui for adding dependencies and lots of other things, but most importantly navigate to tasks on the left
### Go to the build task. Click Run Task if any new dependencies are added.  Otherwise you go right to serve tab
### Here you click Run Task and then when its done with the loading circle on the right, above the loading circle is a button titled Open App click that
### Now you have a local version of the web-app running and you can make changes to the code and watch it change live on that webpage

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

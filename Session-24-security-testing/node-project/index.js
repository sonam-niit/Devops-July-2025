const express = require('express')
const app = express() //server

//security problems
const dbUser='admin'
const dbPassword='passworrd123'

//api
app.get('/',(req,res)=>{
    res.send('Hello From SonarQube!')
})
//duplicated logics
//Unused Function
function debugLog(msg){
    console.log('DEBUG: ',msg)
}

//server starting
app.listen(3000,()=>console.log('server started'))
const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const http = require('http')
const server = http.createServer(app)
const path = require('path')

const port = 3000
let ip = require('ip')
console.dir(ip.address())


app.use(bodyParser.urlencoded({extended: true}))

app.get("/",(req,res)=>{
    res.send({
        "city": {
            "insee": "92050",
            "cp": 92000,
            "name": "Nanterre",
            "latitude": 48.8961,
            "longitude": 2.2067,
            "altitude": 43
        },
        "update": "2023-02-03T10:14:37+01:00",
        "forecast": {
            "insee": "78124",
            "cp": 78420,
            "latitude": 48.9119,
            "longitude": 2.1784,
            "day": 0,
            "datetime": "2023-02-03T01:00:00+0100",
            "wind10m": 10,
            "gust10m": 33,
            "dirwind10m": 269,
            "rr10": 0,
            "rr1": 0,
            "probarain": 10,
            "weather": 3,
            "tmin": 6,
            "tmax": 12,
            "sun_hours": 2,
            "etp": -99,
            "probafrost": 0,
            "probafog": 30,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 33
        }
    })
})

server.listen(port, () =>{
    console.log(`On écoute sur le port ${port}`)
})
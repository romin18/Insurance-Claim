var express = require("express")
const bodyParser = require("body-parser")
var mongoose = require("mongoose")

const app = express()

app.use(bodyParser.json())
app.use(express.static('public'))
app.use(bodyParser.urlencoded({
    extended:true
}))

mongoose.connect('mongodb://localhost:27017/Database')
var db=mongoose.connection
db.on('error',()=> console.log("Error in connecting to Database"))
db.once('open',()=> console.log("Connected to Database"))

app.post("/sign_up",(req,res) => {
    var name = req.body.name
    var age = req.body.age
    var userId = req.body.userId
    var service = req.body.service
    var date = req.body.date

    var data = {
        "name":name,
        "age":age,
        "userId":userId,
        "service":service,
        "date":date
    }
    
    db.collection('users').insertOne(data,(err,collection) => {
        if(err){
            throw err;
        }
        // console.log(name,userId)
        console.log("Registered successfully")
    })
    return res.redirect('signup_success.html')
    
})

app.get("/", (req,res) => {
    res.set({
        "Allow access Allow origin":'*'
    })
    return res.redirect('index.html')
}).listen(7000);

console.log("Listening on port 7000")
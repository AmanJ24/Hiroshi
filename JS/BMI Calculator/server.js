const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/bmiCalculator", function (req, res) {
    res.sendFile(__dirname + '/bmiCalculator.html');
});

app.post("/bmiCalculator", function (req, res) {

    var height = Number(req.body.height);
    var weight = Number(req.body.weight);

    var result = Math.round(weight / (height ** 2));

    res.send("Your BMI is " + result);

});

app.listen(3000, function () {
    console.log("Server started on port 3000.")
});
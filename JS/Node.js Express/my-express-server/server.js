const express = require('express');

const app = express();

app.get("/", function(req, res) {
    res.send("Hello");
});

app.get("/contact", function(req, res) {
    res.send("Contact me at: Aman@gmail.com");
});

app.get("/hobbies", function(req, res) {
    res.send("<ul><li>Programming</li><li>Basketball</li></ul>");
});

app.get("/about", function(req, res) {
    res.send("This server is hosted By Aman Jangir.");
});

app.listen(3000, function () {
    console.log("Server started on port 3000");
});



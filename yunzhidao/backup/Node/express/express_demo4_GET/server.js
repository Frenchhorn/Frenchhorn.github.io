//GET方法
var util = require('util');
var express = require('express');
var app = express();

app.get('/index.html', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/process_get', function(req, res) {
    response = {
        first_name: req.query.first_name,
        last_name: req.query.last_name
    };
    console.log(response);
    res.end(JSON.stringify(response));
});

var server = app.listen(8081, function() {
    var address = server.address();
    console.log(util.inspect(address));
});
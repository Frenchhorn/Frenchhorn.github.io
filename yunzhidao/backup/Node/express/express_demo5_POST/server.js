//POST
var util = require('util');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

var urlEncodedParser = bodyParser.urlencoded({extended: false})

app.get('/index.html', function(req, res) {
    res.sendFile(__dirname + '/' + 'index.html');
});

app.post('/process_post', urlEncodedParser, function(req, res) {
    response = {
        first_name: req.body.first_name,
        last_name: req.body.last_name
    };
    console.log(response);
    res.end(JSON.stringify(response));
});

var server = app.listen(8081, function() {
    var address = server.address()
    console.log(util.inspect(address, true));
})
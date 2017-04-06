var url = require('url');

function route(requestUrl) {
    var pathname = url.parse(requestUrl).pathname;
    console.log('About to route a request for ' + pathname);
}

exports.route = route;
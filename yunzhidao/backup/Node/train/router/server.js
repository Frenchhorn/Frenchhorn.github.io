var http = require('http');

function start(route) {
    var onRequest = function(request, response) {
        route(request.url);
        
        response.writeHead(200, {'Content-Type': 'text/plain'});
        response.write('Hello World!');
        response.end();
    }
    
    http.createServer(onRequest).listen(8888);
    console.log('Server has started.')
}

exports.start = start;
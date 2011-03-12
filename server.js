var http = require('http')

http.createServer(function(req, res) {

	res.writeHead(200, {})
	res.end('coming soon: monokro.me')

}).listen(80);


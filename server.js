var http = require('zest/http'),
    debug = false,
    port_number = 80

if (debug) port_number = 8000

server = new http.Server()
server.port = port_number

server.listen('monokro.me/urls')


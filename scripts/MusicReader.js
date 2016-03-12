var http = require("http");
var port = 3001;
var serverUrl = "http://localhost";

var server = http.createServer(function(req, res) {

  console.log("Request: " + req.url);
  
  var now = new Date();
  var html = "<p>Hello World, the time is " + now + ".</p>";
  res.end(html);

});

console.log("Listening at " + serverUrl + ":" + port);
server.listen(port, serverUrl);
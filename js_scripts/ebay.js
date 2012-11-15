var request = require('dojo/request/xhr');

var api_base = 'http://api.terapeak.com/v1/research/xml?api_key=99afqy42ehfwck5su2habgvd';

request.post({url:api_base, headers: {"Content-Type": "text/xml"}}, function(err, resp, body) {
  console.log(body);
  console.log(err);
});

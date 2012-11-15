var request = require('request');
var fs = require('fs');

var api_base = 'http://3taps.net/search?authToken=5ddc7c5c5a8245f8b0ae63340287b218&source=CRAIG';

var NUM_PAGES = 100;//90874
var RPP = 1000;
var start = Date.now();

function getData(results, page){
  if (!results) results = [];
  if (!page) page = 0;
  if (page > NUM_PAGES) {
    fs.writeFile('POSTS_LARGE.txt', JSON.stringify(results,null,2), function (err) {
      if (err) throw err;
      console.log("It's saved!");
      console.log((Date.now() - start)/1000);
    });
  } else {
    var url = api_base + '&rpp=' + RPP + '&page=' + page;
    console.log('page');
    request.get(url, function(err, resp, body) {
      if (body) body = JSON.parse(body).results;
      else return getData(results, page);
      console.log('page success');
      getData(results.concat(body), page+1);
    });
  }
}

getData();

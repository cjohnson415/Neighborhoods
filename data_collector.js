var request = require('request');
var async = require('async');

var api_base = 'http://3taps.net/search?authToken=5ddc7c5c5a8245f8b0ae63340287b218&source=CRAIG';

var NUM_PAGES = 10;//90874
var RPP = 1000;

function getCodes(results, page){
  if (!results) var results = {};
  if (!results.seen) results.seen = 0;
  if (!results.dirty) results.seen = 0;
  if (!results.metroCodes) results.metroCodes = {};
  if (!page) page = 0;
  if (page > NUM_PAGES) {
    console.log(results);
  } else {
    var url = api_base + '&rpp=' + RPP + '&page=' + page;
    request.get(url, function(err, resp, body) {
      if (body) body = JSON.parse(body).results;
      else return getCodes(results, page);
      async.forEach(body, function(post, callback) {
        results.seen++;
        var loc = post.location;
        if (!loc.metroCode) results.dirty++;
        else if (!(results.metroCodes[loc.metroCode])) {
          results.metroCodes[loc.metroCode] = 1;
        }
        else {
          results.metroCodes[loc.metroCode]++;
        }
        callback();
      }, function (err) {
        console.log('page');
        getCodes(results, page+1);
      });
    });
  }
}

getCodes();

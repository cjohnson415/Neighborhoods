var fs = require('fs');
var async = require('async');

function getCodes() {
  fs.readFile('POSTS_MEDIUM.json', null, function(err, data) {
    posts = JSON.parse(data);
    var cityCodes = {};
    var seen = 0;
    var dirty = 0;
    var uniques = 0;


    async.forEach(posts, function(post, callback) {
      seen++;
      var loc = post.location;
      if (!loc.cityCode) dirty++;
      else {
        if (!(cityCodes[loc.cityCode])) {
          cityCodes[loc.cityCode] = {};
          cityCodes[loc.cityCode].numPosts = 1;
          cityCodes[loc.cityCode].titleLength = post.heading.length;
          cityCodes[loc.cityCode].bodyLength = post.body.length;
          cityCodes[loc.cityCode].numImages = post.images.length;
          uniques++;
        } else {
          cityCodes[loc.cityCode].numPosts++;
          cityCodes[loc.cityCode].titleLength += post.heading.length;
          cityCodes[loc.cityCode].bodyLength += post.body.length;
          cityCodes[loc.cityCode].numImages += post.images.length;
        }
      }
        callback();
    }, function(err) {
      console.log('done');
      dirtyPercent = dirty / seen;
      async.forEach(Object.keys(cityCodes), function(cityCode, callback) {
        cityCodes[cityCode].titleLength /= cityCodes[cityCode].numPosts;
        cityCodes[cityCode].bodyLength /= cityCodes[cityCode].numPosts;
        cityCodes[cityCode].numImages /= cityCodes[cityCode].numPosts;
        callback();
      }, function(err) {
        results = {uniques:uniques, seen: seen, percent_dirty: dirtyPercent, cityCodes: cityCodes};
        fs.writeFile('CITY_CODES.json', JSON.stringify(results, null, 2), function(err) {
          if (err) console.log(err);
          console.log("It's saved!");
        });
      });
    });
  });
}

getCodes();

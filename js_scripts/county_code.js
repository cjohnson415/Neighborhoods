var fs = require('fs');
var async = require('async');

function getCodes() {
  fs.readFile('POSTS_MEDIUM.json', null, function(err, data) {
    posts = JSON.parse(data);
    var countyCodes = {};
    var seen = 0;
    var dirty = 0;
    var uniques = 0;
    async.forEach(posts, function(post, callback) {
      seen++;
      var loc = post.location;
      if (!loc.countyCode) dirty++;
      else if (!(countyCodes[loc.countyCode])) {
        countyCodes[loc.countyCode] = 1;
        uniques++;
      } else countyCodes[loc.countyCode]++;
      callback();
    }, function(err) {
      console.log('done');
      dirtyPercent = dirty / seen;
      results = {uniques:uniques, seen: seen, percent_dirty: dirtyPercent, countyCodes: countyCodes};
      fs.writeFile('COUNTY_CODES.json', JSON.stringify(results, null, 2), function(err) {
        if (err) console.log(err);
        console.log("It's saved!");
      });
    });
  });
}

getCodes();

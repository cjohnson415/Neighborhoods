var fs = require('fs');
var async = require('async');

function getCodes() {
  fs.readFile('POSTS_MEDIUM.json', null, function(err, data) {
    posts = JSON.parse(data);
    var localityCodes = {};
    var seen = 0;
    var dirty = 0;
    var uniques = 0;
    async.forEach(posts, function(post, callback) {
      seen++;
      var loc = post.location;
      if (!loc.localityCode) dirty++;
      else if (!(localityCodes[loc.localityCode])) {
        localityCodes[loc.localityCode] = 1;
        uniques++;
      } else localityCodes[loc.localityCode]++;
      callback();
    }, function(err) {
      console.log('done');
      dirtyPercent = dirty / seen;
      results = {uniques:uniques, seen: seen, percent_dirty: dirtyPercent, localityCodes: localityCodes};
      fs.writeFile('LOCALITY_CODES.json', JSON.stringify(results, null, 2), function(err) {
        if (err) console.log(err);
        console.log("It's saved!");
      });
    });
  });
}

getCodes();

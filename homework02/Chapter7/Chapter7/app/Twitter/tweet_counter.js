var ntwitter = require("ntwitter"),
redis = require("redis"),
credentials = require("./credentials.json"),

twitter,
counts = {};

twitter = ntwitter(credentials);

client = redis.createClient();

counts.awesome = 0;
twitter.stream(
    "statuses/filter",

    {"track":["awesome","cool","rad","gnarly","groovy"]},

    function(stream) {
        stream.on("data", function(tweet){
            if (tweet.text.indexOf("awesome") >= -1) {
                client.incr("awesome");
                counts.awesome = counts.awesome + 1;
            }
        });
    }
);

module.exports = counts;



var express = require('express');
var router = express.Router();

/* GET users listing. */
//router.get('/', function(req, res, next) {
//    res.send('respond with a resource');
//});

router.use(function timeLog(req, res, next) {
  console.log('Time: ', Date.now());
  next();
});

router.route('/')
    .get(function(req, res, next) {
        res.send('GET: respond with a resource');
    })
    .post(function(req, res, next) {
        res.send('POST: respond with a resource');
    })

module.exports = router;

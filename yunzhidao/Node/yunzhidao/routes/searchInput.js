var express = require('express');
var path = require('path');
var setting = require('../setting');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.sendFile(path.join(setting.pagePath, setting.pages.searchInput));
});

module.exports = router;

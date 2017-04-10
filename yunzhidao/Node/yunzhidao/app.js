var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var routes = {
    "index": require('./routes/index'),
    "login": require('./routes/login'),
    "logout": require('./routes/logout'),
    "category": require('./routes/category'),
    "imageDetail": require('./routes/imageDetail'),
    "searchInput": require('./routes/searchInput'),
    "searchResults": require('./routes/searchResults'),
};


var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

//Index Page
app.use('/', routes.index);
app.use('/index.html', routes.index);
//Login Page
app.use('/login.html', routes.login);
//Logout Page
app.use('/logout.html', routes.logout);
//Category Page
app.use(/\/category\..+\.html$/, routes.category);
//ImageDetail Page
app.use('/imageDetail.html', routes.imageDetail);
//SearchInput Page
app.use('/searchInput.html', routes.searchInput);
//SearchResults Page
app.use('/searchResults.html', routes.searchResults);
// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;

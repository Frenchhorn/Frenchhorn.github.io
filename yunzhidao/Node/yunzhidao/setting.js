var path = require('path');

var setting = {
    "pagePath": path.join(__dirname, "pages"),
    "pages": {
        "index": "index.html",
        "category": "category.html",
        "imageDetail": "imageDetail.html",
        "login": "login.html",
        "logout": "logout.html",
        "searchInput": "searchInput.html",
        "searchResults": "searchResults.html"
    }
};

module.exports = setting;
$(function($){  
      var url = 'http://v.juhe.cn/weather/index';  
      $.ajax(url, {  
        data: {  
          'cityname': '襄阳',  
          'dtype': 'jsonp',  
          'key': 'xxxx',  
          '_': new Date().getTime()  
        },  
        dataType: 'jsonp',  
        crossDomain: true,  
        success: function(data) {  
          if(data && data.resultcode == '200'){  
            console.log(data.result.today);  
          }  
        }  
      });  

      var url2 = 'http://v.juhe.cn/weather/index?callback=?';  
      $.getJSON(url2, {  
        'cityname': '北京',  
        'dtype': 'jsonp',  
        'key': 'xxxx',  
        '_': new Date().getTime()  
      }, function(data){  
        if(data && data.resultcode == '200'){  
          console.log(data.result.today);  
        }  
      });  
  
      var url3 = 'http://v.juhe.cn/weather/index?callback=?';  
      $.get(url3, {  
        'cityname': '澳门',  
        'dtype': 'jsonp',  
        'key': 'xxxx',  
        '_': new Date().getTime()  
      }, function(data){  
        if(data && data.resultcode == '200'){  
          console.log(data.result.today);  
        }  
      }, 'json');  
    });  

var loadAjax1 = $.ajax({
    type: 'GET',
    dataType: 'json',
    async: false,
    url: '/libs/cq/i18n/dict.en.json'
});

loadAjax1.done(function(data, textStatus, jqXHR) {
    window.yunzhidao.productInfo.json = data;
});

loadAjax1.fail(function(jqXHR, textStatus, errorThrown) {});
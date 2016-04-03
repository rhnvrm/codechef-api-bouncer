# codechef-api-bouncer

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

The codechef API cannot be accessed via simple XHR requests or JSONP from a web browser. To bypass this, this project utilizes python's requests module and flask to bounce their data. 

## Bouncer API Usage

`/<contest name>/<filter>`

eg. `https://cc-bouncer.herokuapp.com/APRIL16/Institution%3DShiv Nadar University%2C Chithera`

## Sample AJAX Request

https://github.com/ACM-SNU/competitive-ranklist/blob/gh-pages/index.html

```javascript
$.ajax({
        type: "GET",
        dataType: 'json',
        url: 'https://cc-bouncer.herokuapp.com/APRIL16/Institution%3DShiv%20Nadar%20University%2C%20Chithera',
        success: function(data) {
          d = data.result.list;
          inside = '<table>';
          for(i = 0; i < d.length; i++){
            inside += '<tr>';
            inside += '<td>' + d[i].rank + '</td>';
            inside += '<td>' + d[i].score + '</td>';
            inside += '<td>' + d[i].user_handle + '</td>';
            inside += '</tr>';
          }
          inside += '</table>';
          document.getElementById("rank-cc-apr-16").innerHTML = inside;
        },
        error: function(e) {
          console.log(e.message);
        }
      });
```

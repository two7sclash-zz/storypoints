/*
 jquery-param (c) 2015 KNOWLEDGECODE | MIT
*/
(function(f) {
    var c = function(c) {
        var g = [],
            f = /\[\]$/,
            h = function(d, a) {
                a = "function" === typeof a ? a() : null === a ? "" : void 0 === a ? "" : a;
                g[g.length] = encodeURIComponent(d) + "=" + encodeURIComponent(a)
            }, e = function(d, a) {
                var b, c;
                if (d) if ("[object Array]" === Object.prototype.toString.call(a)) for (b = 0, c = a.length; b < c; b++) f.test(d) ? h(d, a[b]) : e(d + "[" + ("object" === typeof a[b] ? b : "") + "]", a[b]);
                else if (a && "[object Object]" === String(a)) for (b in a) e(d + "[" + b + "]", a[b]);
                else h(d, a);
                else if ("[object Array]" === Object.prototype.toString.call(a)) for (b = 0, c = a.length; b < c; b++) h(a[b].name, a[b].value);
                else for (b in a) e(b, a[b]);
                return g
            };
        return e("", c).join("&").replace(/%20/g, "+")
    };
    "object" === typeof module && "object" === typeof module.exports ? module.exports = c : "function" === typeof define && define.amd ? define([], function() {
        return c
    }) : f.param = c
})(this);
// Return an array of the selected opion values
// select is an HTML select element
function getSelectValues(select) {
  var result = [];
  var options = select && select.options;
  var opt;
  for (var i = 0, iLen = options.length; i < iLen; i++) {
    opt = options[i];

    if (opt.selected) {
      result.push(opt.value || opt.text);
    }
  }
  return result;
}

function getSelectedOption(sel) {
        var opt;
        for ( var i = 0, len = sel.options.length; i < len; i++ ) {
            opt = sel.options[i];
            if ( opt.selected === true ) {
                break;
            }
        }
        return opt;
    }

function handlerFunction (e){
    
   
    
  var val = getSelectValues(select),
  query = {
    val: val
  };
  
  debugger
  
  if (location.pathname ===  ( "/critera/" || "/critera" )){
      debugger
      
      window.history.pushState({}, null, val[0]);
      }

  else {
      debugger;
      window.location.href += ( window.location.search ? '&' : "?" ) + window.param( query );
      }
}


var select = document.getElementById("select"),
button = document.getElementById("button");
button.onclick = handlerFunction;

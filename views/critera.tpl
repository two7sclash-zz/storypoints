% import urllib
<!DOCTYPE html>
<html>
  <body>
   <select id="select" multiple>
       % for item in vars:
       % myUrl = urllib.quote_plus(item.encode('utf-8').strip())
         <option value='{{myUrl}}'>{{item}}</option>
       % end
        <option value="kindergarten">Kindergarten</option>
   </select>
   <br />
   <button id="button">Generate report</button>
   <script type="text/javascript" src="/static/main.js" charset="utf-8"></script>
 </body>
</html>

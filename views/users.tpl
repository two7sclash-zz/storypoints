<form action="/critera/users" method="get" id="form1">
  User(s) name: <input type="text" id="input">
  <br />
    <small>use white space or commas to seperate</small>

</form>

  
<button type="submit" form="form1" value="Submit">Submit</button>

<script>

window.addEventListener("load", function () {
 
  // We need to access the form element
  var form = document.getElementById("form1");
  
  function addHidden(value) {
    // Create a hidden input element, and append it to the form:
    var input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'val[]';
    input.value = value;
    form.appendChild(input);
    }   
  

  // to takeover its submit event.
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    var input = document.getElementById("input").value.split(/[ ,]+/);
    input.map(addHidden);
    
    
    
    this.submit();
  });
});
</script>

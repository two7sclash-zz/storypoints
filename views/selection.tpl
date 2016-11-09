<!DOCTYPE html>
<html>
<header>
<style>
h1 {    
    text-transform: capitalize;
}
</style>
</header>
<body>
<div id="content">
<h1>Story Points by {{criteron}}</h1>
<ul>
  % for selection, point in zip(selections, points):
    <li>{{ selection }}: {{ point }}</li>
  % end
</ul>
<p>Total: {{ sum(points) }}</p>
</div>
</body>
</html>

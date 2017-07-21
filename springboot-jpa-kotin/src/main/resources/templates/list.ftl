<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<h1>User detail</h1>
<#list users as user>
<ul>
    <li><a href="/get/id/${user.id}">${user.firstName} ${user.lastName}</a></li>
</ul>
</#list>
<a href="/add/1/caden/zhou">add caden zhou</a>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title><#if user??>${user.id}</#if></title>
</head>
<body>
<#if user??>
<h1>User detail</h1>
<h2>id: ${user.id}</h2>
<h2>first name: ${user.firstName}</h2>
<h2>last name: ${user.lastName}</h2>
<#else>
<h1>no such user</h1>
</#if>
</body>
</html>
<code>curl -X POST https://acdc-api.onrender.com/check-inmate -H "Content-Type: application/json" -d "{ \"inmates\": [ {\"firstName\": \"X\", \"lastName\": \"Y\"}, {\"firstName\": \"X\", \"lastName\": \"Y\"} ] }"</code>
<br><br>
<code>{"found_inmates":[{"firstName":"X","lastName":"Y"},{"firstName":"X","lastName":"Y"}],"status":"Inmates found"}
C:\Users>
</code>

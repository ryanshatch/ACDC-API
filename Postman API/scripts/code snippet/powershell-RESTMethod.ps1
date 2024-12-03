$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Content-Type", "application/json")

$body = @"
{{requestBody}}
"@

$response = Invoke-RestMethod 'https://acdc-api.onrender.com/check-inmate' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
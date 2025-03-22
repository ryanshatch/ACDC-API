<code>curl --location --max-time 90 --request POST "https://acdc-api.onrender.com/check-inmate" --header "Content-Type: application/json" --data "{\"inmates\":[{\"firstName\":\"Foster\",\"lastName\":\"Fech\"}]}"
</code>
<br><br>
<h3>For ios HTTPBot:</h3>
<code>curl -v \
	-X POST \
	-H "User-Agent: HTTPBot/2024.1.4" \
	-H "Content-Type: application/json" \
	-d "{
  \"inmates\": [
    { \"firstName\": \"Jack\", \"lastName\": \"Jackson\" }
  ]
}" \
	"https://acdc-api.onrender.com/check-inmate"</code>

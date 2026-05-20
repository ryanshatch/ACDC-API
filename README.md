<h1>ACDC-API</h1>

<p>A small Flask API that checks whether specified individuals appear in the Aiken County Sheriff’s Office inmate search system. Clients send a list of inmates (first/last names) to the API, which submits each entry to the county search endpoint and returns the subset that appear to be found.</p>

<blockquote>
  <p><strong>Note</strong>: This project performs automated lookups against the Aiken County Sheriff’s Office inmate search page. Ensure your usage complies with the site’s terms of service and applicable laws.</p>
</blockquote>

<hr>

<h2>Table of Contents</h2>

<ul>
  <li><a href="#features">Features</a></li>
  <li><a href="#how-it-works">How It Works</a></li>
  <li><a href="#api-endpoints">API Endpoints</a></li>
  <li><a href="#request--response-examples">Request &amp; Response Examples</a></li>
  <li><a href="#running-locally">Running Locally</a></li>
  <li><a href="#deployment">Deployment</a></li>
  <li><a href="#postman-collection">Postman Collection</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#dependencies">Dependencies</a></li>
  <li><a href="#notes--limitations">Notes &amp; Limitations</a></li>
  <li><a href="#license">License</a></li>
</ul>

<hr>

<h2 id="features">Features</h2>

<ul>
  <li><strong>Simple JSON API</strong> for inmate lookup by first and last name.</li>
  <li><strong>Batch input</strong>: submit multiple inmates in a single request.</li>
  <li><strong>Minimal dependencies</strong>: Flask + requests.</li>
  <li><strong>Postman collection</strong> included for quick testing.</li>
  <li><strong>Sample responses</strong> stored in the <code>Responses/</code> folder.</li>
</ul>

<hr>

<h2 id="how-it-works">How It Works</h2>

<p>The <code>/check-inmate</code> endpoint accepts a JSON payload like:</p>

<pre><code class="language-json">{
  "inmates": [
    { "firstName": "Jack", "lastName": "Jackson" }
  ]
}</code></pre>

<p>For each inmate object, the API posts the data to the Aiken County Sheriff’s Office inmate search page. If the response does <strong>not</strong> contain <code>"No records found"</code>, that inmate is considered a match and included in the response.</p>

<hr>

<h2 id="api-endpoints">API Endpoints</h2>

<h3><code>GET /</code></h3>

<p><strong>Description:</strong> Health/welcome endpoint.</p>

<p><strong>Response:</strong></p>

<pre><code class="language-json">{
  "message": "Welcome to the Inmate Search API. Use /check-inmate to search for inmates."
}</code></pre>

<hr>

<h3><code>POST /check-inmate</code></h3>

<p><strong>Description:</strong> Submit a list of inmates to check.</p>

<p><strong>Request Body:</strong></p>

<pre><code class="language-json">{
  "inmates": [
    { "firstName": "Kevin", "lastName": "McNasty" },
    { "firstName": "Adam", "lastName": "Jones" }
  ]
}</code></pre>

<p><strong>Response (example):</strong></p>

<pre><code class="language-json">{
  "found_inmates": [
    { "firstName": "Kevin", "lastName": "McNasty" },
    { "firstName": "Adam", "lastName": "Jones" }
  ],
  "status": "Inmates found"
}</code></pre>

<hr>

<h2 id="request--response-examples">Request &amp; Response Examples</h2>

<h3>cURL</h3>

<pre><code class="language-bash">curl --location --max-time 90 \
  --request POST "https://acdc-api.onrender.com/check-inmate" \
  --header "Content-Type: application/json" \
  --data "{
    \"inmates\": [
      { \"firstName\": \"Jack\", \"lastName\": \"Jackson\" }
    ]
  }"</code></pre>

<h3>Sample Responses (from <code>Responses/</code>)</h3>

<p>Two example response formats exist in the repo:</p>

<pre><code class="language-json">{
  "found_inmates": [
    { "firstName": "Kevin", "lastName": "McNasty" },
    { "firstName": "Adam", "lastName": "Jones" }
  ],
  "status": "Inmates found"
}</code></pre>

<pre><code class="language-json">{
  "found_inmates": [
    { "firstName": "Kevin", "lastName": "McNasty" },
    { "firstName": "Adam", "lastName": "Jones" }
  ],
  "status": "Inmates found., "
}</code></pre>

<hr>

<h2 id="running-locally">Running Locally</h2>

<h3>1) Install dependencies</h3>

<pre><code class="language-bash">pip install -r requirements.txt</code></pre>

<h3>2) Start the API</h3>

<pre><code class="language-bash">python acdc-api.py</code></pre>

<p>By default Flask runs at: <code>http://127.0.0.1:5000</code></p>

<h3>3) Test locally</h3>

<pre><code class="language-bash">curl -X POST http://127.0.0.1:5000/check-inmate \
  -H "Content-Type: application/json" \
  -d '{"inmates":[{"firstName":"Kevin","lastName":"McNasty"}]}'</code></pre>

<hr>

<h2 id="deployment">Deployment</h2>

<p>The repository includes <code>gunicorn</code> in <code>requirements.txt</code>, so you can deploy using a WSGI server:</p>

<pre><code class="language-bash">gunicorn acdc-api:app</code></pre>

<p>Example hosting platforms: Render, Railway, Heroku, or any VPS with Python.</p>

<hr>

<h2 id="postman-collection">Postman Collection</h2>

<p>A Postman collection is available at:</p>

<pre><code>Postman API/ACDC API Request.postman.json</code></pre>

<p>It includes:</p>

<ul>
  <li>Pre-request script to build the JSON body</li>
  <li>Tests that validate HTTP status and response structure</li>
  <li>A visualizer for displaying results in a table</li>
</ul>

<hr>

<h2 id="project-structure">Project Structure</h2>

<pre><code>.
├── acdc-api.py                 # Flask app / API logic
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── Responses/                  # Sample JSON responses
└── Postman API/                # Postman collection + scripts</code></pre>

<hr>

<h2 id="dependencies">Dependencies</h2>

<ul>
  <li><strong>Flask</strong> – web framework</li>
  <li><strong>requests</strong> – HTTP client</li>
  <li><strong>gunicorn</strong> – production WSGI server</li>
</ul>

<hr>

<h2 id="notes--limitations">Notes &amp; Limitations</h2>

<ul>
  <li>This API depends on the <strong>HTML responses</strong> of the Aiken County Sheriff’s Office inmate search site. If the site changes its structure or response messages, this API may stop working or give incorrect results.</li>
  <li>The logic currently checks for <code>"No records found"</code> in the response HTML. If that phrase changes, results may be inaccurate.</li>
  <li>For large input lists, each inmate is checked sequentially (no parallelization).</li>
</ul>

<hr>

<h2 id="license">License</h2>

<p>See the <a href="https://github.com/ryanshatch/ACDC-API/tree/main?tab=License-1-ov-file">License</a> file for details.</p>

<!-- <code>curl --location --max-time 90 --request POST "https://acdc-api.onrender.com/check-inmate" --header "Content-Type: application/json" --data "{\"inmates\":[{\"firstName\":\"Jack\",\"lastName\":\"Jackson\"}]}"
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
	"https://acdc-api.onrender.com/check-inmate"</code> -->
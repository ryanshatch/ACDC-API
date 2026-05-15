# ACDC-API

A small Flask API that checks whether specified individuals appear in the Aiken County Sheriff’s Office inmate search system. Clients send a list of inmates (first/last names) to the API, which submits each entry to the county search endpoint and returns the subset that appear to be found.

> **Note**: This project performs automated lookups against the Aiken County Sheriff’s Office inmate search page. Ensure your usage complies with the site’s terms of service and applicable laws.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [API Endpoints](#api-endpoints)
- [Request & Response Examples](#request--response-examples)
- [Running Locally](#running-locally)
- [Deployment](#deployment)
- [Postman Collection](#postman-collection)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Notes & Limitations](#notes--limitations)
- [License](#license)

---

## Features

- **Simple JSON API** for inmate lookup by first and last name.
- **Batch input**: submit multiple inmates in a single request.
- **Minimal dependencies**: Flask + requests.
- **Postman collection** included for quick testing.
- **Sample responses** stored in the `Responses/` folder.

---

## How It Works

The `/check-inmate` endpoint accepts a JSON payload like:

```json
{
  "inmates": [
    { "firstName": "Jack", "lastName": "Jackson" }
  ]
}
```

For each inmate object, the API posts the data to the Aiken County Sheriff’s Office inmate search page. If the response does **not** contain `"No records found"`, that inmate is considered a match and included in the response.

---

## API Endpoints

### `GET /`
**Description:** Health/welcome endpoint.

**Response:**
```json
{
  "message": "Welcome to the Inmate Search API. Use /check-inmate to search for inmates."
}
```

---

### `POST /check-inmate`
**Description:** Submit a list of inmates to check.

**Request Body:**
```json
{
  "inmates": [
    { "firstName": "Kevin", "lastName": "McNasty" },
    { "firstName": "Adam", "lastName": "Jones" }
  ]
}
```

**Response (example):**
```json
{
  "found_inmates": [
    { "firstName": "Kevin", "lastName": "McNasty" },
    { "firstName": "Adam", "lastName": "Jones" }
  ],
  "status": "Inmates found"
}
```

---

## Request & Response Examples

### cURL
```bash
curl --location --max-time 90 \
  --request POST "https://acdc-api.onrender.com/check-inmate" \
  --header "Content-Type: application/json" \
  --data "{
    \"inmates\": [
      { \"firstName\": \"Jack\", \"lastName\": \"Jackson\" }
    ]
  }"
```

### Sample Responses (from `Responses/`)
Two example response formats exist in the repo:

```json
{
  "found_inmates": [
    { "firstName": "Kevin", "lastName": "McNasty" },
    { "firstName": "Adam", "lastName": "Jones" }
  ],
  "status": "Inmates found"
}
```

```json
{
  "found_inmates": [
    { "firstName": "Kevin", "lastName": "McNasty" },
    { "firstName": "Adam", "lastName": "Jones" }
  ],
  "status": "Inmates found., "
}
```

---

## Running Locally

### 1) Install dependencies
```bash
pip install -r requirements.txt
```

### 2) Start the API
```bash
python acdc-api.py
```

By default Flask runs at: `http://127.0.0.1:5000`

### 3) Test locally
```bash
curl -X POST http://127.0.0.1:5000/check-inmate \
  -H "Content-Type: application/json" \
  -d '{"inmates":[{"firstName":"Kevin","lastName":"McNasty"}]}'
```

---

## Deployment

The repository includes `gunicorn` in `requirements.txt`, so you can deploy using a WSGI server:

```bash
gunicorn acdc-api:app
```

Example hosting platforms: Render, Railway, Heroku, or any VPS with Python.

---

## Postman Collection

A Postman collection is available at:

```
Postman API/ACDC API Request.postman.json
```

It includes:
- Pre-request script to build the JSON body
- Tests that validate HTTP status and response structure
- A visualizer for displaying results in a table

---

## Project Structure

```
.
├── acdc-api.py                 # Flask app / API logic
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── Responses/                  # Sample JSON responses
└── Postman API/                # Postman collection + scripts
```

---

## Dependencies

- **Flask** – web framework
- **requests** – HTTP client
- **gunicorn** – production WSGI server

---

## Notes & Limitations

- This API depends on the **HTML responses** of the Aiken County Sheriff’s Office inmate search site. If the site changes its structure or response messages, this API may stop working or give incorrect results.
- The logic currently checks for `"No records found"` in the response HTML. If that phrase changes, results may be inaccurate.
- For large input lists, each inmate is checked sequentially (no parallelization).

---

## License

See the [License](https://github.com/ryanshatch/ACDC-API/tree/main?tab=License-1-ov-file) file for details.

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

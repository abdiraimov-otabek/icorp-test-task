# Test API Code Concatenation Script

This is a single-file Python script that demonstrates **HTTP communication and data handling** by interacting with a test API.

---

## Features

* Sends a **POST request** with a message and your receiving URL.
* Receives **part1** from the API response.
* Waits for **part2** sent by the API to your endpoint.
* Combines **part1 + part2** into a full code.
* Sends a **GET request** with the combined code to retrieve the original message.
* Fully implemented in **one Python file**.

---

## Requirements

* Python 3.8+
* `requests` library

```bash
pip install requests
```

* Optional: **ngrok** or another public tunnel if you run a local server.

---

## Setup & Usage

1. **Start ngrok** (if using local server):

```bash
ngrok http 8000
```

Copy the HTTPS URL from the “Forwarding” line.

2. **Edit the script** `task.py`:

```python
PUBLIC_URL = "https://<your-ngrok-id>.ngrok-free.app"
```

3. **Run the script**:

```bash
python3 task.py
```

4. **Output**:

```
Part 1 received: <part1>
Part 2 received: <part2>
Combined code: <part1+part2>
Final Message: <your original message>
```

---

## Notes

* The script uses Python’s built-in `http.server` to receive `part2`.
* Make sure ngrok (or any public tunnel) is running **before** executing the script.
* Fully self-contained, demonstrates working with **POST, GET, and JSON processing**.

---

## Author

Otabek Abdiraimov

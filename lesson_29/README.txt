## 🚀 How to Run the Project in Docker

### 1. Go to the project folder:
```bash
cd lesson_29
```

### 2. Build and run everything:
```bash
docker compose up --build
```
This will:
- Start PostgreSQL (`db` service)
- Run the test suite in a Python container (`math-app` service)
- Log results to `test_log.txt`

### 3. Shut down after tests complete:
```bash
docker compose down
```

## 🧪 What’s Tested?
- Database connection
- Insert, update, fetch, delete from DB
- Math logic (add, subtract, multiply, divide)

Logs are written to `test_log.txt` with timestamps and details.
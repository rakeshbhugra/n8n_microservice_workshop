```bash
pip install fastapi uvicorn
```

How to run the app
```python
uvicorn main:app --reload --host 0.0.0.0 --port 4001
```

How to test the API
```bash
# Test root endpoint
curl http://localhost:4001/

# Test webhook endpoint
curl -X POST http://localhost:4001/webhook \
  -H "Content-Type: application/json" \
  -d '{"aqi_level": "moderate", "warning_message": "Air quality is acceptable"}'
```
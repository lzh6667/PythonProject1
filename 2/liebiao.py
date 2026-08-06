api_logs = [
    {"status": 200, "tokens": 150},
    {"status": 500, "tokens": 0},
    {"status": 200, "tokens": 320}
]
successful_tokens=[suc["tokens"] for suc in api_logs if suc["status"] == 200]
print(successful_tokens)
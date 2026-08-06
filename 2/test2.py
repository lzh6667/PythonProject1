tool_result = {
    "tool_name": "weather_api",
    "status_code": 200,
    "data": {
        "city": "Beijing",
        "forecast": [
            {"day": "Today", "temp": "25C", "condition": "Sunny"},
            {"day": "Tomorrow", "temp": "22C", "condition": "Rainy"}
        ]
    }
}
tomorrow_temp=tool_result["data"]["forecast"][-1]["temp"]
err=tool_result.get("error_msg","No Error")
print(err)
print(tomorrow_temp)
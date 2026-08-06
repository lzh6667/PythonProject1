action_logs = [
    {"tool": "search", "status": "success"},
    {"tool": "calculator", "status": "failed"},
    {"tool": "search", "status": "success"},
    {"tool": "weather", "status": "success"},
    {"tool": "calculator", "status": "success"}
]
successful_tools=(suc["tool"]for suc in action_logs if suc["status"] == "success")
unique_tools=(set(successful_tools))
print(unique_tools)
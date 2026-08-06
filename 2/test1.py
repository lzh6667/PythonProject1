chat_history = [
    {"role": "user", "content": "你好", "tokens": 5},
    {"role": "assistant", "content": "你好！有什么可以帮您？", "tokens": 12},
    {"role": "user", "content": "帮我查一下北京的天气", "tokens": 10},
    {"role": "system", "content": "系统指令：忽略前文", "tokens": 8}
]
user_messages=[str["content"] for str in chat_history if str["role"] == "user"]
print(user_messages)

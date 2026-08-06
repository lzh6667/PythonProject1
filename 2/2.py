from random import choice

api_response = {
    "model_name": "gpt-4o",
    "choices": [
        {"role": "assistant", "content": "你好，我是 AI 助手！"},
        {"role": "assistant", "content": "今天天气很好，适合出门。"}
    ]
    # 注意：该字典中没有 "usage" 这个键
}
usage_info=api_response.get("usage",{"total_tokens": 0})
last_content=api_response["choices"][-1]["content"]
print(last_content)
print(usage_info)
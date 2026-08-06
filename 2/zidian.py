
tool_info={
    "name":"calculator",
    "description":"用于执行加减乘除数学运算",
    "is_active": True
}

timeout_val=tool_info.get("timeout",30)
print(timeout_val)
tool_info["is_active"]=False
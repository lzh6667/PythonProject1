tokens=100
task=False
for attempt in range(1,6):
    tokens=tokens-18
    print(f"第{attempt}次尝试，剩余Token:{tokens}")
    if tokens<40:
        print(f"Token 余额不足，触发保护机制终止循环！")
        break
    if attempt==3:
         task=True
         print("🎉 任务在第 3 次尝试时执行成功！")
         break
if task:
    print("最终结论：Agent 顺利完成任务！")
else:
    print( "最终结论：Agent 任务未完成。")
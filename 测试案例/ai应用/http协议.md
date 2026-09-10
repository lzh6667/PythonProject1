## 响应数据格式

```
HTTP/1.1 200                     相应行（协议，状态码）  
Server:nginx/1.24.0           响应头（格式key：value）
Date:Tue，16 Dec 2025 12:38:08 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
[code:1, msg:'success",data: null}    响应体（存放响应的数值）
```
### 常见的几种状态码
**200：客户端请求成功**
**400：请求参数错误**
**404：请求资源不存在，url输入有误，或者网站资源被删除了**
**500：服务器发生了不可预期的错误**
## 请求数据格式
```
POST /api/courses HTTP/1.1       请求行（请求方式，资源路径，协议）         
Accept: application/json, text/plain, */*
Accept-Encoding: gzip,deflate,br,zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length:139
Content-Type: application/json
Host:localhost:90
Origin: http://localhost:90Referer:http://localhost:9o/resource/courseSec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent:Mozilla/5.0 (Windows NT 10.0;Win64;x64) Chrome/143.0.0.0                           //请求头
{"phone':"18808088080","channel":1, "name":"咆","gender":1,"age":"32"}     请求体（请求参数部分get 方式没有 post才可以有）
```
### GET和POST的区别
**依据我的主要看法 他们两者的主要区别是**
**GET请求参数在请求行中  请求大小有限制**
**POST的请求参数在请求体中  请求大小没有限制**

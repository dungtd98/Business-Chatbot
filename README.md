# Business-Chatbot
### 1. Tạo .env file
Thêm vào .env file
```
  SECRECT_KEY = '<YOUR_SECRECT_KEY>'
  SALT_STRING = '<YOUR_SALT_STRING>'
```

### 2. Tạo access_token
Sử dụng admin account POST request đến http://127.0.0.1:8000/token/ với request body như sau:
```
{
    "api_key": "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",
    "hostdomain": "OPENAI"
} 
```
### 3. Lấy encrypted token
Gửi GET request đến http://127.0.0.1:8000/token/user-access-token/ thêm host_domain params vào request:
```
host_domain = <DOMAIN_EXIST_IN_DB>
```
Response nhận về token ngẫu nhiên từ các api_key liên kết đến domain đó như sau:
```
{
    "id": 2,
    "hostdomain": "OPENAI",
    "access_token":"b'gA...=='"
}

```

### 4. Gửi request đến domain
Gửi POST request đến http://127.0.0.1:8000/api/ với request body:

```
{
  "host_domain":"Tên domain",
  "request_method":"Method",
    "body":{
      <Nội dung request body đến domain>
            }
}
```
Ví dụ:
```
{
  "host_domain":"https://api.openai.com/v1/completions",
  "request_method":"POST",
  "body":{
    "model": "text-davinci-003",
    "prompt": "Hello, bạn có thể miêu tả con mèo ko?",
    "max_tokens": 100,
    "temperature": 0.5,
    "top_p": 1,
    "stream": false,
    "stop": "."
          }
}
```
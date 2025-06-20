#!/bin/sh

url="https://api.chatfire.cn/v1"
sk="sk-zO8exlBicZh7nJeZn5GuC5X9SPuVrZzXoGyOW0i9BFvN62ON"

curl "${url}/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: ${sk}" \
    -d '{
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "developer",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Hello!"
                }
            ],
            "stream": true
        }'


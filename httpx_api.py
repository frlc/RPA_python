from httpx import get, post

response = post('https://www.google.com.br')
print(response.text)

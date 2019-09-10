import requests

headers = {}

headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY4MDY2MDU4LCJqdGkiOiI4ZjM4NmFiN2Q1OGQ0MzM4YTcxOTNkM2RmNjBlMDBjMyIsInVzZXJfaWQiOjF9.7DTr_n2oQk9Sr2Tzoky-lnfk1pVY8VcEztkPi6NFp7w'

r = requests.get('http://127.0.0.1:8000/paradigms', headers =headers )

print(r.text)
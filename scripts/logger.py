import requests
import time

nanoseconds = time.time_ns()

payload = {
	"streams": [{
		"stream": {
			"server": "backend-01",
			"app": "blog-01"
		},
		"values": [
			[str(nanoseconds), "Lorem ipsum dolor sit amet, consectetur adipiscing elit."]
		]
	}]
}

print(payload)

r = requests.post('http://loki:3100/loki/api/v1/push', json=payload)

print(r.status_code)
print(r.content)
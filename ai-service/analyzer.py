import requests

PROMETHEUS_URL = "http://localhost:9090"

def get_cpu_usage():
    query = "rate(container_cpu_usage_seconds_total[1m])"
    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": query}
    )
    return response.json()

def get_requests():
    query = "rate(app_requests_total[1m])"
    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": query}
    )
    return response.json()

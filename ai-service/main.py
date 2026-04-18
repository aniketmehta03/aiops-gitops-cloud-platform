from strands import Agent
from strands.models.ollama import OllamaModel
from analyzer import get_cpu_usage, get_requests

# Initialize model
model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3"
)

agent = Agent(model=model)

def analyze():
    cpu = get_cpu_usage()
    req = get_requests()

    prompt = f"""
    Analyze the following Kubernetes metrics:

    CPU:
    {cpu}

    Request Rate:
    {req}

    Provide:
    - Issue
    - Reason
    - Solution
    """

    result = agent(prompt)
    print(result)

if __name__ == "__main__":
    analyze()

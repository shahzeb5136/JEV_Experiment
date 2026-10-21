"""
Quick test of a Vercel AI Gateway API key against Jev (typesafe-ai/jev).

Setup:
    pip install requests
    export AI_GATEWAY_API_KEY="your-key-here"      # macOS / Linux
    setx AI_GATEWAY_API_KEY "your-key-here"        # Windows (then reopen the terminal)

Run:
    python main.py
"""

import json
import os
import sys

import requests

API_KEY = os.environ.get("AI_GATEWAY_API_KEY")
if not API_KEY:
    sys.exit("AI_GATEWAY_API_KEY is not set. Please set the AI_GATEWAY_API_KEY environment variable.")

URL = "https://ai-gateway.vercel.sh/v1/evaluate"

payload = {
    "model": "typesafe-ai/jev",
    "state": "I was charged twice for my subscription and I want my money back.",
    "questions": {
        # Boolean: returns a probability between 0 and 1
        "wants_refund": {
            "type": "boolean",
            "instructions": "Is the customer asking for money back?",
        },
        # Choice: picks one option and gives a probability for each
        "route": {
            "type": "choice",
            "instructions": "Route this support ticket.",
            "criteria": {
                "billing": "payment or charge problems",
                "shipping": "delivery problems",
                "technical": "application bugs",
            },
        },
        # Score: rates along an ordered scale (lowest to highest)
        "urgency": {
            "type": "score",
            "instructions": "How urgent is this ticket?",
            "criteria": ["low", "medium", "high"],
        },
    },
}

resp = requests.post(
    URL,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    json=payload,
    timeout=30,
)

print(f"HTTP {resp.status_code}")

if resp.status_code == 401:
    sys.exit("401: the key was rejected. Re-check AI_GATEWAY_API_KEY.")
if resp.status_code == 402:
    sys.exit("402: no credits. Add credits or a payment method in Vercel (Budgets & Spend).")
if not resp.ok:
    sys.exit(f"Request failed:\n{resp.text}")

data = resp.json()
print("\nAnswers:")
print(json.dumps(data.get("answers"), indent=2))
print("\nUsage:", data.get("usage"))
cost = data.get("providerMetadata", {}).get("gateway", {}).get("cost")
print("Cost:", cost)
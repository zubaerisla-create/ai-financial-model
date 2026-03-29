import requests
import json

url = "http://127.0.0.1:8000/api/simulate/"
data = {
    "monthlyIncome": 5000,
    "rent": 1200,
    "utilities": 200,
    "subscriptionsInsurance": 100,
    "existingLoans": 300,
    "variableExpenses": 800,
    "currentSavings": 10000,
    "dependents": 0,
    "householdResponsibilityLevel": "half",
    "incomeStability": "very_stable",
    "riskTolerance": "safe",
    "purchaseAmount": 2000,
    "paymentType": "full"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

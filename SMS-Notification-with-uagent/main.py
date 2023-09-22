from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests

class Message(Model):
    message: str 

currency_agent = Agent(
    name="currency_agent",
    port=8000,
    seed="currency_secret_phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(currency_agent.wallet.address())

# Define the base currency for surveillance
base_currency = input("Enter the base currency (e.g., USD): ").upper()

# Prompt the user for target currencies and their desired minimum and maximum values
target_currencies = {}
num_targets = int(input("Enter the number of target currencies: "))
for i in range(num_targets):
    target_currency = input(f"Enter target currency {i + 1} (e.g., EUR): ").upper()
    min_value = float(input(f"Enter the desired minimum value for {target_currency}: "))
    max_value = float(input(f"Enter the desired maximum value for {target_currency}: "))
    target_currencies[target_currency] = {"min": min_value, "max": max_value}

API_URL = f"https://v6.exchangerate-api.com/v6/{YOU_API_KEY_HERE}/latest/{base_currency}"

def get_exchange_rates(base_currency):
    try:
        response = requests.get(API_URL)
        data = response.json()
        
        if response.status_code == 200:
            return data['conversion_rates']
        else:
            print(f"Failed to fetch exchange rates. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching exchange rate data: {e}")
        return None

def monitor_exchange_rates():
    exchange_rates = get_exchange_rates(base_currency)
    if exchange_rates is not None:
        alerts = []
        for currency, limits in target_currencies.items():
            rate = exchange_rates.get(currency)
            if rate is not None:
                if rate < limits["min"]:
                    alerts.append(f"{currency} rate is below the desired minimum ({limits['min']}).")
                elif rate > limits["max"]:
                    alerts.append(f"{currency} rate is above the desired maximum ({limits['max']}).")
                # else:
                #     alerts.append(f"{currency} rate is within the desired minimum ({limits['min']} and desired maximum ({limits['max']}))")
        return alerts
    else:
        return []
async def notify_user(alert):

    for message in alert:
        servicePlanId = "YOUR_SERVICE_PLAN_ID_HERE"
        apiToken = "YOUR_API_TOKRN_HERE"
        sinchNumber = "YOUR_SINCH_NUMBER_HERE"
        toNumber = "USERS_NUMBER_HERE"
        url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

        payload = {
        "from": sinchNumber,
        "to": [
            toNumber
        ],
        "body": message
        }
        headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiToken
        }

        response = requests.post(url, json=payload, headers=headers)

        data = response.json()
        print(data)

@currency_agent.on_interval(period=3600.0)  # Check every hour
async def currency_monitor(ctx: Context):
    alerts = monitor_exchange_rates()
    ctx.logger.info(alerts)
    if alerts:
        await notify_user(alerts)

if __name__ == "__main__":
    currency_agent.run()

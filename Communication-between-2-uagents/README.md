# Currency Monitoring Agent - Remote communication between two uAgents  🌡️📲

This repository contains a Currency Monitoring Agent that checks the currency in a selected location and sends a text message notification to the user if the currency falls below or rises above the user's desired currency range. This project was developed for the [Fetch.ai Hackathon](https://lu.ma/fetchai-hackathon) organized by [Fetch.ai](https://fetch.ai/).

## Getting Started 🚀

To use the Currency Monitoring Agent which can communicate remotely, follow these steps:

### Step 1: Obtain API Keys 🔑

Before running the agent, you need to obtain the required API keys:

- **Exchange Rate API Key:** Get an API key from OpenWeatherMap by signing up at [Exchange Rate API](https://v6.exchangerate-api.com).

### Step 2: Set Environment Variables 🌐

Create a `.env` file in the project directory and export the obtained API keys as environment variables:

```shell
export EXCHANGE_RATE_API_KEY="YOUR_EXCHANGE_RATE_API_KEY"
export SINCH_API_TOKEN="YOUR_SINCH_API_TOKEN"
```

### Step 3: Install Dependencies ⚙️

To use the environment variables from the .env file and install the project dependencies, run the following commands:

```shell
source .env
poetry install
```

### Step 4: Run the Agent 🏃

To run the Currency Monitoring Agent:

```shell 
python currency-agent.py
python agent-bob.py
```

- **Enter the Currency you want as a base currency.**
- **Enter your currencies you want to be observed with their minimum and maximum values respectively.**
- **Now, the agent will periodically check the currency from the selected observable currencies and send bob(uAgent) a message on remote server if it falls below or rises above your desired currency value range.**

### Example Usage

Here's an example of how to use the Temperature Monitoring Agent:

- **Enter the base currency (e.g., USD): USD**
- **Enter the number of target currencies: 1**
- **Enter target currency 1 (e.g., EUR): INR**
- **Enter the desired minimum value for INR: 70** 
- **Enter the desired maximum value for INR: 80**
- **The agent will periodically check the currency from the selected currencies.**
- **If the currency falls below or rises above your desired range, you will receive a text message notification.**

Now you can stay informed about currency changes in your selected currencies!

Enjoy monitoring currencies with remote communication functionality! 🌡️📲

## Video Explanation 🎥

For a more detailed overview and step-by-step walkthrough of the projects included in this repository, watch our video explanation below:

Youtube Link: https://demo-link.org

Gdrive Link: https://demo-link.org

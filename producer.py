# producer.py
"""
This script generates fake Bitcoin price data.
It prints one price update every second.
"""

import time
import random
import json
from datetime import datetime

# Function to generate one price tick
def generate_tick(symbol="BTCUSD"):
    # Price around 40,000 with random +/- changes
    price = round(40000 + random.uniform(-300, 300), 2)

    # Current time in UTC format
    ts = datetime.utcnow().isoformat() + "Z"

    # Return the data as a dictionary
    return {
        "symbol": symbol,
        "price": price,
        "timestamp": ts
    }


# Run the generator continuously
if __name__ == "__main__":
    while True:
        tick = generate_tick()
        print(json.dumps(tick))  # Convert to text and print
        time.sleep(1)  # Pause 1 second before next tick

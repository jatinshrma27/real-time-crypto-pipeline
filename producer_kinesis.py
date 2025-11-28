# producer_kinesis.py
"""
This script generates fake Bitcoin price data
and sends it to a Kinesis Data Stream every second.
"""

import time
import random
import json
from datetime import datetime
import boto3

# Connect to AWS Kinesis
kinesis = boto3.client('kinesis', region_name="ap-south-1")

STREAM_NAME = "price-ticks"   # exact name from Step 2

# Function to generate one fake price tick
def generate_tick(symbol="BTCUSD"):
    price = round(40000 + random.uniform(-300, 300), 2)
    ts = datetime.utcnow().isoformat() + "Z"

    return {
        "symbol": symbol,
        "price": price,
        "timestamp": ts
    }


# Main loop: send 1 record per second
if __name__ == "__main__":
    while True:
        tick = generate_tick()

        # Send to AWS Kinesis
        response = kinesis.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(tick),
            PartitionKey=tick["symbol"]  # simple key to group data
        )

        print("Sent:", tick)
        time.sleep(1)

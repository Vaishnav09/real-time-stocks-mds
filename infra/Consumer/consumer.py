#Import requirements
import json
import boto3
import time
from kafka import KafkaConsumer

#connection to s3/Minio
s3 = boto3.client(
    "s3",
    endpoint_url = "http://localhost:9002",
    aws_access_key_id = "ACCOUNT_ACCESS_KEY",
    aws_secret_access_key="YOUR_PASSWORD"
)

bucket_name = "transactions"

#Defined the Consumer
consumer = KafkaConsumer(
    "stock-quotes",
    bootstrap_servers = ["localhost:29092"],
    enable_auto_commit = True,
    auto_offset_reset = "earliest",
    group_id="bronze-consumer1",
    value_deserializer = lambda v:json.loads(v.decode("utf-8"))
)

print("consumer streaming and saving to s3...")

#Main Function
for message in consumer:
    record = message.value
    symbol = record.get("symbol")
    ts = record.get("fetched_at")
    if ts is None:
        ts = int(time.time())
    key = f"{symbol}/{ts}_{message.offset}.json"

    s3.put_object(
        Bucket = bucket_name,
        Key=key,
        Body = json.dumps(record),
        ContentType = "application/json"
    )
    print(f"Saved record for {symbol} = s3://{bucket_name}/{key}")
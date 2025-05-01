import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

kinesis = boto3.client("kinesis")

STREAM_NAME = "E-commerce-RTL-pipeline"

REQUIRED_FIELDS = [
    "invoice", "stock_code", "description", "quantity", 
    "timestamp", "price", "customer_id", "country", 
    "year", "month"
]

def lambda_handler(event, context):
    try:
        raw_body = event.get("body")
        if not raw_body:
            logger.error("No body found in request.")
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing request body"})
            }

        data = json.loads(raw_body)

        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            logger.error(f"Missing fields: {missing}")
            return {
                "statusCode": 400,
                "body": json.dumps({"message": f"Missing fields: {missing}"})
            }

        data["quantity"] = int(data["quantity"])
        data["price"] = float(data["price"])
        data["year"] = int(data["year"])
        data["month"] = int(data["month"])

        # Send to Kinesis
        response = kinesis.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(data),
            PartitionKey=str(data["customer_id"])
        )

        logger.info(f"Record sent: {response['SequenceNumber']}")
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Success", "sequence_number": response["SequenceNumber"]})
        }

    except Exception as e:
        logger.exception("Error during processing")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error", "error": str(e)})
        }

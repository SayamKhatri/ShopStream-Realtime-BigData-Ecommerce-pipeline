# ShopStream-Realtime-BigData-Ecommerce-pipeline

A scalable, cloud-native data pipeline designed to process over **1 million e-commerce transactions per minute** using AWS services. This architecture ensures real-time data ingestion, processing, and analytics, leveraging AWS components such as API Gateway, Kinesis, Lambda, S3, SQS, and Snowflake.


## Overview

**ShopStream** is engineered to handle high-throughput e-commerce data, ensuring real-time processing and analytics. The pipeline captures transactional data via API Gateway, streams it through Kinesis, processes it with Lambda functions, stores raw data in S3, queues messages with SQS, and performs analytics using Snowflake. This setup facilitates immediate insights into user behavior, sales trends, and system performance.


## Architecture

![Application](https://github.com/user-attachments/assets/9516fb8a-1a9e-4248-a692-0f9d58e826b7)


The pipeline's architecture comprises the following AWS services:

1. **API Gateway**: Serves as the entry point for incoming e-commerce transaction data.
2. **Kinesis Data Streams**: Ingests and buffers real-time data for processing.
3. **AWS Lambda**: Processes streaming data, performs transformations, and routes data accordingly.
4. **Amazon S3**: Stores raw and processed data for archival and batch processing needs.
5. **Amazon SQS**: Queues messages for asynchronous processing and ensures decoupling between services.
6. **Snowflake**: Provides a scalable data warehouse for complex analytics and reporting.


## Data Flow

1. **Transaction Submission**: Clients send transaction data to API Gateway.
2. **Streaming**: API Gateway forwards the data to Kinesis Data Streams.
3. **Processing**: Lambda functions consume data from Kinesis, transform it, and route it to S3 and SQS.
4. **Storage**:
   - Transformed data is stored in S3 for archival.
   - Messages are queued in SQS for further processing.
5. **Analytics**: Data is loaded into Snowflake for real-time analytics and reporting. 


## Monitoring & Logging

- **AWS CloudWatch**: Monitors Lambda functions, Kinesis streams, and API Gateway for performance metrics and logs.
- **Snowflake Monitoring**: Utilize Snowflake's Query History and Performance dashboards to monitor query performance and warehouse utilization.


## Security & Compliance

- **Data Encryption**:
  - Data at rest in S3 and Snowflake is encrypted using AWS KMS and Snowflake's encryption mechanisms.
  - Data in transit is secured using HTTPS and SSL/TLS protocols.
- **Access Control**:
  - IAM roles and policies restrict access to AWS resources.
  - Snowflake roles and permissions manage access to data warehouses and databases.
- **Compliance**:
  - Ensure compliance with data protection regulations like GDPR and CCPA by implementing data masking and access auditing in Snowflake.


## License

This project is licensed under the MIT License.


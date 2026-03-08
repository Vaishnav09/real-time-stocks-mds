# Real-Time Stock Market Data Pipeline

## Overview

This project implements an end-to-end real-time data pipeline that ingests live stock market data, processes it using a modern data stack, and delivers analytics-ready insights.

The pipeline streams stock data through Apache Kafka, stores raw data in MinIO object storage, orchestrates ingestion with Apache Airflow, transforms the data using dbt, and loads it into Snowflake for analytical querying and visualization in Power BI.

This project demonstrates how modern data engineering systems convert raw streaming data into structured analytics for business insights.

---

## Architecture

The pipeline follows a modern data stack architecture designed for scalable and automated data processing.

<img width="1035" height="540" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/7b35ca8a-1f1d-4d2a-a8d6-15ca3c92b8a5" />

---

## Tech Stack

| Layer | Technology |
|------|------------|
| Data Ingestion | Python |
| Streaming | Apache Kafka |
| Workflow Orchestration | Apache Airflow |
| Object Storage | MinIO |
| Data Warehouse | Snowflake |
| Data Transformation | dbt |
| Visualization | Power BI |
| Infrastructure | Docker Compose |

---

## Data Pipeline Workflow

### 1. Data Ingestion (Producer)

A Python producer script fetches real-time stock data from the Finnhub API.

The producer:
- retrieves stock market data for selected companies
- attaches timestamps
- converts responses to JSON format
- streams data to a Kafka topic

Example stocks monitored:
- Apple (AAPL)
- Amazon (AMZN)
- Google (GOOGL)
- Microsoft (MSFT)
- Tesla (TSLA)

---

### 2. Event Streaming (Kafka)

Apache Kafka acts as the event streaming platform.

It buffers incoming stock events and enables scalable real-time ingestion while decoupling producers and consumers.

---

### 3. Data Storage (MinIO)

A Kafka consumer reads messages from the topic and writes them as JSON files into MinIO object storage.

MinIO functions as the raw data lake layer of the pipeline.

---

### 4. Data Orchestration (Airflow)

Apache Airflow manages pipeline execution through a Directed Acyclic Graph (DAG).

The DAG automatically:

1. detects new data in MinIO
2. loads raw files into Snowflake
3. triggers transformation workflows

This enables fully automated pipeline execution.

---

### 5. Data Warehouse (Snowflake)

Snowflake serves as the central analytics warehouse.

Raw JSON data is stored in a bronze table using the VARIANT data type, allowing efficient ingestion of semi-structured data.

---

### 6. Data Transformation (dbt)

dbt transforms raw warehouse data into structured analytics models using a medallion architecture.

#### Bronze Layer
Stores raw ingested JSON data.

Example table:

```
stocks_bronze_raw
```

#### Silver Layer
Cleans and structures the data.

Transforms include:

- parsing JSON attributes
- extracting stock price fields
- formatting timestamps
- enforcing schema consistency

#### Gold Layer
Creates analytics-ready views for reporting.

Examples include:

- latest stock price KPIs
- open/high/low/close metrics
- daily price movements
- volatility analysis

---

### 7. Data Visualization (Power BI)

Power BI connects directly to Snowflake using DirectQuery.

This allows dashboards to retrieve real-time data without importing datasets locally.

Example insights include:

- real-time stock price indicators
- price change percentages
- volatility comparisons
- candlestick trend charts

---

## Project Structure

```
real-time-stocks-mds
│
├── infra
│   ├── producer
│   │   └── producer.py
│   │
│   ├── consumer
│   │   └── consumer.py
│   │
│   ├── dags
│   │   └── minio_to_snowflake.py
│   │
│   ├── plugins
│   └── docker-compose.yml
│
├── dbt_stocks
│   ├── models
│   │   ├── bronze
│   │   ├── silver
│   │   └── gold
│   │
│   ├── macros
│   ├── tests
│   ├── seeds
│   ├── snapshots
│   └── dbt_project.yml
│
├── Architecture Diagram.png
├── requirements.txt
└── README.md
```

---

## Key Features

- Real-time stock market data ingestion
- Event streaming using Apache Kafka
- Scalable object storage with MinIO
- Automated workflow orchestration with Airflow
- Layered data transformations using dbt
- Cloud analytics warehouse using Snowflake
- Interactive analytics dashboards in Power BI
- Fully containerized infrastructure using Docker Compose

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Vaishnav09/real-time-stocks-mds.git
cd real-time-stocks-mds
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start infrastructure

```bash
docker-compose up -d
```

This launches the following services:

- Kafka
- Zookeeper
- Airflow
- MinIO
- PostgreSQL

### 4. Run the producer

Start the Kafka producer to stream stock data.

### 5. Execute Airflow DAG

Trigger the Airflow DAG to load data from MinIO into Snowflake.

### 6. Run dbt transformations

```bash
dbt run
```

### 7. Connect Power BI

Connect Power BI to Snowflake using DirectQuery and build analytics dashboards.
---<img width="897" height="506" alt="Screenshot 2026-03-07 at 8 03 40 PM" src="https://github.com/user-attachments/assets/9fa2ba02-ec34-44ec-98c6-d5ecf055bdf6" />


## Security Notes

Sensitive credentials such as API keys and Snowflake credentials are excluded from this repository.

Users should configure credentials locally using environment variables or configuration files.

---

## Learning Outcomes

This project demonstrates:

- designing modern data pipelines
- streaming data processing
- data lake and warehouse architecture
- automated workflow orchestration
- scalable analytics transformation workflows
- building analytics-ready data models

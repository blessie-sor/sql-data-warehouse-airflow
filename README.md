# Sales Analytics Data Warehouse (PostgreSQL + Airflow)

## Overview
This project focuses on designing and implementing a modern **Data Warehouse** to consolidate sales data from multiple source systems into a single, analytics-ready platform. 
The solution transforms raw CSV data from operational systems into structured datasets that drive better business decision-making around customer behavior, product performance, and sales trends.

The warehouse follows a **Medallion Architecture (Bronze / Silver / Gold)** to ensure data quality, maintainability, and scalability. Originally built on SQL Server, the project was migrated to PostgreSQL for cross-platform compatibility and containerized with Docker, with pipeline orchestration added via Apache Airflow.


## Business Problem
Sales data is distributed across multiple operational systems, making it difficult for business and analytics teams to:
- Trust reported metrics
- Analyze customer and product performance consistently
- Identify sales trends over time

This project addresses these challenges by integrating ERP and CRM data into a unified model designed for reporting and insights.


## Architecture Overview

![Architecture](docs/data_architecture.png)

### Data Sources
- **ERP System** (CSV files)
- **CRM System** (CSV files)


### Architecture Pattern
- **Bronze Layer** – Raw data ingestion from CSV files
- **Silver Layer** – Cleansed and standardized data with data quality rules applied
- **Gold Layer** – Business-ready fact and dimension views implementing a star schema


### Pipeline Flow
```
CSV Files (CRM + ERP)
        ↓
Bronze Layer (raw ingestion)       ~60,000 records
        ↓
Silver Layer (cleansed data)       ~18,484 records
        ↓
Gold Layer (star schema views)     dim_customers, dim_products, fact_sales
```

## Data Modeling

![Schema](docs/database_schema.png)

The warehouse uses dimensional modeling to support analytical queries efficiently.

- **Fact View** – Sales transactions
- **Dimension Views** – Customers, Products

The star schema design:
- Simplifies analytical queries
- Improves query performance
- Provides consistent metric definitions across reporting use cases


## Data Quality & Transformation
To ensure reliable analytics, the following data quality steps are applied:
- Handling missing and invalid values
- Deduplication of records
- Standardization of keys and formats
- Validation of referential integrity between fact and dimension data


## ETL Process

![Data Flow](docs/data_flow.png)

1. **Extract** – Import raw CSV data from ERP and CRM systems into the Bronze layer
2. **Transform** – Cleanse and standardize data in the Silver layer, apply business rules
3. **Load** – Populate analytics-ready fact and dimension views in the Gold layer


## How to Run
Note: Credentials in this project are for local development only.

### Prerequisites
- Docker Desktop installed

### Steps
1. Clone the repo
```bash
   git clone https://github.com/blessie-sor/sql-data-warehouse-airflow.git
   cd sql-data-warehouse-airflow
```

2. Start the containers
```bash
   docker-compose up -d
```

3. Open Airflow at `http://localhost:8080`
   - Username: `airflow`
   - Password: `airflow`

4. Trigger the `medallion_pipeline` DAG


## Analytics & Reporting
The Gold layer supports SQL-based analytics for:
- Customer Behavior
- Product Performance
- Sales Trends

## Documentation
- Data model documentation
- Star schema design overview
- Table and column definitions
- Business metric descriptions


## Technologies Used
| Tool | Purpose |
|---|---|
| PostgreSQL | Data warehouse |
| Apache Airflow | Pipeline orchestration |
| Docker | Containerization |
| Python | Pipeline scripting |
| SQL | Data transformation |
| Medallion Architecture | Data organization pattern |
| Dimensional Modeling | Analytics-ready data structure |

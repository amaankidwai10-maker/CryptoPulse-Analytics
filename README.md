# CryptoPulse Analytics

A complete end-to-end cryptocurrency analytics project that extracts real-time market data from the CoinGecko API, processes and transforms the data using Python and Pandas, stores it in SQLite, and visualizes key market insights through an interactive Power BI dashboard.

---

## Project Overview

CryptoPulse Analytics was developed to demonstrate practical data analytics and business intelligence skills through a real-world data pipeline. Instead of relying on static datasets, the project retrieves live cryptocurrency market data directly from the CoinGecko API and transforms it into actionable insights.

The project covers the complete analytics workflow, including data extraction, transformation, storage, querying, and visualization.

---

## Objectives

- Collect live cryptocurrency market data using a public API
- Perform data cleaning and transformation using Python
- Store processed data in a relational database
- Build an interactive Power BI dashboard
- Generate insights on cryptocurrency market performance

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Extraction & Processing |
| Requests | API Integration |
| Pandas | Data Cleaning & Transformation |
| SQLite | Database Storage |
| SQL | Data Querying |
| Power BI | Dashboard Development |
| DAX | KPI Calculations & Analytics |

---

## Data Pipeline

```text
CoinGecko API
      ↓
Python Requests
      ↓
JSON Response
      ↓
Pandas DataFrame
      ↓
Data Cleaning & Transformation
      ↓
SQLite Database
      ↓
Power BI Dashboard
```

---

## Dashboard Features

### Key Performance Indicators (KPIs)

- Total Market Capitalization
- Total Trading Volume
- Total Cryptocurrencies Tracked
- Average 24-Hour Price Change

### Analytical Visualizations

- Top 10 Cryptocurrencies by Market Capitalization
- Top 10 Cryptocurrencies by Trading Volume
- Top 10 Gainers (24-Hour Performance)
- Top 10 Losers (24-Hour Performance)

### Interactive Capabilities

- Dynamic Filtering
- Cross-Visual Interaction
- Market Performance Analysis

---

## Dashboard Preview

![Dashboard Preview](screenshots/Dashboard.png)

---

## Project Structure

```text
CryptoPulse-Analytics/
│
├── Crypto_Analytics_Dashboard.pbix
├── crypto_pipeline.py
├── crypto_cleaned.csv
├── crypto_data.csv
├── requirements.txt
├── README.md
│
└── screenshots/
    └── Dashboard.png
```

---

## Data Source

This project uses the CoinGecko Public API to retrieve real-time cryptocurrency market data.

Source:
https://www.coingecko.com/en/api

---

## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CryptoPulse-Analytics.git
cd CryptoPulse-Analytics
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Data Pipeline

```bash
python crypto_pipeline.py
```

### 4. Open the Dashboard

Open:

```text
Crypto_Analytics_Dashboard.pbix
```

in Power BI Desktop.

---

## Workflow

1. Fetch cryptocurrency market data from the CoinGecko API.
2. Convert JSON responses into a Pandas DataFrame.
3. Clean and transform the dataset.
4. Export processed data to CSV.
5. Store cleaned data in SQLite.
6. Query and analyze the data.
7. Build interactive visualizations in Power BI.

---

## Skills Demonstrated

- API Integration
- Data Extraction
- Data Cleaning
- ETL Pipeline Development
- Database Management
- SQL Querying
- Data Modeling
- Business Intelligence
- Dashboard Design
- Data Visualization
- Power BI Development
- DAX Measures

---

## Future Enhancements

- Automated data refresh scheduling
- Historical trend analysis
- Additional cryptocurrency metrics
- Multi-source API integration
- Predictive analytics and forecasting
- Advanced Power BI reporting features

---

## Author

**Amaan Kidwai**

Aspiring Data Analyst | Python | SQL | Power BI | Data Analytics

---

## Project Highlights

- Live cryptocurrency data via API integration
- Automated ETL pipeline using Python
- Structured SQLite database implementation
- Interactive Power BI dashboard
- End-to-end analytics workflow
- Real-world business intelligence project

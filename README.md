## 📊 Retail Sales Analytics Dashboard (SQL + Python + Streamlit)

## 🚀 Project Overview

This project demonstrates a complete end-to-end data analytics workflow using SQL and Python. It involves loading raw CSV data into a database, performing advanced SQL analysis, and building an interactive dashboard for business insights.

---

## 🔄 Data Pipeline

CSV → SQLite Database → SQL Queries → Python Processing → Streamlit Dashboard

---

## 🎯 Key Features

* Data loading from CSV into SQLite database
* SQL-based data analysis and aggregation
* Advanced SQL queries (Window Functions, Ranking, Growth %)
* KPI Metrics (Revenue, Orders, Average Order Value)
* Interactive dashboard with filters
* Data visualization using Plotly

---

## 🛠️ Tech Stack

* Python (Pandas)
* SQL (SQLite)
* Visualization (Matplotlib, Plotly)
* Dashboard (Streamlit)

---

## 📁 Project Structure

```
sales-analytics-portfolio/
│
├── data/                
├── sql/                  
│   ├── schema.sql
│   ├── advanced_queries.sql
│
├── src/                  # Backend scripts
│   ├── load_data.py
│   ├── analysis.py
│
├── app/                  # Streamlit dashboard
│   └── dashboard.py
│
├── images/               # Output charts/screenshots
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sales-analytics-portfolio.git
cd sales-analytics-portfolio
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Load Data into Database

```bash
python src/load_data.py
```

### 4. Run the Dashboard

```bash
streamlit run app/dashboard.py
```

---

## 📊 Dashboard Features

* 📌 KPI Cards (Total Revenue, Total Orders, Average Order Value)
* 📈 Monthly Revenue Trend
* 🌍 Region-based filtering
* 🏆 Top-performing products

---

## 📈 Business Insights

* Identifies revenue growth trends over time
* Highlights top-performing products and categories
* Compares regional sales performance
* Calculates key business KPIs like AOV

---

## 🚀 Future Enhancements

* Deploy dashboard using Streamlit Cloud
* Integrate with PostgreSQL / MySQL
* Add sales forecasting using Machine Learning
* Automate data pipeline

---

## 📸 Output

* Charts saved in `images/` folder
* Dashboard provides real-time interactive insights

---

## 👨‍💻 Author

Prathmesh YadavPatil

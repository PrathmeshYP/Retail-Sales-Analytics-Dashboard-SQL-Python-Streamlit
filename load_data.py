import sqlite3
import pandas as pd

def load_data():
    try:
        conn = sqlite3.connect("sales.db")

        df = pd.read_csv("data/sales_data.csv")

        # Clean date format
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['order_date'] = df['order_date'].dt.strftime('%Y-%m-%d')

        df.to_sql("sales", conn, if_exists="replace", index=False)

        conn.commit()
        conn.close()

        print("✅ Data loaded successfully!")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    load_data()
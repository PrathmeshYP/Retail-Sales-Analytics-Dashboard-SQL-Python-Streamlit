import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_analysis():
    try:
        conn = sqlite3.connect("sales.db")

        os.makedirs("images", exist_ok=True)

        # Monthly Revenue
        query1 = """
        SELECT strftime('%Y-%m', order_date) AS month,
               SUM(quantity * price) AS revenue
        FROM sales
        GROUP BY month
        ORDER BY month;
        """

        df1 = pd.read_sql(query1, conn)

        plt.figure()
        sns.lineplot(x='month', y='revenue', data=df1)
        plt.title("Monthly Revenue Trend")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("images/monthly_trend.png")
        plt.close()

        # Top Products
        query2 = """
        SELECT product, SUM(quantity * price) AS revenue
        FROM sales
        GROUP BY product
        ORDER BY revenue DESC
        LIMIT 5;
        """

        df2 = pd.read_sql(query2, conn)

        plt.figure()
        sns.barplot(x='revenue', y='product', data=df2)
        plt.title("Top Products")
        plt.tight_layout()
        plt.savefig("images/top_products.png")
        plt.close()

        conn.close()
        print("✅ Analysis complete. Charts saved in /images")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    run_analysis()
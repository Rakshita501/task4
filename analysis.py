"""Task 4: End-to-end sales data analysis.

Place your sales CSV in this folder and name it sales.csv.
Expected columns: Date, Product, Quantity, Sales.
Edit COLUMN_MAP below if your CSV uses different headings.
"""
from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

HERE = Path(__file__).resolve().parent
CSV_FILE = HERE / "sales.csv"

# Change the values to match your CSV column headings, if needed.
COLUMN_MAP = {
    "Date": "Date",
    "Product": "Product",
    "Quantity": "Units Sold",
    "Sales": "Sales Amount",
}


def main():
    if not CSV_FILE.exists():
        print(f"Dataset not found: {CSV_FILE}")
        print("Download a sales CSV, copy it into this folder, and name it sales.csv.")
        sys.exit(1)

    df = pd.read_csv(CSV_FILE)
    print("Columns in your dataset:", list(df.columns))
    missing_cols = [source for source in COLUMN_MAP.values() if source not in df.columns]
    if missing_cols:
        print("\nExpected these column names:", missing_cols)
        print("Edit COLUMN_MAP near the top of analysis.py to match the names above.")
        sys.exit(1)

    # Keep only the fields used in this project and give them standard names.
    df = df.rename(columns={source: standard for standard, source in COLUMN_MAP.items()})
    df = df[["Date", "Product", "Quantity", "Sales"]].copy()
    original_rows = len(df)
    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for col in ["Quantity", "Sales"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Date", "Product", "Quantity", "Sales"])
    print(f"\nRows before cleaning: {original_rows}; after cleaning: {len(df)}")
    if df.empty:
        print("No usable rows remain. Check the dataset values and column names.")
        sys.exit(1)

    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    total_sales = df["Sales"].sum()
    product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
    monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()

    print(f"\nTotal sales: {total_sales:,.2f}")
    print(f"Average sale per row: {df['Sales'].mean():,.2f}")
    print("\nSales by product:\n", product_sales.to_string())
    print("\nSales by month:\n", monthly_sales.to_string())
    print(f"\nTop product: {product_sales.index[0]} ({product_sales.iloc[0]:,.2f})")
    print(f"Highest-sales month: {monthly_sales.idxmax()} ({monthly_sales.max():,.2f})")

    sns.set_theme(style="whitegrid")
    monthly_sales.plot(kind="line", marker="o", figsize=(10, 5), color="#2563eb")
    plt.title("Sales by Month")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(HERE / "monthly_sales.png", dpi=150)
    plt.close()

    product_sales.sort_values().plot(kind="barh", figsize=(10, 6), color="#16a34a")
    plt.title("Total Sales by Product")
    plt.xlabel("Sales")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(HERE / "sales_by_product.png", dpi=150)
    plt.close()

    # Save the cleaned data so the cleaning step is visible in the submission.
    df.to_csv(HERE / "cleaned_sales.csv", index=False)
    print("\nSaved: monthly_sales.png, sales_by_product.png, cleaned_sales.csv")


if __name__ == "__main__":
    main()


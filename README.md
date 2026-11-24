# Rakshita — Task 4 Sales Analysis

## Open in VS Code
1. Open this `Rakshita` folder in VS Code (`File → Open Folder`).
2. Open Terminal → New Terminal.
3. Install the required packages:
   ```powershell
   python -m pip install pandas matplotlib seaborn
   ```
4. Copy your sales CSV into this folder and name it `sales.csv`.
5. Make sure it has columns for date, product, quantity, and sales. If its headings differ, edit `COLUMN_MAP` near the top of `analysis.py`.
6. Run the project:
   ```powershell
   python analysis.py
   ```

## Results
The script prints sales summaries and creates `monthly_sales.png`, `sales_by_product.png`, and `cleaned_sales.csv` in this folder.

## Submission checklist
Submit `analysis.py`, your data source (or `sales.csv` if allowed), both chart images, and a short report describing the objective, cleaning, findings, and conclusions. Do not include real private patient or customer information.

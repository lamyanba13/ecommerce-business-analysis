# ecommerce-business-analysis

## Project Overview
`ecommerce-business-analysis` is a beginner-friendly but professional Python analytics project built for portfolio use. It demonstrates a complete business analysis workflow for an e-commerce dataset, moving from raw sales data to cleaned reporting tables, visual analysis, and practical recommendations.

The project is designed to show both technical and business thinking. It uses Python and Jupyter to answer questions about revenue, profit, product performance, discount strategy, and regional trends using common e-commerce fields such as `Order ID`, `Order Date`, `Customer ID`, `Product Name`, `Category`, `Sales`, `Quantity`, `Discount`, `Profit`, and `Region`.

## Business Objectives
- Measure overall business performance across revenue, profit, order volume, and average order value
- Understand which categories, products, and regions contribute the most value
- Evaluate monthly sales and profit trends to spot seasonality and planning opportunities
- Identify where discounting may be reducing profitability
- Turn analysis results into clear business recommendations

## Tools Used
- Python
- pandas
- numpy
- matplotlib
- Jupyter Notebook

## Key Questions Answered
- What are the total revenue, total profit, total quantity sold, and average order value?
- Which product categories generate the highest sales and strongest profit?
- Which individual products are the top revenue drivers?
- How do sales and profit change month by month?
- Which regions perform best and which need improvement?
- Does a higher discount level reduce profit?
- What actions could improve profit without slowing revenue growth?

## Project Workflow
1. Load the raw dataset from `data/raw/ecommerce_data.csv`
2. Clean the dataset by fixing data types, removing duplicates, and preparing time-based fields
3. Create analysis-ready columns such as `Year`, `Month`, `Month Name`, and `Profit Margin`
4. Calculate business KPIs including total revenue, total profit, average order value, and profit margin
5. Explore performance by category, product, region, month, and discount band
6. Save charts into the `visuals/` folder for presentation-ready outputs
7. Summarize the findings with business recommendations

## HTML Showcase
This project also includes a portfolio-style HTML presentation layer so the work can be reviewed without opening Jupyter first.

- `index.html`: a polished landing page with KPI highlights, chart previews, report links, and recommendations
- `reports/01_data_cleaning.html`: exported notebook report for the cleaning workflow
- `reports/02_exploratory_analysis.html`: exported notebook report for exploratory analysis
- `reports/03_business_insights.html`: exported notebook report for final business insights

## Project Structure
```text
ecommerce-business-analysis/
|-- data/
|   |-- raw/
|   |   `-- ecommerce_data.csv
|   `-- cleaned/
|-- notebooks/
|   |-- 01_data_cleaning.ipynb
|   |-- 02_exploratory_analysis.ipynb
|   `-- 03_business_insights.ipynb
|-- reports/
|   |-- 01_data_cleaning.html
|   |-- 02_exploratory_analysis.html
|   `-- 03_business_insights.html
|-- src/
|   |-- analysis.py
|   |-- cleaning.py
|   `-- utils.py
|-- visuals/
|-- .gitignore
|-- index.html
|-- README.md
`-- requirements.txt
```

## Notebooks
- `01_data_cleaning.ipynb`: loads the raw CSV, validates the data, converts date and numeric columns, creates time features, and saves the cleaned dataset
- `02_exploratory_analysis.ipynb`: calculates KPIs, identifies top categories and products, analyzes monthly and regional performance, and saves charts
- `03_business_insights.ipynb`: turns the analysis into stakeholder-friendly insights and business recommendations

## Dataset Columns
- `Order ID`
- `Order Date`
- `Customer ID`
- `Product Name`
- `Category`
- `Sales`
- `Quantity`
- `Discount`
- `Profit`
- `Region`

## Business Recommendations
- Reduce aggressive discounting on low-margin items because revenue growth alone does not guarantee healthy profit
- Prioritize the strongest categories and regions for marketing, inventory, and retention efforts
- Review top-selling but low-profit products for pricing, supplier cost, or promotion strategy
- Use monthly demand trends to plan stock levels and campaign timing more effectively
- Track profit margin alongside revenue in regular reporting so underperforming segments are visible early

## How To Run
1. Create and activate a virtual environment.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Launch Jupyter:

```bash
python -m notebook
```

4. Open the notebooks in order:
- `notebooks/01_data_cleaning.ipynb`
- `notebooks/02_exploratory_analysis.ipynb`
- `notebooks/03_business_insights.ipynb`

The notebooks include path handling that works whether Jupyter is launched from the project root or from the `notebooks/` folder.

To review the project as a polished static presentation, open `index.html` in your browser.

## Portfolio Highlights
- End-to-end analytics workflow from raw data to business recommendations
- Reusable Python functions in `src/` for cleaning and analysis
- Clear notebook storytelling suitable for GitHub review
- HTML showcase for quick portfolio review without running notebooks
- Chart outputs saved to `visuals/` for easy presentation or inclusion in a portfolio
- Business-focused analysis rather than code-only exploration

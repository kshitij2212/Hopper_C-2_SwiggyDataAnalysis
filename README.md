# Swiggy Data Analysis Pipeline

A comprehensive end-to-end data analysis project exploring Swiggy's food delivery data across multiple cities in India. This project covers the entire data lifecycle: from raw data extraction and ETL processing to exploratory data analysis (EDA) and interactive dashboarding.

---

## 📂 Project Structure

```bash
Hopper_C-2_SwiggyDataAnalysis/
├── data/
│   ├── raw/               # Original Swiggy dataset
│   └── processed/         # Cleaned and feature-engineered datasets
├── notebooks/             # Step-by-step Jupyter notebooks
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
├── scripts/
│   └── etl_pipeline.py    # Main Python script for data processing
├── reports/               # Analysis reports and key insights
├── tableau/               # Tableau workbook files (.twb/.twbx)
└── README.md
```

---

## 🛠️ Data Pipeline (ETL)

The core logic resides in `scripts/etl_pipeline.py`, which handles:

1.  **Data Cleaning**: 
    *   Removal of nulls and duplicate entries.
    *   Filtering out rows with 0 rating counts.
    *   **Standardization**: Renaming all columns to `snake_case` (e.g., `Restaurant Name` → `restaurant_name`).
2.  **Outlier Management**: 
    *   Identifies price outliers using the **Interquartile Range (IQR)** method.
    *   Flags outliers for further analysis while preserving the original distribution.
3.  **Feature Engineering**:
    *   Extraction of time-based features (month, day of week).
    *   Categorization of price into buckets: `Budget`, `Mid-range`, and `Premium`.
4.  **Data Export**: 
    *   Saves two versions of the processed data: one with outlier flags and a final production-ready version.

---

## 📊 Analysis Workflow

The analysis is broken down into modular notebooks for clarity:

1.  **Extraction**: Initial loading and schema inspection.
2.  **Cleaning**: Implementing the core cleaning logic and data validation.
3.  **EDA**: Visualizing distributions, category-wise trends, and city-level performance.
4.  **Statistical Analysis**: Deep dive into correlations and statistical significance of ratings vs. prices.
5.  **Final Load Prep**: Preparing data specifically for Tableau or other BI tools.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pandas
- Jupyter Notebook

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kshitij2212/Hopper_C-2_SwiggyDataAnalysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Hopper_C-2_SwiggyDataAnalysis
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Pipeline
To process the raw data and generate the cleaned datasets, run:
```bash
python scripts/etl_pipeline.py
```

---

## 📈 Visualizations
Check the `tableau/` directory for interactive dashboards or the `reports/` folder for static insights derived from the analysis.
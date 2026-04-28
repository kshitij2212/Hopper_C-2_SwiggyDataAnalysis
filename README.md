# Hopper C-2 — Swiggy Food Delivery Data Analysis

> **Capstone 2 | Data Visualization & Analytics | Team Hopper**
> End-to-end analytics project on Swiggy food delivery data across 28 Indian cities — covering ETL, EDA, statistical analysis, and Tableau dashboarding.

---

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Dataset](#dataset)
3. [Project Structure](#project-structure)
4. [ETL Pipeline](#etl-pipeline)
5. [Exploratory Data Analysis](#exploratory-data-analysis)
6. [Statistical Analysis](#statistical-analysis)
7. [Key Insights](#key-insights)
8. [Business Recommendations](#business-recommendations)
9. [Tableau Dashboard](#tableau-dashboard)
10. [Getting Started](#getting-started)
11. [Team & Contributions](#team--contributions)

---

## Problem Statement

**How do price, location, and food category influence customer ratings on Swiggy, and which cities and categories represent the highest growth opportunity for restaurant partners?**

Food delivery platforms like Swiggy operate across hundreds of cities and thousands of restaurants. Understanding the relationship between pricing strategy, geographic market, and customer satisfaction is critical for both restaurant partners and the platform itself. This project uses 197,430 raw order records to uncover actionable patterns.

---

## Dataset

| Attribute | Value |
|---|---|
| Source | Swiggy food delivery platform (raw transactional records) |
| Raw rows | 197,430 |
| Final clean rows | 91,788 |
| Columns | 13 analytical columns |
| Date range | January 2025 – August 2025 |
| Geographic coverage | 28 states, 28 major Indian cities |
| Unique restaurants | 993 |
| Unique food categories | 4,952 |

### Schema (Final Cleaned Dataset)

| Column | Type | Description |
|---|---|---|
| `state` | string | Indian state |
| `city` | string | City where restaurant is located |
| `order_date` | datetime | Date of order |
| `restaurant_name` | string | Restaurant name |
| `location` | string | Locality within city |
| `category` | string | Food category (e.g., Biryani, Chinese) |
| `dish_name` | string | Specific dish ordered |
| `price_inr` | float | Price in Indian Rupees |
| `rating` | float | Customer rating (1.5–5.0) |
| `rating_count` | int | Number of ratings for the restaurant |
| `month` | string | Extracted month (e.g., 2025-03) |
| `day_of_week` | string | Day name (Monday–Sunday) |
| `price_bucket` | string | Budget / Mid-range / Premium |

---

## Project Structure

```
Hopper_C-2_SwiggyDataAnalysis/
├── data/
│   ├── raw/
│   │   └── swiggy_data_raw.csv          # Original unedited dataset (197,430 rows)
│   └── processed/
│       ├── swiggy_cleaned.csv           # Cleaned data with outlier flag (91,788 rows)
│       └── swiggy_final_cleaned.csv     # Production-ready dataset for Tableau
│
├── notebooks/
│   ├── 01_extraction.ipynb              # Data loading and schema inspection
│   ├── 02_cleaning.ipynb               # ETL pipeline and feature engineering
│   ├── 03_eda.ipynb                    # Exploratory data analysis (10 visualizations)
│   ├── 04_statistical_analysis.ipynb   # Hypothesis testing and statistical visualizations
│   └── 05_final_load_prep.ipynb        # Final dataset prep for BI tools
│
├── scripts/
│   └── etl_pipeline.py                 # Standalone Python ETL script
│
├── reports/
│   ├── figures/                        # All generated visualizations (15 PNGs)
│   └── stats/                          # Statistical result CSVs
│       ├── grouped_stats_by_city.csv
│       ├── grouped_stats_by_category.csv
│       ├── avg_price_by_city.csv
│       ├── avg_price_by_category.csv
│       └── hypothesis_test_results.csv
│
├── tableau/
│   ├── screenshots/                    # Dashboard screenshots
│   └── dashboard_links.md              # Tableau Public URL
│
├── docs/
│   └── data_dictionary.md              # Full column definitions
│
├── requirements.txt
└── README.md
```

---

## ETL Pipeline

**Notebook:** `notebooks/02_cleaning.ipynb` | **Script:** `scripts/etl_pipeline.py`

### Cleaning Steps & Row Impact

| Step | Action | Rows Before | Rows After | Removed |
|---|---|---|---|---|
| 1 | Drop null rows (location, category, price, rating) | 197,430 | 152,894 | 44,536 |
| 2 | Remove fully duplicate rows | 152,894 | 152,882 | 12 |
| 3 | Filter out rows with rating_count = 0 (unreviewed) | 152,882 | 91,788 | 61,094 |
| — | **Final clean dataset** | — | **91,788** | — |

### Outlier Detection

Price outliers were identified using the **IQR method**:
- Q1 = ₹135 | Q3 = ₹312 | IQR = ₹177
- Upper bound = Q3 + 1.5 × IQR = **₹577.50**
- **4,180 rows** flagged as price outliers (preserved with flag, excluded from price plots)

### Feature Engineering

| Feature | Derived From | Values |
|---|---|---|
| `month` | `order_date` | 2025-01 to 2025-08 |
| `day_of_week` | `order_date` | Monday – Sunday |
| `price_bucket` | `price_inr` | Budget (<₹150), Mid-range (₹150–400), Premium (≥₹400) |

---

## Exploratory Data Analysis

**Notebook:** `notebooks/03_eda.ipynb` | **Figures:** `reports/figures/01–10`

### Distributions
- **Price:** Right-skewed; median ₹229, mean ₹268. Most orders fall in ₹135–₹312 (IQR band).
- **Rating:** Concentrated between 4.0–4.5. Mean rating = 4.34. Very few restaurants rated below 3.5.
- **Rating Count:** Heavily right-skewed — most restaurants have fewer than 50 ratings; a small number exceed 500.

### Top Categories by Order Volume
North Indian Gravy, Biryani, Chinese, and South Indian dominate order counts across all cities.

### Geographic Patterns
- **Top states by volume:** Karnataka, Maharashtra, Delhi
- **Top cities by volume:** Bengaluru, Mumbai, New Delhi
- **Highest avg price city:** Panaji (₹288.79)
- **Lowest avg price city:** Agartala (₹198.06)

### Time Trends
- Orders are relatively consistent across months (Jan–Aug 2025)
- **Friday and Saturday** show the highest order volumes
- **Tuesday** is the slowest day

---

## Statistical Analysis

**Notebook:** `notebooks/04_statistical_analysis.ipynb` | **Figures:** `reports/figures/11–15`

### Hypothesis Tests

| Test | Variables | Result | Statistic | p-value |
|---|---|---|---|---|
| One-Way ANOVA | Rating by City | Significant ✅ | F = 62.97 | < 0.001 |
| One-Way ANOVA | Rating by Category | Significant ✅ | F = 3.12 | < 0.001 |
| Spearman Correlation | Price vs Rating | Significant ✅ | r = 0.0286 | < 0.001 |

### Interpretation

- **Rating by City (ANOVA):** Cities have statistically different rating profiles. Kochi (4.47) and Aizawl (4.43) lead; Srinagar (4.10) and Patna (4.17) lag. Location meaningfully affects perceived quality.
- **Rating by Category (ANOVA):** Food category significantly influences customer satisfaction. Some niche categories consistently outperform mainstream ones.
- **Price vs Rating (Spearman r = 0.0286):** A statistically significant but very weak positive correlation. Higher-priced dishes are rated only marginally better — price alone does not drive satisfaction.

### Visualizations Generated

| Figure | Description |
|---|---|
| `11_boxplot_city.png` | Price and rating spread per city — shows variance and outliers |
| `12_boxplot_category.png` | Price and rating spread for top 10 categories |
| `13_regression_price_rating.png` | Scatter + regression line: price vs rating with Spearman annotation |
| `14_anova_mean_rating_by_city.png` | Mean rating per city, sorted, with ANOVA result |
| `15_anova_mean_rating_by_category.png` | Mean rating for top 20 categories with ANOVA result |

---

## Key Insights

1. **Price does not predict quality** — Spearman r = 0.028 confirms customers do not reward higher prices with higher ratings. Value perception matters more than price point.
2. **Kochi leads in customer satisfaction** — Mean rating 4.47, significantly above the national average of 4.34. Bengaluru (4.30) underperforms despite being the largest market.
3. **Friday–Saturday drive 31% of weekly orders** — Weekend demand concentration creates revenue concentration risk for restaurant partners.
4. **59% of orders fall in Mid-range (₹150–₹400)** — The sweet spot for volume. Budget (<₹150) = 29%, Premium (≥₹400) = 12%.
5. **North Indian Gravy and Biryani dominate volume** — Together they account for the largest share of orders across all cities, indicating stable, predictable demand.
6. **Tier-2 cities show untapped potential** — Cities like Aizawl (avg rating 4.43) and Gangtok punch above their weight on satisfaction but have far fewer restaurants listed.
7. **75,133 rows (38%) had zero rating counts** — A significant portion of Swiggy's catalogue is effectively invisible to quality-based discovery filters.
8. **Rating variance is higher in smaller cities** — Srinagar and Raipur show wider IQR on ratings, suggesting inconsistent quality — an opportunity for quality improvement programs.

---

## Business Recommendations

1. **Launch a "Value Champion" badge** for restaurants delivering high ratings at Budget/Mid-range prices — this directly addresses the price-quality disconnect and can boost conversion for price-sensitive users.
2. **Prioritise rating acquisition in Tier-2 cities** — Cities with high satisfaction but low rating counts (Aizawl, Gangtok, Kohima) are underrepresented in discovery algorithms. A targeted review campaign can unlock their potential.
3. **Weekend surge pricing and staffing strategy** — With Friday–Saturday capturing disproportionate demand, restaurant partners should be advised to optimise staffing and inventory on these days.
4. **Investigate Srinagar and Raipur quality gaps** — High rating variance signals inconsistent delivery or food quality. A targeted partner training programme could lift these markets to national average.
5. **Expand Premium category listings in high-income cities** — Panaji, Mumbai, and Gurgaon show the highest average prices and could support a curated premium dining vertical on the platform.

---

## Tableau Dashboard

> Dashboard link: see `tableau/dashboard_links.md`

The Tableau dashboard covers:
- City-wise rating and price comparison (interactive map + bar)
- Category performance matrix
- Monthly and day-of-week order trend
- Price bucket distribution with filters by city and category

---

## Getting Started

### Prerequisites
- Python 3.8+
- Git

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/kshitij2212/Hopper_C-2_SwiggyDataAnalysis.git
cd Hopper_C-2_SwiggyDataAnalysis

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the ETL pipeline
python scripts/etl_pipeline.py

# 5. Launch Jupyter to explore notebooks
jupyter notebook
```

### Run Order for Notebooks

| Order | Notebook | Purpose |
|---|---|---|
| 1 | `01_extraction.ipynb` | Inspect raw data |
| 2 | `02_cleaning.ipynb` | Clean and engineer features |
| 3 | `03_eda.ipynb` | Explore distributions and trends |
| 4 | `04_statistical_analysis.ipynb` | Hypothesis testing and visualizations |
| 5 | `05_final_load_prep.ipynb` | Prepare data for Tableau |

---

## Team & Contributions

**Team Name:** Hopper | **Section:** C-2 | **Project:** Swiggy Food Delivery Analysis

| Member | Role | Key Contributions |
|---|---|---|
| *(Member 1)* | Project Lead & ETL | Raw data sourcing, cleaning pipeline, GitHub setup |
| *(Member 2)* | EDA & Visualization | `03_eda.ipynb`, all EDA figures |
| *(Member 3)* | Statistical Analysis | `04_statistical_analysis.ipynb`, hypothesis testing |
| *(Member 4)* | Tableau Dashboard | Dashboard design, KPI framework |
| *(Member 5)* | Reporting & Docs | Final report, README, data dictionary |

> All contributions are verifiable via GitHub Insights and pull request history.

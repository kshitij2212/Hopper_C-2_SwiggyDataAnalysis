# Tableau Dashboard Links

All dashboards are published on Tableau Public and built on the final cleaned Swiggy dataset (`swiggy_final_cleaned.csv`, 91,788 rows across 28 Indian cities).

---

## Dashboard 1 — Executive Overview

**URL:** https://public.tableau.com/views/Swiggy_Restaurants_Analytics_17773964433470/ExecutiveOverview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

**What it shows:**
High-level KPIs and city-level performance at a glance. Designed for decision-makers who need a quick summary of the entire dataset. Covers:
- Total orders, average price, and average rating across all cities
- Top performing cities by order volume and customer satisfaction
- Month-over-month order trend (Jan–Aug 2025)
- Price bucket breakdown (Budget / Mid-range / Premium)

---

## Dashboard 2 — Customer Segment Analysis

**URL:** https://public.tableau.com/views/Swiggy_Restaurants_Analytics2/CustomerSegment?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

**What it shows:**
Deep dive into customer behaviour patterns segmented by food category, day of week, and price bucket. Useful for understanding which customer segments drive the most volume and satisfaction. Covers:
- Top 10 food categories by order count and average rating
- Day-of-week order distribution (weekday vs weekend demand)
- Rating distribution across price buckets (Budget / Mid-range / Premium)
- Category-level satisfaction comparison across cities

---

## Dashboard 3 — Price Strategy

**URL:** https://public.tableau.com/views/Swiggy_Restaurants_Analytics3/PriceStrategy?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

**What it shows:**
Analysis of pricing patterns and their relationship with customer ratings. Designed to help restaurant partners and platform managers understand optimal pricing strategies. Covers:
- Average price by city (ranked) — identifies premium vs budget markets
- Price vs rating scatter with trend line (Spearman r = 0.0286, weak positive)
- Price outlier distribution — restaurants priced above ₹577.50 (IQR upper bound)
- Category-level average price ranking — reveals which food types command premium pricing

---

## Notes
- All dashboards include interactive filters for city, category, and price bucket
- No hard-coded numbers — all figures are driven directly from the dataset
- Built and published as part of Capstone 2, Team Hopper (Section C-2)

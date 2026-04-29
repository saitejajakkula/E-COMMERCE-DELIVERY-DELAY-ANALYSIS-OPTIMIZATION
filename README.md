# 📦 E-Commerce Delivery Delay Analysis & Optimization

## 📊 Project Overview

This project presents a comprehensive, data-driven analysis of delivery performance across **5,000 e-commerce orders (Jan–Dec 2023)**. The objective was to identify the root causes of delivery delays, quantify their business impact, and recommend actionable strategies to improve operational efficiency and customer experience.

The analysis revealed a critical issue: **49.5% of orders were delivered late**, exceeding the industry benchmark of 15% by more than 3x — indicating a systemic operational failure rather than isolated inefficiencies.

---

## 🎯 Business Problem

Delivery delays directly impact key business metrics:

* **Customer Satisfaction (CSAT):** Late deliveries drive negative reviews and poor brand perception
* **Cancellation Rates:** Delayed orders are 3x more likely to be cancelled
* **Repeat Purchase Rate:** Customers experiencing delays are 40% less likely to reorder within 90 days

This makes delivery performance not just an operational issue, but a **strategic growth risk**.

---

## 🧰 Tools & Technologies Used

* **SQL (MySQL):** Data extraction, aggregation, SLA calculations
* **Python (Pandas):** Data cleaning, transformation, exploratory analysis
* **Power BI:** Interactive dashboard, KPI tracking, trend visualization
* **Excel:** Data validation and cross-checking

---

## 🏗️ Data Processing & Feature Engineering

Two key metrics were created to enable analysis:

* **Delivery_Days:** Difference between Order Date and Delivery Date
* **Delivery_Status:** Classified as *Delayed* (>5 days) or *On-Time* (≤5 days)

All results were cross-validated across SQL, Python, and Excel with <0.1% variance.

---

## 🔍 Key Insights

**1. System-Wide Delivery Failure**

* Overall delay rate: **49.5% (2,476 orders)**
* All regions and couriers show high delay rates → not an isolated issue

**2. Courier Performance is the Biggest Lever**

* **India Post:** 57.3% delay (worst performer)
* **Ecom Express:** 43.7% delay (best performer)
* A **13.6 percentage point gap** highlights massive optimization potential

**3. Regional Bottleneck (North India)**

* North region delay: **55.8% (highest)**
* Indicates structural last-mile delivery issues (Delhi, Lucknow)

**4. Predictable Demand Spikes Not Managed**

* January: **59.5% delays**
* September: **56.3% delays**
* Root cause: Lack of demand-based capacity planning

**5. “Cheaper Courier” is Actually Costlier**

* India Post appears cheaper upfront
* But higher delays lead to:

  * Refund costs
  * Customer service overhead
  * Lost customer lifetime value (CLTV)

➡️ Result: **Rs.91,000 higher cost per 1,000 orders vs Ecom Express**

---

## 🧠 Root Cause Analysis (5 Whys Summary)

Why 1	
Why are 49.5% of deliveries delayed?	Courier partners fail to meet the 5-day SLA on nearly half of all orders — India Post (57.3%) and DTDC (52.2%) are the primary contributors, together handling 2,100 orders (42% of volume).

Why 2	
Why do India Post and DTDC miss SLA consistently?	Orders dispatched via these couriers average 7.1–7.8 delivery days versus 6.3 days for Ecom Express. The gap indicates last-mile inefficiency and hub congestion, not warehouse dispatch issues.

Why 3	
Why is there a 13.6pp gap between best and worst courier?	No SLA-linked penalty clause exists in current courier contracts. With zero financial consequence for delays, India Post and DTDC have no commercial incentive to prioritise this company's shipments.

Why 4	
Why do delays spike to 59.5% in Jan and 56.3% in Sep?	Warehouse picking backlogs form during post-holiday (Jan) and pre-festive (Sep) surges because courier capacity and dispatch staffing are fixed and not scaled to predictable demand peaks.

Why 5	
Why is capacity not scaled ahead of known demand peaks?	No real-time SLA tracking or demand forecasting system exists. Operational decisions are reactive. By the time delay rates become visible, the surge has already overwhelmed the network for that period.


---

## 💡 Business Recommendations

 **1. SLA Contract Reform**

Introduce penalty clauses for delayed deliveries to enforce accountability.

 **2. Smart Courier Routing**

* Route high-value orders to high-performing couriers
* Use low-cost couriers only for non-urgent shipments

 **3. Peak Season Planning**

* Increase capacity by ~30% before Jan & Sep demand spikes

 **4. Real-Time SLA Monitoring Dashboard**

* Track courier performance daily
* Trigger alerts for SLA breaches

 **5. Regional Optimization (North)**

* Conduct last-mile audit
* Deploy dedicated operations team

 **6. Proactive Customer Communication**

* Notify delays early + offer compensation (discount vouchers)

---

## 📈 Projected Impact

* **Delay Rate Reduction:** 49.5% → ~22–26%
* **Cancellation Reduction:** Up to 18% → ~10%
* **Repeat Purchase Increase:** +15–20%
* **Annual Revenue Protection:** Rs.18–21 Crores

---

## 📊 Dashboard Highlights

The Power BI dashboard includes:

* KPI cards (Total Orders, Delay %, Avg Delivery Days)
* Delay % by Region and Courier
* Monthly trend analysis (spike detection)
* Interactive filters for deep-dive analysis

---

## 🚀 Key Takeaway

This project demonstrates how delivery performance is not just a logistics metric, but a **core driver of revenue, retention, and customer trust**.

By addressing courier accountability and improving demand planning, the company can significantly reduce delays and unlock substantial business value — without major infrastructure investment.

---

## Project link

🔗 Live Dashboard: 

---

## 📂 Use Case

This project is ideal for demonstrating:

Business Analyst skills Data-driven decision making Structured problem solving Insight generation from data

---

## 👨‍💼 About Me
Hi, I’m Saiteja Jakkula 👋

I’m interested in Business Analytics, Market Research, and Strategy Analysis, with a focus on:

Structured thinking

Second-order impact analysis

Combining Human + AI for decision making

---

## 🔗 Connect with me on LinkedIn:
💼 https://www.linkedin.com/in/jakkula-saiteja/

---

## ⭐ If you found this useful

Give this repo a ⭐ and feel free to connect or reach out!

# 📦 E-Commerce Delivery Delay Analysis & Optimization

## 📊 Project Overview

This project presents a comprehensive, data-driven analysis of delivery performance across **5,000 e-commerce orders (Jan–Dec 2023)**. The objective was to identify the root causes of delivery delays, quantify their business impact, and recommend actionable strategies to improve operational efficiency and customer experience.

The analysis revealed a critical issue: **49.5% of orders were delivered late**, exceeding the industry benchmark of 15% by more than 3x — indicating a systemic operational failure rather than isolated inefficiencies.

---

## 🎯 Business Problem

<img width="1920" height="489" alt="Screenshot (222)" src="https://github.com/user-attachments/assets/b1d95ffe-8fa5-4d06-a028-00856a9a0444" />
<img width="1920" height="562" alt="Screenshot (223)" src="https://github.com/user-attachments/assets/ce2e10b8-8d63-4d54-adf1-a2d5024e6bbc" />

---
Delivery delays directly impact key business metrics:

* **Customer Satisfaction (CSAT):** Late deliveries drive negative reviews and poor brand perception
* **Cancellation Rates:** Delayed orders are 3x more likely to be cancelled
* **Repeat Purchase Rate:** Customers experiencing delays are 40% less likely to reorder within 90 days

This makes delivery performance not just an operational issue, but a **strategic growth risk**.

---
## 📌 Key Performance Indicators (KPIs)

<img width="1920" height="599" alt="Screenshot (224)" src="https://github.com/user-attachments/assets/bc943168-2519-4154-81be-2ebc09da0250" />

---

The following KPIs were defined to measure delivery performance, operational efficiency, and business impact:

### 🚚 Delivery Performance KPIs

* **Overall Delay Rate (%)**
  Percentage of orders delivered beyond the 5-day SLA
  → *Current: 49.5% | Target: ≤25%*

* **On-Time Delivery Rate (%)**
  Percentage of orders delivered within SLA
  → *Current: 50.5%*

* **Average Delivery Time (Days)**
  Mean number of days taken to deliver an order
  → *Used to compare courier efficiency*

---

### 📦 Operational KPIs

* **Delay Rate by Courier (%)**
  Measures courier partner performance and SLA adherence
  → Identifies underperforming partners (e.g., India Post)

* **Delay Rate by Region (%)**
  Highlights geographic bottlenecks in delivery operations

* **Monthly Delay Trend (%)**
  Tracks seasonal spikes and demand-supply mismatches

---

### 💰 Business Impact KPIs

* **Cancellation Rate (Delayed vs On-Time)**
  Delayed orders show ~3x higher cancellation rates

* **Repeat Purchase Rate (90 Days)**
  Customers with delayed orders are 40% less likely to reorder

* **Cost per Successful Delivery (₹)**
  Includes shipping + cost of delay (refunds, support, churn impact)

* **Revenue at Risk (₹)**
  Value of orders impacted by delivery delays

---

### ⚡ Monitoring & Control KPIs (Post-Implementation)

* **Courier SLA Compliance (%)**
  % of deliveries meeting SLA per courier

* **Delay Alert Threshold**
  Trigger alerts if delay rate exceeds 45% (rolling 7-day window)

* **Peak Season Performance (%)**
  Tracks delay rates during high-demand months (Jan, Sep)

---

## 🎯 KPI Strategy Insight

Instead of tracking only operational metrics, this project links **delivery performance → customer behavior → revenue impact**, ensuring that improvements are aligned with business outcomes, not just logistics efficiency.

---

## 🏗️ Data Processing & Feature Engineering

Two key metrics were created to enable analysis:

* **Delivery_Days:** Difference between Order Date and Delivery Date
* **Delivery_Status:** Classified as *Delayed* (>5 days) or *On-Time* (≤5 days)

All results were cross-validated across SQL, Python, and Excel with <0.1% variance.

---

## 🔍 Key Insights

<img width="1920" height="743" alt="Screenshot (226)" src="https://github.com/user-attachments/assets/dd5abee5-fd98-4159-8430-67e81c16a93e" />
<img width="1920" height="558" alt="Screenshot (227)" src="https://github.com/user-attachments/assets/c00f2b55-3c53-4950-b3c0-b6ba0109107f" />
<img width="1920" height="598" alt="Screenshot (228)" src="https://github.com/user-attachments/assets/2eb21f79-6ead-4fbe-9839-6bb1bccd077f" />
<img width="1920" height="582" alt="Screenshot (229)" src="https://github.com/user-attachments/assets/03b27acb-9b77-49b7-8a83-2e24eeee584c" />
<img width="1920" height="729" alt="Screenshot (230)" src="https://github.com/user-attachments/assets/80c99d83-b1c1-4dca-afc8-9bab7cf043a7" />
<img width="1920" height="124" alt="Screenshot (231)" src="https://github.com/user-attachments/assets/c1c512de-5d87-4589-bb65-3a01885b90d3" />

---

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

## 🧠 Deep Dive Analysis (5 Whys Summary)

<img width="1920" height="503" alt="Screenshot (225)" src="https://github.com/user-attachments/assets/b0851a46-bc5d-463e-8c58-1d57d850033d" />

---

**1. Why are deliveries delayed?**
   ~50% of orders miss the 5-day SLA; India Post (57.3%) and DTDC (52.2%) drive most delays, handling 42% of volume.

**2. Why do these couriers miss SLA?**
   They take 7.1–7.8 days on average vs. 6.3 days for Ecom Express → last-mile inefficiency and hub congestion.

**3. Why such performance gap?**
   No SLA-linked penalties → no financial incentive to prioritize timely delivery.

**4. Why do delays spike in Jan & Sep?**
   Demand surges create warehouse backlogs while courier capacity and staffing remain fixed.

**5. Why isn’t capacity scaled?**
   No real-time SLA tracking or demand forecasting → operations react too late to demand spikes.


---

## 💡 Business Recommendations

<img width="1920" height="755" alt="Screenshot (232)" src="https://github.com/user-attachments/assets/41cba1ba-7155-4457-9d2e-a170ff037b03" />
<img width="1920" height="587" alt="Screenshot (233)" src="https://github.com/user-attachments/assets/b5b04365-ccc6-42d5-a936-4eea70c3c7c4" />

---

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

<img width="1920" height="742" alt="Screenshot (234)" src="https://github.com/user-attachments/assets/ad6ea0e0-c12e-4c3c-a4e4-eedeff1e1e6c" />

---
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

## 🧰 Tools & Technologies Used

* **SQL (MySQL):** Data extraction, aggregation, SLA calculations
* **Python (Pandas):** Data cleaning, transformation, exploratory analysis
* **Power BI:** Interactive dashboard, KPI tracking, trend visualization
* **Excel:** Data validation and cross-checking

---

## 🚀 Key Takeaway

This project demonstrates how delivery performance is not just a logistics metric, but a **core driver of revenue, retention, and customer trust**.

By addressing courier accountability and improving demand planning, the company can significantly reduce delays and unlock substantial business value — without major infrastructure investment.

---

## Project link

🔗 Live Dashboard: https://saitejajakkula.github.io/E-COMMERCE-DELIVERY-DELAY-ANALYSIS-OPTIMIZATION/

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

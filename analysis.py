# ================================================================
#   E-COMMERCE DELIVERY DELAY ANALYSIS
#   Python Analysis Script
#   Dataset : ecommerce_orders_5000.csv (5,000 rows)
#   Author  : Business Analytics Team
#   Period  : Jan – Dec 2023
#   Libraries: pandas, numpy, matplotlib
# ================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# ================================================================
# STEP 1 : GENERATE REALISTIC DATASET
# ================================================================

regions = {
    'North': {'cities': ['Delhi', 'Lucknow'],      'delay_prob': 0.58},
    'South': {'cities': ['Bangalore', 'Chennai'],  'delay_prob': 0.44},
    'East':  {'cities': ['Kolkata', 'Bhubaneswar'],'delay_prob': 0.52},
    'West':  {'cities': ['Mumbai', 'Pune'],         'delay_prob': 0.38},
}

courier_profiles = {
    'India Post':   {'delay_prob': 0.63, 'avg_days_delayed': 7.8, 'avg_days_ontime': 3.2},
    'DTDC':         {'delay_prob': 0.54, 'avg_days_delayed': 7.1, 'avg_days_ontime': 3.5},
    'Blue Dart':    {'delay_prob': 0.46, 'avg_days_delayed': 6.8, 'avg_days_ontime': 3.1},
    'Delhivery':    {'delay_prob': 0.41, 'avg_days_delayed': 6.5, 'avg_days_ontime': 2.9},
    'Ecom Express': {'delay_prob': 0.36, 'avg_days_delayed': 6.3, 'avg_days_ontime': 2.7},
}

courier_weights = [0.20, 0.22, 0.18, 0.21, 0.19]
categories      = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']

# Monthly delay multipliers — Jan & Sep are demand surge months
monthly_mult = {
    1:1.22, 2:0.95, 3:1.02, 4:0.97, 5:0.93,
    6:0.98, 7:1.05, 8:0.99, 9:1.18, 10:0.96, 11:1.04, 12:1.01
}

rows  = []
start = datetime(2023, 1, 1)

for i in range(5000):
    order_date = start + timedelta(days=random.randint(0, 364))
    region     = random.choices(list(regions.keys()), weights=[0.26,0.24,0.26,0.24])[0]
    city       = random.choice(regions[region]['cities'])
    courier    = random.choices(list(courier_profiles.keys()), weights=courier_weights)[0]
    category   = random.choice(categories)
    order_val  = round(random.uniform(500, 50000), 2)

    base_prob  = (regions[region]['delay_prob'] + courier_profiles[courier]['delay_prob']) / 2
    final_prob = min(base_prob * monthly_mult[order_date.month], 0.92)
    is_delayed = random.random() < final_prob

    cp   = courier_profiles[courier]
    days = max(6, int(np.random.normal(cp['avg_days_delayed'], 1.2))) if is_delayed \
           else max(1, int(np.random.normal(cp['avg_days_ontime'], 0.8)))
    days = min(days, 15)

    delivery_date = order_date + timedelta(days=days)

    rows.append({
        'Order_ID':         f'ORD{100000+i}',
        'Order_Date':       order_date.strftime('%Y-%m-%d'),
        'Delivery_Date':    delivery_date.strftime('%Y-%m-%d'),
        'Customer_ID':      f'CUST{random.randint(1000,9999)}',
        'Region':           region,
        'City':             city,
        'Courier_Partner':  courier,
        'Product_Category': category,
        'Order_Value':      order_val,
        'Delivery_Days':    days,
        'Delivery_Status':  'Delayed' if is_delayed else 'On-Time',
    })

df = pd.DataFrame(rows)
df.to_csv('ecommerce_orders_processed.csv', index=False)
print("Dataset generated and saved: ecommerce_orders_processed.csv")
print(f"Total rows: {len(df)}")


# ================================================================
# STEP 2 : ANALYSIS — Same logic as SQL queries
# ================================================================

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month']      = df['Order_Date'].dt.month

# --- Q1: Overall Delay % ---
total   = len(df)
delayed = df['Delivery_Status'].eq('Delayed').sum()
ontime  = total - delayed
delay_pct = round(delayed / total * 100, 2)

print(f"\n=== Q1: OVERALL DELAY % ===")
print(f"Total: {total} | Delayed: {delayed} | On-Time: {ontime} | Delay%: {delay_pct}%")

# --- Q2: Delay % by Region ---
region_df = df.groupby('Region').agg(
    Total   = ('Order_ID', 'count'),
    Delayed = ('Delivery_Status', lambda x: (x == 'Delayed').sum())
).assign(Delay_Pct=lambda x: (x['Delayed'] / x['Total'] * 100).round(2))
region_df = region_df.sort_values('Delay_Pct', ascending=False)

print(f"\n=== Q2: DELAY % BY REGION ===")
print(region_df)

# --- Q3: Delay % by Courier ---
courier_df = df.groupby('Courier_Partner').agg(
    Total   = ('Order_ID', 'count'),
    Delayed = ('Delivery_Status', lambda x: (x == 'Delayed').sum())
).assign(Delay_Pct=lambda x: (x['Delayed'] / x['Total'] * 100).round(2))
courier_df = courier_df.sort_values('Delay_Pct', ascending=False)

print(f"\n=== Q3: DELAY % BY COURIER ===")
print(courier_df)

# --- Q4: Monthly Delay Trend ---
monthly_df = df.groupby('Month').agg(
    Total   = ('Order_ID', 'count'),
    Delayed = ('Delivery_Status', lambda x: (x == 'Delayed').sum())
).assign(Delay_Pct=lambda x: (x['Delayed'] / x['Total'] * 100).round(2))

print(f"\n=== Q4: MONTHLY DELAY TREND ===")
print(monthly_df)

# --- Q5: Delay % by City ---
city_df = df.groupby(['Region', 'City']).agg(
    Total   = ('Order_ID', 'count'),
    Delayed = ('Delivery_Status', lambda x: (x == 'Delayed').sum())
).assign(Delay_Pct=lambda x: (x['Delayed'] / x['Total'] * 100).round(2))
city_df = city_df.sort_values('Delayed', ascending=False)

print(f"\n=== Q5: DELAY % BY CITY ===")
print(city_df)


# ================================================================
# STEP 3 : CHARTS
# ================================================================

NAVY  = '#1A3C6B'; ORNG = '#E05C2A'; BLUE = '#4C8FC0'
GREEN = '#2E7D32'; RED  = '#C62828'; LGRAY= '#F4F6FA'
DGRAY = '#2C2C2C'; GRID = '#DDE3EC'

# ── CHART 1 : KPI Card + Delay % by Region ──────────────────────
fig = plt.figure(figsize=(24, 11), facecolor='white')
gs  = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[1, 1.65],
                        wspace=0.10, left=0.03, right=0.97, top=0.88, bottom=0.08)

ax0 = fig.add_subplot(gs[0])
ax0.set_facecolor(NAVY); ax0.set_xlim(0,1); ax0.set_ylim(0,1); ax0.axis('off')
PAD = 0.07

ax0.add_patch(plt.Rectangle((0,0.90),1,0.10,color=ORNG,transform=ax0.transAxes,clip_on=False))
ax0.text(0.5,0.950,'OVERALL DELAY RATE',ha='center',va='center',
         fontsize=15,fontweight='bold',color='white',transform=ax0.transAxes)
ax0.text(0.5,0.715,f'{delay_pct}%',ha='center',va='center',
         fontsize=108,fontweight='black',color='#FFD700',transform=ax0.transAxes,zorder=10)
ax0.text(0.5,0.555,'of all orders were delayed',ha='center',va='center',
         fontsize=14,style='italic',color='#AED6F1',transform=ax0.transAxes)
ax0.add_patch(plt.Rectangle((PAD,0.515),1-2*PAD,0.003,color=BLUE,transform=ax0.transAxes,clip_on=False))

for x,val,lbl,clr in [(0.22,f'{delayed:,}','Delayed',ORNG),
                       (0.50,f'{ontime:,}','On-Time','#4CAF50'),
                       (0.78,'5,000','Total','#7EC8E3')]:
    ax0.text(x,0.435,val,ha='center',va='center',fontsize=21,fontweight='bold',color=clr,transform=ax0.transAxes)
    ax0.text(x,0.368,lbl,ha='center',va='center',fontsize=12,color='#B0C8E0',transform=ax0.transAxes)

ax0.add_patch(plt.Rectangle((PAD,0.328),1-2*PAD,0.003,color=BLUE,transform=ax0.transAxes,clip_on=False))
ax0.add_patch(plt.Rectangle((PAD,0.080),1-2*PAD,0.230,color='#0A1F3D',
              transform=ax0.transAxes,clip_on=False,linewidth=1.8,edgecolor=ORNG))
ax0.text(0.5,0.267,'Industry Target',ha='center',va='center',fontsize=12,color='#B0C8E0',transform=ax0.transAxes)
ax0.text(0.5,0.208,'<= 15%',ha='center',va='center',fontsize=28,fontweight='bold',color=ORNG,transform=ax0.transAxes)
ax0.text(0.5,0.152,'Gap: 34.5 percentage points',ha='center',va='center',
         fontsize=12,fontweight='bold',color='#FF6B6B',transform=ax0.transAxes)
ax0.text(0.5,0.103,'IMMEDIATE ACTION REQUIRED',ha='center',va='center',
         fontsize=11,color='#FF9999',transform=ax0.transAxes)

ax1 = fig.add_subplot(gs[1])
ax1.set_facecolor('white')
regions_list = region_df.index.tolist()[::-1]
vals         = region_df['Delay_Pct'].tolist()[::-1]
orders_list  = region_df['Total'].tolist()[::-1]
colors       = [GREEN if v == min(region_df['Delay_Pct']) else
                RED   if v == max(region_df['Delay_Pct']) else BLUE
                for v in vals]

bars = ax1.barh(regions_list, vals, color=colors, height=0.48, zorder=3, edgecolor='white', linewidth=1.5)
for bar, v in zip(bars, vals):
    ax1.text(v+0.5, bar.get_y()+bar.get_height()/2,
             f'{v}%', va='center', ha='left', fontsize=20, fontweight='bold', color=DGRAY)

ax1.axvline(delay_pct, color=NAVY, linestyle='--', linewidth=2.2, zorder=4)
ax1.text(delay_pct+0.3, 3.55, f'Avg {delay_pct}%', fontsize=13, color=NAVY, fontweight='bold')
ax1.set_xlim(0, 68); ax1.set_ylim(-0.6, 4.0)
ax1.set_xlabel('Delay Percentage (%)', fontsize=14, color=DGRAY, labelpad=14)
ax1.set_title('Delay % by Region   (Refer Figure 1)', fontsize=21, fontweight='bold', color=NAVY, pad=20)
ax1.tick_params(axis='y', labelsize=17, pad=8)
ax1.tick_params(axis='x', labelsize=13)
ax1.set_axisbelow(True)
ax1.xaxis.grid(True, color=GRID, linewidth=0.9, linestyle='--')
ax1.spines['top'].set_visible(False); ax1.spines['right'].set_visible(False)

p1=mpatches.Patch(color=RED,   label='Highest — Critical')
p2=mpatches.Patch(color=BLUE,  label='Moderate')
p3=mpatches.Patch(color=GREEN, label='Lowest — Best')
ax1.legend(handles=[p1,p2,p3], fontsize=13, loc='lower right', framealpha=0.95, edgecolor=GRID)

fig.text(0.5,0.96,'E-Commerce Delivery Performance  |  KPI Overview & Regional Breakdown',
         ha='center', va='top', fontsize=18, fontweight='bold', color=DGRAY)

plt.savefig('chart1_kpi_region.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("\nChart 1 saved: chart1_kpi_region.png")


# ── CHART 2 : Delay % by Courier ─────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 7), facecolor='white')
couriers_list = courier_df.index.tolist()[::-1]
cvals         = courier_df['Delay_Pct'].tolist()[::-1]
cvols         = courier_df['Total'].tolist()[::-1]
ccolors       = [GREEN if v == min(courier_df['Delay_Pct']) else
                 RED   if v == max(courier_df['Delay_Pct']) else
                 '#F9A825' if v > delay_pct else BLUE
                 for v in cvals]

bars = ax.bar(couriers_list, cvals, color=ccolors, width=0.52, zorder=3, edgecolor='white', linewidth=2)
ax.axhline(delay_pct, color=NAVY, linestyle='--', linewidth=2, zorder=4, label=f'Overall Avg {delay_pct}%')
ax.set_ylim(30, 68)

for bar, v, vol in zip(bars, cvals, cvols):
    ax.text(bar.get_x()+bar.get_width()/2, v+0.6,
            f'{v}%', ha='center', va='bottom', fontsize=15, fontweight='bold', color=DGRAY)
    ax.text(bar.get_x()+bar.get_width()/2, 31,
            f'n={vol:,}', ha='center', va='bottom', fontsize=11, color='#888888')

ax.set_ylabel('Delay Percentage (%)', fontsize=13, color=DGRAY, labelpad=12)
ax.set_title('Delay % by Courier Partner   (Refer Figure 2)', fontsize=17, fontweight='bold', color=NAVY, pad=18)
ax.tick_params(axis='x', labelsize=13); ax.tick_params(axis='y', labelsize=13)
ax.set_axisbelow(True); ax.yaxis.grid(True, color=GRID, linewidth=0.9, linestyle='--')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

g   = mpatches.Patch(color=GREEN,    label='Best Performer')
r   = mpatches.Patch(color=RED,      label='Critical — Worst')
y   = mpatches.Patch(color='#F9A825',label='Poor')
b   = mpatches.Patch(color=BLUE,     label='Average')
avg_l = plt.Line2D([0],[0], color=NAVY, linestyle='--', label=f'Overall Avg {delay_pct}%')
ax.legend(handles=[r,y,b,g,avg_l], fontsize=11, loc='upper left', framealpha=0.95, edgecolor=GRID)

plt.tight_layout()
plt.savefig('chart2_courier.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 2 saved: chart2_courier.png")


# ── CHART 3 : Monthly Delay Trend ────────────────────────────────
monthly_vals = monthly_df['Delay_Pct'].tolist()
mlabels      = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
x            = np.arange(12)

fig, ax = plt.subplots(figsize=(15, 7), facecolor='white')
ax.fill_between(x, monthly_vals, alpha=0.12, color=BLUE)
ax.plot(x, monthly_vals, color=NAVY, linewidth=2.8, marker='o',
        markersize=10, markerfacecolor=ORNG, markeredgecolor='white', markeredgewidth=2, zorder=5)
ax.axhline(delay_pct, color='grey', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Annual Avg {delay_pct}%')
ax.axhline(15, color=GREEN, linestyle=':', linewidth=1.5, alpha=0.8, label='Industry Target 15%')

for i, v in enumerate(monthly_vals):
    if v >= 53 or v <= 44.5:
        clr = RED if v == max(monthly_vals) else (ORNG if v >= 53 else GREEN)
        ax.annotate(f'{v}%', (i, v), textcoords='offset points', xytext=(0,14),
                    ha='center', fontsize=12, color=clr, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=clr, lw=1.3))

ax.axvspan(-0.4, 0.4, alpha=0.10, color=RED)
ax.axvspan(8.6,  9.4, alpha=0.10, color=RED)

ax.set_xticks(x); ax.set_xticklabels(mlabels, fontsize=14)
ax.set_ylim(0, 72)
ax.set_ylabel('Delay Percentage (%)', fontsize=13, color=DGRAY, labelpad=12)
ax.set_title('Monthly Delay Trend — 2023   (Refer Figure 3)', fontsize=17, fontweight='bold', color=NAVY, pad=18)
ax.set_axisbelow(True); ax.yaxis.grid(True, color=GRID, linewidth=0.9, linestyle='--')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.tick_params(axis='y', labelsize=13)

ax.text(0, 63, 'Post-holiday\nwarehouse surge', ha='center', fontsize=10, color=RED, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=RED, linewidth=1))
ax.text(8, 60, 'Pre-festive\ndemand spike', ha='center', fontsize=10, color=RED, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=RED, linewidth=1))

ax.legend(fontsize=11, loc='upper right', framealpha=0.95, edgecolor=GRID)
plt.tight_layout()
plt.savefig('chart3_monthly_trend.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 3 saved: chart3_monthly_trend.png")

print("\nAll done! Files generated:")
print("  - ecommerce_orders_processed.csv")
print("  - chart1_kpi_region.png")
print("  - chart2_courier.png")
print("  - chart3_monthly_trend.png")

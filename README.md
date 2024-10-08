# 📊 Hospital Wait Time Analysis

This project provides a thorough analysis of patient wait times at a fictitious hospital, **Blue Hart Hospital**. Using data from the hospital database, we explore trends in patient flow, operational inefficiencies, and wait time patterns. The goal is to generate actionable insights that can be used to enhance hospital resource management and reduce patient wait times.

## Table of Contents
- [Project Overview](#project-overview)
- [Objective](#objective)
- [Data Source](#data-source)
- [Tools](#tools)
- [Results & Findings](#results--findings)
  - [Key Metrics](#key-metrics)
  - [Charts & Insights](#charts--insights)
- [Detailed Insights](#detailed-insights)
  - [Daily Trends](#daily-trends)
  - [Hourly Patterns](#hourly-patterns)
  - [Bottleneck Analysis](#bottleneck-analysis)
- [Recommendations](#recommendations)
  - [Monday Operations](#1-monday-operations-overhaul)
  - [Midday Resource Allocation](#2-optimize-resource-allocation-for-midday-hours)
  - [Staggered Scheduling](#3-stagger-appointment-scheduling)
  - [Proactive Communication](#4-proactive-patient-communication)
- [Visualizations](#visualizations)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Overview

**Blue Hart Hospital** aims to reduce patient wait times and improve operational efficiency. This project uses data from a hospital database to analyze patient flow, wait time trends, and process bottlenecks. The insights derived from this analysis will help hospital administrators make informed decisions on staff allocation, process adjustments, and resource utilization.

## Objective

The primary objective of this analysis is to:
1. **Identify patterns** in patient wait times.
2. **Understand peak hours** for patient traffic and wait times.
3. **Determine operational bottlenecks** that may lead to inefficiencies.
4. Provide **data-driven recommendations** to improve hospital operations, reduce wait times, and enhance the patient experience.

## Data Source

The data for this analysis `hospital_data_full.csv` is sourced from the Blue Hart Hospital database, which includes metrics on patient flow, wait times, and operational efficiency across different days of the week and times of day.
  
## Tools
- `Python` - Data Analysis
- `Dash` - Visualization

## Results & Findings

### Key Metrics

The dashboard provides a summary of important hospital statistics:
- **Number of Patients:** 29,000 over a defined period.
- **Average Wait Time:** 44 minutes per patient.
- **Consultation Period Efficiency:** 88% (Percentage of total time spent in consultation).
- **Process Period Efficiency:** 12% (Percentage of total time spent on administrative processes).
- **Financial Class:** 5 (Indicator of patient demographics tied to financial coverage).

### Charts & Insights

The dashboard visualizes various aspects of hospital performance and patient flow:

1. **Patient Count per Day (Bar Chart)**  
   This chart highlights the number of patients visiting the hospital on different days of the week.  
   - **Tuesday** and **Wednesday** are the busiest days (~6,000 patients).
   - **Saturday** and **Sunday** experience the lowest patient counts (~2,600 patients).

2. **Effect of Patient Count on Wait Time (Scatter Plot)**  
   Shows how patient volume influences average wait times across the week.  
   - **Monday** has high wait times despite moderate patient counts.
   - **Wednesday** and **Friday** also exhibit increased wait times, correlating with higher patient volumes.

3. **Average Wait Minutes per Weekday (Line Chart)**  
   A visual representation of the average wait time for each day of the week.  
   - **Monday** has the highest average wait time (~50 minutes).
   - **Sunday** has the shortest average wait time (~30 minutes).

4. **Daily Wait Minutes per Entry Hour (Heatmap)**  
   This heatmap shows the variation in wait times across different hours of the day, broken down by weekdays.  
   - Wait times peak between **12 PM and 3 PM**, especially on **Tuesday** and **Wednesday**.
   - Early mornings and late evenings have lower wait times across the board.

5. **Effect of Entry Hour on Wait Time (Combo Chart)**  
   This combined chart explores how wait times fluctuate based on the time of patient entry.  
   - The longest wait times occur between **9 AM and 12 PM**, with the peak around **9 AM**.

## Detailed Insights

### Daily Trends

1. **Tuesday and Wednesday Peaks:**  
   - The patient count is highest on **Tuesday** (6,091 patients) and **Wednesday** (6,264 patients).  
   - Wait times tend to be higher on these days due to the surge in patient numbers.

2. **Monday Anomaly:**  
   - **Monday** experiences the longest average wait time (~50 minutes) despite having a lower patient count compared to Tuesday and Wednesday.  
   - This suggests a potential **bottleneck in operations** on Mondays, possibly caused by administrative backlogs from the weekend.

3. **Weekend Patterns:**  
   - **Saturday** and **Sunday** have the lowest patient counts, as well as the shortest wait times.  
   - This is likely due to the shift in patient visits from elective procedures during the week to more urgent/emergency visits on weekends.

### Hourly Patterns

1. **Morning Surge:**  
   - The **9 AM to 12 PM** window experiences the highest wait times, with the **9 AM** slot showing the most congestion.  
   - This could be caused by patients arriving early, expecting to be seen sooner, but overwhelming hospital resources in the early hours.

2. **Midday Peak Congestion:**  
   - Wait times are at their highest between **12 PM and 3 PM** on **Tuesday** and **Wednesday**.  
   - This period sees both high patient volumes and extended wait times, suggesting that resource allocation during midday is insufficient to handle the influx.

3. **Low Wait Times in Early and Late Hours:**  
   - Wait times before **9 AM** and after **6 PM** are consistently low.  
   - This suggests that patient volumes are lower during these hours, presenting an opportunity to **redistribute patient appointments** and better manage hospital resources.

### Bottleneck Analysis

- **Monday Operational Inefficiency:**  
  Despite moderate patient numbers, **Monday** has the highest average wait time. This suggests potential inefficiencies in transitioning from the weekend to the start of the week. Administrative or staffing constraints may be responsible for this delay.

- **Midday Resource Strain:**  
  The **12 PM to 3 PM** window consistently shows high wait times, indicating that hospital resources (e.g., staff, consultation rooms) are stretched thin during these hours.

## Recommendations

### 1. **Monday Operations Overhaul**
- **Investigate the root cause** of delays on Monday. Possible areas of concern include:
  - Administrative backlogs from the weekend.
  - Lower staffing levels on Monday mornings.
  - Inefficiencies in patient intake and triage.
  
- **Proposed Actions:**
  - Increase staff availability on Monday mornings.
  - Streamline intake and administrative processes to ensure patients are seen promptly.

### 2. **Optimize Resource Allocation for Midday Hours**
- Peak congestion occurs between **12 PM and 3 PM** on weekdays, particularly **Tuesday** and **Wednesday**.  
- **Proposed Actions:**
  - **Increase staff** (doctors, nurses, administrative personnel) during midday hours to handle the increased patient volume.
  - Adjust shift changes or stagger breaks to ensure full coverage during this period.

### 3. **Stagger Appointment Scheduling**
- The surge of patients around **9 AM** leads to long wait times early in the day.
- **Proposed Actions:**
  - Implement **staggered appointment slots** to evenly distribute patient visits throughout the day, reducing the morning rush.
  - Encourage patients to book appointments during non-peak hours by offering incentives such as reduced wait times or priority service for off-peak slots.

### 4. **Proactive Patient Communication**
- Provide patients with real-time updates on expected wait times, especially during peak periods (9 AM - 12 PM, 12 PM - 3 PM).
- **Proposed Actions:**
  - Use automated text messages or an online portal to keep patients informed about wait times and encourage rescheduling to less busy periods.

## Visualizations
Explore the live interactive dashboard here:
  - [View Dashboard](https://hospital-wait-time-dashboard.onrender.com)

## Installation

If you'd like to analyze the data further or run your visualizations, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hospital-wait-time-analysis.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd hospital-wait-time-analysis
   ```

3. **Install dependencies** (if needed):
   The project uses standard data analysis libraries such as `Pandas`, `Plotly`, and `Dash`. Install them via pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the analysis or explore the visualizations:
1. Ensure you have the required dependencies installed.
2. Execute the analysis script to generate visualizations.
3. To contribute new analyses or improve on current insights, simply fork the repository, make your changes, and submit a pull request.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-name`).
5. Open a Pull Request.

## Screenshots

### Dashboard Overview
![Blue Hart Hospital Dashboard](assets/Blue-Hart-Dashboard.png)

### Sample Visualizations
- **Patient Count by Day:**
  ![Patient Count](assets/Patient-Count.png)

- **Wait Time per Hour:**
  ![Wait Time per Hour](assets/Wait-Time.png)

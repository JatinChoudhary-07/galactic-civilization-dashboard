# Galactic Civilization Dashboard

A data visualization platform for monitoring, comparing, and analyzing fictional interstellar civilizations through interactive dashboards and intelligence reports.

---

## Live Links

| Resource         | Link                                                                          |
| ---------------- | ----------------------------------------------------------------------------- |
| Live Application | https://galactic-civilization-dashboard-bw3w5rjzfhanw896jfmvwm.streamlit.app/ |
| Source Code      | https://github.com/JatinChoudhary-07/galactic-civilization-dashboard          |

---

## Overview

The Galactic Civilization Dashboard allows users to explore a fictional galaxy populated by evolving civilizations.

Each planet possesses unique characteristics such as population, economy, military strength, technological advancement, and happiness levels. Users can analyze historical trends, compare civilizations, generate intelligence reports, and monitor the overall state of the galaxy through an interactive dashboard.

---

## Dashboard Capabilities

| Module              | Description                                                     |
| ------------------- | --------------------------------------------------------------- |
| Planet Intelligence | Displays planet imagery, civilization lore, and current status  |
| Metrics Dashboard   | Shows key civilization indicators and growth trends             |
| Trend Analysis      | Visualizes historical development across multiple metrics       |
| Rankings            | Compares civilizations based on selected performance indicators |
| Comparison Engine   | Allows side by side analysis of multiple planets                |
| PDF Reports         | Generates downloadable civilization intelligence reports        |
| Theme Engine        | Supports both Dark and Light modes                              |

---

## Metrics Tracked

| Metric     | Purpose                         |
| ---------- | ------------------------------- |
| Population | Civilization size and growth    |
| Economy    | Economic development index      |
| Military   | Defense and military capability |
| Technology | Technological advancement level |
| Happiness  | Citizen satisfaction indicator  |

---

## Technology Stack

| Layer             | Technology |
| ----------------- | ---------- |
| Frontend          | Streamlit  |
| Language          | Python     |
| Data Processing   | Pandas     |
| Visualization     | Plotly     |
| Report Generation | ReportLab  |
| Styling           | Custom CSS |

---

# System Architecture

```text
                    Galactic Civilization Dashboard

┌────────────────────────────────────────────────────┐
│                  Civilization Dataset              │
└──────────────────────────┬─────────────────────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │    loader.py     │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │      app.py      │
                  │ Main Controller  │
                  └────────┬─────────┘
                           │

      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼

 Sidebar Layer      Visualization Layer    Utility Layer

      │                    │                    │

      ▼                    ▼                    ▼

 sidebar.py         charts.py            theme.py
                    metrics.py           lore.py
                    rankings.py
                    comparison.py
                    pdf_export.py
                    planet_image.py
                    status.py
```

---

# Dashboard Workflow

```text
User Input
(Planet + Year)
        │
        ▼
Dataset Filtering
        │
        ▼
Civilization Analysis
        │
 ┌──────┼───────────────┬───────────────┬───────────────┐
 │      │               │               │               │
 ▼      ▼               ▼               ▼               ▼

Metrics Trends      Rankings     Comparison     PDF Export
```

---

## Feature Summary

| Feature                | Status |
| ---------------------- | ------ |
| Planet Search          | ✓      |
| Planet Selection       | ✓      |
| Historical Analysis    | ✓      |
| Interactive Charts     | ✓      |
| Civilization Rankings  | ✓      |
| Radar Chart Comparison | ✓      |
| PDF Report Generation  | ✓      |
| Dark Theme             | ✓      |
| Light Theme            | ✓      |
| Responsive Layout      | ✓      |

---

## Project Structure

```text
galactic-civilization-dashboard/

├── app.py
│
├── assets/
│   └── planets/
│
├── components/
│   ├── charts.py
│   ├── comparison.py
│   ├── metrics.py
│   ├── pdf_export.py
│   ├── planet_image.py
│   ├── rankings.py
│   ├── sidebar.py
│   └── status.py
│
├── data/
│   └── galactic_civilization_data.csv
│
├── styles/
│   ├── main.css
│   └── light.css
│
├── utils/
│   ├── loader.py
│   ├── lore.py
│   └── theme.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/JatinChoudhary-07/galactic-civilization-dashboard.git
cd galactic-civilization-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Application

```bash
streamlit run app.py
```

---

## Future Enhancements

| Planned Feature    | Description                               |
| ------------------ | ----------------------------------------- |
| Forecast Engine    | Predict future civilization growth        |
| Resource Analytics | Track resource production and consumption |
| Diplomacy System   | Interplanetary relations and alliances    |
| Galactic Events    | Dynamic events affecting civilizations    |
| Expanded Reports   | Advanced intelligence reporting           |

---

## Author

| Field     | Information                                   |
| --------- | --------------------------------------------- |
| Name      | Jatin Choudhary                               |
| Program   | B.Tech CSE (Blockchain Technology)            |
| Batch     | 2025–2029                                     |

```
```

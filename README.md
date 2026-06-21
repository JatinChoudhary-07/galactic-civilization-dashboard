# Galactic Civilization Dashboard

## Overview

Galactic Civilization Dashboard is an interactive data visualization platform that enables users to explore, analyze, and compare the growth of fictional interstellar civilizations over time.

The application provides historical trend analysis, planetary rankings, civilization comparisons, downloadable reports, and theme customization through an intuitive dashboard interface.

---

## Features

### Civilization Monitoring

* Planet selection
* Year selection
* Planet search
* Civilization status tracking
* Historical performance analysis

### Analytics

* Population trends
* Economic growth tracking
* Military development monitoring
* Technology progression analysis
* Happiness index visualization

### Comparison Tools

* Multi-planet comparison
* Radar chart visualization
* Civilization rankings
* Cross-planet performance analysis

### Reporting

* Downloadable PDF reports
* Current civilization snapshot export

### User Experience

* Dark mode
* Light mode
* Interactive Plotly visualizations
* Responsive dashboard layout

---

## System Architecture

```text
                        ┌─────────────────┐
                        │   CSV Dataset   │
                        └────────┬────────┘
                                 │
                                 ▼
                      ┌────────────────────┐
                      │     loader.py      │
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │       app.py       │
                      │ Dashboard Control  │
                      └─────────┬──────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼

  Sidebar Module        Visualization Layer      Utility Layer

        │                       │                       │

        ▼                       ▼                       ▼

   sidebar.py             charts.py             theme.py
                          rankings.py           lore.py
                          comparison.py
                          metrics.py
                          pdf_export.py
                          planet_image.py
```

---

## Data Flow

```text
Dataset
   │
   ▼
Load Data
   │
   ▼
User Input
(Planet + Year)
   │
   ▼
Filtered Dataset
   │
   ├── Metrics
   ├── Trends
   ├── Rankings
   ├── Comparison
   ├── Planet Intelligence
   └── PDF Reports
```

---

## Project Structure

```text
galactic-dashboard/

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
│   └── sidebar.py
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

## Technology Stack

| Component         | Technology |
| ----------------- | ---------- |
| Frontend          | Streamlit  |
| Language          | Python     |
| Data Processing   | Pandas     |
| Visualization     | Plotly     |
| Report Generation | ReportLab  |
| Styling           | CSS        |

---

## Dashboard Modules

### Metrics Dashboard

Displays current civilization statistics and growth indicators.

### Trend Analysis

Interactive historical analysis for:

* Population
* Economy
* Military
* Technology
* Happiness

### Rankings

Planet rankings based on:

* Economy
* Technology
* Happiness

### Comparison Engine

Allows side-by-side comparison of multiple civilizations using:

* Tabular comparison
* Radar chart visualization

### Planet Intelligence

Provides:

* Planet imagery
* Civilization descriptions
* Lore information

### Report Generator

Creates downloadable PDF reports containing current civilization metrics.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd galactic-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

* Predictive civilization forecasting
* Resource management metrics
* Energy production analytics
* Diplomacy and alliance systems
* Real-time galactic events
* Advanced reporting system

---

## Author

Jatin Choudhary


Batch 2025–2029

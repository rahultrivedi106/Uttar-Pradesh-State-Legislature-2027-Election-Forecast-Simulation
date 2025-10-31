
---

## 🗳️ Uttar Pradesh State Legislature 2027 Election Forecast Simulation
### 📁 Folder Structure
```
up_forecast_2027/
├── data/
│   ├── assembly_2012.csv
│   ├── assembly_2017.csv
│   ├── assembly_2022.csv
│   ├── municipal_2017.csv
│   ├── municipal_2023.csv
├── output/
│   ├── party_seat_forecast_chart.png(auto generate after run)
│   ├── forecast_table.csv( auto generate after run )
├── up_prediction.py
├──code results/
│   ├── image1
│   ├── image2



```

---

### 📌 Project Overview

This project forecasts party-wise seat counts for the **Uttar Pradesh State Legislature Election 2027** using:

- Historical Assembly election results (2012, 2017, 2022)
- Urban Local Body (ULB) performance from municipal elections (2017, 2023)
- AI-powered regression modeling with urban boost logic
- Clean tabular output and colourful year-wise bar chart

---

### ⚙️ Tools & Technologies Used

| Tool/Library        | Purpose                                |
|---------------------|----------------------------------------|
| `pandas`            | Data loading and manipulation          |
| `matplotlib`        | Chart generation and visualization     |
| `scikit-learn`      | Linear regression for AI prediction    |
| `Python 3.x`        | Core scripting language                |

---

### 📊 Data Sources

All data is stored in CSV format inside the `/data` folder:

- `assembly_2012.csv`, `assembly_2017.csv`, `assembly_2022.csv`: Party-wise seat counts
- `municipal_2017.csv`, `municipal_2023.csv`: Mayor wins and Nigam seat counts

---

### 🚀 How to Run

```bash
pip install pandas matplotlib scikit-learn
python up_predictor.py
```

This will:
- Print a party-wise seat comparison table (2012–2027)
- Generate and save a colourful bar chart as `party_seat_forecast_chart.png`

---

### 📉 Forecast Logic

- Linear regression on Assembly seat trends (2012–2022)
- Urban boost factor based on 2023 municipal Nigam seat share
- Final prediction for 2027 seats per party

---
Results :
<img width="3000" height="1200" alt="Generated Image111" src="https://github.com/user-attachments/assets/7bce88de-ad93-4e78-9ac7-d36744aa3605" />



<img width="1000" height="600" alt="image2" src="https://github.com/user-attachments/assets/714abdbf-c2a4-4624-857b-35fa1e2029d5" />




### ⚠️ Disclaimer

This project is intended **solely for educational and learning purposes**.  
All forecasts are based on simplified models and publicly available data.  
It does **not represent any political endorsement, real-world prediction, or electoral consultancy**.


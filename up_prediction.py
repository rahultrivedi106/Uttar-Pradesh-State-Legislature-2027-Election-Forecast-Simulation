import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import os

os.makedirs('output', exist_ok=True)

def load_data():
    df_2012 = pd.read_csv('data/assembly_2012.csv')
    df_2017 = pd.read_csv('data/assembly_2017.csv')
    df_2022 = pd.read_csv('data/assembly_2022.csv')
    df_muni_2017 = pd.read_csv('data/municipal_2017.csv')
    df_muni_2023 = pd.read_csv('data/municipal_2023.csv')
    return df_2012, df_2017, df_2022, df_muni_2017, df_muni_2023

def ai_predict(df_2012, df_2017, df_2022, df_muni_2023):
    parties = df_2022['Party']
    lower_bounds = []
    upper_bounds = []
    mid_points = []

    for party in parties:
        x = np.array([2012, 2017, 2022]).reshape(-1, 1)
        y = np.array([
            df_2012.loc[df_2012['Party'] == party, 'Seats'].values[0],
            df_2017.loc[df_2017['Party'] == party, 'Seats'].values[0],
            df_2022.loc[df_2022['Party'] == party, 'Seats'].values[0]
        ])
        model = LinearRegression().fit(x, y)
        base_pred = model.predict(np.array([[2027]]))[0]

        urban_boost = df_muni_2023.loc[df_muni_2023['Party'] == party, 'Nigam_Seats'].values[0] / 800
        final_pred = base_pred * (1 + 0.05 * urban_boost)

        lower = round(final_pred * 0.95)
        upper = round(final_pred * 1.05)
        mid = round(final_pred)

        lower_bounds.append(lower)
        upper_bounds.append(upper)
        mid_points.append(mid)

    return pd.DataFrame({
        'Party': parties,
        '2027_Lower': lower_bounds,
        '2027_Upper': upper_bounds,
        '2027_Midpoint': mid_points
    })

def generate_table(df_2012, df_2017, df_2022, df_pred):
    merged = pd.merge(pd.merge(df_2012, df_2017, on='Party', suffixes=('_2012', '_2017')),
                      df_2022, on='Party')
    merged = pd.merge(merged, df_pred, on='Party')
    merged.rename(columns={'Seats': '2022'}, inplace=True)
    merged.columns = ['Party', '2012', '2017', '2022', '2027_Lower', '2027_Upper', '2027_Midpoint']
    merged = merged[['Party', '2012', '2017', '2022', '2027_Lower', '2027_Upper']]

    total_row = pd.DataFrame([{
        'Party': '🧮 Total',
        '2012': df_2012['Seats'].sum(),
        '2017': df_2017['Seats'].sum(),
        '2022': df_2022['Seats'].sum(),
        '2027_Lower': df_pred['2027_Lower'].sum(),
        '2027_Upper': df_pred['2027_Upper'].sum()
    }])

    final_table = pd.concat([merged, total_row], ignore_index=True)
    print("\n🗳️ UP Vidhan Sabha Party-wise Seat Forecast Table (Range-Based)\n")
    print(final_table)
    final_table.to_csv('output/forecast_table.csv', index=False)

def generate_chart(df_pred, df_2012, df_2017, df_2022):
    parties = df_pred['Party']
    years = ['2012', '2017', '2022', '2027']
    colors = ['teal', 'orange', 'purple', 'green']
    bar_width = 0.2
    x = np.arange(len(parties))

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, df in enumerate([df_2012, df_2017, df_2022]):
        ax.bar(x + i * bar_width, df['Seats'], width=bar_width, label=years[i], color=colors[i])

    ax.bar(x + 3 * bar_width, df_pred['2027_Midpoint'], width=bar_width,
           label='2027 (AI Forecast)', color=colors[3])

    ax.set_xticks(x + 1.5 * bar_width)
    ax.set_xticklabels(parties)
    ax.set_ylabel('Seat Count')
    ax.set_title('UP Vidhan Sabha Party-wise Seat Comparison (2012–2027)')
    ax.legend()
    plt.tight_layout()
    plt.savefig('output/party_seat_forecast_chart.png')
    plt.show()

if __name__ == "__main__":
    df_2012, df_2017, df_2022, df_muni_2017, df_muni_2023 = load_data()
    df_pred = ai_predict(df_2012, df_2017, df_2022, df_muni_2023)
    generate_table(df_2012, df_2017, df_2022, df_pred)
    generate_chart(df_pred, df_2012, df_2017, df_2022)
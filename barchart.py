import pandas as pd
import bar_chart_race as bcr

# Load your original data
df = pd.read_csv('international_results.csv')
df['Match Date'] = pd.to_datetime(df['Match Date'])

# Total number of records in the dataset
print(f"Total records in the dataset: {len(df)}")

# Get the unique team names from both 'Team 1' and 'Team 2'
unique_teams = pd.concat([df['Team 1'], df['Team 2']]).unique()

# Create a DataFrame to store the winning counts for each team
end_date = pd.to_datetime('2023-08-01')
start_date = pd.to_datetime('2015-01-01')
team_wins = pd.DataFrame(columns=['Match Date'] + list(unique_teams))
team_wins['Match Date'] = pd.date_range(start=start_date, end=end_date)

# Initialize the winning counts for each team to 0
team_wins.iloc[:, 1:] = 0

# Iterate through the filtered data to update the winning counts
for index, row in df.iterrows():
    winner = row['Winner']
    match_date = row['Match Date']

    # Check if the winner is a valid team name before updating
    if winner in team_wins.columns:
        team_wins.loc[team_wins['Match Date'] == match_date, winner] += 1

# Create a copy of the team_wins DataFrame to accumulate the counts
accumulated_wins = team_wins.copy()

# Set 'Match Date' as the index for the wide_data DataFrame
wide_data = accumulated_wins.set_index('Match Date')

# Resample the data to get weekly counts and start from 0
weekly_wins = wide_data.resample('W').sum().fillna(0)
weekly_wins = weekly_wins.cumsum()
print(weekly_wins)

# Calculate the total matches played weekly
# total_matches_played_weekly = weekly_wins.sum(axis=1)
# print(total_matches_played_weekly)

bcr.bar_chart_race(
    title='Top 15 Cricket Teams',
    df=weekly_wins,
    filename='top_winning_teams_accumulated_weekly.mp4',
    orientation='h',
    sort='desc',
    n_bars=15,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=1,
    period_length=250,  # Adjust this value to reduce the video length (e.g., 250 milliseconds)
    interpolate_period=True,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    figsize=(10, 6),
    filter_column_colors=True,
    cmap='Antique',
    writer='ffmpeg',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
    's': f'Total Matches: {v.sum():,.0f}',
    'ha': 'right', 'size': 12, 'family': 'Courier New'},
)

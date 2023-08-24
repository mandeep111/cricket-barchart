import pandas as pd
import matplotlib.pyplot as plt

# Your dataset
csv_file_path = "international_results.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
# Create a DataFrame
df = pd.DataFrame(df, columns=["S.N", "Team 1", "Team 2", "Winner", "Margin", "Ground", "Match Date", "Scorecard"])

# Count the number of matches played by each team
matches_played = pd.concat([df["Team 1"], df["Team 2"]]).value_counts()
print( matches_played)
# Count the number of matches won by each team
matches_won = df["Winner"].value_counts()
print(matches_won)
# Create a histogram
fig, ax = plt.subplots(figsize=(10, 6))

# Plot matches played
ax.bar(matches_played.index, matches_played.values, label="Matches Played", alpha=0.7)
# Plot matches won
ax.bar(matches_won.index, matches_won.values, label="Matches Won", alpha=0.7)

# Customize the plot
ax.set_xlabel("Teams")
ax.set_ylabel("Number of Matches")
ax.set_title("Number of Matches Played and Won by Each Team")
ax.legend()

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

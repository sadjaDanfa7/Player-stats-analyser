import pandas as pd
data = {
    "players": ["sadja", "charlie", "josh"],
    "age": ["18","18", "18"],
    "goals": ["23", "12", "15"],
    "assits":["10", "12", "14"],
    "team":["NO TEAM", "american team", "heston fc"]
}
df =pd.DataFrame(data)
print(df)
df["goals"] = pd.to_numeric(df["goals"])
print("aveage goals:", df["goals"].mean())

top_scorer = df.loc[df["goals"].idxmax()]
print("top scorer:", top_scorer["players"])

df.to_csv("player_stats.csv", index=False)
print("file created : player_stats.csv") 

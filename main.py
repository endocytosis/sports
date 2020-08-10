from sportsreference.nfl.teams import Teams
season = input("What season do you want to know about: ")
print("Great, gathering information on the", season, "season")
teams = Teams(season)
w = 0
l = 0
best_record = 0 #team with the best record during the season
best_team = 'Unknown' #string name of the best team
best_team_wins = 0
best_team_losses = 0

for team in teams:
    #print(team.name, team.wins, team.losses)
    w = team.wins
    l = team.losses
    winloss = w/l
    #print("Win/loss ratio", winloss)
    if winloss > 0 and winloss > best_record:
            best_team = team.name
            best_record = winloss
            best_team_wins = w
            best_team_losses = l

print("The best team is:", best_team)
print("They had", best_team_wins, "wins and", best_team_losses, "losses.")
print("They had a win/loss ratio of:", best_record)

#print team names, print team wins, team losses
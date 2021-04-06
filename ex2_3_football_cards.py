# Most football fans love it for the goals and excitement. Well, this problem doesn't. 
# You are to handle the referee's little notebook and count the players who were sent off for fouls 
# and misbehavior. 
# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered 
# from 1 to 11. Any player may be sent off the field by being given a red card. If one of the teams has 
# less than 7 players remaining, the game is stopped immediately by the referee, and the team with 
# less than 7 players loses. A card is a string with the team's letter ('A' or 'B') followed by a single
# dash and player's number. e.g.the card 'B-7'means player #7 from team B received a card. 
# (index 6 of the list)
# The task: Given a list of cards (could be empty), return the number of remaining players on each 
# team at the end of the game in the format: "Team A -{players_count}; Team B -{players_count}". If 
# the game was terminated print an additional line: "Game was terminated

card_list = input().split()
cards_A = 0
cards_B = 0
terminated = False
team_size = 11

for card in range(len(card_list)):

    if card_list[card][0] == 'A':
        cards_A +=1
    
    if card_list[card][0] == 'B':
        cards_B += 1 

    if (team_size - cards_A) < 7 or (team_size - cards_B) < 7: # less than 7 players left...
        terminated = True
        break

print("Team A: - " + str(team_size - cards_A) + "; Team B: - " + str(team_size - cards_B) )
if terminated:
    print("Game was terminated")

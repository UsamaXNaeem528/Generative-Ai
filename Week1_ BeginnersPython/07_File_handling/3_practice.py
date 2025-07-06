player_scores = { 
}
with open(r'Week1_ BeginnersPython\07_File_handling\scores.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        print(type(tokens))
        player = tokens[0]
        score = int(tokens[1])  # after converting int into the \n with player score is removed
        print(player,score)
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]   #==> dict ka andar new key : value add karna
print(player_scores)

for player_name, player_score in player_scores.items():
    max_score = max(player_score)
    min_score = min(player_score)
    avg_score = sum(player_score) / len(player_score)
    print(f'{player_name} ===> Min:{min_score}, Max:{max_score}, Avg:{avg_score}')






    

        
         
    
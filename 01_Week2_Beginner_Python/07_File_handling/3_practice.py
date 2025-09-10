"""
Question:

You are given a CSV file scores.csv where each line contains a player's name followed by their score,
separated by a comma (e.g., Alice,45). Write a Python program to read this file and do the following:

Store the scores of each player in a dictionary,
where the key is the player's name and the value is a list of their scores.

For each player, calculate and display:
The minimum score
The maximum score
The average score

Sample output format:
Alice ===> Min:30, Max:90, Avg:60.0
Bob ===> Min:40, Max:70, Avg:55.0
"""

player_scores = { 
}
with open(r'C:\Users\Admin\OneDrive\Desktop\Gen Ai\1_Python\07_File_handling\scores.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        # print(type(tokens))#
        player = tokens[0]
        score = int(tokens[1])  # after converting int into the \n with player score is removed
        # print(player,score)
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






    

        
         
    
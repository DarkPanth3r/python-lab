#Program checks how many hits were found from a lotery bet.
drawn = [5, 11, 9, 42, 3, 49] 
bets = [3, 7, 11, 42, 34, 49] 
hits = 0 
hit_list = [] 

for number in bets: 
    if number in drawn: 
        hits += 1 
        hit_list.append(number) 

print(hits) 
print(hit_list) 
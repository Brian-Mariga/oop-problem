def scoreboard(participants):
    results =[]
    for participant in participants:
        score = 0
        score += participant.get('chickenwings', 0) * 5
        score += participant.get('hamburgers', 0) * 3
        score += participant.get('hotdogs', 0) * 2
        results.append({'name': participant['name'], 'score': score})
    results.sort(key=lambda x: (-x['score'], x['name']))
    print(results)


scoreboard([
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11},
    {'name': "Small Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
])
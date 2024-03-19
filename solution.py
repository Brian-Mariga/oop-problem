def scoreboard(participants):
    results =[]
    for participant in participants:
        score = participant['chickenwings']*5 + participant['hamburgers']*3 + participant['hotdogs']*2
        results.append({'name': participant['name'], 'score': score})
    results.sort(key=lambda x: (-x['score'], x['name']))
    print(results)


scoreboard([
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
])
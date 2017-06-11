def print_max_activities(activities):
    choise,activities = activities[0],activities[1:]
    print(choise)
    for i in activities:
        if i[0] >= choise[1]:
            choise = i
            print(choise)

if __name__ == '__main__':
    #[(start,finish)]
    activities = [(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
    activities.sort(key=lambda x : x[1]) #Bitişe göre sıralama
    print_max_activities(activities)

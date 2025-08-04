friends = 5
out = 1
DUNBAR = 150
weeks = 0
while(friends < DUNBAR):
    friends = (friends - out) * 2
    out += 1
    weeks += 1
    print("Professor had", friends, "friends in week", weeks)

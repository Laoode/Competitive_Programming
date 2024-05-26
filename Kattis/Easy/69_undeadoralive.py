inp = input()


if ':)' in inp and ':(' in inp:
    print('double agent')
elif ':)' in inp:
    print("alive")
elif ':(' in inp:
    print('undead')
else:
    print("machine")
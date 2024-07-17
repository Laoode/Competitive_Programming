g, s, c = map(int, input().split())

card_cost = {"Province": 8, "Duchy": 5, "Estate": 2}
card_buy = {"Gold": 6, "Silver": 3, "Copper": 0}

total_buying_power = g * 3 + s * 2 + c * 1

if total_buying_power >= card_cost["Province"]:
    best_victory = "Province"
elif total_buying_power >= card_cost["Duchy"]:
    best_victory = "Duchy"
elif total_buying_power >= card_cost["Estate"]:
    best_victory = "Estate"
else:
    best_victory = None

if total_buying_power >= card_buy["Gold"]:
    best_treasure = "Gold"
elif total_buying_power >= card_buy["Silver"]:
    best_treasure = "Silver"
else:
    best_treasure = "Copper"

if best_victory:
    print(f"{best_victory} or {best_treasure}")
else:
    print(best_treasure)
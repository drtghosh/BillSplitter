card_value = {}
min_number, max_number = 2, 11
for i in range(min_number, max_number):
    card_value[f'{i}'] = i
card_value['Jack'] = 11
card_value['Queen'] = 12
card_value['King'] = 13
card_value['Ace'] = 14

cards = 6
total_value = 0
for _ in range(cards):
    hand_card = input()
    total_value += card_value[hand_card]

print(total_value / cards)
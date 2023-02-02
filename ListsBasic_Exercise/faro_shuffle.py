deck_of_cards = list(input().split())
count_of_shuffles = int(input())
half = int(len(deck_of_cards) / 2)

result = []

for shuffle in range(count_of_shuffles):
    result = []
    for i in range(half):
        result.append(deck_of_cards[i])
        result.append(deck_of_cards[i + half])

    deck_of_cards = result

print(result)

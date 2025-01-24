from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check_cards = list(map(int, input().split()))

card_counter = Counter(cards)

print(' '.join(str(card_counter[card]) for card in check_cards))
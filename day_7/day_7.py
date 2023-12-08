from collections import defaultdict, Counter

CARDS = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def get_type(cards: str) -> int:
    card_mapping = Counter(cards)
    if 5 in card_mapping.values():
        return 6
    elif 4 in card_mapping.values():
        return 5
    elif 3 in card_mapping.values() and 2 in card_mapping.values():
        return 4
    elif 3 in card_mapping.values():
        return 3
    elif list(card_mapping.values()).count(2) > 1:
        return 2
    elif 2 in card_mapping.values():
        return 1
    return 0


def get_order(cards: str) -> list:
    return [CARDS.get(card, card) for card in cards]


def best_swap(cards: str) -> int:
    combinations = []
    possible_swaps = list(CARDS.keys())[1:]
    for possible_swap in possible_swaps:
        combination = cards.replace("J", possible_swap)
        combinations.append(combination)

    result = 0
    for combination in combinations:
        value = get_type(cards=combination)
        result = max(result, value)
    return result


def combine_sort(cards: str) -> tuple[int, int]:
    if "J" not in cards:
        return get_type(cards=cards), get_order(cards=cards)
    return best_swap(cards), get_order(cards=cards)


data = defaultdict(int)
with open("input.txt") as input_file:
    lines = input_file.readlines()
    for line in lines:
        cards, bid = line.strip().split()
        data[cards] = int(bid)

all_cards = list(data.keys())
all_cards.sort(key=lambda x: combine_sort(x))

result = 0
for index, cards in enumerate(all_cards):
    index += 1
    result += index * data[cards]

print(f"Part 2: {result}")

def maybe_move(items: list[str], first: str, second: str):
    first_idx = items.index(first)
    second_idx = items.index(second)

    if first_idx > second_idx:
        first_item = items.pop(first_idx)
        items.insert(second_idx, first_item)  # inserts before the given index.
        return True
    return False


def recoverSecret(triplets):
    # add all the chars in the triplets
    items = list(set([c for t in triplets for c in t]))

    while True:
        # print("Current state: ", items)

        conditions_satisfied_cnt = 0

        for triplet in triplets:
            if not maybe_move(items, triplet[0], triplet[1]):
                conditions_satisfied_cnt += 1

            if not maybe_move(items, triplet[1], triplet[2]):
                conditions_satisfied_cnt += 1

        if conditions_satisfied_cnt == len(triplets) * 2:
            break

    return "".join(items)


secret = "whatisup"
triplets = [["t", "u", "p"], ["w", "h", "i"], ["t", "s", "u"], ["a", "t", "s"], ["h", "a", "p"], ["t", "i", "s"], ["w", "h", "s"]]

assert recoverSecret(triplets) == secret

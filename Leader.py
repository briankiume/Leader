from collections import Counter


def leaders(a):
    indexes = []
    for i in range(len(a)):
        seq_1 = a[:i + 1]
        seq_2 = a[i + 1:]
        counts_1 = Counter(seq_1)
        counts_2 = Counter(seq_2)
        try:
            possible_dom_1 = counts_1.most_common(1)[0]
            possible_dom_2 = counts_2.most_common(1)[0]
        except IndexError:
            continue

        occurrences_1 = possible_dom_1[1]
        occurrences_2 = possible_dom_2[1]
        dom_key_1 = possible_dom_1[0]
        dom_key_2 = possible_dom_2[0]
        if dom_key_1 == dom_key_2:
            if (occurrences_1 > (len(seq_1) / 2)) & (occurrences_2 > (len(seq_2) / 2)):
                indexes.append(i)
    eqs = len(indexes)
    return eqs


print(leaders([4, 3, 4, 4, 4, 2]))

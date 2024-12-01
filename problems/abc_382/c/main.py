N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


class Person:

    def __init__(self, bishokudo, index):
        self.bishokudo = bishokudo
        self.index = index

    def __lt__(self, other):
        return self.bishokudo < other.bishokudo

    def __repr__(self):
        return f"[index: {self.index}, bishokudo:{self.bishokudo}]"


people = []
for i, a in enumerate(A):
    p = Person(a, i)
    people.append(p)
people.sort()
# print(people)


for b in B:
    ng = -1
    ok = N

    def is_ok(index):
        if index < 0:
            return False
        if index >= N:
            return True
        return b >= people[index].bishokudo

    while (ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

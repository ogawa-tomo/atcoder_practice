points = list(map(int, input().split()))

S = ["A", "B", "C", "D", "E"]


class Person:
    def __init__(self, name, point):
        self.name = name
        self.point = point

    def __repr__(self):
        return f"[name: {self.name}, point: {self.point}]"

    def __lt__(self, other):
        return self.point > other.point


people: list[Person] = []
for i in range(1, 32):
    name = []
    point = 0
    for shift in range(5):
        if i >> shift & 1:
            name.append(S[shift])
            point += points[shift]
    person = Person("".join(name), point)
    # names.append(name)
    people.append(person)
# people.sort()
sorted_people = sorted(people, key=lambda person: person.name)
sorted_people.sort()
# print(sorted_people)
for person in sorted_people:
    print(person.name)

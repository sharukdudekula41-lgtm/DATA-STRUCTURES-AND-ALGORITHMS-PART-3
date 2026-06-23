
import collections

DoubleEnded = collections.queue(["Mon","Tue","Wed"])

DoubleEnded.append("Thu")

print("Append at right -")
print("DoubleEnded")

DoubleEnded.appendedleft("Sun")

print("Appended at right at left is -")
print(DoubleEnded)

DoubleEnded.pop()

print("Deleting from right -")
print(DoubleEnded)

DoubleEnded.popleft()

print("Deleting from left -")
print(DoubleEnded)
Appended at right -
dequeue(['Mon','Tue','Wed','Thu'])
Appended at right at left is -
dequeue(['Sun','Mon','Tue','Wed','Thu'])

Deleting from right -
dequeue(['Sun','Mon','Tue','Wed'])
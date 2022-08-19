'''
In our particular instance of the game, the target rewards 4 different amounts
of points, depending on where the dart lands:

If the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points.
The outer circle has a radius of 10 units (this is equivalent to the total radius for the target),
the middle circle a radius of 5 units, and the inner circle a radius of 1.
Of course, they are all centered at the same point
(that is, the circles are concentric) defined by the coordinates (0, 0).
'''
def score(x, y):
    if abs(x) > 10 or abs(y) > 10:
        return 0
    elif abs(x) > 5 or abs(y) > 5:
        return 1
    elif abs(x) > 1 or abs(y) > 5:
        return 5
    elif abs(x) <= 1 and abs(y) <= 1:
        return 10

"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """
        Decrement Alien health by one point.
        """
        self.health -=1

    def is_alive(self):
        """
        Return a boolean for if Alien is alive (health > 0).
        """
        return bool(self.health > 0)

    def teleport(self, x_coordinate: int, y_coordinate: int):
        """
        Move Alien object to new coordinates
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other):
        """
        TBD
        """

def new_aliens_collection(coordinates_list: list):
    """
    docstring
    """
    alien_list = []
    for coordinate in coordinates_list:
        alien_list.append(Alien(coordinate[0],coordinate[1]))
    return alien_list

jujuba = Alien(2,2)
print(jujuba.x_coordinate)
jujuba.teleport(7,8)
print(jujuba.x_coordinate)
"""Head
Torso
Arm
Hand
Leg
Feet"""

class Feet:
    def __init__(self):
        pass

class Leg:
    def __init__(self, feet : Feet):
        self.feet = feet

class Hand:
    def __init__(self):
        pass


class Arm:
    def __init__(self, hand : Hand):
        self.hand = hand

class Torso:
    def __init__(self, right_arm, left_arm, right_leg, left_leg, head):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Head:
    def __init__(self):
        pass

class Human:
    def __init__(self, torso):
        self.torso = torso

#manos
right_hand = Hand()
left_hand = Hand()

#pies
right_feet = Feet()
left_feet = Feet()

#cabeza
head = Head()

#brazos
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

#piernas
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

#torso
torso = Torso(right_arm, left_arm, right_leg, left_leg, head)

#humano
human =Human(torso)


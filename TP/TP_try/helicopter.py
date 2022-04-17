
class   Helicopter():
    """
        This class is an abstraction of a combat helicopter carrying soldiers.
    """
    def __init__(self):
        self.crew = 6
        self.healthy_soldiers = self.crew
        self.wounded_soldiers = 0
        self.loaded_bullets = 30
        self.stock_bullets = 120
        self.speed = 70


    def accelerate(self, speed):
        """ Increases the speed of the helicopter by speed km/h """
        self.speed += speed
        print("Speed is now at ", speed)


    def decelerate(self, speed):
        """ Decreases the speed of the helicopter by speed km/h, floored to 0 """
        if self.speed - speed < 0:
            self.speed = 0
            print("Speed is now at ", self.speed)
        else:
            self.speed -= speed
            print("Speed is now at ", self.speed)


    def shoot(self, nb_bullets):
        """ Shoots nb_bullets, reloading other bullets if needed. Displays a
        warning when stock_bullets is equal to 0 (no more ammos)."""
        while nb_bullets > 0 and loaded_bullets > 0:
            self.nb_bullets -= 1
            self.loaded_bullets -= 1
            if loaded_bullet == 0:
                if self.stock_bullets == 0:
                    print("We don't have any bullets !")
                    break
                elif self.stock_bullets <= 30:
                    self.loaded_bullets = self.stock_bullets
                    self.stock_bullets = 0
                else:
                    self.loaded_bullets = 30
                    self.stock_bullets -= 30


    def hit(self):
        """ The helicopter takes a hit. Wounded soldiers die, and one healthy
        soldier gets wounded."""
        self.crew -= self.wounded_soldiers

        print("We are hit !")
        print("{} soldiers are dead !".format(self.wounded_soldiers))
        print("A soldier got wounded !")

        self.healthy_soldiers -= 1
        self.wounded_soldiers += 1


    def land(self):
        """ Land the helicopter on the ground. Sets the speed to 0, and heals one man """
        self.speed = 0
        self.wounded_soldiers -= 1
        self.healthy_soldiers += 1
        print("We are landing !")


    def emergency_ejection(self, nb_soldiers):
        """ Just in case... ejects nb_soldiers out of the helicopter to parachute them """
        if nb_soldiers <= self.crew:
            print("Ejection of {} soldier(s) !".format(nb_soldiers))
            self.crew -= nb_soldiers

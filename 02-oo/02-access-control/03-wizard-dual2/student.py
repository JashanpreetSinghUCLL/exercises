class Wizard:
    def cast_fireball(self, target):
        if self.__mana >= 20:
            self.__mana -= 20
            target.get_fireballed()
            return f"{self.name} casts fireball at {target.name}"
        else:
            raise ValueError(f"{self.name} cannot cast fireball")
            



    # don't touch below this line

    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        fireball_damage = 30
        self.__health -= fireball_damage
        if self.__health <= 0:
            print(f"{self.name} is dead")

    def drink_mana_potion(self):
        self.__mana += 40

wizard = Wizard("Jashan")
wizard2 = Wizard("Sonam")
print(wizard.cast_fireball(wizard2))
print(wizard.get_mana())
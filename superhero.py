class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.__health = 100  # Encapsulated attribute

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
        return f"{self.name} takes {damage} damage. Health: {self.__health}"

    def move(self):
        return f"{self.name} moves with basic agility."

class Superhero(Hero):
    def __init__(self, name, power, special_ability):
        super().__init__(name, power)
        self.special_ability = special_ability

    def move(self):
        return f"{self.name} uses {self.special_ability} to move swiftly!"

    def use_power(self):
        return f"{self.name} unleashes {self.power}!"

# Example usage
if __name__ == "__main__":
    hero = Hero("Common Hero", "Strength")
    super_hero = Superhero("Spider-Man", "Web-Slinging", "web-swinging")
    print(hero.move())
    print(super_hero.move())
    print(super_hero.use_power())
    print(hero.take_damage(20))
    print(super_hero.take_damage(30))

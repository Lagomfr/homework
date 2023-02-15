class Hero:
    ...

    def __init__(self, name, ability):
        self.name = name
        self.ability = ability


class HeroSuper(Hero):

    def __init__(self, name, ability):
        super().__init__(name, ability)

    def __str__(self):
        return f'name is {self.name}\n' \
               f'ability is {self.ability}'

    def prints(self):
        print(f"his name is {self.name} and it is super_hero")

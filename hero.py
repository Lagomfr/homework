class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f'nickname is {self.nickname}\n' \
               f'superpower is {self.superpower}\n' \
               f'health points = {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


class FlyingHero(SuperHero):
    people1 = 'flying_people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.flight = fly

    def squaring_health_points(self):
        self.health_points = self.health_points * self.health_points
        self.flight = True

    def prints_flying(self):
        return f'fly in the {self.flight}_phrase'


class SpaceHero(FlyingHero):
    people2 = 'space_people'


class Villain(SpaceHero):
    monster = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2


if __name__ == "__main__":
    first_hero = SuperHero('Bruce Wayne', 'Batman', 'Money', 100, 'I am Batman!')
    print(f'name is {first_hero.get_name()}')
    first_hero.double_health_points()
    print(f'length of the catchphrase is {len(first_hero)}')
    print(first_hero)
    print()
    sky_hero = FlyingHero('Tony Stark', 'Iron Man', 'Intelligence', 100, 'I am the Iron man', 50)
    sky_hero.squaring_health_points()
    print(sky_hero.prints_flying())
    print(sky_hero)
    print()
    space_hero = SpaceHero('Кэрол Дэнверс', 'капитан марвел', 'СВЕРХ СИЛА', 1000, 'я крутая', 500)
    space_hero.squaring_health_points()
    print(space_hero.prints_flying())
    print(space_hero)
    print()
    super_villain = Villain('дуэйн джонсон', 'Black Adam', 'сила богов', 1000, 'GigaChad', 500)
    super_villain.crit()
    print(super_villain)

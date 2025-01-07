from task1.models import Buyer, Game

def run():
    # Создание покупателей
    buyer1 = Buyer.objects.create(name="Ilya", balance=1500.05, age=24)
    buyer2 = Buyer.objects.create(name="Terminator2000", balance=42.15, age=52)
    buyer3 = Buyer.objects.create(name="Ubivator432", balance=0.5, age=16)

    # Создание игр
    game1 = Game.objects.create(title="Cyberpunk 2077", cost=31, size=46.2, description="Game of the year", age_limited=True)
    game2 = Game.objects.create(title="Mario", cost=5, size=0.5, description="Old Game", age_limited=False)
    game3 = Game.objects.create(title="Hitman", cost=12, size=36.6, description="Who kills Mark?", age_limited=True)

    # Связи между покупателями и играми
    game1.buyers.set([buyer1])
    game2.buyers.set([buyer1, buyer2])
    game3.buyers.set([buyer1])

    game2.buyers.add(buyer3)

    print("Данные успешно добавлены!")

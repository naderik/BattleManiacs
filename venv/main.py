from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg":60},
         {"name": "Thunder", "cost": 15, "dmg":80},
         {"name": "Blizzard", "cost": 10, "dmg":60}]

player = Person(500, 65, 60, 35, magic)
enemy = Person(1200, 65, 45 , 35, magic)




import random

class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12

    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)


    def make_extra_walls(self, count=3):
        # skapa väggar
        x = random.randint(2, self.width - 7)
        y = random.randint(2, self.height - 7)



        for _ in range(count):
            # Rita väggen Före vi förflyttar x
            for i in range(5):
                self.set(x + i, y, self.wall)  # horisontell
            for i in range(1, 5):
                self.set(x, y + i, self.wall)  # vertikal

            # Förflytta sedan till nästa position
            x += 6
            if x > self.width - 7:
                break

    def make_trap(self):
        trap_x = random.randint(1, self.width - 2)
        trap_y = random.randint(1, self.height - 2)
        # test utskrift
        #print(f"trap x position{trap_x} trap y position{trap_y}")
        #print(f"höjd {self.height} bredd {self.width}")

        # Försök placera fällan, flytta ett steg om blockerad
        for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            if self.is_empty(trap_x + dx, trap_y + dy):
                trap_x, trap_y = trap_x + dx, trap_y + dy
                # testutskrift ny position
                #print(f"new trap x position{trap_x} new trap y position{trap_y}")
                #print(f"höjd {self.height} bredd {self.width}")
                self.set(trap_x, trap_y,"T")
                break

    # skapa exit
    def make_exit(self):
        trap_x = random.randint(1, self.width - 2)
        trap_y = random.randint(1, self.height - 2)


        # Försök placera Exit, flytta ett steg om blockerad
        for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            if self.is_empty(trap_x + dx, trap_y + dy):
                trap_x, trap_y = trap_x + dx, trap_y + dy
                self.set(trap_x, trap_y,"E")
                break


    # Används i filen pickups.py

    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty


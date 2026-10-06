class Player():
        
    def __init__(self):
        self.players = {}
        self.scores = {}

    def create_player(self, player_id: str = "", name: str = "") -> bool:
        if player_id in self.players:
            return False
        if player_id is None or player_id == "":
            return False
        if name is None or name == "":
            return False
        else:
            self.players[player_id] = {
                "name": name,
                "points": 0
            }

            self.scores[player_id] = []

            return True


    def add_points(self, player_id: str = "", points: int = 0, round_number: int = 0, timestamp: int = 0) -> bool:
        if player_id not in self.players:
            return False
        if player_id is None or player_id == "":
            return False
        if points is None:
            return False
        if round_number is None or round_number <= 0:
            return False
        if timestamp is None or timestamp < 0:
            return False
        else:
            new_score = {
                "points": points,
                "round_number": round_number,
                "timestamp": timestamp
            }

            self.scores[player_id].append(new_score)

            self.players[player_id]["points"] += points

            return True
            
            
t = Player()

print(t.create_player("P1", "Thalys"))
print(t.add_points("P1", 25, 1, 2))

print(t.__dict__)

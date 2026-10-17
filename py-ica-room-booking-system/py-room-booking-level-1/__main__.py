class Cadastro():

    def __init__(self):
        self.rooms = {}
        self.bookings = {}

    def create_room(self, room_id : str = "", name : str = "", capacity : int = 1) -> bool:
        if room_id is None or room_id == "":
            return False
        if room_id in self.rooms:
            return False
        if name is None or name == "":
            return False
        if capacity is None or capacity <= 0:
            return False

        self.rooms[room_id] = {
            "name": name,
            "capacity": capacity
        }

        self.bookings[room_id] = []

        return True

    def book_room(self, room_id : str = "", user_id : str = "", start : int = 1, end : int = 60) -> bool:
        if room_id is None or room_id == "":
            return False
        if room_id not in self.rooms:
            return False
        if room_id not in self.bookings:
            return False
        if user_id is None or user_id == "":
            return False
        if start <= 0 or end <= 0:
            return False
        if start >= end:
            return False
        
        for b in self.bookings[room_id]:
            bStart = b["start"]
            bEnd = b["end"]

            if bStart < end and start < bEnd:
                return False
                
        new_booking = {
            "user_id": user_id,
            "start": start,
            "end": end
        }

        self.bookings[room_id].append(new_booking)

        return True
        

    def get_room_info(self, room_id : str = "") -> dict | None:
        if room_id is None or room_id == "":
            return None
        if room_id not in self.rooms:
            return None
        if room_id not in self.bookings:
            return None

        return {
            "room_id": room_id,
            "name": self.rooms[room_id]["name"],
            "capacity": self.rooms[room_id]["capacity"],
            "total_bookings": len(self.bookings[room_id])
        }
        

t = Cadastro()

print(t.create_room("DTC01", "Marvin's Room"))
print(t.create_room("DTC02", "Marvin's Room II", 5))
print(t.book_room("DTC01", "Drake", 20, 120))
print(t.book_room("DTC01", "Drake", 120, 170))

print(t.bookings)
print(t.get_room_info("DTC01"))
        
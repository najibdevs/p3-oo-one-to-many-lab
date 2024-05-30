# owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only instances of Pet can be added as pets")
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        self.all.append(self)

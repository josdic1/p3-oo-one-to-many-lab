class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type.lower() not in self.PET_TYPES:
            raise Exception(f"'{pet_type}' is not a valid pet type.")
        self._name = name
        self._pet_type = pet_type.lower()
        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance.")
        self._owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"Pet(name='{self._name}', type='{self._pet_type}')"

    @property
    def name(self):
        return self._name

    @property
    def pet_type(self):
        return self._pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if not isinstance(new_owner, Owner):
            raise Exception("Must be an Owner instance.")
        self._owner = new_owner


class Owner:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
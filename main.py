# Реалізуйте базу даних зі штрафами податкової
# інспекції. Ідентифікувати кожну конкретну людину буде
# персональний ідентифікаційний код. В однієї людини може
# бути багато штрафів.
# Реалізуйте:
# 1. Повний друк бази даних;
# 2. Друк даних за конкретним кодом;
# 3. Друк даних за конкретним типом штрафу;
# 4. Друк даних за конкретним містом;
# 5. Додавання нової людини з інформацією про неї;
# 6. Додавання нових штрафів для вже існуючого запису;
# 7. Видалення штрафу;
# 8. Заміна інформації про людину та її штрафи.
# Використайте дерево для реалізації цього завдання.


class FinesClass:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_fine(self, data):
        if data["id"] == self.data["id"]:
            return
        if data["id"] < self.data["id"]:
            if self.left:
                self.left.add_fine(data)
            else:
                self.left = FinesClass(data)
        else:
            if self.right:
                self.right.add_fine(data)
            else:
                self.right = FinesClass(data)

    def order(self):
        elements = []
        if self.left:
            elements += self.left.order()
        elements.append(self.data)
        if self.right:
            elements += self.right.order()
        return elements

    def search_by_id(self, id_val):
        if self.data["id"] == id_val:
            return True
        if id_val < self.data["id"]:
            if self.left:
                return self.left.search_by_id(id_val)
            else:
                return False
        else:
            if self.right:
                return self.right.search_by_id(id_val)
            else:
                return False

    def search_by_fine_type(self, fine_type):
        if self.data["Fine"] == fine_type:
            return True
        if fine_type < self.data["Fine"]:
            if self.left:
                return self.left.search_by_fine_type(fine_type)
            else:
                return False
        else:
            if self.right:
                return self.right.search_by_fine_type(fine_type)
            else:
                return False

    def search_by_city(self, city):
        if self.data["City"] == city:
            return True
        if city < self.data["City"]:
            if self.left:
                return self.left.search_by_city(city)
            else:
                return False
        else:
            if self.right:
                return self.right.search_by_city(city)
            else:
                return False

    def add_person(self, person_data):
        self.add_fine(person_data)


def build_tree(elements):
    root = None
    for data in elements:
        if root is None:
            root = FinesClass(data)
        else:
            root.add_fine(data)
    return root


if __name__ == "__main__":
    data = [
        {"id": 1, "name": "John", "Fine": "A", "City": "New York"},
        {"id": 4, "name": "Anna", "Fine": "B", "City": "London"},
        {"id": 2, "name": "Alice", "Fine": "С", "City": "Paris"}
    ]
    db = build_tree(data)

    print(db.order(), "\n")
    print(db.search_by_id(4), "\n")
    print(db.search_by_fine_type("A"), "\n")
    print(db.search_by_city("New York"), "\n")

    new_person = {"id": 5, "name": "Tom", "Fine": "D", "City": "Berlin"}
    db.add_person(new_person)

    print(db.order())
























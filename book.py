class Book:
    def __init__(self, id, title, author, year, is_available=True):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    # book -> dictionary (for saving to json)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_available": self.is_available
        }

    # dictionary -> book (for loading from json)
    @staticmethod
    def from_dict(data):
        return Book(data["id"], data["title"], data["author"],
                    data["year"], data["is_available"])

    def __str__(self):
        if self.is_available:
            status = "available"
        else:
            status = "taken"
        return f"#{self.id} | {self.title} | {self.author} | {self.year} | {status}"
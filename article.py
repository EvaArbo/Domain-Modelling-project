class Article:
    _all = []  # Keeps track of all articles

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 chars.")
        if hasattr(self, "_title"):  # Prevent reassignment
            #hasattr(self, "_title") checks if the title has already been set
            raise Exception("Title cannot be changed once set.")
        self._title = title.strip()
        Article._all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from author import Author
        if not isinstance(value, Author):
            raise Exception("Author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be a Magazine instance.")
        self._magazine = value

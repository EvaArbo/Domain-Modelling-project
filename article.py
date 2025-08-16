class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Article title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be between 5 and 50 characters")

        from author import Author
        from magazine import Magazine

        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")

        self._title = title
        self._author = author
        self._magazine = magazine

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

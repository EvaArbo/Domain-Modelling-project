class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Magazine name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("Magazine category must be a string")
        if len(category) == 0:
            raise ValueError("Magazine category cannot be empty")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        """Return list of articles published in this magazine"""
        return self._articles

    def contributors(self):
        """Return list of unique authors that wrote in this magazine"""
        return list({article.author for article in self._articles})

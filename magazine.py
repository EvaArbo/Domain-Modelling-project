from article import Article

class Magazine:
    _all = []  # To track all magazines for top_publisher

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 chars.")
        self._name = value.strip()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = value.strip()

    def articles(self):
        """Return all articles for this magazine"""
        return [article for article in Article._all if article.magazine == self]

    def contributors(self):
        """Return unique authors who wrote for this magazine"""
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        """Return all article titles or None"""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """Return authors with >2 articles for this magazine"""
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        """Return magazine with most articles or None"""
        if not Article._all:
            return None
        return max(cls._all, key=lambda mag: len(mag.articles()))

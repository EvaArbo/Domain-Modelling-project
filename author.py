from article import Article
from magazine import Magazine

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Author name must be a non-empty string.")
        if hasattr(self, "_name"):  # Prevents reassignment after creation
            raise Exception("Author name cannot be changed once set.")
        self._name = name.strip()

    @property
    def name(self):
        return self._name

    def articles(self):
        """Return all articles written by this author"""
        return [article for article in Article._all if article.author == self]

    def magazines(self):
        """Return unique magazines this author has contributed to"""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """Create and return a new Article instance"""
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance.")
        return Article(self, magazine, title)

    def topic_areas(self):
        """Return unique list of categories or None if no articles"""
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))

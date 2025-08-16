class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        if len(name) == 0:
            raise ValueError("Author name cannot be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        """Return list of articles written by this author"""
        return self._articles

    def magazines(self):
        """Return list of unique magazines this author has written for"""
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        from article import Article
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)
        return article

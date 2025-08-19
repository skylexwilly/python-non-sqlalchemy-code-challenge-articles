class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be Author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be Magazine instance")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    # title immutable (ignore assignment)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass  # ignore changes

    # author mutable
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    # magazine mutable
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non-empty string")
        self._name = name

    # name immutable (ignore assignment)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass  # ignore changes

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    # name mutable but ignores invalid values
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # else: ignore assignment

    # category mutable but ignores invalid values
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # else: ignore assignment

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [a for a in set(authors) if authors.count(a) > 2]
        return result if result else None

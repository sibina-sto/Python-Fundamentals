class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new):
        self.content = new

    def change_author(self, new):
        self.author = new

    def rename(self, new):
        self.title = new

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"

article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)

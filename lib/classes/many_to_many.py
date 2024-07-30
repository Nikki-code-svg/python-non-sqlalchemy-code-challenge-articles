class Article:

    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)
       
       #common between author, magazine

    def __repr__(self):
        return f" Article(author={self.author}, magazine={self.magazine}, title={self.title})"

    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, title):
       if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, 'title'):
           self._title = title
       else:
           raise Exception("Title needs name to be betweeen 5 and 50 characters")

    @property
    def author(self):
       return self._author


    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("Must be an Author name")
        else:
           self._author = author


    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
          raise Exception("Must be a magazine")
        else:
          self._magazine = magazine


class Author:
    
    def __init__(self, name):
        self.name = name
        self._articles_list = []
       

    def __repr__(self):
        return f"Author(name={self.name})"


    @property
    def name(self):
       return self._name

    @name.setter    
    def name(self, name):
       if isinstance(name, str) and len(name) > 0 and not hasattr(self, 'name'):
         self._name = name
       else:
           raise Exception("Name needs Input")


    def articles(self):
      return [ article for article in Article.all_articles if article.author == self ]

    def magazines(self):
        return list(set(article.magazine for article in Article.all_articles if article.author == self ))


    def add_article(self, magazine, title):
       new_articles = Article(self, magazine, title)
       self._articles_list.append(new_articles)
       return new_articles
    
    def topic_areas(self):
        topics = set(article.magazine.category for article in Article.all_articles if article.author == self)
        return list(topics) if topics else None
        # articles = self.articles()
        # if not articles:
        #     return None
        # return list(set([article.magazine.category for article in Article.all_articles if article.author == self ]))
        


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f"Magazine(name={self.name}, category={self.category})"
        
    
    @property
    def name(self):
       return self._name

    @name.setter    
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Name needs to be between 2 and 16 characters")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 <len(category):
            self._category = category
        else:
            raise Exception("Must have a Category")
    

    def articles(self):
       return [ article for article in Article.all_articles if article.magazine == self ]


    def contributors(self):
        return list(set( article.author for article in Article.all_articles if article.magazine == self ))

    def article_titles(self):
        article_titles = []

        article_titles = [ article.title for article in Article.all_articles if article.magazine == self ]
        if not article_titles:
            return None
        return article_titles
      

    def contributing_authors(self):
           authors = [
            author for author in self.contributors()
            if len([article for article in author.articles() if article.magazine == self]) > 2
        ]
           return authors if authors else None
   
  
        
            
        
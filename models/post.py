from database import Database
import uuid
import datetime

class Post(object):

    def __init__(self, blog_id, title, content, author, post_date = datetime.datetime.utcnow(), post_id=None):
          self.blog_id = blog_id
          self.post_id = uuid.uuid4().hex if post_id is None else post_id
          self.title = title
          self.content = content
          self.author = author
          self.post_date = post_date



    def save_to_mongo(self):
        Database.insert(collection = 'posts',
                        data = self.json())

    def json(self):
        return {
            "post_id": self.post_id,
            "blog_id": self.blog_id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "date" : self.post_date
        }

    # title = "This is a title"
    # content = "This is the content"
    # author = "John Does"


    # def __init__(self):
    #       self.title = "This is a title"
    #       self.content = "This is the content"
    #       self.author = "John Does"
    #
    # # print(title)
    @staticmethod
    def from_mongo(post_id):
        return Database.find_one(collection='posts', query={'post_id': post_id})

    @staticmethod
    def from_blog(post_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': post_id})]






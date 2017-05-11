__author__ = 'root_geek'
from database import Database
from models.post import Post

# import pymongo
#
# uri ="mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['students']
# collection =  database['students']
# # show dbs
# # use students
# # show collections
#
# # students = collection.find({})
# # # print(students)
#
#
# student_list = [students["course"] for students in students.collection.find({}) if students['course']]
# print(student_list)
#
# # for students in students:
# #     print(students)

Database.initialize()


post = Post(blog_id = "123",
            title = "This is the the first title",
            content = "This is content for the first post",
            author = "John Doe"
            )

post.save_to_mongo()

# post1 = Post("Post 2 Title", "Post 2 Content","Post 2 Author")

# post1.title = "This is the title for post 2"
# print(post1.title)
# print(post.title)
# print(post.title, post.content, post.author)









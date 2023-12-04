# blog_posts/domain/services/services.py
from blog_posts.domain.daos import AuthorDAO


class AuthorService:

    def __init__(self):
        self.author_dao = AuthorDAO()

    def create_author(self,
                      email: str,
                      password: str,
                      username: str,
                      bio: str,
                      profile_pic: str
                      ):
        return self.author_dao.create_author(email, password, username, bio, profile_pic)

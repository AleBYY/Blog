from blog_posts.domain.services.services import AuthorService


class AuthorRegisterUseCase:
    def __init__(self):
        self.author_service = AuthorService()

    def execute(self,
                email: str,
                password: str,
                username: str,
                bio: str,
                profile_pic: str
                ):
        author_entity = self.author_service.create_author(email, password, username, bio, profile_pic)
        return author_entity

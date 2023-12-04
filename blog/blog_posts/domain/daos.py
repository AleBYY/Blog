from django.contrib.auth import get_user_model
from blog_posts.domain.converters import AuthorEntityConverter
from blog_posts.domain.entities import AuthorEntity
from blog_posts.models import Author

User = get_user_model()


class AuthorDAO:
    @classmethod
    def create_author(cls,
                      email: str,
                      password: str,
                      username: str,
                      bio: str,
                      profile_pic: str
                      ) -> AuthorEntity:
        user = User.objects.create_user(
            email=email,
            password=password,
            username=username,
            bio=bio,
            profile_pic=profile_pic
        )
        return AuthorEntityConverter.to_entity(user)

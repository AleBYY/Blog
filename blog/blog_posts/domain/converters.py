from blog_posts.domain.entities import AuthorEntity
from blog_posts.models import Author


class AuthorEntityConverter:
    @classmethod
    def to_entity(cls, orm_object: Author) -> AuthorEntity:
        return AuthorEntity(
            pk=orm_object.pk,
            email=orm_object.email,
            username=orm_object.username,
            profile_pic=orm_object.profile_pic,
            following=list(orm_object.following.values_list('pk', flat=True)),
            followers=list(orm_object.followers.values_list('pk', flat=True)),
            bio=orm_object.bio
        )

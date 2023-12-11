from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from django.contrib.auth.models import User

from .models import Post


@dataclass
class PostDTO:
    id: int
    title: str
    content: str
    #author_id: User
    created_at: datetime
    updated_at: datetime
    published: bool

    @classmethod
    def from_django_model(cls, post_service: Post) -> 'Post_DTO':
        return PostDTO(
            id=post_service.id,
            title=post_service.title,
            content=post_service.content,
            #author_id=post_service.author,
            created_at=post_service.created_at,
            updated_at=post_service.updated_at,
            published=post_service.published
        )


class IPostService(ABC):

    @classmethod
    @abstractmethod
    def list(cls) -> list[PostDTO]:
        pass

    @classmethod
    @abstractmethod
    def create(cls, title: str, content: str, published: str) -> PostDTO:
        pass

    @classmethod
    @abstractmethod
    def get(cls, id: int) -> PostDTO:
        pass


class PostNotFound(Exception):
    pass


class PostService(IPostService):

    @classmethod
    def list(cls) -> list[PostDTO]:
        return [PostDTO.from_django_model(p) for p in Post.objects.all()]

    @classmethod
    def create(cls, title: str, content: str, published: str) -> PostDTO:
        post = Post.objects.create(
            title=title,
            content=content,
            published=bool(published)
        )
        return PostDTO.from_django_model(post)

    @classmethod
    def get(cls, id: int) -> PostDTO:
        try:
            return PostDTO.from_django_model(Post.objects.get(id=id))
        except Post.DoesNotExist:
            raise PostNotFound

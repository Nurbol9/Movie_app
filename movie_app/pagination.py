from rest_framework.pagination import PageNumberPagination


class MoviePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10


class CategoryPagination(PageNumberPagination):
    page_size = 4
    max_page_size = 10


class GenrePagination(PageNumberPagination):
    page_size = 6
    max_page_size = 10



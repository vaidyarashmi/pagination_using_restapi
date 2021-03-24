from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
class MyPagination(PageNumberPagination):
    pagination_class        =PageNumberPagination
    page_size               =5
    page_query_param        ='MyPage'
    page_size_query_param   ='num'
    max_page_size           =15
    last_page_strings       =('endpage',)

class MyOffsetPagination(LimitOffsetPagination):
    pagination_class        =LimitOffsetPagination
    default_limit           =15
    limit_query_param       ="mylimit"
    offset_query_param      ="myoffest"
    max_limit               =20

class MyCursorPagination(CursorPagination):
    cursor_query_description="pointer"
    ordering                ='-esal'
    page_size               =5

    
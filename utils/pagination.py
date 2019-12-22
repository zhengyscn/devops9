from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 15
    max_page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'page_size'


    def get_page_size(self, request):
        page_size = super(CustomPagination, self).get_page_size(request)
        try:
            page_size = int(request.GET.get('page_size', page_size))
        except:
            pass
        return page_size
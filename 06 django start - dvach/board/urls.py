from django.conf.urls import url

urlpatterns = [  
    url(r'^$', 'board.views.show_board', name='show_board'),
    url(r'^post/(?P<post_id>\d+)', 'board.views.comment', 
        name='comment'),
]
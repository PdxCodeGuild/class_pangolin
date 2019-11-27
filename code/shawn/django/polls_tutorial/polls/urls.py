from django.urls import path
from . import views

# create a namespace specficially for these urls
app_name = 'polls'

# FOR CLASS BASED VIEWS
urlpatterns = [                                                             # this is a magic name...must use "urlpatterns"
    path('', views.IndexView.as_view(), name="index"),                                    # if the request from the client is just an empty string (so "website.com/")
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote")
]


#  FOR FUNCTIONAL BASED VIEWS
# server will return 404 response if the url is not mapped to a function here in urlpatterns
# only looks at what's between the domain/port and the ?
# urlpatterns = [                                                             # this is a magic name...must use "urlpatterns"
#     path('', views.index, name="index"),                                    # if the request from the client is just an empty string (so "website.com/")
#     path('<int:question_id>/', views.detail, name="detail"),
#     path('<int:question_id>/results/', views.results, name="results"),
#     path('<int:question_id>/vote/', views.vote, name="vote")
# ]
from django.urls import path
from . import views

# server will return 404 response if the url is not mapped to a function here in urlpatterns
# only looks at what's between the domain/port and the ?
urlpatterns = [                                                             # this is a magic name...must use "urlpatterns"
    path('', views.index, name="index"),                                    # if the request from the client is just an empty string (so "website.com/")
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote")
]


from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$',views.Index,name="index"),
	url(r'^data/',views.Data , name = "Data"),
	url(r'^mentionedin/',views.MentionedIN , name ="mentionedin"),
	url(r'^minimumyear/',views.MinimumYear,name ="MinimumYear")
]
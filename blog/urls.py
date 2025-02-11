from	django.urls	import	path
from	.views	import	post_list,detail_post
urlpatterns	=	[
				path('',	post_list,	name='post_list'),
                path('<int:id>', detail_post, name='detail_post')
                
]                     
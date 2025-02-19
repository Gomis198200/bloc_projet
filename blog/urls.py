from	django.urls	import	path
from	.views	import	post_list,detail_post,home,blog
urlpatterns	=	[
				path('',	post_list,	name='post_list'),
                path('<int:id>', detail_post, name='detail_post'),
                path('home/',home,name='home'),
                path('blog/',blog,name='blog'),
                
];                    
from django.contrib import admin
from .models import Community_post
from .models import Post
from .models import Member_info
from .models import My_under
from .models import My_role



admin.site.register(Post)
admin.site.register(Community_post)
admin.site.register(Member_info)
admin.site.register(My_under)
admin.site.register(My_role)


# Register your models here.

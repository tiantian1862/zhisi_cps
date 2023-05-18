from django.contrib import admin

# Register your models here.
from .models import pici_data,chenben_test_data,furongwang_gongshi_test_data,baisha_gongshi_test_data

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)
#admin.site.register(BookInstance)
#admin.site.register(chengben_data)
#admin.site.register(zhiliang_data)
#admin.site.register(shengchan_data)
#admin.site.register(xiaolv_data)
admin.site.register(pici_data)
admin.site.register(chenben_test_data)
admin.site.register(furongwang_gongshi_test_data)
admin.site.register(baisha_gongshi_test_data)

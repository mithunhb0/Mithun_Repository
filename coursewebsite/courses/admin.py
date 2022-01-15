from django.contrib import admin
from courses.models import *
from django.utils.html import format_html


class TagAdmin(admin.TabularInline):
    model = Tag

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite
    
class LearningAdmin(admin.TabularInline):
    model = Learning


class VideoAdmin(admin.TabularInline):
    model = Video

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, PrerequisiteAdmin, LearningAdmin, VideoAdmin ]
    list_display = ['name','get_price','get_discount','active']
    list_filter = ['discount','active']
    
    def get_discount(self,course):
        return f'{course.discount} %'

    def get_price(self,course):
        return f'₹ {course.price}'
    
    get_discount.short_description = 'Discount'
    get_price.short_description = 'Price'
    
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ['order_id','get_user','get_course','status']
    list_filter = ['course','status']

    def get_user(self,payment):
        return format_html(f'<a target="_blank" href="/admin/auth/user/{payment.user.id}">{payment.user}</a>')
    
    def get_course(self,payment):
        return format_html(f'<a target="_blank" href="/admin/courses/course/{payment.course.id}">{payment.course}</a>')
    
    get_user.short_description = 'User'
    get_course.short_description = 'Course'
    
class UserCourseAdmin(admin.ModelAdmin):
    model = UserCourse
    list_display = ['click','get_user','get_course','date']
    list_filter = ['user','course','date']
    
    def click(self,usercourse):
        return "click here to open usercourse"

    def get_user(self,usercourse):
        return format_html(f'<a target="_blank" href="/admin/auth/user/{usercourse.user.id}">{usercourse.user}</a>')
    
    def get_course(self,usercourse):
        return format_html(f'<a target="_blank" href="/admin/courses/course/{usercourse.course.id}">{usercourse.course}</a>')
    
    get_user.short_description = 'Click'
    get_user.short_description = 'User'
    get_course.short_description = 'Course'    

    
admin.site.register(Video)
admin.site.register(UserCourse, UserCourseAdmin )
admin.site.register(Payment,PaymentAdmin)

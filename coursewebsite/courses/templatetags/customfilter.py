from django import template
from courses.models import *
import math
register = template.Library()

@register.simple_tag
def cal_sellprice(price, discount):
    if discount is None or discount is 0:
        return price
    
    sellprice = price - ( price * discount * 0.01 )
    return math.floor(sellprice)

@register.filter
def rupee(price):
    return f'₹{price}'

@register.simple_tag
def is_enrolled(request, course):
    is_enrolled = False
    user = None
    if request.user.is_authenticated==False:
        return False
    
    user = request.user
    
    try:
        usercourse = UserCourse.objects.get(user=user,course=course)
        return True
    except:
        return False
    
    return is_enrolled
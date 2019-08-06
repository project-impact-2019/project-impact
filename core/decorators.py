# Decorators Created Here
from django.contrib.auth.decorators import login_required, user_passes_test

user_pair_required = user_passes_test(lambda user: user.is_paired, login_url='/')

def chatroompair_required(view_func):
    decorated_view_func = login_required(user_pair_required(view_func))
    return decorated_view_func
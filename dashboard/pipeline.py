from django.shortcuts import redirect
from django.contrib.auth.models import User
from social_core.pipeline.partial import partial

@partial
def get_other_data(strategy, backend, request, details, user, is_new=False, *args, **kwargs):
    complete = strategy.session_get('finish', None)
    user_instance = strategy.session_get('user_instance', None)
    user_obj = user if not is_new else User.objects.filter(id=user_instance).first()

    if (not user_obj or not complete) and is_new:
        current_partial = kwargs.get('current_partial')
        return redirect('/register?partial_token={0}'.format(current_partial.token))
        
    
    # continue the pipeline
    return {
        'user': user_obj
    }

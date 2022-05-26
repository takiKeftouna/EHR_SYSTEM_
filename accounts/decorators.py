from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

#doctor_decorator for assured is doctor
def doctor_required(function=None , redirect_field_name=REDIRECT_FIELD_NAME,login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_doctor,
        login_url=login_url,
        redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator


#patient decorator for assured is doctor

def patient_required(function = None , redirect_field_name=REDIRECT_FIELD_NAME,login_ur ='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.is_patient)  ,
        login_url=login_ur,
        redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator

def pharmacist_required(function=None , redirect_field_name=REDIRECT_FIELD_NAME,login_ur='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_pharmacist,
        login_url=login_ur,
        redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator


def laboratory_required(function=None , redirect_field_name=REDIRECT_FIELD_NAME,login_ur='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_laboratory,
        login_url=login_ur,
        redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator
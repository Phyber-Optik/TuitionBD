from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import SignUpForm
import account.verify


def signup(request):
    template_name = 'signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.token = account.verify.send_activation_email(request=request, user=user)
            user.save()
            return redirect('sign_up_success')
    else:
        form = SignUpForm()

    return render(request, template_name, {'form': form})


def activate(request, uidb64, token):
    user = account.verify.activate(uidb64, token)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account/account_activation_invalid.html')


def sign_up_success(request):
    return render(request, 'account/signUpSuccess.html')

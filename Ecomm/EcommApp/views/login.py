from django.views import View
from EcommApp.models.user import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect


class Login(View):
    return_Url=None
    def get(self,request):
        Login.return_Url=request.GET.get('return_Url')
        return render(request, 'login.html')
    def post(self, request):
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.get_customer_by_email(email)
            error_message = None

            if user:
                # Check if password matches
                if check_password(password, user.password):
                    # On successful login, set session data for the user
                    request.session['user_id'] = user.id
                    request.session['user_fname'] = user.fname
                    request.session['user_lname'] = user.lname
                    request.session['user_email'] = user.email
                    request.session['user_phone'] = user.phone
                    request.session['user_profileImg'] = user.profileImg.url if user.profileImg else None

                    # Redirect to the home page after successful login
                    return redirect('home')  
                else:
                    error_message = "Invalid password!"
            else:
                error_message = "User not found!"

            # If login fails, render the login page again with an error message
            return render(request, 'login.html', {'error': error_message})
def logout(request):
    request.session.clear()
    return redirect('login')
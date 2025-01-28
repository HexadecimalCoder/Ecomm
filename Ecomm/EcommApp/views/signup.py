from django.shortcuts import render,redirect
from django.views import View
from EcommApp.models.user import User
from django.contrib.auth.hashers import make_password


class Sign_up(View):


    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData = request.POST
        fname = postData.get("fname")
        lname = postData.get("lname")
        phone = postData.get("phone")
        email = postData.get("email")
        password = postData.get("password")
        confirmPassword = postData.get("confirmPassword")
        profileImg = request.FILES.get("profileImg")

        value = {
            "fname": fname,
            "lname": lname,
            "phone": phone,
            "email": email
        }
        
        error_message = None
        
        user = User( 
            fname=fname,
            lname=lname,
            phone=phone,
            email=email,
            password=password,
            profileImg=profileImg
        )
        
        error_message = self.validateUser(user,confirmPassword)

        if not error_message:
            
            user.password = make_password(user.password)
            user.save()
          
            return redirect('/login')
        else:
            # Return the form with error message
            data = {
                'error': error_message,
                "values": value
            }
            return render(request, 'signup.html', data)

    def  validateUser(self, user,confirmPassword): ...
 
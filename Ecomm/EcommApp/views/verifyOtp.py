from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View



otp_storage={}

class VeryfyOTP(View):
    def get(self,request):
        return render(request,'varify_otp.html')
    
    def post(self,request):
        email = request.session.get('email')  # Retrieve email from session
        
        if not email:
            # If the email is not found in session, redirect to forget password page
            return redirect('forget-password')
        
        otp_enter = int(request.POST.get('otp'))

        stored_otp = request.session.get('otp')
        
        print(f"OTP entered: {otp_enter}")  # Debugging line
        print(f"Session email: {email}")  # Debugging line
        print(f"Stored OTP from session: {stored_otp}")
              
        if stored_otp  == otp_enter:
            return redirect('/reset-password')
        else:
            error_message = "Invalid OTP. Please try again."
            return render(request, 'varify_otp.html', {'error': error_message})
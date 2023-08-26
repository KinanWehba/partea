from django.shortcuts import redirect

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # التحقق من الصلاحيات هنا
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            return redirect('/accounts/profile')  # اسم الصفحة التي تود توجيه المستخدم إليها
        response = self.get_response(request)
        return response

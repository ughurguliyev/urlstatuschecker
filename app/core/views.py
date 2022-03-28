from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import URL
from core.repository import core_repo


class HomePageView(LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = URL
    context_object_name = "urls"
    
    def post(self, request, *args, **kwargs):
        success = False

        if request.POST['action'] == 'check_url':
            success = core_repo.check_url_response_code(
                request.POST['url']
                )

            return JsonResponse(
                {"success": success}, status=200,
            )
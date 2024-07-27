from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.models import Lead
from client.models import Client
from team.models import Team
from userprofile.models import Userprofile

@login_required
def dashboard(request):
    # Try to get the active team from UserProfile
    try:
        user_profile = request.user.userprofile
        team = user_profile.get_active_team()
    except Userprofile.DoesNotExist:
        # Handle the case where UserProfile does not exist
        return render(request, 'dashboard/dashboard.html', {
            'leads': [],
            'clients': [],
            'error': 'User profile does not exist. Please contact support.',
        })
    team = request.user.userprofile.get_active_team()

    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]

    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })
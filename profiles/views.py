from django.shortcuts import render

from profiles.models import Profile

def my_recomendations_view(request):
    profile = Profile.objects.get(user = request.user)
    my_recs = profile.get_reffered_profiles()
    context={'my_recs': my_recs}
    return render(request, 'profile.html', context)

























# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Profile
# from .serializers import ProfileSerializer
# import random
# import string
# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

#     @action(detail=True, methods=['post'])
#     def activate_invite(self, request, pk=None):
#         try:
#             invited_profile = Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             return Response({"detail": "Профиль не найден"}, status=status.HTTP_400_BAD_REQUEST)
        
#         current_profile = self.get_object()

#         if current_profile.invite_code_used:
#             return Response({"detail": "Код уже используется"}, status=status.HTTP_400_BAD_REQUEST)

#         current_profile.invite_code_used = True
#         current_profile.referred_by = invited_profile
#         current_profile.save()

#         return Response({"detail": "Код активирован удачно"}, status=status.HTTP_200_OK)



# def test_activation(request):
#     return render(request, 'base.html')

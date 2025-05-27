from django.urls import path
from users.views import CustomPasswordReset,sign_up, SignIn, sign_out, activate_user, AdminDashboard, assign_role, create_group, group_list

urlpatterns = [
    path('sign-up/', sign_up, name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', sign_out, name='logout'),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('admin/admin-dashboard/', AdminDashboard.as_view(), name='admin-dashboard'),
    path('admin/<int:user_id>/assign-role/', assign_role, name='assign-role'),
    path('admin/create-group/', create_group, name='create-group'),
    path('admin/group-list/', group_list, name='group-list'),
    path('password-reset/',CustomPasswordReset.as_view(), name='password-reset')
]
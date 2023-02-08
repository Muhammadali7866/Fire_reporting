"""fire_reporting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="home"),
    path("login/",views.admin_login,name="login"),
    path("report_submit/",views.submit_report,name="report_submit"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("add_team/",views.add_teams,name="add-team"),
    path("view_team/",views.view_team,name="view-team"),
    path("edit_team/<int:id>/",views.edit_team,name="edit-team"),
    path("delete_team/<int:id>/",views.delete_team,name="delete-team"),
    path("new_request/",views.new_request,name="new-request"),
    path("view_request/<int:id>/",views.view_request,name="view-request"),
   # path("assign_request/",views.assign_request,name="assign"),
    path("assign_request1/",views.assign_request1,name="assign-request"),
    path("team_way/",views.team_on_way,name="team-way"),
    path("work_progress/",views.work_in_progress,name="work-progress"),
    path("request_complete/",views.complete_request,name="request-complete"),
    path("All_Request/",views.all_request,name="all-request"),
    path("delete_request/<int:id>",views.delete_request,name="delete-request"),
    path("logout/",views.Logout,name="logout"),
    path("view_status/",views.view_status,name="view-status"),
    path("view_StatsDetail/<int:pid>/",views.viw_status_detail,name="view-status-detail")
]

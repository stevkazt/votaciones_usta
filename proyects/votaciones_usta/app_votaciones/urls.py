from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.logIn, name='logIn'),
    path('/', views.logIn, name='logIn'),
    path('logIn/', views.logIn, name='logIn'),
    path('index/', views.index, name='index'),
    path('createStudent/', views.createStudent, name='createStudent'),
    path('createCycleVoting/', views.createCycleVoting, name='createCycleVoting'),
    path('changeCycleVotingStatus/', views.changeCycleVotingStatus, name='changeCycleVotingStatus'),
    path('consultCycleVoting/', views.consultCycleVoting, name='consultCycleVoting'),
    path('createFacultyVoting/', views.createFacultyVoting, name='createFacultyVoting'),
    path('placeFacultyStudent/', views.placeFacultyStudent, name='placeFacultyStudent'),
    path('changeFacultyVotingStatus/', views.changeFacultyVotingStatus, name='changeFacultyVotingStatus'),
    path('consultFacultyVoting/', views.consultFacultyVoting, name='consultFacultyVoting'),
    path('consultVotingListDean/', views.consultVotingListDean, name='consultVotingListDean'),
    path('applyToCycleVoting/', views.applyToCycleVoting, name='applyToCycleVoting'),
    path('voteCycle/', views.voteCycle, name='voteCycle'),
    path('voteFaculty/', views.voteFaculty, name='voteFaculty'),
    path('consultVoteResults/', views.consultVoteResults, name='consultVoteResults'),
    path('consultMyVote/', views.consultMyVote, name='consultMyVote'),
    path('consultVotingListStudent/', views.consultVotingListStudent, name='consultVotingListStudent'),
    path('consultFacultyStudentList/', views.consultFacultyStudentList, name='consultFacultyStudentList'),
]
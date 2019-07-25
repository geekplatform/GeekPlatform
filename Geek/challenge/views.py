from django.shortcuts import render, redirect,get_list_or_404
from .models import Challenge, Solve, Category
from django.contrib.auth.decorators import login_required
from accounts.models import Teams
from django.db.models import Sum, Max, Count
from django.db import connection

cursor = connection.cursor()
# Create your views here.
from .forms import SubmitForms, ScoreboardForm
from django.contrib.auth.models import User


@login_required
def index(request):
    challenge_list = Challenge.objects.all().order_by('-created_time')
    current_user = request.user
    if request.method == "POST":
        form = SubmitForms(request.POST)
        if form.is_valid():
            id = request.POST.get('challenge_id')
            flag = form.cleaned_data['s_flag']
            query = Challenge.objects.filter(id=id)
            if len(query) == 1:
                if query[0].flag == flag:
                    #如果没有提交过就在数据库中添加
                    if not Solve.objects.filter(challenge_id_id=id, team_id_id=current_user.id):
                        Solve.objects.create(challenge_id_id=id, team_id_id=current_user.id)
                    return redirect('sucess.html')
                #错误返回
                else:
                    return redirect('wrong.html')
            #没有这道题返回
            else:
                return redirect('id_flag_wrong.html')
    else:
        form = SubmitForms()
    return render(request, 'test.html', context={'challenge_list': challenge_list, 'form': form})


@login_required
def scoreboard(request):
    results = {}
    if request.method == "POST":
        form = ScoreboardForm(request.POST)
        if form.is_valid():
            choices = form.clean()
            freshman = choices['Form_is_freshman']
            category = choices['Form_category']
            #看所有
            if category == 1 and freshman == 0:
                sql = "SELECT MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id  GROUP BY team_id_id ORDER BY score DESC ;"
                cursor.execute(sql)
            #看所有分类+大一
            elif category == 1 and freshman == 1:
                sql = "SELECT MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id JOIN accounts_teams ON  accounts_teams.team_id=challenge_solve.team_id_id WHERE   accounts_teams.is_freshman= 1  GROUP BY team_id_id ORDER BY score DESC ;"
                cursor.execute(sql)
            #看指定分类+所有人
            elif category != 1 and freshman == 0:
                sql = "SELECT MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id WHERE challenge_challenge.category_id=%s GROUP BY team_id_id ORDER BY score DESC ;"
                cursor.execute(sql, category)
            #看所有分类+大一
            elif category != 1 and freshman == 1:
                sql = "SELECT MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id JOIN accounts_teams ON  accounts_teams.team_id=challenge_solve.team_id_id WHERE challenge_challenge.category_id=%s AND accounts_teams.is_freshman= 1  GROUP BY team_id_id ORDER BY score DESC ;"
                cursor.execute(sql, category)
            results = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            return render(request, 'scoreboard.html', context={'form': form, 'results': results})
    else:
        #默认看所有人+所有分类
        sql = "SELECT MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id   GROUP BY team_id_id ORDER BY score DESC ;"
        cursor.execute(sql)
        results = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
        form = ScoreboardForm()
        return render(request, 'scoreboard.html', context={'form': form, 'results': results})
def info(request,pk):
    pass





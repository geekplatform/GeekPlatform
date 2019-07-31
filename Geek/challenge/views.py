from django.shortcuts import render, redirect, get_object_or_404
from .models import Challenge, Solve, Category
from django.contrib.auth.decorators import login_required
from accounts.models import Teams
from django.db.models import Sum, Max, Count
from django.db import connection
from .forms import SubmitForms
from django.contrib.auth.models import User

# Create your views here.
SECRET = 123456789

cursor = connection.cursor()


@login_required
def index(request):

    pk = request.user.id
    team_name = get_object_or_404(User, pk=pk)
    has_solved = {}
    has_solved_title = []
    sql = "select challenge_challenge.title from challenge_solve join challenge_challenge on challenge_solve.challenge_id_id= challenge_challenge.id where team_id_id=%s"
    cursor.execute(sql, pk)
    has_solved = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
    for i in has_solved:
        has_solved_title.append(i['title'])

    tags = Category.objects.all()
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
                    # 如果没有提交过就在数据库中添加
                    if not Solve.objects.filter(challenge_id_id=id, team_id_id=current_user.id):
                        Solve.objects.create(challenge_id_id=id, team_id_id=current_user.id)
                        
                    return redirect('challenge:success')
                    # success = {"success":'Flag正确'}
                    # sql = "select challenge_challenge.title from challenge_solve join challenge_challenge on challenge_solve.challenge_id_id= challenge_challenge.id where team_id_id=%s"
                    # cursor.execute(sql, pk)
                    # has_solved = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
                    # for i in has_solved:
                    #     if i not in has_solved_title:
                    #         has_solved_title.append(i['title'])
                    # return render(request, 'challenges.html', context={'tags':tags,'has_solved_title':has_solved_title, 'success': success})
                # 错误返回
                else:
                    return redirect('challenge:wrong')
                    # wrong = {"wrong":'Flag错误' }
                    # return render(request, 'challenges.html', context={'tags':tags,'has_solved_title':has_solved_title, 'wrong': wrong})
            # 没有这道题返回
            else:
                return redirect('id_flag_wrong.html')
    else:
        form = SubmitForms()
    return render(request, 'challenges.html', context={'tags':tags,'has_solved_title':has_solved_title})


"""
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
                sql = "SELECT team_id_id AS id, MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id  GROUP BY team_id_id ORDER BY score DESC ;"
                cursor.execute(sql)
            #看所有分类+大一
            elif category == 1 and freshman == 1:
                sql = "SELECT team_id_id AS id,MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id JOIN accounts_teams ON  accounts_teams.team_id=challenge_solve.team_id_id WHERE   accounts_teams.is_freshman= 1  GROUP BY team_id_id ORDER BY score DESC ;"
                cursor.execute(sql)
            #看指定分类+所有人
            elif category != 1 and freshman == 0:
                sql = "SELECT team_id_id AS id,MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id WHERE challenge_challenge.category_id=%s GROUP BY team_id_id ORDER BY score DESC ;"
                cursor.execute(sql, category)
            #看所有分类+大一
            elif category != 1 and freshman == 1:
                sql = "SELECT team_id_id AS id,MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id JOIN accounts_teams ON  accounts_teams.team_id=challenge_solve.team_id_id WHERE challenge_challenge.category_id=%s AND accounts_teams.is_freshman= 1  GROUP BY team_id_id ORDER BY score DESC ;"
                cursor.execute(sql, category)
            results = enumerate([dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()])
            return render(request, 'scoreboard.html', context={'form': form, 'results': results})
    else:
        #默认看所有人+所有分类
        sql = "SELECT team_id_id AS id,MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id   GROUP BY team_id_id ORDER BY score DESC ;"
        cursor.execute(sql)
        results = enumerate([dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()])
        form = ScoreboardForm()
        return render(request, 'scoreboard.html', context={'form': form, 'results': results})
"""

@login_required
def info(request, pk):

    team_name = get_object_or_404(User, pk=pk)

    categories = {}
    all_challenges = {}

    current_user = team_name
    challenges = current_user.team_id.all().order_by('-created_time')
    for challenge in challenges:

        if challenge.challenge_id.category.name in categories:
            categories[challenge.challenge_id.category.name] += 1
        else:
            categories[challenge.challenge_id.category.name] = 1

    for category in Category.objects.all():
        all_challenges[category.name] = len(category.challenge_set.all())

        if category.name  not in categories:
            categories[category.name] = 0
    

    categories= sorted(categories.items(),key=lambda x:x[0])
    all_challenges = sorted(all_challenges.items(),key=lambda x:x[0])

    return render(request, "info.html", context={"teamname": team_name, "categories" : categories,'all_challenges':all_challenges,'challenges':challenges})


@login_required
def scoreboard(request, secret, category):
    results = {}
    if secret == SECRET:  # 看新生
        freshman = 1
    else:
        freshman = 0  # 不看新生

    # 开始查数据 看所有
    if category == 0 and freshman == 0:
        sql = "SELECT team_id_id AS id, MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id  GROUP BY team_id_id ORDER BY score DESC ;"
        cursor.execute(sql)
    # 看所有分类+大一
    elif category == 1 and freshman == 1:
        sql = "SELECT team_id_id AS id,MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id JOIN accounts_teams ON  accounts_teams.team_id=challenge_solve.team_id_id WHERE   accounts_teams.is_freshman= 1  GROUP BY team_id_id ORDER BY score DESC ;"
        cursor.execute(sql)
    # 看指定分类+所有人
    elif category != 0 and freshman == 0:
        sql = "SELECT team_id_id AS id,MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id WHERE challenge_challenge.category_id=%s GROUP BY team_id_id ORDER BY score DESC ;"
        cursor.execute(sql, category)
    # 看所有分类+大一
    elif category != 0 and freshman == 1:
        sql = "SELECT team_id_id AS id,MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id JOIN accounts_teams ON  accounts_teams.team_id=challenge_solve.team_id_id WHERE challenge_challenge.category_id=%s AND accounts_teams.is_freshman= 1  GROUP BY team_id_id ORDER BY score DESC ;"
        cursor.execute(sql, category)
    
    results = enumerate([dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()])
    # 题目分类
    tags = Category.objects.all()
    return render(request, 'scoreboard.html', context={'results': results,'tags': tags})


def rank(request):
    sql = "SELECT team_id_id AS id, MAX(auth_user.username) AS teamname,SUM(challenge_challenge.value) AS score FROM challenge_solve JOIN challenge_challenge ON challenge_challenge.id = challenge_solve.challenge_id_id JOIN auth_user ON auth_user.id=challenge_solve.team_id_id  GROUP BY team_id_id ORDER BY score DESC ;"
    cursor.execute(sql)
    results = enumerate([dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()])
    # 题目所有分类
    tags = Category.objects.all()
    return render(request, 'scoreboard.html', context={'results': results,'tags': tags})



@login_required(login_url='accounts:login')
def wrong(request):
    return render(request,'wrong.html')



@login_required(login_url='accounts:login')
def success(request):
    return render(request,'success.html')
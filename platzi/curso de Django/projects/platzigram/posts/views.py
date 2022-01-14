from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#Django-----------------------------
from django.http import HttpResponse
from django.http import JsonResponse
#utils------------------------------
from datetime import datetime
posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]


@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})

    # posts=[
    #     {'name':'post1',
    #      'user':'dani echeverry',
    #      'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
    #      'image':'https://picsum.photos/200/300'},
    #
    #     {'name':'yesterday\'s post',
    #      'user':'figo cardona',
    #      'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
    #      'image':'https://picsum.photos/200/300'},
    #
    #     {'name':'timestamp',
    #      'user':'prrrrr',
    #      'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
    #      'image':'https://picsum.photos/200/300'},
    # ]
    # content=[]
    # for post in posts:
    #
    #     ## QUESTION: que es lo que hace esto en format?
    #     content.append("""
    #         <p><strong>{name}<strong><p>
    #         <p><small>{user}-<i>{timestamp}<i> <small><p>
    #         <figure><img src="{image}"></figure>
    #     """.format(**post))
    # return HttpResponse('<br>'.join(content))

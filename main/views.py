from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

def secondpage(request):
    return render(request, 'main/secondpage.html')

def mainpage(request):
    context = {
        'generation': 14,                   
        'info': {  
            'date' : '2026.04.01',                         
            'topic': 'Django',
            'week': '1학기 2주차',
            'instructor': '백엔드 교육팀 11기 차은호'
        },
        'shortcuts': [
            'Django_Project : 하나의 서비스 전체를 의미',
            'Django_App : Project를 구성하는 기능의 집합 단위',
            '첫 페이지 생성: HTML/VIEW/URL 작성 ',
            'Template 언어: URL 연결 / 변수 사용 / 반복문',
            '-> 크게 URL 연결, 변수 사용, 반복문, 조건문, 필터 기능 지원!',     
            '중복되는 html 파일 정리: template 상속 / navbar 분리',          
            '정적 파일 분리: css 분리 / image 분리'
        ]
    }
    return render(request, 'main/mainpage.html', context)
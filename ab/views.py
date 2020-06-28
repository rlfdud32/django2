from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def 전체(request):
    
    ex1 = '경찰'

    ex2 = '아시아'

    ex3 = '비판'

    ex4 = '코로나'

    ex5 = '홍콩'


    sum1 = '9일 경찰에 따르면 그동안 숨진 손씨의 전 직장동료로 알려진 신고자는 윤미향(더불어민주당) 의원의 보좌진 중 한 명인 것으로 확인됐다.'

    sum2 = '이 전 이사장 측은 이에 “추가 고소인은 다른 피해자들의 검찰 조사 당시에도 참고인 조사를 받아왔으나 진술을 하지 않다가 뒤늦게 고소를 했다”며 “조사받는 중에도 상당히 많은 금액을 요구해 온 사정도 있다”고 주장했다.'

    sum3 = '특히 손씨 사망 최초 신고자가 윤미향 의원 보좌진으로 뒤늦게 알려지면서 논란이 더 커지고 있다.가족도 아닌 직장동료 신고에 곧바로 수색에 나선 것에 대해서는 "신고자가 손씨의 극단적 선택이 우려된다고 했다"면서 "손씨가 평소 신고자에게 극단적 선택을 암시하는 말들을 했다고 한다"고 설명했다.'

    sum4 = '경찰이 손씨 휴대전화에 대한 디지털포렌식 작업을 통해 마지막 통화자 등을 확인해 정확한 사망 경위를 규명한다는 방침이다. 9일 경기 파주경찰서에 따르면 정의기억연대의 일본군 위안부 피해자 마포쉼터(평화의 우리집) 소장 손모(60)씨가 자신의 파주 아파트로 돌아올 때 휴대전화가 차에 있던 것으로 조사됐다.'

    sum5 = '윤 의원 보좌진이 손씨의 경기도 파주 아파트까지 찾아가 “집 안에서 응답이 없다”면서 119에 신고한 것으로 드러났기 때문이다.'


    return render(request, 'news/전체.html', {'example1': ex1,'example2': ex2, 'example3': ex3, 'example4':ex4, 'example5': ex5,'sum1': sum1,'sum2': sum2,'sum3': sum3,'sum4': sum4,'sum5': sum5})
def 정치(request):
    return render(request, 'news/정치.html')
def 사회(request):
    return render(request, 'news/사회.html')
def 경제(request):
    return render(request, 'news/경제.html')
def 생활문화(request):
    return render(request, 'news/생활문화.html')
def 세계(request):
    return render(request, 'news/세계.html')
def IT과학(request):
    return render(request, 'news/IT과학.html')
def 스포츠(request):
    return render(request, 'news/스포츠.html')
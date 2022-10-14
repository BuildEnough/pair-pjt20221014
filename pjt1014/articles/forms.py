from django import forms  # 장고기능의 forms라는 기능을 참조해서 사용할거야.
from .models import Review


class ppp(forms.ModelForm):  # ppp{클래스이름 임의로 지정} (#참조한 모델을 상속시킴 )
    class Meta:
        model = Review  # 폼을 사용할 모델 지정
        fields = ["title"]  # 폼에서 사용할 input 필드지정

import requests
import json

import sys
sys.path.append('../../METADATA')   #저장 되어 있는 전 전 디렉터리 가서 METADATA를 참고하라
#이렇게 하면 검색이 안되므로 (왜냐 저장소 밖에 있으니까) 큰 프로젝트를 관리하기 더 효율적이다.
import METADATA


params = {  #또 다른 정보
    'visualFeatures': 'Description',
    'language': 'en'
         }

headers = { #우리가 보내는 데이터 타입
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.VISION_KEY
}

data = {    #사진 자료
    'url':'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Classroom.jpeg/525px-Classroom.jpeg'
}

res = requests.post('https://koreacentral.api.cognitive.microsoft.com/vision/v1.0/analyze',
                        params=params, headers=headers, json=data)


#여기까지해서 requests하면 통신을 해서 값을 받아올 수 있다.
#####################################################################################

#다음으로 딕셔너리,리스트 자료형을 해서 원하는 정보 값을 알 수 있다.(알맞은 자료형으로 변환해서 사용)

res_dict = json.loads(res.text)
subscribed_text = res_dict['description']['captions'][0]['text']


params = {  #또 다른 정보
    'api-version': '3.0',
    'from': 'en',
    'to' : 'ko'
         }

headers = { #우리가 보내는 데이터 타입
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.TRANSLATE_KEY
}

data = [{    #사진 자료
    'text' : subscribed_text
}]

res = requests.post('https://api.cognitive.microsofttranslator.com/translate',
                        params=params, headers=headers, json=data)


res_dict = json.loads(res.text)
result = res_dict[0]['translations'][0]['text']
print(result)
# Point-Checker
객체 인식과 OCR를 활용한 객관·단답식 시험 채점 AI 소프트웨어


# 프로젝트 개요
## 문제 정의
✔ 종이 기반 시험은 수기 채점이나 광학마크인식을 활용하여 채점함.
✔ 수기 채점은 사람이 직접 채점하여 많은 인력과 시간이 소요되며 부정확함.
✔ 광학마크인식을 활용한 채점은 별도의 답안지 작성이 필요하여, 답안지 구매 비용을 부담해야 하고 단답식 문항은 채점할 수 없음.

## 솔루션
종이 시험지에 표시된 답안을 객체 인식과 OCR을 활용하여 자동으로 문항을 인식하고 채점하는 AI 채점 소프트웨어 < POINT-CHECKER >를 개발.

## 기대효과 및 의의
1. 비용 절감 : 답안지 및 시험 채점을 위한 인건비, 시간, 비용 절감
2. 환경 보호 : 답안지에 사용되는 종이 사용량을 줄여 환경 보호에 기여
3. 답안지 작성 교육 불필요 : 답안지 작성 교육에 필요한 시간, 비용 절감


# 서비스 소개
## 시험지 양식 적용

## 채점하기

사용자는 시험 정보를 입력하고 응시한 시험지를 스캔한 파일(.pdf)과 답 파일(.xlsx)을 업로드 함. ‘채점하기' 버튼을 통해 시험지 채점을 수행함.

## 채점 결과 확인하기

채점 결과는 응시자가 시험지에 작성한 응시자 ID를 추출하여, 각 응시자의 문항별 응답과 정답 여부를 정오표 형태로 출력함. 사용자는 해당 데이터를 직접 추가, 수정, 삭제할 수 있으며, 엑셀 파일로 다운로드 할 수 있음.


## 실행 방법
### (1) 파이썬 파일을 사용하는 경우
1. 리포지토리 클론
```bash
git clone https://github.com/Moment-Capture/Point-Checker.git
```

2. 라이브러리 설치
```bash
pip install -r requirements.txt
```
Python 3.9 이상 환경에서 구동 가능합니다.

3. main.py 실행
```bash
python main.py
```

### (2) .exe 어플리케이션 사용하는 경우
POINT-CHECKER.exe 파일을 누르면 실행됩니다.

# 기술 소개
## 시스템 구조도


## 채점 엔진
### 시스템 플로우


### 채점 엔진 소개
#### 문항 영역 추출
- Yolov8으로 각 시험지의 문항 영역을 탐지
- 사용한 라벨: multiple, multiple_cropped, subjective, subjective_cropped, q_mark, s_period, q_period

#### 잘린 문항 매칭
- Yolov8으로 잘린 문항 분류, 일치하는 유형 매칭
- 사용한 라벨: front_num, front_1, front_2, front_3, front_4, front_5, back_num, back_1, back_2, back_3, back_4, back_5, etc

#### 객관식 답안 추출
- Yolov8으로 문항 번호와 선지 인식
- Yolov8 라벨링 결과를 통해 선지 분류
- EasyOCR을 통해 문항 번호 추출
- 사용한 라벨: num, check1, check2, check3, check4, check5

#### 단답식 답안 추출
- Yolov8으로 문항 번호와 답안 인식
- tamil-ocr을 통해 필기 답안 인식
- EasyOCR을 통해 문항 번호 추출
- 사용한 라벨: num, answer


# 성능 평가
## 소요 시간
✔ 1부 30문항 기준 35초
✔ 5부 30문항 기준 207초
✔ 10부 30문항 기준 403초

## 채점 정확도
✔ 문항 번호 인식 : 98 %
✔ 정답 인식 : 98 %
✔ 최종 인식 : 96 %


# 데모 영상
https://youtu.be/WLkjEvUcV60


# 기술 블로그
https://velog.io/@gongkeo/%EC%9D%B4%ED%99%94%EC%97%AC%EB%8C%80-%EC%BA%A1%EC%8A%A4%ED%86%A4-%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8F%AC%EC%9D%B8%ED%8A%B8-%EC%B2%B4%EC%BB%A4-%EA%B0%9D%EC%B2%B4-%EC%9D%B8%EC%8B%9D%EA%B3%BC-OCR%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EA%B0%9D%EA%B4%80%EB%8B%A8%EB%8B%B5%EC%8B%9D-%EC%8B%9C%ED%97%98-%EC%B1%84%EC%A0%90-AI-%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8


# 레퍼런스
- [Yolov8](https://github.com/ultralytics/yolov8)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Tamil-Ocr](https://github.com/tamil-ocr/tamil-ocr)


# 연락처

질문이나 문제가 있으시면 리포지토리에 이슈를 남기시거나 [momentcaptureteam@gmail.com](mailto:momentcaptureteam@gmail.com)으로 연락주세요.
# 2023 건국대학교 클라우드 IoT 서비스 프로젝트

- 기획한 스마트 헬스케어 서비스를 Amazon AWS서비스 기반으로 구현
- 개발요구사항
  - AWS IoT Core사용
  - 어플리케이션 인터페이스가 RESTful API제공
    - RESTful API를제공하지않으면감점)
  - Amazon API Gateway와 Amazon Lambda서비스를 사용해서 구현
    - API Gateway와 Lambda서비스를 사용하지 않으면 감점
  - DBMS (MongoDB)를사용해서구현–DBMS미사용시감점.
    - NoSQL MongoDB 대신 Amazon RDS 서비스 사용시 감점

##  📌 주제 : 거북목 방지 헬스케어 서비스

담당 : 라즈베리 파이와 AWS를 사용한 사용자 거북목 감지 및 방지 알림 서비스

### 1. 시스템 설계
<img width="500" alt="image" src="https://github.com/zeunxx/2023-Cloud-IoT/assets/81572478/104f584d-28e3-48fa-94d9-bb11ec997667">
<br>

### 2. 아키텍처

<img src="https://github.com/zeunxx/2023-Cloud-IoT/assets/81572478/4ce52d38-2c8e-49b5-b51b-11b1f340759a" width="70%" height="70%"/>

<Br>

#### 💡 서비스 흐름도

- <img src="https://github.com/zeunxx/2023-Cloud-IoT/assets/81572478/29ccbd8e-918d-4927-9da2-a4f5b6cf447e" width="70%" height="70%"/>

<br>

###  🔎 과정
1. Raspberrypi Server의 app.py 실행 
2. ‘/setDistance’ api에 사용자가 원하는 거리를 설정
3. 원하는 거리를 api 통해 받으면 해당 값이 전달되어 distance가 설정된다.
4. 유저는 ‘http://192.168.219.104:5000/move’의 주소로 API Get요청한다.
- raspberrypi:5000/move에서 연결된 초음파 센서는 사용자를 지속적으로 모니터링 하다가 위에서 설정한 값 안으로 사용자가 들어옴을 감지하면 MQTT 메시지를 생성하여 AWS IoT Core에 토픽으로 게시한다.
5. AWS IoT Core는 설정된 규칙을 통해 AWS SNS에서 사용자에게 Topic 값을 문자로 전송한다.
6. AWS IoT Core는 설정된 규칙을 통해 API Gateway의 엔드포인트에 API 요청을 한다.
7. API가 요청되면 해당 API와 연결된 Lambda가 실행되어, Mongo DB에 해당 시각을 저장한다.

<Br>

###  🔎 실행 결과

- 휴대폰(aws sns의 엔드포인트) 문자 메시지
<img src="https://github.com/zeunxx/2023-Cloud-IoT/assets/81572478/45efafbe-2256-4c12-aaf0-a6ae04ddf9fb" width="20%" height="20%"/>
<BR> <br>

- Mongo DB

<img src="https://github.com/zeunxx/2023-Cloud-IoT/assets/81572478/57ecf0f2-8da0-4181-ae68-06245c14da16" width="50%" height="50%"/>


<br>

#### ✅ 제출한 최종 보고서
[[10팀] 과제 7. 스마트 헬스케어 서비스 구현 보고서.pdf](https://github.com/zeunxx/2023-Cloud-IoT/files/11779032/10.7.pdf)

<BR>

#### ✅ 시연 동영상 링크
https://www.youtube.com/watch?v=n5odK9daVu4


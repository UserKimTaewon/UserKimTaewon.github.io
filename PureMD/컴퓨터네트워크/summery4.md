6장 wireless and mobile networks

===

무선통신과 이동통신.

>둘이 좀 다름.

>말 그대로 선이 없는 거 뿐 vs 움직이면서 쓰기.



mobile은 여러 장소를 옮겨다녀도 문제 없어야!

- 사실 중간에 base station이 있음..?

- 일정 지역까지는 cover가 되지만

- 다른 station 범위로 넘어갈 때도 smooth하게 연결되야.



무선->mobile은 아님.

근데 보통 mobile->무선 이긴 함.



# 무선 통신.요소?

wiresless host

- laptop|smartphone|...

- mac/ip addr,통신 규약 지킬 줄 알아야.

- run app

- 고정적/mobile 일 수도.



보통 base station까지는 유선 연결, 거기서 호스트에 무선 연결 제공.

- 특정 지역만 cover

	- 그게 Cell

	- Cell phone의 어원.

- 그래서 얘들끼지 '잘' 협력해서

- cell 넘어갈 때 안끊기게.



## base station

relay?

- 자기 구역의 host들의 packet을 wired network에 넘겨줄 책임 있음.



기지국이나

무선 공유기 등.

## wireless link

통신 매체임.

- 물리적 선 아니어도 뭐던 link할 매체는 있어야.

보통 moble(s)를 base station에 연결하려고 씀.



유선보다 불리함..

- 신호 감쇠..

- 방해물...

	- 회절?반사?

- 잡음...

- 거기에 독점도 아니고.

	- 여러 channal?

- multiple acccess protocol

	- coordinates link access..?

- 다향한 주파수 영역,전송 속도,전송 거리...

	- 지금은 

 



## infrastructure mode?

handoff:

moble이 다른 base station네로 가는 거.

handoff는 벗어나는 거,

handover는 넘기는 거.



## ad hoc mode?

늑 p2p

no base station

범위가 닿는 노드끼리만 통신 가능.

노드들끼리 직접 organize해서 network를 만듬.

- node 간의 routing...



ex:bluteooth,wi-fi direct,...



## infrastructure

>AP나 외부 base station 등

### single hop

user-base station-host로 

유저끼리 한 hop으로 서로 연결 가능?

대부분의 환경.



중?앙 집중적.

### multiple hop

보기 쉽지 않음.

여러 wireless node를 걸쳐 접속?

mesh net 등?

## no infrastructure

### single hop

no base station,

no conn to internet



bluteooth,ad hoc net 등?

### multiple hop

no base station

no conn to internet(www?)



may have to relay to reach other 

a given wireless node..?



MANNET:이동형 ad-hoc net

VANNET:차량간 ad-hoc net

- 미쿡 등 넓은 곳에선

- 차끼리 무선통신을 해서

- 차-train 비스무레한 거..?

# wireless.link.charactorlistic

wired랑 비교해서 큰,중요한 차이가...

1.decreased signal strength

- 신호 감쇠.

- 신호가 거리에 따라 약해짐...

- 유선도 있긴 하지만 그건 걍 리피터-설치하면 되거나

- 그럴 일이 거의 없음.

- 사거리 문제...

	- 기지국 더 까는 거 밖에 답이...

interference from other sources

- 다른 기기들의 간섭?

- 주파수 ex:AM/FM의 차이

- '황금 주파수 대역'..?

	- AM/FM 차이나는 것처럼 대역폭마다 장/단점이 있음.

	- 이 대역폭이 무선통신 최적화 대역폭인듯.

 >울나라 등 여러 나라에선 '회사가' 대역폭을 낙찰받아야 사용 가능.

	- 그래서 간섭이 심함...

	- 2.4GHz 등?

multipath propagation

- 회절/반사 땜시 메?아리 오거나, 시간이 달라지거나.



## SNR=신호 대비 잡음 비율

Signal to Noise Ratio

- 이게 클수록 signal을 extract하기 좋음..?

- 클수록 '좋은'거.

SNR vs BER tradeoff?

- 반비례 관계

- BER=비트-오류율..?

- 긍께 시간당 마니 보낼수록 오류율 증가..?



고로 같은 환경에서도 BER에 따라 전송 속도 바꿀 수도..?



근데 SNR도 움직임에 따라 변할 수 있어서

- 물리 계층?에서 '잘'해야..?



# 무선통신의 대역폭

802.11이 wi-fi임.

>외워두셈.

>ref ppt.

- 뒤에 붙은  글자?는 속도?에 따라.

- 무선-근거리...



802.15가 bluetooth



# IEEE 802.11 Wireless LAN

=wifi

2.4 Ghz가 마니 애용받네....

!졸기 시작

SU-MIMO

- 안테나당 user 1명 할당.

MU-MIMO

- 안테나당 여러 유저 사용 ㄱㄴ.

>우리가 주로 쓴느 거.



## .arkitecture

>졸다 놓침

## chan select

알아서 '잘'선택해야..?

- 2.

chan/associationsP

- 보통 ap가 알림..?

>ap1

passive/active scanning



becea con frame은 hred로 함.



frame ctlr?

- chd 5g

seq #도 존재.

ap



## addressing?

802.11 addr은

AP-출발지-라우터 mac addr이 먼저..?

거기서 벗겨지며 하위? 프로토콜로.



## rate adaptation?

그러니까 저 SNR은 속도?ish 한 거고,

AP에 가까우면 더 마니..?

>몰?루 겠다

>더 찾아봐야 될듯.



## CSMA in Wireless?

전송 전에 사용 여부 감지하고

충돌시 재전송.

문제점:

- 사용 여부 감지가 늦거나,

- 충돌 감지를 못하거나.



거기에다...

### hidden terminal problem

A-B,B-C는 통신이 가능하지만

A-C 사이엔 방해물이 있어서 직-통신이 안되는 경우에

A->B,C->B를 동시에 보내는데

A,C는 서로 충돌나는 줄 모를 수 있음.

### Signal attenuation

이번엔 방해물은 없음.

근데 signal strength 땜시

A->C는 못감..

- 간섭도 있어서..?

고로 avoid collisons:2+개의 node가 충돌 못하게!



CSMA:먼저 detect하고 보내기.



근데 그게 좀 힘드네...



고로 CSMA/CA=Collision Avoidance



### CSMA/CA

sender:

DIFS=Distributed Inter-Frame Space

시간 만큼 기다렸다 조용하면 전체-프레임을 걍 보냄.



근데 channel이 busy한 것 같으면

- random backoff time을기다리고,

>

일단 busy가 끝나면

바로 보내지 말고

일단 DIFS만큼 기다리고,

그리고 backoff만큼 일단 기다리기.

- 그건 랜-덤으로 정해짐.

- 그리고 accumulative?임.

- timer 시작~다른 곳에서 frame 전송 시작한 시간

	- 만큼 내가 기다린 시간만큼 줄어듦.

- 긍께 timer 시작하고

- 전송 감지하면 stop,

- 전송 끝나면 DIFS 기다리고 rezoom

- timer 끝나면 전송.

- timer 초기값은 random이고.



reciver:

다 받고

SIFS=?

만큼 기다렸다 ACK 보냄.



단,DIFS>SIFS?

- ACK가 send보다 우선순위?에 있게.



#### Collision Avoidance-RTS-CTS exchange?



그러면 공유기 상황에선

자기 RTS를 경쟁적으로 보내고

공유기가 CTS로 누구 1명에게 전송 허락을 줌.

그러겸 CTS 받은 쪽만 전송 시작.

frame type=RTS|CTS|

### CDMA=Code Division Multiple Access

일종의 암호?화를 함.



data bit 1개에 대해

긴 코드 전체와 xor을 함.



받는 쪽에서는 sender code를 아니까

저 code를 기반으로 decode?를 함..?



그러니까 encode는

Z(i,m)=d_i*c_m



비유로는 한명 그룹은 영어로 말하고

다른 그룹ㅇ느 한국어로 말하면

한쪽을 못알아듣겠어서 걍 skip?



기본적인 거는 자료 조사로 하셈!





# 블루투스 vs zigbee

blutooth

zigbee

2001 MIT 서 개발

소형.저전력

>bluetooth보다 소형,저전력,

보안 기능도 추가.



bluetoogh vs zigbee

확장성:

- bluetooth는 최대 7

- 얘는 inf

대신 보낼 수 있는 data rate는 별로...



얘는 p2p?



스마트 에너지/홈 엔터테인먼트 등.

iot 환경에선 이 프로토콜이 주?

- 스위치 정보 정도에 완전 빠른 속ㄷ도는 알 거 없음...

물론 얘랑-이터넷?이랑 연결하려면

중간 장비가 따로 있어야.





# 무선과 모바일

## 모바일리티?

no~high까지.

기지국간 이동시 어떻게 넘어가나?



no인건 한 AP만 쓰는 mobile user



### CDMA?

encoded=original `cross` chipping?

decoded=recived `dot` chipping?



그러니까 encode는 1xn을

mxn으로 바꾸고 flatten

decode는 

mxn을

>울나라가 첫 상용화..?

>다른 데는 GSM?=FDM+TDM 썼음.



그러니까 CDMA면

매 비트가 * 코드로 encode되고

받은 걸 





# cellurar network

## cellular network.topology?

cell=무선 통신이 가능한 영역.

- 크기는 설치 비용과 품질의 tradeoff로 결정됨.

보통 정육각형-단위로 cell 구성?

- 사각형/원 구조보다 효율 높음..?

	- 원은 사각지대 생기고

	- 4각형은 효율이...



구조가..

BS=Base Station

- 1차적 연결?

- 802.11 AP...?

- 모바일 사용자는 여기에 연결함.

MSC=Mobile Switching Center?

- BS들을 묶어서 컨트롤/연결하는 곳.

- BS들과 유선-인터넷 망과의 연결도 관리?

- mobility를 얘가 관리.



## 이동통신.역사

1~4G

1G

- 아날로그.

- 음성 only

- FDMA 방식 only

	- 즉,주파수 분할 only

- 2.4 kbps

### 2G

이제서야 Base Station System이 생..김..?

BTS-BSC-MSC-인터넷 순으로 연결?

아래일수록 수가 많음.



BTS=Base Station Transiciver Sybsystem?

=기지국

- 직접 이동전화와 연결되는 곳.

BSC=Base Station Controler

=제어국

MSC

=교환기

- 핵심 임.

- 외?부 전화망과의 연결을 얘가 해줌.



#### 2G.GSM 방식

FDMA+TDMA를 섞은 방식임.

여러 Freq band에 여러 



### 3G

음성+데이터 둘 다 지원.

4G와의 차이는

음성은 따로 다른 path 씀..?



radio network 

### 4G

전부 ip,패킷-기반임.

음성도.



방식[2]={LTE,WiMAX}

LTE

- 기존의 3G망 재사용.

WiMAX

- 백본도 무선..?



특징

- 모두 IP 기반.

- 음성/데이터 차별 없음.



### 5G

망 자체는 4G랑 동일.

대신 속도를 향상

(대신 coverage가 작아진 듯...)



전력소모도 줄고

mobility도 증가..?

- 500km/h로 달려도 끊김 없이!

handover interrupion time < 10ms

- 그 념겨주는 시간.



IOT의 통신 기반이 될 예정?

- 자율주행

	- 자동차-속도에서도 서버에서 정보를 얻을 수 있어야.

- 군사용?

자료 많으니 pass





# mobile.addressing/routing

## 단어들

home network?

- 처음 연결된 거기..?

- dhcp의 도움으로 처음 할당받은 데..?

permanant address?

- 이 ip로 연결하면 언제나 mobile에 접속 ㄱㄴ..?

- 물론 완전 perm은 아님...

	- 상대방 입장에서 perm이라는 거.

home agent?

- mobility를 담?당?

넘어가면..

visited network?

- 넘어가서 연결한 network

foregin agent

- 저쪽 네트웤의 agent?

permnant address

- 주소가 유지됨!

care-of-address

- 방문 네트웤에서 새 ip주소도 받음.

correspondent

- mobile div랑 통신하고 싶은 상대.

- 서버라고 생각해도 무방.



작동 원리?

- home agent한테만 care-of-address 알려줌.

- 그러면 home agent가 permnant address로 받으면

- 그걸 care-of-address로 보냄..?

다른 작동 원리?

- ...???



비유:

- 계속 이동중인 친구가 있음

- 걔 주소로 편지 보내고 싶은데 어케 보냄..?

- 1.모든 전화번호부 뒤져보기?

	- 현실적으로 ㅂㄱㄴ...

	- 모든 라우터가 반영해서 라우팅 할 수 있다면..

- 2.걔내 부모님께 물어보기?

- 3.facebook처럼 어디로 가는지 계속 남기기..?



### 방법[0]

라우터가 하게 한다면..?



forwardiing table을 저정도로 실시간으로 update하라고?!

현실적으로 불가능...

- 매 div를 관리하긴 table 크기 문제...

- subnet만 보고

보통 라우터는 subnet 주소 정도만 보고 라우팅 함..



차라리 end-system이 하게 하자...

### 방법[1]

간접 라우팅



home agent랑 통신을 하고,

mobile<->home agent<->server



### 방법[2]

home agent의 주소를 물어보면

그 주소대로

mobile<->server

양쪽 다 Home agent는 

Home agent 없는 채로 처음 연결한 거기가 home agent 역할을 하게 됨.



### RFC 3344

간접 라우팅 방식.

모바일-지원 라우터면 지원해야.



3단계 있음.

1.agent discovery

- HomeAgent와 ForeginAgent가 서로 정보 주거니 받거니?



2.registration with home agent

- home agent에게 care-of-address 알려줌.

3.indirect routing of datagram

- server->mobile은 home agent 거쳐야 하지만

- mobile->server는 그런거 없이 바로 보내도 됨.



1단계에서 ICMP 프로토콜을 씀..?

- 네트웤 관리용 프로토콜?

- Application Layer.

- 이 단계에선 type=9로 설정해야?

- RBHMGV bit..?

	- R:registraion requred?

- 보내는 care-of-address는 0개 이상..?!





그러니까...

foregin agent에 연결시

foregin agent느 COA를 할당해줌.

그걸 받은 div는

Home Address를 알려줌.

그걸 받고 

foregin agent는 얘가 연결됬다는 걸

broadcast함.

그러면...

- foregin agent는 mobile device를 알게 됨.

- home agent도 걔 주소 알게 됨.

- mobile div에 새 COA=care-of-address가 할당됨.



저 인증에도 lifetime이 있네...

속도가 꽤 많이 빠름.



비효율적일 수도.

- server->mobile은 먼 길 돌아야 됨...



여러번 넘어가면...?

- 재귀적으로 그러는 게 아니라

- home agent한테만 알려주는 거.



### 방법[3]

direct routing

- 없다는 거 들은 서버?가

- 바로 Home agent에게 묻고

바로 COA 찾가감.



>서버?상대? 지원 여부는 언제나 true임.

>Home Agent가 지원해줘야 하는 거지.










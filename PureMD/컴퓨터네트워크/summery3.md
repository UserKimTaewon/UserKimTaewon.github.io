# link layer

# feature?

mac addr

ithernet

# 주요 용어

node

- 네트웤에서 연결 '되'는 모든 것들

- 네트웍에 관여하는 모든 장비?

link=channal

- 노드간의 선로.



wired/wireless link

LAN

- 라우터 없이 물리적 연결 만으로 서로 주고받을 수 잇는 범위?



layer-2 packet=frame

- 이 계층에선 packet을 frame이라 부름

링크-레이어에선

노드 간의 통신을 담당함.



전송 계층에선 end-to-end

ip 계층은 공유기?간

링크 계층은 진짜 그 노드들 사이.



link layer는 물리적으로 연결된 두 node간의 통신 담당.

그래서 솦트/하드 둘 다..?



# link layer.context

각각 다른 방식으로 link 됬을수도..

네트워크에선 같은 AS에선 같은 프로토콜이지만

링크는 링크마다 다른 프로토콜일수도.



Ethernet/frame relay/802.11 등?



ex of 여행객?

- 버스 타고, 지하철 타고, 환승하며 감.



# 하는 일

datagram을 받아

헤더와 테일러?를 붙임.



얘는 header만 붙이는 게 아니라 trailer도 끝에 붙임?



그리고 공유도 담당.

MAC 주소가 이 계층의 ip 역할. 



신뢰성 있는 전송?

- 언제나 '최선을 다할게'

- 보장은 아님



flow control

- 두-노드 간의 데이터 흐름 조절?

- tcp에서도 하던 그거.

- 물론 방식은 다르지..

error detection

- by signam attenuation,noise

	- 긍께 잡?음이 섞이거나,감쇠되거나.

- 물리적으로는 다 아날로그다 보니까...

	- 그래서 감쇠된 걸 1로?0으로? 도 문제 중 하나?

- 보통은 에러를 알리거나 frame을 아예 drop하거나.

error correction

- 어느 정도는알아서 복구 ㄱㄴ.

half duplex?

- 양방향이긴 한데 동시에는 ㅂㄱㄴ.

- 무전기 처럼.

여담:802.11=WiFi

# link layer가 어디에?

랜 카드에서 담당함.

- 여기서 링크 레이어 말고도 물리 계층도 함.

호스트네 시스템-버스에 장착?

이름이 adaptor/NIC=Network Interface Card/랜카드

따로 장착할 수도 있지만 칩으로 내장할수도.



솦트/하드/펌웨어를 적당히 섞어서 사용.



펌웨어?

- 하드와 솦트의 중간.

- ram은 휘발성이라 power 나가면 날아가므

- 그래서 ROM은 power 나가도 ㄱㅊ

- 긍께 ROM=Read Only Memory에 저장된 부분?

	- 말 그대로 Read Only

	- 중요 시스템 파일?부트로더?등.

	- 보통은 그런데 요새는 안그런 경우도..?

# adaprots.work.ex?

send side:

- datagram을 frame르로 감쌈.

- 에러 체크용 비트,flow ctrl 등 더함..

recv side:

- 에러 확인, flow control

- frame->datagram으로 unpack

# frame.구조

사실 프로토콜마다 좀 다름.

Eithernet이나

IEEE 802.3=wifi 등.



공통적으로 payload,header,tailer가 있음



여기선 특이하게 목적지 주소가 먼저,그 뒤에 src 주소.



맨 뒤에 4byte FCS?

- 에러 체크용?



Preemple

- 제어 신호?

- 속도 제어/실제 데이터를?



Ethernet에는 type 필드가 따로 있음..?

- 한 프로토콜만 도는 게 아니라..

- 패킷 전송 말고 다른 거도..?



# 에러 감지&정정

에러가 있는 걸 보낸다면 비효율적..?

- 링크 계층에서 미리 처리해야!

여기선 ACK 같은거 없..음...

- 수정 시도/drop

- 가능하면 재전송 요청?

원 데이타에 에러 발견/정정이 가능하게 추가 정보를 붙임.

그게 EDC.

- 물론 절대 감지율 100%는 없다...

- EDC 필드가 클수록 감지/정정율 높아지긴 할거임

	- tradeoff

## 패리티 비트

가장 간단!

맨 뒤에 1bit을 추가하는 거.

전체 1의 개수를 홀/짝수 중 하나로 맞추는 거.



오류 2개 나면 감지 불가능



2d 패리티..?

행-열에 대해 parity를 체크함.

mxn 비트에 대해

m+n+1개의 패리티가.



그걸로 에러 어디서 났는지 1개는 감지+정정 가능.

- 행-열 감지.

- 물론 2개면 정정은 ㅂㄱㄴ.

- 어느 두 쌍일지 결정 ㅂㄱㄴ

## CRC=Cyclic Redundancy Check

더 센 오류 감지/정정?

div 말고 xor을 하는 방..식..??

위-아래로 나눗셈 하는 그거랑 비슷한데

아래로 내려갈 때 빼는 대신 xor을 함.

그렇게 하면 '나머지'가 남음..?

그걸 붙여서 보냄..??

'나머지'와 '묷'을 다 보냄.

송신자를 [D,R]/G로 나눠서 0이 되면 오류 없는 거..??

- 긍께 concat(D,R)/G=0이 되게 R을 만들고,

- 여기서 그렇게 되면 오류가 없는 거.



여러 링크 레이어 프로토콜에서 애용중인 프로토콜

## 에러 수정

다음 시간에.

해밍 코드가 주 예시.

# 링크.공유

독점하는 경우가 가장 쉽지만

인터넷에서 그러기엔 O(n^2)라...

물리적으로 무리!



대신에 충돌 가능성이 생김...

2+개가 동시에 충돌하는 경우...



링크는 2가지 종류가 있음.

point-to-poinr

- 독점!

	- 둘밖에 없음

- PPP?

broadcast-공유

- Ethernet

- HFC

- 802.11 wireless LAN=WiFi



그러니까 모임에서 말하는 것 같은 거.

- 2명이면 한명이 말하고, 다른 사람이 듣고가 쉬운데



# mac=Multiple AcCess protol?

single-shared-broadcast-channal

- 한 채널을 다같이 씀.

- 사람 대화처럼

- 동시에 말하지 않고

- '적당히 눈치껏' 대화 타이밍을 받음.



## 이상적인 access protocol은..

하나의 노드가 전송을 독점할 수도.

아니면 다수의 노드가 균등하게 전송하거나

아니면 조정자가 '잘'분배하거나.

## MAC.protocol.taxonomy

channal partitionaing

- 채널을 처음부터 분배..?

- 시간/freq/code 기준으로

- 충돌 없음

random access

- 서로 알아서.

- 체널이 안 나눠져있어 충돌 허용..

- 잘 'recover'하게.

- 대신에 쉬는 채널을 쓸 수 있음.

taking turns?

- 순서를 배정?

- 충돌이 없음..

- 한명이 말 끝내고 다음 애보고 말하라고 하는 거.

- 말 할거 없으면 걍 다음 애보고 말하라고 하는 거.



>저 random access는 대부분의 경우인

 >나머지는 쉬고 혼자서만 하는 경우에 강함.

## MAC.protocols.channal.partitioning

### TDMA=Time Division Multiple Access

시간 단위로 쪼개서

다른 노드 차례면 그 노드가 안보내도 쉬어야.

전화 회선에서 주로?

### FDMA=Frequencccy division multiple access

말 그대로 주파수에 따라 나눔.

오케스트라 합주도 이 원리.

- 음색이 구별 ㄱㄴ.

라디오 방송도.

### CDMA code division multiple access

각각 암호화해 보내고

수신 측에서 해독??

## polling

master node가 slave node를 '초대'해야 참가 가능.

그러니까 매우 중앙-집중형.

마스터 노드가 모든 순서 결정!



보통 slave div들이 'dumb'한 경우에..?



단점으로 master가 down이면 암겄도 못함.

## tocken passing

control 'tocken'을 돌림..?

한 노드에서 다른 방향으로..?

긍게 노드들끼리 2방향-연결인..가..??

- 공유는 아니게.

## 랜덤 방식

진짜 눈치게임.

알아서 눈치껏 보내기!

충돌나면 재전송이고.



## random access protocol

각 노드들은 독점을 하려고 하고,

조정도 없음..

그래서 2+가 동시에 보내면 충돌!



일단 감지가 가능해야 하고.

그리고 나면 어케 해결+재전송?



slotted ALOHA/ALOHA/CSMA/...

등 여러 방식이 존재.



### ALOHAnet

하와이 대학에서 1971년에 개발.

Adaptive ... 어차피 ALOHA에 끼워맞췄겠지.



전송 기간이 겹치면 양쪽 다 실패임...



각 프레임은 같은 길이를 가짐->전송 기간도 같음.

각 노드들은 랜덤하게 각자 알아서 전송 시작함.

충돌 나면 재전송.

감지는 echo 안오는 거로 timeout.



#### pure=unslotted ALOHA

가장 간단.

서로 조정같은거 없음.

3개가 동시에 겹치면 다 날아감...

A-B,B-C 겹치면 B를 날려서 A,C는 살린다? 그런 거 없음!

효율이 약 18%...?

#### slotted ALOHA

각자 시간을 나눔.

충돌이 나면 random 시간을 기다리고,

- 눈치싸움

그 뒤에 보냄.



그나마 충돌 확률이 반으로 줄어듦.



약 37% 효율..?



### CSMA=Carroer Sense Multiple Access

transmit하기 전에 상대방이 보내는지는 확인함

말하는 사람이 없어지면 그제서야 보내기 시작.



물론 충돌 완전히 해결은 못함.

- 확인-send-다른노드에게 도착 간의 미묘한 간격동안 다른 node도 같은 선택을 할지도.

	- 컴퓨터 속도,물리적 전파 속도 등의 문제 땜시.

	- 둘 다 아무도 안말하는 줄 알고 말했는데 뭐가 들리네..?

- starvation...

	- 기다리다 시간 다 지남..



#### CSMA/CD

CD=Collegion Deteaction?

전송 signal의 강도 감지해서 그거로 충돌 여부 판단.

일단은 전송 취소하고 jam signam을 보내서

상대방도 그만두라고 말함.





### Ethernet네 CSMA/CD?

ppt 보셈

NIC=랜 카드.

//"taking turns" MAC protocols?



>random access protocols

## 채널 분할.장점

부하가 높을 때

모든 사용자?가 공평하게 받을 수 있음.



부하가 적거나 불균등하면 비효율...

- 공용 1/N의 부하...

- 쉬는 대역폭?을 끌어올 수 없음

## taking turns.문제

링크가 끊어지면(그러니까 저 발언권?이 증발하면) 문제...

>mac protocols

# LANs

## MAC 주소와 ARP?

랜 카드의 id? 주소가 mac adress

mac<->ip 주소를 연동시켜주는 프로토콜이 ARP

ip address는 일종의 집주소.

- 논리적 주소!

- logical-network-layer adress



### mac 주소-48bit

매 랜 카드에게 고유함.

전세계적으로 고유함.

- 주민/여권번호 같은거..?

- 얘는 ipv4처럼 꼼수 안써도 되나 보네?

- 각 어댑터마다 unique하게 있음.

NIC의 ROM에 저장되어 있음.

- 가끔은 sw로 set 가능하기도.

앞 3byte가 제조사 고유번호

그 뒤 3byte는 제품의 시리얼 번호

- 긍께 기기-종속적인 거.

alllocation by IEEE

- 제안+관장

ip 주소는 목적지 '네트웍' 찾는게 주 목적.

MAC 주소는 최종-목적지 '기기'를 찾는 게 목적.

mac네 dst는 항상 바로 옆 기기임.

ip는 endpoint를 가리키는데.

## ARP=Adress Resolution Protocol

ip 주소는 일단 알겠는데 mac 주소는 어케 암?



managed by switch?

스위치는 ARP table을 갖고 있음.

- ip 주소<->mac 주소 mapping

- TTL이 존재

	- 보통 20분 동안만 유효.

## ARP in same LAN

A->B로 보내고 싶지만

A는 B의 ip addr만 앎.



그러면 a가 ARP query packet을 broadcast함.

- ip 주소가 거기 있음.

- broadcast라 랜 내의 모든 기기가 받음.

그러면 받은 B가 reply함

- B의 MAC 주소를 받고.

- 얘는 broadcast 아님.

- A의 MAC 주소로만 감.

## ARP.다른 네트워크간?

??? 위키에서 찾아본 바로는 ARP가 닿는 범위=한 네트워크의 범위 라고도 하여

ARP는 다른 네트워크에는 안닿는다는데...?

# Ethernet

선-기반 LAN의 주 프로토콜?

간단한 칩 가지고 multiple speed?

첫 기술이고

간단하고 쌈.



## Ethernet.frame

7btte preassemble

- 10101같은 패턴으로만 참...?

- 맨 뒤는 11

- 동기화용

dest.addr

scr.addr



type

data

CRC





최소 64,최대 1518 byte

## 이더넷.물리 구조?

bus

- 한 물리-선에 버스 여럿을 물려 썼음

- 초창기.

- 충돌...

star

- 요새는 switch를 씀.

- 중앙-switch랑 모든 컴터가 연결

- switch는 충돌 안나게 '잘'함.



## Eithernet.특징

connectionless

unreliable

- 에러 알려주는거 따위 없음.

Ethernet.MAC protocol=unslotted CSMA/CD

+Binary Backoff?

Eithernet 표준도 여러 개..?

- MAC protocol과 frame format은 공유.

- 속도와 물리-매체가 다름.

	- 동축 케이블/광케이블/...



 switch

star 구조로 연결이 되있을 때

- 즉, 각 호스트는 스위치와 연결되 있을 때

역할?

- buffering packet

- mac 주소 보고 broadcast를 막?음



# ethernet switch

link layer divice임..?

- store+forward ethernet frame

	- 긍께 저장하고 적당한 연결에 보냄.

	- ARP table 기반으로.

- input네 MAC 주소를 보고

	- '적당한' 곳으로 보냄

	- broadcast일 수도 있고,아닐 수도 있고.



transparent

- 사용자 입장에서는 switch 있으나 없으나 해야 될 일은 안바뀜.

# swith table

스위치는 어디로 가야 어느 호스트로 갈지를 '배움'

- frame을 내부-기기에서 받고

- 다음에 dest에서 src로 오면

- broadcast 대신 걍 src로만 보내면 되겠네

- sender/location pair을 switch table에 저장..?

- 유효-시간이 있음.



저장하는 data가

MAC addr, interface_no,ttl

이 끝임.



switch table에 없으면

flood(broadcast랑 같은 뜻)를 함



있으면 걍 한곳에만 보내지.



스위치도 계층적-구조일 수도.





# 스위치 vs 라우터

거의 일이 비슷함.

라우터가 더 복잡하고 하는 일 많음.



둘 다 '적당한 곳'으로 보내는 역할.



둘 다 forwarding table이 존재.



 data center

건물 하나에 수많은 container가 있음.



# road balancing..?

- 조사 해보셈

- 서버 '하나'로는 감당하긴 무리....

- 긍께 요청을 '적당한' 물리-서버 랙에 할당하는 거..?

- 그거만을 위한 컴터가 따로 존재.

- 스위치 말고도.



사실 스위치도 top-down 형태만 하지 말고

신뢰성을 위해 서로 연결하는 경우도?



물론 같은 높?이 끼리 연결은 없음.

- 재귀 문제?








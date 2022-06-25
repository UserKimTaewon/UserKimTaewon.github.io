\\<-- !4장 네트워크 계층과 데이터 평면 -->
# 서론

tcp/udp는 끝냈고

application layer는 했으니



이제 transport layer에 내려온 뒤에 어떻게 되는지



# 용어

application(data)->

transport(segment)->

network(data gram)

으로 각 계층마다 보내는 단위 데이터를 다르게 표현하며

다 '패킷'으로 통칭 가능



# 네트워크 계층

## 서론

하는 일="transport segment from sending to reciving host"

- 즉,그 segment를 실제로 전달



송/수신측의 일?

- 송신측:sgement를 datagram으로 감쌈.

- 수신측:datagram을 다시 segment로 위 계층에 보냄.



동작하는 곳?

- transport 계층까지는 end-to-end였고

- 이제야 호스트=각 라우터에서 돌아감.



라우터는 하는 일이 좀 많음

- 고로 tcp/udp에 비해 일 자체가 꽤 단순화됨..?



라우터 각각도 ident가 존재해야..

- by ip 주소체계?

- network 계층네 헤더에 붙음.



더 밑에 링크 계층도 존재...



네트워크 계층에서는 라우터가 등장함.

크게 3가지 일을 함.

## 라우터

### 라우터.작동

간단히 말하자면 컴퓨터임.

ip routing만을 전담하는.

- 긍께 받은 data gram을 '적당한' 데로 전달하는 거만 함.



하위-네트워크 게층의 도움을 받아

data gram을 받는/보내는 input/output Queue가 있음.

- queue가 input/output 별로 1개 이상 존재할수도.

여기서 데이터 그램의 헤더를 보고

어디로 보낼 지 결정

이때 주로 보는 게 ip 주소임.

- 하위 레이어에서는 ip 주소만 갖고 모든 주소 결정하니.



고로 ip 주소 쳬계도 공부 할거임.



사실 이 '결정'도 여러 방식이 있음

고전은 걍 table-사용. 고정적.

최근은 펌웨어 적.



솦트웨어/하드웨어/펌웨어?

- 펌웨어는 하드웨어+소프트웨어?

	- 걍 특수목적 칩.

	- 속도는 빨라짐.



이런 개별 라우터가 작동하는 곳이

'data plane'

여기서 하는 게 ip 주소 체계.



ip 주소는 ipv4 기준으로

0~255로 4개의 숫자를 사용.

어디까지는 네트워크 지칭, 나머지는 호스트 지칭..?

- 호스트마다 ip가 있으니까.

	- 호스트가 소속된 네트웤 주소..?

	- 이것도 class A~D가 있음.

		- A는 네트웤 부분이 길고, 호스트가 짧음.

		- 기관마다 쓰는 종류가 다..름..?



#### 경로 테이블?

- ip 주소->output 경로 인 table

- 누가 만듦?어케 결정?관리?(동적 변경?)

- 이 table 만드는 게 routing algorithm

	- runtime에 바뀔 수 있음...

	- 이쪽도 공부해야..?

	- 크게 2개 정도람..?

	- full lookup vs nearby lookup?



그래서 네트워크-계층은 4,5장으로 2개로 나누어짐.



#### 라우터 방식[3]

- 즉,스위칭 패브릭 종류

1.memory

- 걍 범용-컴터

- 고전

- 소프트웨어적으로.

- 지금은 안씀.

2.bus

- 중?앙 라우터가 연결된 모든 망?에 대해 책임지는 거.

- 하드웨어-버스 경로 하나를 다 공유

- 여기서 경쟁이 일어날 수도...

- Cisco 5600

3.cross bar

- bus 비스무레하지만 여러-경로가 존재.

- 어느 걸 쓸지 결정 ㄱㄴ?

- =interconnection network?

- bus랑 비스무레-하지만 여러 경로가 존재

	- 근데 이 교차점이 문제..

- 계랑판이 banyan network?

### 라우터.구조

- routing processer

	- 경로 계산용

	- sw 기반-milisecond

- high-speed switching fabric?

	- 하드웨어-기반->nanosecond latency?

- i/o ports



#### input port

##### function

물리-라인->링크 계층->큐

를 다 담당함.

여기 도착하면 data gram이 됨.

뒤에 switching fabric에 들어감.

##### queueing

fabric이 전체 input port에서 들어오는 것보다 느리면

각 input port에서 queueing이 일어남.



이거 때문에

- queueing delay

- loss

	- buffer overflow 땜시.



Head-of-the-line blocking?

- 긍께 맨-앞에 있는 datagram때문에

- 뒤에 있는 datagram은 사실 갈 수 있는데 못가는거.



#### output port

buffer->링크 계층->물리 라인.



링크 계층 오류 정정에도 버퍼가 필요.

이쪽 버퍼 크기도 중요.

- Head-of-the-line blocking을 막기 위해.



#### Scheduling?

그러니까 어느걸 먼저 전송할지 결정하는 거.



policies:proority

- 우선 순위 큐.

- 우선순위 높은 거 먼저 전송.

policies:round robin

- 걍 돌아가면 주기.

weighted Fair queueing:

- 라운드 로빈+우선순위.

	- 각각의 '가중치'에 따라.



그만큼 여러 방법이 존재,잘 설정해야.

### forwarding

#### destination-based forwarding

ipv4

- 32bit *4

주소 범위->보낼 링크인 테이블이 존재.

그거 lookup



사실 lookup도 여러 방법이 있음..?



longest prefix matching

- 가장 길게 match되는 곳으로 보냄

- 앞?에서부터 ip주소(bit단위?)비교해가며

- table 범위에 더 '잘' 맞게..?

- 사실 matching은 비쌈...

- 고로 전용-램이 존재..?

	- ternary content addressable memories=TCAM

	- 특수-메모리.

	- CISCO?가 이쪽 명?가?

		- 자격증도.



transport layer는 양 끝에서 작동.

network layer부터 중간의 기기에서 작동.



## network.layer.key_function[2]

1.forwarding

- 걍 라우터가 받은 걸 어디로 넘겨줄지 결정하는 거.

- 매번 하는 거.

- 개별 라우터 에서 동작.

2.routing

- 한 패킷이 가야 할 전체 경로 설정하는 거.

- 포워딩이 이거로 만든 라우팅 table을 참조함.

- 5장 내용.

## data/control plane..?

- control은 예전엔 각-라우터가 책임졌음.

- 근데 이제는 담당하는 특정-서버를 만듦..?

	- 이런 방식을 software defined networking이라 함.



### data plane

forwarding 하는 데?

개별-라우터에서 동작

local임.



### control plane

routing 하는 데?

네트워크-전체 단위.

전통적/SDN 으로 2가지 방법이 있음

전통적은 라우터끼리 협력하는 거.

- 일종의 p2p? 중앙이 없이 서로 교류만으로 하니까...

SDN은 중앙-서버가 존재하는 거.



## network.service.model

희망사항으로는...

- guranteed dilivery

- guranteed bandwodth



하지만 현실 network layer는 그런 거 없음.

>ATM이라고 다른 통신망-모델이 존재..?

>찾아보셈

>우리 수업에선 안나옴.



## ip datagram.format

### 16bit

protol.version.no

head len

service.type:4bit

>사실 ipv4/ipv6이랑 구조가 좀 다름...

16bit:

length

- 전체 길이

identifier

16bit{flags,fragment offset}

8bit time to live

- 최대-hop 수.

- 라우터 지날 때마다 --

- 0되면 걍 drop

	- 일종의 스택-깊이-제한 ish한거.

8bit upper layer

16bit header hecksum

- 헤더에 대해서만 체크섬.

	- tcp는 데이터에 대해서도 했지만 애는 그런 거 없음.

32bit src.ip.addr

32bit dst.ip.addr

va_len options

- timestamp, list of routers to visit? 등

va_len data



최소 20byte IP

## IP.fragmentation

라우터마다

MTU=최대-datagram-크기

가 있음

그래서 너무 크면 라우터에서? 쪼갬.

- 이때 쓰는게 위쪽 fragment offset

분해 된건 end에서 도착해서야 재-조합됨.



ex:

4000byte data gram

MTU=1500byte

원본 length=4000,id=x,fragflag=0,offset=0

파편[0] length=1500,id=x,fragflag-1,offset=0

파편[1] length=1500,id=x,fragflag-1,offset=185..?

파편[2] length=1040,id=x,fragflag-1,offset=370..?

- 헤더 길이 20byte 생각해야.

- 이때 실제 data len은 최대 1480임.





## ip addressing

사실 라우터는 연결되는 경로 개수만큼 여러-ip-주소가 있어야..?



### 계층적 주소 체계?

우편 번호.ex

12345면

12가 특별 시/도

3이 시/군/구

45가 동

전화번호도

+81-32-8005-3224 처럼

국가-지역-로컬-방번호



이렇게 ip도 네트워크+호스트 주소의 결합.





### ip 주소.등급

ICANN에서 ip 주소를 총 관리함.

class A~E가 존재.

저거 별로 

0

10

110

1110

으로 시작 비트가 다르고

A->D로 갈수록 network id에 할당하는 bit 증가, host id에 할당하는 bit 감소

학교는 class C를 애용.

class A는 초창기-기관에서 반 잘라서 독점?함.

- 엄청난 수의 host를 독점 ㄱㄴ.

class C는 한 ip 주소에 

### subnet

저 ip-주소 문제 때문에 한 거.

host id의 앞쪽 일부를 sub-network id로 활용할 수 있게 하는 거..?



그러니까 ip 주소를 재-분할하는 거.

subnet mask를 이용하여 결정.

ex:subnet mask가 255.255.255.0이면 앞 24bit을 네트워크 id로 사용하겠다는 거.



그래서 subnet mask를 보면 최대 몇개의 기기가 더 달릴지 알 수 있음..?



### CIDR

=supernetting?

=Classless Interdomain Routing

반대로 network id의 일부분을 host id로 쓰는 거.

ex:200.23.12.0/23이면 앞 23bit까지를 subnet으로 쓰겠다..?



필요성?

class A는 네트워크 128개

B는 약 16000개

C는 충분히 많이 배부는 가능하지만 호스트 개수가 너무 적음...



### ip address.how to get?

예전엔 수동으로 해야 됬는데

DHCP 프로토콜이 자동으로 해줌

- Dynamic Host ...



노트북 ex에선

인터넷?네트워크?연결이 되자 마나

dhcp server라 있는지를 broadcast함.

=dhcp discover

그걸 dhcp 서버가 할당을 해줌



DHCP도 사실 응용-계층, UDP 기반.



사실 학생-수 만큼 갖고 았는 게아니라

적당히 돌려씀..?

### NAT

=Network Address Translation

주로 가정 내에서.

인터넷 공유기 1개에만 ip 주소 할당이 되어있음

같은 공유기에 연결된 기기에선느 가상(사설)ip를 부여

외부에서는 하나의 ip만 노출.

가상 ip는 내부에서만 통용됨.

- port forwarding이 이래서 필요...

그래서 사설 ip 영역:

A:10.x.x.x

B:172.16.x.x

C:192.168. ...

으로 해서 이 영역은 무조건 사설 ip



그래서 









# 네트워크 계층.control plane


라우터 관리하는 거.

각각의 라우터-레벨에서 돌거나

라우터 묶음을 상위-레벨에서 관리하는 서버가 있거나



OSPF,BGF,....



forwarding

- in data plane



routing

- in control plane



routing.way[2]

- per-router ctrl

- centeralized



# 라우팅=?

라우팅 테이블을 만드는 과정.

라우팅 테이블?

- 받은 패킷을 어디로 보낼 지 결정하는 table

- cost까지 table에 내장..?

# 라우팅.방식



per-router-control plane

- 기존 방식

- 라우터끼리 통신.

logically centralized control plane

- 최신 방식

- 중앙-서버랑 라우터가 통신하고

	- 각종 정보도  보내줌

- 중앙 서버가 라우팅 테이블 정해줌



기존 방식[2]

- link state?

- distance vector?



결국 목적은 가장 '적절한' path 찾는 거.



## routing.protocol.goal

가장 '좋은' path 찾는 거.

cost도 적고,빠른 거.

## network.추상화.그래프

그래프는 노드와 엣지로 표현됨.

엣지는 노드 간 연결=경로임.



cost?

- 엣지 간 거리같은 비용.

- 가장 단순한-모델은 모든 cost=1

- 하지만 현실적으로는 혼잡도 등 때문에 달라짐

- 암튼 경로마다 있는 값.

- 총 비용은 단순히 지난 경로의 cost를 합하면 됨.





## static vs dynamic

static=수동 라우팅

- 관리자가 직접 바꿈.

- 변화가 느림

- 솦트가 간단.

- 소규모, 변화 거의 없는 네트웤용

	- 인터넷에선 거의 불가능한 조건...

dynamic

- route 조건은 자주 바뀜...

- 어차피 초기에는 관리자가 초기화 해줘야.

- 현재 대부분의 프로토콜

## dynamic.way[2]

global

- 라우터는 전체 네트워크 구조,연결 비용을 알고 있음.

	- 이상적, 중앙집중-에서나 가능

- "link state" 알고리듬?

decentralized

- 직접 연결된 라우터 정보, 최종 목적지를 가기 위한 경로 비용, 다음 라우터 정보만 앎.

- 계속 계산-실험-보내기 반복

- "distance vector"

## routing.algorithm

### link state

각 가우터는 전체 네티웤의 구성=topology와

링크 상태 정보를 앎

각 라우터는 전체 네트워크의 상태 정보로 최적-라우팅 테이블 만듦.



즉, 최단-경로-알고리듬이잖아

다익스트라 방법이 가장 유명

- 다익스트라: 이쪽 분야에 많이 기여한 분?



Link State Advertisement(LSA) message?

- 나와 직접 연결된 이웃 라우터 정보

- 내 이웃의 링크 정보

	- 연결,비용,상황 등...



#### 실행 방법

LSA.생성?

- 이웃 라우터의 정보가 바뀌면

- 아니면 주기적 체크(보통 30s)

라우터는 LSA를 같은 네트워크(AS?)에 속한 모든 라우터에 전달.

각 라우터는 받은 LSA를 기초로 전체 네트워크 토폴로지를 결정

그리고 그거 갖고 최소-경로 정함.

##### 다익스트라.알고리듬

iterative임. 라우터 개수만큼 반복.

일단 최소 O(n)임..?

>모든 라우터 확인해야.





>가정은 각 노드에는 출발->자기 거리 저장한는 variable 필드 하나,

>그리고 자기가 연결된 모든 노드와 자기->걔 거리 저장하는 static이고 가변 길이인 필드 하나

가 있음.



각 노드에는 출발-node로부터의 거리가 저장되어 있음.

시작은 inf,

출발-node는 0



그리고 아직 확인 안한=unchecked 노드 배?열 (보통은 최소-힙으로 구현?)

이 있음. 처음에는 전체 노드를 다 담음.



그러면 unchecked에서 거리가 min인 node를 하나 pop함.

그리고 그 노드에 대해 연결된 노드들에 대해 거리를 update함.

- 연결된 모든 노드에 대해 거리를 출발->걔 거리를 min(출발->걔 거리,출발->자기+자기->걔 거리) 로 정함.

그리고 다시 pop으로 돌아감.



확인 안한 node가 없어지면 끝!



가정?

- 근데 그러면 한번 pop한 노드 거리는 안바뀔거라고 가정하네..?

- 얘를 update하려면 얘보다 거리가 짧은 경로가 존재해야 하는데

- 근데 얘가 현재 알려진 최단 경로니

- 얘보다 나중에 있는 노드에서 update 하려면

- 자기 거리+연결 거리이니

- 걔는 무조건 얘 거리보다 기니.

	- 그래서 연결 거리가 <0일 수 있으면 동작 안하는 구나...



시간 복잡도가 약 O(n log n)

라우팅 테이블에서는 

다익스트라로 최단거리를 걍 구하는 것 말고도

어디로 보내야 최단거리인지도 저장함.

##### 다익스트라.문제?

ocillations possible?

현실에서는 저 노드 간 거리-비용이 static이 아니라

오히려 자기가 보낸 트래픽과도 관련이 있어서

이쪽이 최적이어서 보냈더니

거기로 트래픽이 몰려서 느려지고

그래서 그쪽이 최적이 아니게 되서 다시 다른 쪽으로 보내고

이번에는 이쪽이 느려지고...

같은 문제.

- 이경우에는 반?반?나눠 보낸것보다 효율이 안좋아짐...

- 고로 거리-비용 결정할 때 자기가 보낼 패킷에 대한 적응도? 같은 거 고려해야.

	- 복잡!





### distance vector

#### bellman-ford equation

d(x,y)가 x->y로 가는 최선의 비용이라 하고

c(x,v)가 x에 인접한 v로 가는 비용이라 하면

d(x,y)=min(c(x,v)+d(v,y)for v in 이웃(v))

임.

여기서 d(x,x)=0(자명)이니

그거 갖고서 나머지도 resolve 하게 됨?



이거 쓰면 누구를 통해 가는 게 가장 효율적인 것도 알 수 있음?

- 긍께 다음 라우터에 얘한테로 보내주세요도 할 수 있음..?



#### 약점?

자기 이웃만 알고 있음..?

- 긍께 내가 전체적을 모..름..??



- 자기가 저장하는 건 자기->연결된 라우터->목적지의 최소 비용 뿐.

	- 중간에 어느 과정이 있는지느 몰?루

- 그리고 자기->연결된 라우터 의 비용

- 전체적-구조는 저장 안함.



- 긍께 보내는 정보가

- 모든 목적지에 대해 자기->목적지 비용의 최소값을 보냄.



"good news travels fast"

- 최선 경우?

- 별 문제 없이 잘 돌아감

"bad news travels slow"

- count-to-infinity problem?



x<->y가 5

x<->z가 50

z<->y가 1이면

z 입장에서는 z->?->x는

걍 y로 보내면 6 cost로 보낼 수 있음.

고로 z->x 비용을 6으로 저장,



여기서 y가 x<->y가 60이 된 걸 감지하게 되면...

일단 z에서 z->x를 cost 6으로 할 수 있다고 했으니

y->x의 비용은 min(x<->y,y->z->x)=7이지.

근데 사실 그 z->x는 y를 생각한 거라 그 y->x 비용 7된 update를 받으면

같은 맥락으로 z에서도 z->x 비용을 8로 update함.

그러면 그걸 받은 y에서도 z->x비용을 update하고...

그거를 z->x가 60이 될때까지 44?번이나 update를 해야 converge...

### 비교?

distance vector-RIP,IGRP,...

- 간단,flat?

	- 최소-범위에서 사용 ㄱㄴ.

link state-OSPF,ISIS

- 크고 계층적인 네트웤 용.



# internet.real

저 예제에서는 모든 라우터=노드가 동등함

근데 현실에서는 그럴 수가 없음.



그래서 Autonumus Systems=AS 그룹으로 묶어서 사용..?

- 한 기관에서 관리하는 네트웤.

- 같은 네트워크 id를 가는 집합..?



intra-AS routing

- 같은 AS 내의 라우팅.

- 같은 AS 내에서는 동일한 라우팅 프로토콜 공유해야.

	- 다른 AS면 달라도 ㄱㅊ.

- 게이트웨이 라우터?

	- 얘는 한 AS 소속이면서 다른 AS소속 라우터와 연결된 라우터.

inter-AS routing

- 게이트웨이-라우터 간에만 일어남.



그래서 AS에서는

intra+inter -AS routing이 다 협력해서

routing table을 만듦...?



IGP=Interior Gateway Protocol

- Intra-AS

- AS 내에서만 사용.

- ex

	- RIP-Distance Vector

	- OSPF-Link state



EGP=Extorior Gateway Protocol

- Inter-AS

- ex-BGP(Path vector 방식?)



## Intra-AS Routing

RIP,OSPF,

IGRF?

- 시스코네 고유?



### RIP=Routing Information Protocol

초창기,레거시 에 가까움.

요즘은 안씀.

단순화된 거리 벡터 방식

링크 비용을 모두 1로 가정.

30초마다



보안 문제 있어서 안쓰임.



최대 15개까지의 소규모 네트워크에서만 가능..?

초기 설정이 쉬운 표준-라우팅 프로토콜?



### OSPF=Open Shortest Path First

Open-개방형 라우터?

- 제조사 다른 라우터에서도 사용 ㄱㄴ.

- 일종의 플랫폼-독립적?



link-state 사용.

LSA 메세지를 '전체' AS 라우터에 다 매번 보냄.

- flooding!

보안

- 거짓 정보로 인한 네트워크 문제를 차단..?



얘는 링크의 상태 변할 때마다 알림.

Convergence time이 빠른 편?

라우팅 정보 갱신 회수가 적음

링크 유형에 따라 경로 비용을 다르게 설정 가능.

- 고로 RIP에 비해 쵝 설정이 복잡...

경로 설정을 하기 위한 연산이 필요.

- 라우터의 성능이 중요...

RIP보다 속도?좋음



장점-계층 구조 사용 가능?

한 AS가 다른 여러 AS르 포함-ish가 가능? 

게이트웨이=바운더리



#### 계층적 OSPF

AS가 너무 크면 하나의 OSPF나으로 운행하기엔 트래픽 부담이..

이를 해결하기 위해 지역화(subnet?)

2-level 구조.

- local area

- backbone



라우터

- area-border

	- 한 하부-AS와 backbone-AS 사이.

- boundery



## Inter-AS routing

일단 AS1의 라우터가 AS3으로 가는 데이터그램을 받았다고 하자.

어느 게이트웨이로 보내야 하지..?



고로 AS1이 알하야 하는건

- 어디를 통해야 AS2로 보낼 수 있는지



### BGP

표준-프로토콜임.

"glue that holds the internet together"



BGP는 각AS에게 정보[2]..?

- eBGP-게이트웨이 간 정보

- IBGP-게이트웨이->내부 라우터?



그러니까 eBGP는 게이트웨이-간에서 할 일,

iBGP는 게이트웨이가 자기 소속 AS의 라우터들에게 할 일.



eBGP는 어디로 가야 외부-연결이 되는지를 확인하고

iBGP는 그걸 내부의 라우터들에게 알리고.





# the SDN control plane

ip 계층의 라우팅..?



road balancing이 문제가 생김...?

- 적당히 트래픽을 나눠 보낼 필요가..?



기존엔 control/data plane이 분리 안됨..?



이제는 네트워크 관리자가 패킷의 흐름을 제어할 수 잇게 함.

중앙 remote control plane이 각 라우터의 forwarding table을 관리함.



## 왜 logically centrazed control plane?

네트워크 관리가 수월

유연성

상황에 따른 유연성

programming routers..?

>OpenFlow API?

- distributed면 각 라우터 update 하는게 좀 힘듦...

- 하지만 중앙이면 중앙-서버만 update하면 새 라우팅 알고리듬 ㄱㄴ!

기존에는 라우터-제조-화사가 다 관리했다면

이제는 programm 가능.



### 비유-mainframe to personal

컴퓨터도 mainframe 시절에는 폐쇠적이었지만

PC 시대가 오면서 open,호환성,...



각 라우터가 정보를 모아서

위의 서버에 보냄.

그거 갖고 라우팅 테이블 만들어서

아래 라우터들에게 보냄.



### generalized forwarding?

기존

- 목적지 기반 forwarding?

- ip 주소만 갖고 결정



이제는 헤더의 여러 정보를 검토해서 포워딩함.



이제 flow table.

SDN이 계산해준거 사용.

### sdn 관점

상위 network control app

- 이 사이에 northbound API?

SDN controlser

- 이 사이에 southbound

### sdn.controler.일?

interface layer

- network graph/RESTful/indent...

- 사용자에게 보이기 위한.

network-side state management layer

- flow table manage가 여기에서.

- 각종 정보 처리도 여기서.

communication layer

- OpenFlow/SNMP

- 라우터랑 통신하는 계층

### openflow protocol

tcp/tsl?

- 보안 기능 내장.



메세지 종류?

- controller-to-switch

	- 동기적. 잘 받았다고 응답 기다리기.

- switch-to-controler

	- 비동기적. 잘 받던 못받던 기다릴 필요 없음.

- 기타...



#### controler-to-switch

스위치를 관리.

설정 관리,

state를 add/delete?

packet-out?

- 컨트롤러가 '이 패킷을 이 경로로 보내라'고 할수도..?

- 아니면 특정 패킷을 특정 스위치로..?

- 아니면 이 패킷을 그 스위치에서 보내라?



#### switch-to-controler

packet-in?

패킷을 아예 컨트롤러에 올리기..?

flow-removed

port status

이제 저 사용자-api에서

다익스트라를 쓰던, 자기네 알고리듬을 쓰던.



### Openflow::flow table.entry?

#### 구조

rule

- 대상 패킷 지정.

- port,mac src/dst,ip addr 등...

action

- forward packet to port/drop/modify field/....

stats

- 말 그대로 통계.








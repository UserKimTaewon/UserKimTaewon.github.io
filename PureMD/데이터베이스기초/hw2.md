
ER다이어그램 작성 
===
# 문제1) 택배 회사의 배송 업무

단국 택배회사는 전국에 여러 지점을 가지고 있으며 각 지점에는 직원들이 소속되어져 있다. 고객은 보내고자 하는 물건을 각 지점에 가지고 오면 직원들이 이를 접수하여 배송처리를 한다. 지점의 정보는 지점 이름, 주소, 전화번호, 팩스 번호가 필요하다. 직원들을 관리하기 위해서는 이름, 직책, 전화번호, 업무 등이 필요하며, 고객의 정보로는 고객번호, 이름, 전화번호, 주소 등이 필요하다.

정확한 배송을 위해 물품을 접수 받을 때 물품번호, 물품명, 수신자, 송신자 주소, 가격, 무게 등 정보가 필요하다. 배송 정보를 고객들에게 핸드폰으로 알려주기 위해 배송 상태, 처리번호, 일시, 배송자, 수신자 등의 정보가 필요하다. 직원들은 접수를 할 때 접수번호, 접수일, 배송방식, 배송료, 결제방식 등의 정보가 필요하다.

```mermaid
flowchart LR
    지점[지점]
    지점이름((지점이름))
    지점주소((주소))
    지점전화번호((전화번호))
    지점팩스번호((팩스번호))
    지점 --- 지점이름
    지점 --- 지점주소
    지점 --- 지점전화번호
    지점 --- 지점팩스번호
    
    지점고용{고용}
    지점 --- 지점고용
    지점고용 --- 직원
    
    직원[직원]
    직원이름((이름))
    직원 --- 직원이름
    직원직책((직책))
    직원 --- 직원직책
    직원전화번호((전화번호))
    직원 --- 직원전화번호
    직원업무((업무))
    직원 --- 직원업무
    
    
    물품[물품]
    물품번호((<u>물품번호</u>))
    물품 --- 물품번호
    물품명((물품명))
    물품 --- 물품명
    물품수신자((수신자))
    물품 --- 물품수신자
    물품송신자_주소((송신자_주소))
    물품 --- 물품송신자_주소
    물품가격((가격))
    물품 --- 물품가격
    물품무게((무게))
    물품 --- 물품무게
    
   
    
    배송[배송정보]
    배송상태((배송상태))
    배송 --- 배송상태
    배송처리번호((<u>처리번호</u>))
    배송 --- 배송처리번호
    배송일시((일시))
    배송 --- 배송일시
    배송자((배송자))
    배송 --- 배송자
    배송수신자((수신자))
    배송 --- 배송수신자
    
    접수[접수정보]
    접수번호((<u>접수번호</u>))
    접수 --- 접수번호
    접수일((접수일))
    접수 --- 접수일
    접수배송방식((배송방식))
    접수 --- 접수배송방식
    접수배송료((배송료))
    접수 --- 접수배송료
    접수결제방식((결제방식))
    접수 --- 접수결제방식
```

# 문제2) 컨설팅 회사

단국 컨설팅(주)은 여러 컨설턴트를 고용하고 있으며, 이들은 상근 또는 시간제로 근무하고 있다. 상근과 시간제 컨설턴트는 모두 수행한 프로젝트 용역 시간에 따라 월급제로 급여를 받는다. 컨설턴트에는 직원번호, 이름, 주소, 전화번호, 전문분야, 기술 등급에 대한 정보를 갖는다. 컨설턴트는 하나 이상의 프로젝트에 할당되어 고객의 문제를 해결하는 일을 한다. 프로젝트에는 번호, 이름, 시작일, 종료일 등을 기록한다.

각 프로젝트에 따라 여러 컨설턴트가 할당 될 때도 있다. 각 컨설턴트는 할당된 프로젝트의 수행을 완료하면 회사 규정에 따라 상급 컨설턴트에 의해 평가를 받게 되며 회사는 이 자료를 관리한다.

고객은 하나 이상의 프로젝트를 의뢰할 수가 있고 고객의 정보는 번호, 이름, 주소, 전화번호 등을 기록한다. 고객은 개인 고객과 법인 고객으로 나뉘어진다.

회사는 과제를 의뢰한 고객에게 프로젝트가 완료되면 컨설팅 대금 전액을 청구하고, 고객은 청구 대금을 여러 차례에 걸쳐 납기일까지 지불할 수가 있다. 청구서에는 청구서 번호. 납기일, 그리고 금액을 기록한다.

```mermaid
flowchart LR
    컨설턴트근로조건((근로조건))
    컨설턴트 --- 컨설턴트근로조건
    컨설턴트용역_시간((용역_시간))
    style 컨설턴트용역_시간 stroke-dasharray: 5 5
    컨설턴트 --- 컨설턴트용역_시간
    컨설턴트급여((급여))
    style 컨설턴트급여 stroke-dasharray: 5 5
    컨설턴트 --- 컨설턴트급여
    컨설턴트직원번호((직원번호))
    컨설턴트 --- 컨설턴트직원번호
    컨설턴트이름((이름))
    컨설턴트 --- 컨설턴트이름
    컨설턴트주소((주소))
    컨설턴트 --- 컨설턴트주소
    컨설턴트전화번호((전화번호))
    컨설턴트 --- 컨설턴트전화번호
    컨설턴트전문분야((전문분야))
    컨설턴트 --- 컨설턴트전문분야
    컨설턴트기술등급((기술등급))
    컨설턴트 --- 컨설턴트기술등급

    프로젝트고용{고용}
    컨설턴트 -- N --- 프로젝트고용
    프로젝트고용 -- M --- 프로젝트
    
    프로젝트평가{평가}
    컨설턴트 -- 평가자 --- 프로젝트평가
    프로젝트평가 --- 평가결과((평가결과))
    프로젝트평가 -- 1 --- 프로젝트
    
    프로젝트번호((번호))
    프로젝트 --- 프로젝트번호
    프로젝트이름((이름))
    프로젝트 --- 프로젝트이름
    프로젝트시작일((시작일))
    프로젝트 --- 프로젝트시작일
    프로젝트종료일((종료일))
    프로젝트 --- 프로젝트종료일
    
    고객번호((번호))
    고객 --- 고객번호
    고객이름((이름))
    고객 --- 고객이름
    고객주소((주소))
    고객 --- 고객주소
    고객전화번호((전화번호))
    고객 --- 고객전화번호
    고객종류((종류))
    고객 --- 고객종류
    
    고객의뢰{의뢰}
    고객의뢰 -- N --- 고객
    고객의뢰 -- 청구 --- 청구서
    
```

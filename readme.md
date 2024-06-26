# 스파르타 마켓 프로젝트

스파르타 마켓 프로젝트는 스파르타 코딩클럽'의 프로젝트 일환으로,
앞서 만들었던 '스파-마켓'을 Django-DRF를 통해 구현해 본 프로젝트 입니다.

</br>
</br>

## 개발기간

- 2024.04.26(금) ~ 2024.05.02(목)

</br>
</br>

## 개발 환경

### 언어

- python


### 프레임워크

- django REST Framework

### 데이터베이스

- django ORM


</br>
</br>

## 기능 상세

- **Product 목록 조회** : 메인 페이지입니다. 물건의 제목, 가격, 이미지를 볼 수 있습니다.
- **Product 목록** : 선택한 물건의 제목, 작성자, 내용, 가격, 이미지, 등록 날짜를 볼 수 있습니다.
- **Product 생성** : 로그인 한 유저는 물품을 등록할 수 있습니다. 필수로 물품의 제목, 내용, 가격, 이미지를 등록해야 합니다.
- **Product 수정** : 물품을 등록할 유저는 등록한 물품을 수정할 수 있습니다.
- **Product 삭제** : 물품을 등록할 유저는등록한 물품을 삭제할 수 있습니다.

- **프로필** : 로그인한 유저의 아이디, 닉네임, 이름, 이메일, 가입날짜 등 이 표시됩니다. 또한 팔로우 및 언팔로우를 통해 관심유저로 설정할 수 있습니다.

- **회원가입** : 회원가입한 유저만 로그인 할 수 있습니다.
- **회원탈퇴** : 회원 탈퇴한 유저는 더이상 로그인 할 수 없습니다.
- **로그인** : 로그인 한 유저는 글을 등록할 수 있고, 팔로우 및 찜 기능을 사용할 수 있습니다.
- **로그아웃** : 로그인 한 유저만 로그아웃이 가능합니다.


</br>
</br>

## ERD

![ERD](https://github.com/LeeJS9856/spartamarket-DRF/blob/develop/image/ERD.png)


</br>
</br>

## API 명세

[API명세](https://documenter.getpostman.com/view/34437162/2sA3JDiRPK)


</br>
</br>


# WORKLOG

## 2026-03-17 (2차) - 노션 데이터 반영 및 콘텐츠 완성

### 이번 세션에서 한 작업
- Notion API(토큰: ntn_42...)를 통해 3개 노션 페이지 데이터 전량 추출
  - 페이지 1 (박정현 - 한국어 CV): 연락처, 학력, 연구관심사, 논문, 학회발표, 연구프로젝트, 경력, 장학금, 수상, 기술, 참고인
  - 페이지 2 (Park Jeonghyeon - 영어 CV): 동일 내용 영문
  - 페이지 3 (상세): 6개 데이터베이스 (학술활동, 학력, 경력1, 경력2-연구과제, 수상내역1-연구장학, 수상내역2-기타)
- 모든 콘텐츠 페이지를 실제 데이터로 업데이트 (한국어/영어 10개 파일)
- TODO/placeholder를 실제 정보로 교체 (연락처 외부 링크만 TODO 유지)
- 빌드 확인 완료

### 생성/수정한 주요 파일
- `src/ko/index.md` - 소개 (학력, 경력, 기술 포함)
- `src/en/index.md` - Bio (education, experience, skills)
- `src/ko/research.md` - 연구 관심사 (환경커뮤니케이션, 텍스트마이닝)
- `src/en/research.md` - Research Interests
- `src/ko/publications.md` - 논문 4편, 학회발표 8건, 수상 4건, 장학 5건
- `src/en/publications.md` - Publications (same content in English)
- `src/ko/projects.md` - 연구프로젝트 6건
- `src/en/projects.md` - Research Projects
- `src/ko/contact.md` - 연락처 (이메일, 소속, 주소)
- `src/en/contact.md` - Contact

### 결정 사항
- Notion API 접근 성공 (Internal Integration Token 사용)
- 전화번호는 개인정보 보호를 위해 공개 사이트에서 제외
- 기숙사 주소 대신 서울대학교 일반 주소만 기재
- 지도교수(윤선진) 정보는 참고인(Reference) 섹션으로 별도 포함하지 않음 (필요 시 추가 가능)

### 남아 있는 TODO
1. 프로필 사진 추가 (`src/assets/images/profile.jpg`)
2. 프로필 사진 적용 (index.md placeholder → img 태그)
3. 외부 프로필 링크 (Google Scholar, ORCID, GitHub, LinkedIn 등)
4. 배포 설정 (GitHub Pages, Netlify 등)
5. favicon 추가
6. 메타태그 / SEO 최적화
7. 참고인(Reference) 섹션 추가 여부 결정

### 다음에 이어서 할 작업
1. 프로필 사진 추가 및 적용
2. 외부 프로필 링크 추가
3. 배포 환경 설정

---

## 2026-03-17 (1차) - 초기 프로젝트 구축

### 이번 세션에서 한 작업
- 빈 폴더에서 학술 개인 홈페이지 프로젝트를 새로 생성
- Eleventy(11ty) v3 기반 정적 사이트 구조 설계 및 구현
- 한국어/영어 이중 언어 구조 구현 (URL 기반: /ko/, /en/)
- 기본 언어 한국어 설정 (루트 → /ko/ 리다이렉트)
- 상단 언어 전환 UI 구현 (현재 페이지 유지하며 언어 전환)
- 반응형 디자인 적용 (모바일/데스크톱)
- 5개 섹션 페이지 생성 (소개, 연구 관심사, 연구성과, 프로젝트, 연락처)

### 결정 사항
- 기술 스택: Eleventy + Nunjucks + Markdown + 순수 CSS
- 다국어 방식: URL 기반 (/ko/, /en/) + 디렉토리 데이터 파일
- 콘텐츠 관리: Markdown 파일 직접 편집 → npm run build
- 네비게이션: JSON 데이터 파일로 관리

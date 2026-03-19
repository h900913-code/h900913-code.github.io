# WORKLOG

---

## 2026-03-19 (5차) - 배포 상태 점검 및 문서 최신화

### 이번 세션에서 한 작업

- 현재 저장소 상태 재확인
- `README.md`, `WORKLOG.md`를 실제 상태 기준으로 다시 정리
- 지금까지 한 작업과 다음에 해야 할 작업을 문서화
- 배포 이슈를 문서에 명시

### 확인 결과

- 로컬 빌드 정상
- GitHub 저장소 `h900913-code/h900913-code.github.io` 존재
- 원격 `main` 브랜치 push 완료 상태
- `.github/workflows/deploy.yml` 원격 반영 완료
- 사이트 접속은 아직 안 됨
  - 증상: `DNS_PROBE_FINISHED_NXDOMAIN`

### 현재 판단

코드 문제보다는 배포 설정 또는 GitHub Pages 프로비저닝 문제일 가능성이 큼.

가능성:

- `Settings > Pages > Source`가 `GitHub Actions`로 설정되지 않음
- GitHub Actions workflow가 아직 실행되지 않음
- GitHub Pages 도메인 반영이 아직 안 끝남

### 다음에 바로 해야 할 일

1. GitHub 저장소 `Settings > Pages`에서 Source를 `GitHub Actions`로 확인
2. `Actions` 탭에서 `Build and Deploy to GitHub Pages` 실행 여부 확인
3. 실행 이력이 없으면 workflow 수동 실행 또는 새 커밋으로 재트리거
4. 이후 `https://h900913-code.github.io` 접속 재확인

---

## 2026-03-19 (4차) - 배포 완료 및 마감 작업

### 이번 세션에서 한 작업

- GitHub 계정 `h900913-code` 확인
- `h900913-code.github.io` 저장소 생성
- 로컬 저장소를 `origin`에 연결하고 `main` 브랜치 첫 push 완료
- 연락처 페이지에 GitHub 프로필 링크 추가
- 프로필 사진 `src/assets/images/profile.jpg` 반영
- favicon 추가 (`src/assets/favicon.svg`)
- 공통 SEO 메타태그 추가
  - description
  - canonical
  - Open Graph
  - Twitter card
  - hreflang
- 불필요한 placeholder / TODO 스타일 정리
- README와 WORKLOG 갱신

### 완료 항목

- 사이트 구축 완료
- 콘텐츠 반영 완료
- GitHub 저장소 생성 완료
- GitHub push 완료
- 프로필 사진 반영 완료
- GitHub 링크 반영 완료
- favicon 추가 완료
- 기본 SEO 메타태그 추가 완료

### 후속 후보 작업

- Google Scholar / ORCID / LinkedIn / ResearchGate 링크 추가
- 페이지별 `pageDescription` 세분화
- sitemap 또는 robots.txt 확장 검토

---

## 2026-03-18 (3차) - GitHub 배포 준비 및 세션 정리

### 이번 세션에서 한 작업

- GitHub Pages 배포 방식 결정
- `.github/workflows/deploy.yml` 생성
- git 초기화 및 최초 커밋 완료
- GitHub 계정과 배포 목표 URL 정리

### 당시 상태

- 사이트 구조 완성
- 콘텐츠 완성
- GitHub Actions 워크플로우 작성 완료
- 로컬 git 저장소 구성 완료
- 원격 저장소 생성 및 push는 다음 세션으로 이월

---

## 2026-03-17 (2차) - 노션 데이터 반영 및 콘텐츠 완성

### 이번 세션에서 한 작업

- Notion 데이터를 바탕으로 한국어/영어 콘텐츠 반영
- 소개, 연구 관심사, 연구성과, 프로젝트, 연락처 페이지 완성
- placeholder를 실제 정보로 교체

### 결정 사항

- 전화번호는 개인정보 보호를 위해 사이트에서 제외
- 주소는 서울대학교 일반 주소로 표기
- 참고인 섹션은 보류

---

## 2026-03-17 (1차) - 초기 프로젝트 구축

### 이번 세션에서 한 작업

- Eleventy 기반 정적 사이트 구조 설계 및 구현
- 한국어/영어 이중언어 구조 구성
- 루트에서 `/ko/`로 리다이렉트 설정
- 상단 언어 전환 UI와 반응형 레이아웃 구현
- 5개 핵심 섹션 페이지 생성

### 결정 사항

- 기술 스택: Eleventy + Nunjucks + Markdown + 순수 CSS
- 다국어 방식: URL 기반 디렉터리 구조
- 콘텐츠 관리: Markdown 직접 편집

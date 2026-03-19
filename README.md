# 박정현 (Park Jeonghyeon) - 학술 개인 홈페이지

한국어/영어 이중 언어를 지원하는 학술용 개인 홈페이지입니다.

**현재 상태**: 사이트 구축, 콘텐츠 반영, GitHub 저장소 연결, GitHub Actions 워크플로우 작성까지 완료  
**배포 대상 URL**: `https://h900913-code.github.io`  
**현재 이슈**: 2026-03-19 기준 브라우저에서 `DNS_PROBE_FINISHED_NXDOMAIN` 확인. 코드 문제라기보다 GitHub Pages 활성화 또는 도메인 프로비저닝 지연 가능성이 큼.

---

## 프로젝트 목적

학술 활동, 연구 관심사, 논문 및 발표, 프로젝트, 연락처를 정리해 공개하는 정적 개인 웹사이트입니다.

## 기술 스택

- 정적 사이트 생성기: [Eleventy (11ty)](https://www.11ty.dev/) v3
- 템플릿 엔진: Nunjucks
- 콘텐츠 형식: Markdown
- 스타일: 순수 CSS
- 런타임: Node.js 18+
- 배포: GitHub Pages + GitHub Actions

## 현재까지 완료한 작업

- Eleventy 기반 한/영 이중언어 사이트 구조 구현
- 노션 기반 실제 CV 콘텐츠 반영
- 연락처 페이지에 GitHub 프로필 링크 추가
- 프로필 사진 반영: `src/assets/images/profile.jpg`
- favicon 추가: `src/assets/favicon.svg`
- 기본 SEO 메타태그 추가
  - description
  - canonical
  - Open Graph
  - Twitter card
  - hreflang
- GitHub 저장소 `h900913-code/h900913-code.github.io` 생성
- 로컬 저장소와 `origin` 연결, `main` push 완료
- GitHub Actions 배포 워크플로우 작성 및 원격 반영 완료

## 현재 확인된 문제

- 로컬 빌드는 정상 동작함
  - 명령: `npm.cmd run build`
- 원격 저장소에는 워크플로우 파일이 올라가 있음
  - 파일: `.github/workflows/deploy.yml`
- 하지만 `https://h900913-code.github.io` 접속 시 `DNS_PROBE_FINISHED_NXDOMAIN`
- 따라서 다음 원인 중 하나일 가능성이 큼
  - GitHub Repository의 `Settings > Pages > Source`가 아직 `GitHub Actions`로 설정되지 않음
  - GitHub Actions가 아직 실제로 실행되지 않음
  - GitHub Pages 도메인 프로비저닝이 아직 안 끝남

## 다음에 들어와서 바로 해야 할 일

### 1. GitHub Pages 상태 확인

GitHub 저장소 `h900913-code/h900913-code.github.io`에서 아래를 확인:

1. `Settings > Pages`
2. `Build and deployment`의 `Source`가 `GitHub Actions`인지 확인
3. `Actions` 탭에서 `Build and Deploy to GitHub Pages` 워크플로우 실행 여부 확인

### 2. Actions가 안 돌았으면 배포 트리거

둘 중 하나 수행:

- `Actions` 탭에서 workflow 수동 실행
- 혹은 로컬에서 사소한 문서 수정 후 다시 push

```bash
git add .
git commit -m "Trigger GitHub Pages deployment"
git push
```

### 3. 사이트 접속 재확인

- `https://h900913-code.github.io`
- 저장소 생성 직후에는 반영이 지연될 수 있으므로 몇 분에서 최대 하루 정도 지켜볼 수 있음

## 페이지 구조

| 페이지 | 한국어 | 영어 |
| --- | --- | --- |
| 소개 / Bio | `/ko/` | `/en/` |
| 연구 관심사 | `/ko/research/` | `/en/research/` |
| 연구성과 | `/ko/publications/` | `/en/publications/` |
| 프로젝트 | `/ko/projects/` | `/en/projects/` |
| 연락처 | `/ko/contact/` | `/en/contact/` |

- 기본 언어는 한국어이며 `/` 접속 시 `/ko/`로 이동
- 상단 언어 전환 UI로 현재 페이지 기준 한/영 전환 가능

## 주요 파일

```text
CV_homepage/
├── .github/workflows/deploy.yml
├── src/_data/site.json
├── src/_includes/base.njk
├── src/assets/css/style.css
├── src/assets/favicon.svg
├── src/assets/images/profile.jpg
├── src/ko/
├── src/en/
├── README.md
└── WORKLOG.md
```

## 로컬 확인 방법

```bash
npm install
npm.cmd run build
npm.cmd run dev
```

- 개발 서버: `http://localhost:8080`

## 운영 원칙

- 한국어와 영어 콘텐츠는 가능한 한 같이 갱신
- 검증되지 않은 경력, 논문, 수상 정보는 추가하지 않음
- `_site/`는 빌드 결과물이므로 직접 수정하지 않음
- 큰 변경이나 외부 데이터 반영 후에는 `WORKLOG.md`에 기록

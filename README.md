# 박정현 (Park Jeonghyeon) - 학술 개인 홈페이지

한국어/영어 이중 언어를 지원하는 학술용 개인 홈페이지입니다.

**현재 상태**: 사이트 구축 및 GitHub 배포 완료  
**배포 URL**: https://h900913-code.github.io

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

## 페이지 구조

| 페이지 | 한국어 | 영어 |
| --- | --- | --- |
| 소개 / Bio | `/ko/` | `/en/` |
| 연구 관심사 | `/ko/research/` | `/en/research/` |
| 연구성과 | `/ko/publications/` | `/en/publications/` |
| 프로젝트 | `/ko/projects/` | `/en/projects/` |
| 연락처 | `/ko/contact/` | `/en/contact/` |

- 기본 언어는 한국어이며 `/` 접속 시 `/ko/`로 이동합니다.
- 상단 언어 전환 UI로 현재 페이지 기준 한/영 전환이 가능합니다.

## 폴더 구조

```text
CV_homepage/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── src/
│   ├── _data/
│   │   ├── navigation.json
│   │   └── site.json
│   ├── _includes/
│   │   └── base.njk
│   ├── assets/
│   │   ├── css/style.css
│   │   ├── favicon.svg
│   │   └── images/profile.jpg
│   ├── ko/
│   ├── en/
│   └── index.njk
├── eleventy.config.js
├── package.json
├── README.md
└── WORKLOG.md
```

## 운영 방법

### 내용 수정

1. `src/ko/` 또는 `src/en/`의 Markdown 파일을 수정합니다.
2. 로컬에서 확인합니다.

```bash
npm.cmd run build
```

3. 변경 사항을 커밋하고 push하면 GitHub Actions가 자동 배포합니다.

```bash
git add .
git commit -m "Update content"
git push
```

### 프로필 사진 교체

- 파일 위치: `src/assets/images/profile.jpg`
- 소개 페이지는 해당 파일을 자동으로 참조합니다.

### SEO / favicon

- 공통 메타태그와 canonical, Open Graph, hreflang은 `src/_includes/base.njk`에서 관리합니다.
- 사이트 기본 메타데이터는 `src/_data/site.json`에서 관리합니다.
- favicon은 `src/assets/favicon.svg`입니다.

## 로컬 실행

```bash
npm install
npm.cmd run dev
```

- 개발 서버: `http://localhost:8080`

## 운영 원칙

- 한국어와 영어 콘텐츠는 가능한 한 함께 갱신합니다.
- 검증되지 않은 경력, 논문, 수상 정보는 추가하지 않습니다.
- `_site/`는 빌드 결과물이므로 직접 수정하지 않습니다.
- 큰 변경이나 외부 데이터 반영 후에는 `WORKLOG.md`에 기록합니다.

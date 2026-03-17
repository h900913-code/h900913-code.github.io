# 박정현 (Park Jeonghyeon) - 학술 개인 홈페이지

한국어/영어 이중 언어를 지원하는 학술용 개인 홈페이지입니다.

## 프로젝트 목적

학술 활동, 연구 관심사, 논문/발표, 프로젝트, 연락처 등을 소개하는 정적 개인 웹사이트를 구축하고 유지보수하는 것이 목적입니다.

## 기술 스택

- **정적 사이트 생성기**: [Eleventy (11ty)](https://www.11ty.dev/) v3
- **템플릿 엔진**: Nunjucks
- **콘텐츠 형식**: Markdown
- **스타일**: 순수 CSS (프레임워크 없음)
- **런타임 요구사항**: Node.js 18+

## 홈페이지 구조

| 페이지 | 한국어 경로 | 영어 경로 |
|--------|------------|-----------|
| 소개/Bio | `/ko/` | `/en/` |
| 연구 관심사 | `/ko/research/` | `/en/research/` |
| 연구성과 | `/ko/publications/` | `/en/publications/` |
| 프로젝트 | `/ko/projects/` | `/en/projects/` |
| 연락처 | `/ko/contact/` | `/en/contact/` |

- 기본 언어: **한국어** (루트 `/` 접속 시 `/ko/`로 리다이렉트)
- 상단 우측에 언어 전환 UI (현재 페이지에서 대응 언어 페이지로 이동)

## 폴더/파일 구조

```
CV_homepage/
├── src/                    # 소스 파일 (Eleventy 입력)
│   ├── _includes/          # 레이아웃 템플릿
│   │   └── base.njk        # 기본 레이아웃 (헤더, 네비게이션, 푸터)
│   ├── _data/              # 전역 데이터 파일
│   │   ├── site.json       # 사이트 기본 정보 (이름, 제목)
│   │   └── navigation.json # 네비게이션 메뉴 구조
│   ├── ko/                 # 한국어 콘텐츠 (Markdown)
│   │   ├── ko.json         # 한국어 페이지 공통 설정
│   │   ├── index.md        # 소개
│   │   ├── research.md     # 연구 관심사
│   │   ├── publications.md # 연구성과
│   │   ├── projects.md     # 프로젝트
│   │   └── contact.md      # 연락처
│   ├── en/                 # 영어 콘텐츠 (Markdown)
│   │   ├── en.json         # 영어 페이지 공통 설정
│   │   ├── index.md        # Bio
│   │   ├── research.md     # Research Interests
│   │   ├── publications.md # Publications
│   │   ├── projects.md     # Projects
│   │   └── contact.md      # Contact
│   ├── assets/
│   │   ├── css/style.css   # 스타일시트
│   │   └── images/         # 이미지 (프로필 사진 등)
│   └── index.njk           # 루트 리다이렉트 (/→/ko/)
├── _site/                  # 빌드 결과물 (배포용, git 제외)
├── eleventy.config.js      # Eleventy 설정
├── package.json
├── README.md
└── WORKLOG.md
```

## 콘텐츠 원본 위치 및 업데이트 방법

### 콘텐츠를 넣는 곳

- **한국어 콘텐츠**: `src/ko/` 폴더의 Markdown 파일 편집
- **영어 콘텐츠**: `src/en/` 폴더의 Markdown 파일 편집
- **사이트 기본 정보**: `src/_data/site.json` 편집
- **네비게이션 메뉴**: `src/_data/navigation.json` 편집
- **프로필 사진**: `src/assets/images/` 에 이미지 파일 추가
- **스타일 변경**: `src/assets/css/style.css` 편집

### 콘텐츠 반영 절차

1. `src/ko/` 또는 `src/en/` 안의 Markdown 파일을 편집합니다.
2. 터미널에서 `npm run build`를 실행합니다.
3. `_site/` 폴더에 최신 HTML이 생성됩니다.
4. 생성된 `_site/` 폴더를 웹 호스팅에 배포합니다.

### 새 페이지 추가 방법

1. `src/ko/새페이지.md`와 `src/en/새페이지.md`를 동시에 생성합니다.
2. 프론트매터에 `pageTitle`을 지정합니다.
3. `src/_data/navigation.json`에 양쪽 언어의 메뉴 항목을 추가합니다.
4. `npm run build`로 재빌드합니다.

## 로컬 실행 방법

```bash
# 의존성 설치 (최초 1회)
npm install

# 개발 서버 실행 (실시간 미리보기, 파일 변경 시 자동 갱신)
npm run dev

# 빌드만 하기
npm run build
```

개발 서버 실행 시 `http://localhost:8080` 에서 확인할 수 있습니다.

## 빌드 방법

```bash
npm run build
```

결과물은 `_site/` 폴더에 생성됩니다. 이 폴더를 GitHub Pages, Netlify, Vercel 등에 배포할 수 있습니다.

## 주의사항 및 운영 원칙

- 한국어/영어 콘텐츠는 반드시 **양쪽 모두** 업데이트하세요. 한쪽만 수정하면 언어 전환 시 내용이 불일치합니다.
- 확인되지 않은 정보(경력, 논문 등)는 추가하지 마세요. TODO 표시된 부분만 채우세요.
- 프로필 사진은 `src/assets/images/profile.jpg` (또는 .png)로 넣고, `src/ko/index.md`와 `src/en/index.md`에서 참조를 업데이트하세요.
- `_site/` 폴더는 빌드 결과물이므로 직접 수정하지 마세요.

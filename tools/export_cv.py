# -*- coding: utf-8 -*-
"""cv.json(SSoT) → 지원서용 실적목록(한/영) + BibTeX 생성.
실행: python tools/export_cv.py  (stdlib만 사용, node 불필요)"""
import json, os, re, sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CV = os.path.join(ROOT, "src", "_data", "cv.json")
OUT = os.path.join(ROOT, "exports")
os.makedirs(OUT, exist_ok=True)
d = json.load(open(CV, encoding="utf-8"))

MONTHS = ["", "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
def datestr(s, lang):
    if not s: return ""
    parts = s.split("-"); y = parts[0]; m = int(parts[1]) if len(parts) > 1 else 0
    if lang == "ko": return f"{y}년 {m}월" if m else f"{y}년"
    return f"{MONTHS[m]} {y}" if m else y
def plain(s): return (s or "").replace("**", "")
def L(o, lang): return o.get(lang, "") if isinstance(o, dict) else (o or "")
def links_md(it): return " ".join(f"[{lk['label']}]({lk['url']})" for lk in it.get("links", []))

def render_list(lang):
    H = {"ko": dict(thesis="학위논문", journal="학술지 논문", first="주저자", co="공동저자", other="기타 저술",
                    present="학회 발표", award="수상", sch="장학", proj="연구 프로젝트"),
         "en": dict(thesis="Theses", journal="Journal Articles", first="First Author", co="Co-Author", other="Other",
                    present="Conference Presentations", award="Awards", sch="Scholarships", proj="Research Projects")}[lang]
    o = []
    o.append("# " + ("연구실적 — 박정현 (Park Jeonghyeon)" if lang == "ko" else "Publications & Activities — Park Jeonghyeon"))
    o.append(f"> cv.json 기준 자동생성 · {d['_meta']['updated']}\n")
    if d["theses"]:
        o.append(f"## {H['thesis']}")
        for t in d["theses"]:
            n = f" ({plain(L(t['note'], lang))})" if L(t['note'], lang) else ""
            o.append(f"- {plain(L(t['title'], lang))}. {plain(L(t['degree'], lang))}, {L(t['venue'], lang)}. {datestr(t['date'], lang)}.{n}")
        o.append("")
    o.append(f"## {H['journal']}")
    for role in ("first", "co", "other"):
        items = [a for a in d["journal_articles"] if a["role"] == role]
        if not items: continue
        o.append(f"### {H[role]}")
        for a in items:
            n = f" {plain(L(a['note'], lang))}" if L(a['note'], lang) else ""
            o.append(f"- {plain(L(a['authors'], lang))}. {plain(L(a['title'], lang))}. {L(a['venue'], lang)}. {datestr(a['date'], lang)}.{n} {links_md(a)}".rstrip())
        o.append("")
    o.append(f"## {H['present']}")
    for role in ("first", "co"):
        items = [p for p in d["presentations"] if p["role"] == role]
        if not items: continue
        o.append(f"### {H[role]}")
        for p in items:
            n = f" {plain(L(p['note'], lang))}" if L(p['note'], lang) else ""
            o.append(f"- {plain(L(p['authors'], lang))}. {plain(L(p['title'], lang))}. {L(p['venue'], lang)}. {datestr(p['date'], lang)}.{n} {links_md(p)}".rstrip())
        o.append("")
    o.append(f"## {H['award']}")
    for a in d["awards"]:
        o.append(f"- {plain(L(a['title'], lang))} ({a['year']}) — {L(a['org'], lang)}")
    o.append("")
    o.append(f"## {H['sch']}")
    for s in d["scholarships"]:
        o.append(f"- {plain(L(s['title'], lang))} ({', '.join(str(y) for y in s['years'])}) — {L(s['org'], lang)}")
    o.append("")
    o.append(f"## {H['proj']}")
    for pr in d["projects"]:
        o.append(f"- {plain(L(pr['title'], lang))} ({L(pr['period'], lang)}) — {L(pr['org'], lang)}")
    o.append("")
    return "\n".join(o)

for lang, fn in (("ko", "실적목록_ko.md"), ("en", "publications_en.md")):
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(render_list(lang))

# BibTeX — 인용 가능한 학위논문·학술지만(저자 약식 → 다저자 항목은 검토 필요)
def bib():
    seen = {}
    def key(base):
        k = base; c = ord('b')
        while k in seen: k = base + chr(c); c += 1
        seen[k] = 1; return k
    def authors_bib(s):
        return plain(s).replace(" & ", " and ")
    out = ["% cv.json 자동생성. 저자명은 약식(예: Park, J.) — 다저자 항목은 reference manager에서 풀네임 검토 권장.\n"]
    for t in d["theses"]:
        y = t["date"][:4]
        out.append(f"@mastersthesis{{{key('park' + y)},\n  title={{{L(t['title'],'en')}}},\n  author={{Park, Jeonghyeon}},\n  school={{Seoul National University}},\n  year={{{y}}}\n}}")
    for a in d["journal_articles"]:
        y = a["date"][:4]
        base = (re.match(r"([A-Za-z]+)", plain(L(a['authors'], 'en'))) or [None, "anon"])[1].lower() + y
        doi = next((lk['url'].replace("https://doi.org/", "") for lk in a.get("links", []) if lk['label'] == "DOI"), "")
        entry = f"@article{{{key(base)},\n  title={{{L(a['title'],'en')}}},\n  author={{{authors_bib(L(a['authors'],'en'))}}},\n  journal={{{L(a['venue'],'en')}}},\n  year={{{y}}}"
        if doi: entry += f",\n  doi={{{doi}}}"
        out.append(entry + "\n}")
    return "\n\n".join(out) + "\n"
open(os.path.join(OUT, "cv.bib"), "w", encoding="utf-8").write(bib())

print("OK — exports/ 생성:")
for fn in sorted(os.listdir(OUT)):
    print(f"   {fn}  ({os.path.getsize(os.path.join(OUT, fn))} B)")
print(f"\ncounts: 학위 {len(d['theses'])} · 학술지 {len(d['journal_articles'])} · 발표 {len(d['presentations'])} · 수상 {len(d['awards'])} · 장학 {len(d['scholarships'])} · 프로젝트 {len(d['projects'])}")

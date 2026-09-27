# ONLY12 빌드(lesson6-trap20.html) → ONLY2012 (동아(윤정미) 중2 5·6과 전용, PWA)
import io, os, re, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'only2012_site'
s = io.open('lesson6-trap20.html', encoding='utf-8').read()

def R(a, b, cnt=1):
    global s
    assert s.count(a) == cnt, (s.count(a), a[:70])
    s = s.replace(a, b)

# 브랜드 · 저장 키
s = s.replace('ONLY12', 'ONLY2012')
R('<span class="mark">ONLY<em>12</em></span><small>2012년생 내신 영어</small>',
  '<span class="mark">ONLY<em>2012</em></span><small>동아 중2 5·6과</small>')
s = s.replace('ONLY<em>12</em>', 'ONLY<em>2012</em>')
R('const LS="lesson6-trap20-v1"', 'const LS="only2012-v1"')

# 메뉴: 홈 · 5과·6과 · 내 기록 (문법 주제별 없음)
R('const NAV=[["home","홈","home"],["book","교과서별","book"],["topic","문법 주제별","tag"],["me","내 기록","trophy"]];',
  'const NAV=[["home","홈","home"],["book","5과·6과","book"],["me","내 기록","trophy"]];')
R('if(base==="book"||base==="topic"||base==="me"){view=base;return}',
  'if(base==="book"||base==="topic"||base==="me"){view=base==="topic"?"book":base;return}')
R('else if(view==="topic") renderTopic();', 'else if(view==="topic") renderBook();')

# 단원: 어디에 나오는지 + 5과 → 6과 순서
R('where:"중2 교과서 9종에 나옴"', 'where:"동아(윤정미) 중2 Lesson 6"', 2)
R('where:"중2 교과서 10종 · 2학기 9종"', 'where:"동아(윤정미) 중2 Lesson 5"')
R('where:"중2 동아(윤정미) Lesson 5"', 'where:"동아(윤정미) 중2 Lesson 5"')
R('where:"두 단원 섞어서"', 'where:"동아(윤정미) 중2 Lesson 6 · 두 단원 섞어서"')
R('/* ---------- 상단 바 · 하단 탭 ---------- */',
  '(()=>{const o={};["relobj","usedto","perc","so","mix"].forEach(k=>o[k]=UNITS[k]);Object.keys(UNITS).forEach(k=>delete UNITS[k]);Object.assign(UNITS,o)})();\n/* ---------- 상단 바 · 하단 탭 ---------- */')

# 5과·6과 화면 (교과서별 화면 대체)
i = s.index('function renderBook(){'); j = s.index('/* ---------- 문법 주제별')
s = s[:i] + '''function renderBook(){
  const L=[["Lesson 5",["relobj","usedto"]],["Lesson 6",["perc","so","mix"]]];
  page(`
  <div class="phead"><span class="label">동아(윤정미) 중2</span><h1>5과·6과 시험에 나오는 문법, 여기 다 있어</h1></div>
  <div class="stack">
  ${L.map(([t,us])=>`<section class="card lesson open"><div class="lh"><span class="ln">${t}</span><span class="lt">${us.filter(k=>k!=="mix").map(k=>esc(UNITS[k].name)).join(" · ")}</span></div><ul class="ulist">${us.map(k=>unitRow(UNITS[k])).join("")}</ul></section>`).join("")}
  </div>`);
}

''' + s[j:]

# 홈 · FAQ 문구
R('["교과서가 달라도 쓸 수 있어?","응. 시험에 나오는 문법은 교과서가 달라도 거의 같아. ‘교과서별’에서 우리 학교 교과서를 찾고, 없으면 ‘문법 주제별’에서 같은 문법으로 들어가면 돼."]',
  '["다른 교과서도 쓸 수 있어?","이 앱은 동아(윤정미) 중2 5과·6과 전용이야. 그래도 목적격 관계대명사, used to, 지각동사, so ~ that은 다른 교과서 시험에도 똑같이 나오니까 그대로 써도 돼."]')
R('["우리 교과서 단원은 언제 나와?","교과서 목차 확인되는 대로 계속 추가 중. 필요한 단원 있으면 말해 줘. 제일 많이 요청된 것부터 만든다."]',
  '["다른 과는 언제 나와?","지금은 5과·6과만 있어. 다음 과도 만드는 중이니까, 시험 범위 나오면 필요한 과 말해 줘."]')
R('"교과서 단원별로 자주 나오는 함정을 정리합니다."', '"동아 중2 5과·6과에서 자주 나오는 함정을 정리합니다."')
R('중학교 내신 ‘어법상 틀린 것 고르기’를 교과서 단원별로, 이유까지 연습하는 곳.',
  '동아(윤정미) 중2 5과·6과 ‘어법상 틀린 것 고르기’를 이유까지 연습하는 곳.')
R('data-nav="book">${ic("book")}내 교과서 단원 찾기</button>', 'data-nav="book">${ic("book")}5과·6과 단원 보기</button>')
R('<b>우리 교과서<br>그대로</b><p>2022 개정 중1·중2 교과서 10종 목차에서 이번 시험 범위를 바로 찾기.</p>',
  '<b>5과·6과<br>시험 범위 그대로</b><p>동아(윤정미) 중2 5과·6과 문법 4개를 전부 담았어.</p>')
R('<p class="lead2">지각동사, so ~ that은 중2 교과서 10종 중 9종에 나와. 새로 추가: 2학기 단골 1순위 목적격 관계대명사!</p>',
  '<p class="lead2">5과 목적격 관계대명사 · used to, 6과 지각동사 · so ~ that. 이 네 개면 5·6과 어법 끝.</p>')
R('<div class="ctrlinks"><button class="btn pill" data-nav="book">${ic("book","sm")}교과서로 찾기</button><button class="btn pill" data-nav="topic">${ic("tag","sm")}문법 주제로 찾기</button></div>',
  '<div class="ctrlinks"><button class="btn pill" data-nav="book">${ic("book","sm")}5과·6과로 보기</button></div>')

# 독립 웹페이지 + PWA
R('<title>ONLY2012</title>', '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>ONLY2012 · 동아 중2 5·6과 어법</title>
<meta name="description" content="동아(윤정미) 중2 5과·6과 ‘어법상 틀린 것 고르기’를 이유까지 연습하는 앱. 가입 없이 별명만.">
<meta name="theme-color" content="#1668E3">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="icon" href="/icons/icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="ONLY2012">
<meta name="apple-mobile-web-app-status-bar-style" content="default">''')
R('<div id="app"></div>', '</head>\n<body>\n<div id="app"></div>')
s = s.rstrip() + '''
<script>
if("serviceWorker" in navigator) window.addEventListener("load",()=>navigator.serviceWorker.register("/sw.js").catch(()=>{}));
</script>
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
'''
assert 'ONLY12' not in s
os.makedirs(OUT, exist_ok=True)
io.open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(s))

# Builds site/index.html for AdaL AI Video Night (Tue 3 Nov 2026, 6 to 9 PM PT, San Francisco).
# Cloned from the "Don't Just Prompt It. Ship It." deck, same design, flow and code style.
# Self-contained (no perth dependency); small labels above headings are stripped on purpose.
import os, sys, re, html as H_
H = os.path.dirname(os.path.abspath(__file__))
css = open(f'{H}/base.css').read() + open(f'{H}/extra.css').read() + open(f'{H}/theme.css').read() + '''
.cmd{white-space:pre-wrap;text-align:left}
.pair{display:grid;gap:clamp(12px,1.6vw,28px);width:100%;margin-top:1.2rem;align-items:start}
.pair>div{display:flex;flex-direction:column;gap:.6rem;min-width:0}
.pair video{width:100%;max-height:60vh;border-radius:14px;background:#000;object-fit:contain}
.pair .t{font-weight:600;font-size:clamp(1rem,1.6vw,1.8rem)}
.pair .t em{font-style:normal;color:var(--accent)}
'''

# ---------- event kit ----------
C = 'san-francisco-ai-video-night-2026-11'
GRANTS = 'https://adal.sylph.ai/grants?utm_source=slides&amp;utm_medium=event&amp;utm_campaign=san-francisco-ai-video-night-2026-11&amp;utm_content=slides_grants_1'
# UTM-tagged and logged in the Growth Engine sheet (campaign san-francisco-ai-video-night-2026-11, source slides).
WEBSITE = 'https://adalagent.ai/?utm_source=slides&amp;utm_medium=event&amp;utm_campaign=san-francisco-ai-video-night-2026-11&amp;utm_content=slides_website_1'
LIBRARY = 'https://adalagent.ai/launch-library?utm_source=slides&amp;utm_medium=event&amp;utm_campaign=san-francisco-ai-video-night-2026-11&amp;utm_content=slides_launch_library_1'
DISCORD = 'https://discord.gg/tB9FEBp4SV'
DISCORD_QR = 'https://api.qrserver.com/v1/create-qr-code/?size=600x600&amp;margin=0&amp;data=https%3A%2F%2Fdiscord.gg%2FtB9FEBp4SV'

# ---------- SUBMIT YOUR VIDEO: no form exists yet ----------
# Leave this empty until the submission link is ready. When set to a real URL the
# "Submit your video" slide renders a live QR; while empty it shows a clearly marked
# placeholder ("QR added on the night"). Jax: paste the link here, then rerun build.py.
SUBMIT = 'https://docs.google.com/forms/d/e/1FAIpQLSdBLZ4Wo9AarXj1-2ImFqrB3NUV6vsfxTCehQFDp49m-tOM0Q/viewform'  # form 1pzHM4WlFItH_DGpcbk2rILbsGylJOBJ-k3vNyGQBJP8 (jax@sylph.ai)

S = []
def add(ag, sec): S.append((ag, sec))

def part(ag, title, cp):
    add(ag, f'''<section class="slide check center" data-cp="{cp}">
    <h1 style="font-size:clamp(3rem,7.4vw,7.6rem)">{title}</h1>
  </section>''')

def prompt(ag, title, text, cp):
    add(ag, f'''<section class="slide" data-cp="{cp}">
    <h2 style="font-size:clamp(2rem,4.2vw,4.6rem)">{title}</h2>
    <div class="cmd" style="font-size:clamp(1rem,1.6vw,1.9rem);line-height:1.5;padding:1.4rem 1.6rem">{H_.escape(text)}</div>
  </section>''')

def qr(url, label, sub, size='clamp(200px,20vw,320px)'):
    return f'''<div style="display:flex;align-items:center;gap:clamp(20px,3vw,48px);margin-top:2.4rem">
      <a class="qr" href="{url}" target="_blank" rel="noopener" style="width:{size};display:block"><img alt="" data-qr="{url}"></a>
      <div><a class="when" href="{url}" target="_blank" rel="noopener" style="font-size:clamp(1.2rem,2.2vw,2.6rem);text-decoration:underline;text-underline-offset:6px">{label}</a><div style="margin-top:.8rem;font-size:clamp(1rem,1.6vw,1.8rem);color:var(--ink-50)">{sub}</div></div>
    </div>'''

def vid(name, title):
    return f'<div><video src="media/{name}.mp4" poster="media/{name}.jpg" controls playsinline preload="metadata"></video><div class="t">{title}</div></div>'

def pair(ag, title, cells, cp=2):
    add(ag, f'''<section class="slide" data-cp="{cp}">
    <h2 style="font-size:clamp(1.8rem,3.6vw,4rem)">{title}</h2>
    <div class="pair" style="grid-template-columns:repeat({len(cells)},1fr)">{''.join(cells)}</div>
  </section>''')

def steps(items):
    # items: list of (title, sub) ; sub may be '' . index numbers auto.
    rows = ''
    for i, (t, s) in enumerate(items):
        rows += f'<div><span class="i">{i+1:02d}</span><span class="t">{t}</span>' + (f'<span class="s">{s}</span>' if s else '') + '</div>'
    return f'<div class="steps">{rows}</div>'

# ============================================================ 6:00 · Dinner and networking
add('w', f'''<section class="slide" data-cp="1">
    <div class="two" style="grid-template-columns:1.2fr 1fr">
      <div>
        <h1>AI Video<br><em>Night</em></h1>
        <div class="when" style="margin-top:1.4rem;font-size:clamp(1.2rem,2.2vw,2.6rem)">Tue 3 Nov 2026 · 6:00 PM PT</div>
        <div class="org" style="margin-top:2.4rem;gap:1.2rem;align-items:center">
          <img src="img/jax-sf.jpg" alt="" style="width:clamp(90px,8vw,140px);height:clamp(90px,8vw,140px);border-radius:50%;object-fit:cover">
          <div><b style="font-size:clamp(1.2rem,2vw,2.2rem)">Jax Koh</b><span class="when" style="display:block;font-size:clamp(.9rem,1.3vw,1.4rem)">DevRel at AdaL</span></div>
        </div>
      </div>
      <img src="img/poster.png" alt="" style="width:100%;max-height:78vh;object-fit:contain;border-radius:18px;box-shadow:0 30px 60px -30px rgba(28,26,22,.6)">
    </div>
  </section>''')

add('w', f'''<section class="slide" data-cp="1">
    <div class="photo">
      <div>
        <h2>Hi, I'm <em>Jax</em></h2>
        <div class="when" style="margin-top:.6rem;font-size:clamp(1.1rem,1.9vw,2.1rem)">DevRel at AdaL · 2 months</div>
        {steps([("Product demos", ""), ("Events", ""), ("Community", "")])}
        <div class="when" style="margin-top:1.4rem;font-size:clamp(1rem,1.5vw,1.6rem)">X @jaxkoh_ · linkedin.com/in/jaxkoh</div>
      </div>
      <div class="polaroid"><img src="img/jax-sf.jpg" alt="Jax in San Francisco"></div>
    </div>
  </section>''')

add('w', '''<section class="slide" data-cp="1">
    <div class="two" style="grid-template-columns:1fr 1.5fr;align-items:center">
      <div><h2 style="font-size:clamp(2rem,4.2vw,4.6rem)">Every model, <em>one app</em></h2><p class="quote" style="margin-top:1.4rem;font-size:clamp(1.1rem,1.9vw,2.1rem)">AdaL is the automation-first agent harness. AdaL stands out with Browser Use combined with multi model plans, comes with 10 major LLM providers and goes to audio, image and video generation. You can code, operate and GTM all at once.</p></div>
      <video class="vid" style="width:100%;max-height:76vh" src="media/models-v3.mp4" poster="media/models-v3.jpg" autoplay loop muted playsinline></video>
    </div>
  </section>''')

add('w', f'''<section class="slide" data-cp="1">
    <h2>Building is <em>fast</em>. GTM isn't.</h2>
    {steps([("Agents ship a feature in an afternoon", ""), ("Getting it seen still takes weeks", "agency, editor, motion designer"), ("The launch video is the first thing people see", ""), ("Tonight: you make yours", "")])}
  </section>''')

add('w', f'''<section class="slide" data-cp="1">
    <h2>While you <em>eat</em></h2>
    {steps([("Apply for AdaL Grants", "$30 of credits"), ("Install AdaL Desktop", "scan next slide"), ("Open your product folder", ""), ("Join Discord", "link top right")])}
  </section>''')

add('w', f'''<section class="slide" data-cp="1">
    <h2>$30 of AdaL credits, <em>free</em></h2>
    <div class="qrs" style="align-items:flex-start;margin-top:1.6rem">
      <div><div class="qr" style="width:clamp(180px,18vw,300px)"><img alt="" data-qr="{GRANTS}"></div><div style="margin-top:.6rem;font-weight:600;font-size:clamp(1rem,1.6vw,1.8rem)">Apply for AdaL Grants</div><div style="font-size:clamp(.85rem,1.2vw,1.3rem);color:var(--ink-50)">7 days · no card</div></div>
      <div><div class="qr" style="width:clamp(180px,18vw,300px)"><img alt="" data-qr="{WEBSITE}"></div><div style="margin-top:.6rem;font-weight:600;font-size:clamp(1rem,1.6vw,1.8rem)">Install AdaL Desktop</div><div style="font-size:clamp(.85rem,1.2vw,1.3rem);color:var(--ink-50)">adalagent.ai</div></div>
    </div>
  </section>''')

add('w', f'''<section class="slide" data-cp="1">
    <h2>Tonight <em>· PT</em></h2>
    <div class="steps">
      <div><span class="i">6:00</span><span class="t">Dinner and networking</span><span class="s">redeem · install · Discord</span></div>
      <div><span class="i">6:50</span><span class="t">Live demo: a launch video with AdaL</span></div>
      <div><span class="i">7:20</span><span class="t">Make your own</span><span class="s">send prompts by 7:35</span></div>
      <div><span class="i">8:20</span><span class="t">Screening: top 10 videos</span></div>
      <div><span class="i">8:35</span><span class="t">Judging and winners</span></div>
    </div>
  </section>''')

# ============================================================ 6:30 · Live demo
part('demo', 'Live: a<br><em>launch video</em>', 2)

add('demo', '''<section class="slide center" data-cp="2">
    <div class="grid g4" style="grid-template-columns:repeat(2,1fr);max-width:70vw">
      <div><span class="label">Agency</span><div class="n">Weeks</div><div class="s">per launch video</div></div>
      <div><span class="label">AdaL</span><div class="n">20 min</div><div class="s">same launch quality</div></div>
    </div>
  </section>''')

add('demo', '''<section class="slide" data-cp="2">
    <h2>What <em>good</em> looks like</h2>
    <video class="vid" style="margin-top:.6rem;max-height:72vh;width:auto;max-width:100%" src="media/ll-launch-film.mp4" poster="media/ll-launch-film.jpg" controls playsinline preload="metadata"></video>
  </section>''')

add('demo', f'''<section class="slide" data-cp="2">
    <h2>The <em>recipe</em></h2>
    {steps([("Pick a reference", "launch library"), ("Prompt 1", "reverse engineer it"), ("Prompt 2", "replicate from scratch")])}
  </section>''')

add('demo', f'''<section class="slide" data-cp="2">
    <h2>Pick your <em>reference</em></h2>
    {qr(LIBRARY, 'adalagent.ai/launch-library', 'Every video, its prompts, its model')}
  </section>''')

pair('demo', 'Lovable <em>to AdaL</em>', [vid('ll-02-ref', 'Lovable original'), vid('ll-02-out', '<em>AdaL</em> style')])
pair('demo', 'OpenAI for law <em>to AdaL for work</em>', [vid('ll-05-ref', 'OpenAI original'), vid('ll-05-out', '<em>AdaL</em> style')])
pair('demo', 'Muse <em>to AdaL</em>', [vid('ll-10-ref', 'Muse original'), vid('ll-10-out', '<em>AdaL</em> style')])

prompt('demo', 'Prompt <em>1</em>', "Video: LINK\n\n(Use the video attached to this post itself, not videos from related posts on the page. Keep all your files in the folder XXXX.)\n\nreverse engineering this video, how can you use AdaL video producer capabilities to produce such videos, audios, and other types of the assets (including effects, fonts, transitions, animations)", 2)
prompt('demo', 'Prompt <em>2</em>', "ok replicate one using AdaL video producer from scratch", 2)

# ---------- Next in SF (from the AdaL Luma calendar, cal-2aFsnO0QCkjMiWi) ----------
CAL = 'https://luma.com/adalagent'
NEXT = [('diwali', 'Diwali Founders Session', 'Fri 6 Nov · 5:30 PM', 'https://luma.com/adalagent-gzch'),
        ('sglang', 'SGLang Summit 2026', 'Thu 12 Nov · 9:00 AM', 'https://luma.com/sglang-summit'),
        ('multimodal', 'The Multimodal Hackathon', 'Fri 13 Nov · 3:00 PM', 'https://luma.com/adalagent-i97q'),
        ('gtm', 'GTM Breakthrough Summit', 'Tue 17 Nov · 5:00 PM', 'https://luma.com/fblgtm')]
cards = ''.join(f'''<a href="{u}" target="_blank" rel="noopener" style="display:flex;flex-direction:column;gap:.5rem;min-width:0;color:inherit;text-decoration:none">
        <img src="img/events/{k}.jpg" alt="" style="width:100%;aspect-ratio:1;object-fit:cover;border-radius:14px;box-shadow:0 20px 40px -24px rgba(28,26,22,.6)">
        <b style="font-size:clamp(.95rem,1.4vw,1.5rem);line-height:1.2">{n}</b>
        <span class="when" style="font-size:clamp(.8rem,1.1vw,1.2rem)">{d}</span></a>''' for k, n, d, u in NEXT)
add('demo', f'''<section class="slide" data-cp="2">
    <div style="display:flex;align-items:center;justify-content:space-between;gap:2rem">
      <h2>Next in <em>SF</em></h2>
      <div style="display:flex;align-items:center;gap:1rem">
        <a class="qr" href="{CAL}" target="_blank" rel="noopener" style="width:clamp(100px,9vw,150px);display:block"><img alt="" data-qr="{CAL}"></a>
        <div><div style="font-weight:600;font-size:clamp(1rem,1.6vw,1.8rem)">Sign up free</div><div class="when" style="font-size:clamp(.85rem,1.2vw,1.3rem)">luma.com/adalagent</div></div>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(12px,1.6vw,28px);margin-top:1.4rem;width:100%">{cards}</div>
  </section>''')

# ============================================================ 7:00 · Make your own
part('make', 'Make <em>your own</em>', 2)

add('make', '''<section class="slide center" data-cp="2">
    <h1 style="font-size:clamp(3rem,7vw,7.4rem)">Send prompt 1 by <em>7:35 PM</em></h1>
    <div class="when" style="margin-top:2rem;font-size:clamp(1.1rem,2vw,2.2rem);line-height:1.6">Renders take 30 to 40 min<br>Post in Discord: which reference, which model</div>
  </section>''')

add('make', f'''<section class="slide" data-cp="2">
    <h2>What makes it <em>slop</em></h2>
    {steps([("No reference video", ""), ("A screen recording of your app", ""), ("Lots of tiny text", ""), ("Every feature at once", "")])}
  </section>''')

prompt('make', 'Product UI <em>skill</em>', "Make a product UI skill for my app. Use browser use to open it (computer use if it's a desktop app), screenshot every main screen and read the real labels from my code. Then rebuild those screens in HTML so you can animate them for my demo videos. Save it as a skill.", 2)

# Submit your video (placeholder until the form link exists)
if SUBMIT:
    submit_inner = qr(SUBMIT, 'Submit by 8:40 PM', 'Top 10 get screened · everyone who ships gets 2 months of Pro', 'clamp(200px,20vw,320px)')
else:
    submit_inner = '''<div style="display:flex;align-items:center;gap:clamp(20px,3vw,48px);margin-top:2.4rem">
      <div class="qr" style="width:clamp(200px,20vw,320px);aspect-ratio:1;display:flex;align-items:center;justify-content:center;border-style:dashed">
        <span style="font-family:var(--mono);color:var(--ink-50);font-size:clamp(.95rem,1.5vw,1.7rem);text-align:center;padding:1rem;line-height:1.4">QR added<br>on the night</span>
      </div>
      <div><div style="font-size:clamp(1.2rem,2.2vw,2.6rem);font-weight:600">Link shared live</div><div style="margin-top:.8rem;font-size:clamp(1rem,1.6vw,1.8rem);color:var(--ink-50)">Top 10 get screened</div></div>
    </div>'''
add('make', f'<section class="slide" data-cp="2"><h2>Submit your <em>video</em></h2>{submit_inner}</section>')

# ============================================================ 8:00 · Screening
part('screen', 'Top 10 on the<br><em>big screen</em>', 2)

# ============================================================ 8:15 · Judging and winners
add('judge', '''<section class="slide" data-cp="3">
    <h2>Prizes</h2>
    <div class="grid g4" style="grid-template-columns:repeat(2,1fr)">
      <div><span class="label">Best launch video</span><div class="n">12 mo</div><div class="s">AdaL Pro</div></div>
      <div><span class="label">People's choice</span><div class="n">6 mo</div><div class="s">AdaL Pro</div></div>
      <div><span class="label">Funniest</span><div class="n">3 mo</div><div class="s">AdaL Pro</div></div>
      <div><span class="label">Everyone who ships</span><div class="n">2 mo</div><div class="s">AdaL Pro</div></div>
    </div>
  </section>''')

add('judge', f'''<section class="slide" data-cp="3">
    <h2>Claim your <em>prize</em></h2>
    {steps([("Submit the form", "if not done yet"), ("Post your video tagging @adalagent", "X or LinkedIn"), ("Drop the link in Discord", "")])}
    {qr(DISCORD, 'discord.gg/tB9FEBp4SV', 'Join the room', 'clamp(130px,12vw,200px)')}
  </section>''')

add('judge', '''<section class="slide center" data-cp="3">
    <h1>Thank <em>you</em></h1>
    <div style="margin-top:1.2rem;font-size:clamp(1.1rem,1.8vw,2rem);color:var(--ink-50)">AdaL · AI Start Academy · Nerd Conf</div>
    <div class="org" style="margin-top:2rem;justify-content:center"><img class="logo" src="img/logos/adal.svg" alt=""></div>
  </section>''')

# ---------- assemble ----------
# Strip any small label that sits right above a heading (reads as AI slop).
LABEL_ABOVE = re.compile(r'<div class="label">[^<]*(?:<[^/][^>]*>[^<]*</[^>]+>[^<]*)*</div>\s*(?=<h[12])')
FL = ['jump_2', 'jump_1', 'walk_t1', 'avatar_working_t1', 'jump_3']
IC = ['rocket', 'megaphone', 'clapper', 'trophy', 'bulb', 'laptop']
def fl(src, css_, r=0):
    return f'<div class="fl" style="{css_};--r:{r}deg"><img src="img/ll/{src}.webp" alt=""></div>'
out_s = []
for i, (ag, sec) in enumerate(S):
    sec = LABEL_ABOVE.sub('', sec)
    if ' check' in sec[:60]:
        f = fl(FL[i % 5], 'width:clamp(110px,11vw,190px);right:2.5vw;bottom:14vh', -6) + fl(IC[i % 6], 'width:clamp(60px,5.5vw,100px);left:2vw;bottom:8vh;animation-delay:-2s', 10)
    elif 'class="pair"' in sec:
        f = ''
    else:
        f = fl(IC[i % 6], 'width:clamp(46px,4vw,72px);right:6.5vw;bottom:2.5vh;animation-delay:-%ds' % (i % 5), 10)
    sec = sec.replace('>', '>' + f, 1).replace('<section ', f'<section data-ag="{ag}" ', 1)
    out_s.append(sec)

AGENDA = [('w', '18:00', '18:50', 'Dinner and networking'),
          ('demo', '18:50', '19:20', 'Live demo: a launch video with AdaL'),
          ('make', '19:20', '20:20', 'Make your own'),
          ('screen', '20:20', '20:35', 'Screening: top 10 videos'),
          ('judge', '20:35', '21:00', 'Judging and winners')]
import json
agenda_html = '<aside class="ag" id="ag"><button class="ag-pill" id="agPill" type="button"><span class="ag-clock" id="agClock">--:--</span><span class="ag-now" id="agNow"></span><span class="ag-left" id="agLeft"></span></button><div class="ag-panel"><div class="label">Agenda · PT</div><ol id="agList"></ol></div></aside><script>window.AGENDA=' + json.dumps(AGENDA) + '</script>'

js = open(f'{H}/deck.js').read()
out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Video Night</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<main id="deck" onclick="">
{chr(10).join(out_s)}
</main>
{agenda_html}
<div class="toasts" id="toasts"></div>
<div class="qrbar"><div class="slideqr" style="padding:6px 16px"><div><div class="t">Wi-Fi · AI Start Academy-Guest</div><div class="u">password: guest123</div></div></div><a class="slideqr dcqr" href="{DISCORD}" target="_blank" rel="noopener"><img alt="" src="{DISCORD_QR}"><div><div class="t">Discord</div><div class="u">Join + share</div></div></a><div class="slideqr"><img alt="" id="slideqr"><div><div class="t">Slides</div><div class="u" id="slideurl"></div><div class="count" id="count">1 / 1</div></div></div></div>
<div class="progress"><i id="bar"></i></div>
<script>{js}</script>
</body>
</html>'''
open(f'{H}/site/index.html', 'w').write(out)
left = len(re.findall(r'<div class="label">[^<]*</div>\s*<h[12]', out))
print(len(out_s), 'slides,', left, 'labels left above headings')

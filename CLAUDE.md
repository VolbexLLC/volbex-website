# Volbex Website — Project Notes

## What this is
Single-page marketing site for **Volbex**, a creative operations agency for championship golf (superintendents, private clubs, tournament organizers). Built as a fully self-contained `index.html` — no build step needed, all assets (images, logos) are base64-inlined directly in the file.

## Key files
- **`index.html`** — the entire site (~1000 lines, 1.6MB). All CSS, JS, and images live here.
- **`Desktop/Local/VolbexLogos/`** — logo source files (PNG):
  - `VOLBEX FINAL LOGO COLOR.png` — white wordmark + orange ibex (for dark backgrounds / top-of-page nav)
  - `VOLBEX FINAL LOGO EF4E43.png` — all-orange logo (for light/cream backgrounds / scrolled nav)
  - `VOLBEX FINAL LOGO BLACK.png` — black version
  - `VOLBEX ORANGE.png` — orange ibex mark only
  - `VOLBEX FINAL VECTOR WHITE.png` — all-white version
- **`.claude/launch.json`** — preview server config (serves on port 3456 via `npx serve`)
- **`.claude/serve.py`** — fallback static server script (Python, no getcwd issue)

## Site sections (in order)
1. Modals (Login, Contact, Portfolio) — top of file, hidden by default
2. **Nav** — fixed top, transitions from transparent → cream on scroll
3. **Hero** — full-width dark topographic background, headline text, CTA buttons
4. **Marquee** — scrolling text strip
5. **Client Logos Strip** — tournament/club logos
6. **Services** — service cards with modals
7. **Clients / Portfolio** — client work grid
8. **About** — company bio
9. **Who We Serve** — target audience
10. **Shop** — product cards
11. **How It Works** — process steps
12. **Vision** — brand statement
13. **CTA** — contact call-to-action
14. **Footer** — links, legal

## Design tokens (CSS vars)
```
--red: #EF4E43          (brand orange-red)
--ink: #1A1F1E          (near-black)
--cream: #F5F0E8        (page background)
--cream-dark: #ECE7DE
--white: #FFFFFF
```
Fonts: `Cormorant Garamond` (headings/italic), `DM Sans` (body), `DM Mono` (labels/caps)

## Nav logo behavior
Two `<img>` tags inside `.nav-logo`:
- `.logo-top` — white+orange COLOR logo, visible by default (transparent nav over dark hero)
- `.logo-scroll` — all-orange EF4E43 logo, shown only when nav has `.stuck` class (cream background)

CSS toggles them: `nav.stuck .logo-top { display:none }` / `nav.stuck .logo-scroll { display:block }`

## Typography scale
- Desktop: `html { font-size: 20px }` (25% bump from default)
- Mobile (`max-width: 900px`): `html { font-size: 16px }` (original, unchanged)

## Git setup
- **Remote:** `https://github.com/VolbexLLC/volbex-website.git`
- **Branch:** `main`
- **Identity:** `Volbex-Mo <info@volbex.com>`
- **Auth:** GitHub CLI (`gh`) installed via Homebrew, logged in as `VolbexLLC`
- **Push:** just `git push` from the project folder — credentials handled by gh

## How to embed a logo
```python
python3 -c "
import base64
with open('/Users/mo/Desktop/Local/VolbexLogos/FILENAME.png','rb') as f:
    print(base64.b64encode(f.read()).decode())
"
```
Then use Python regex to replace the img src in index.html (base64 strings are too large for manual editing).

## Recent changes (as of May 23 2026)
- Hero card removed (ibex card with "Est. NY" tag and "6+ Championship Clients" badge)
- Hero converted from 2-column grid to single full-width column
- Dual nav logos wired up with CSS `.stuck` class toggle
- Nav text/buttons styled for both transparent (white text) and stuck (dark text on cream) states
- Desktop text scaled up ~25%, mobile locked at original size

## Preview server
```bash
# Already configured — just run:
npx serve -l 3456 /Users/mo/Desktop/volbex-website
# Or use Claude Code's preview panel (launch config already set up)
```

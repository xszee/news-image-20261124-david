#!/usr/bin/env python3
"""Draw a one-page newspaper front page for Tuesday 24 November 2026.
Fresh drawing for the david account entry, news-image-20261124.
Lead: Nvidia brings back Jensen Huang. Only verified facts from the
task brief are used. PIL only. Writes art.png (1024x1024)."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
M = 36
RED = (178, 24, 24)
INK = (18, 18, 18)
GREY = (90, 90, 90)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def para(draw, x, y, width, text, fnt, fill=INK, leading=None):
    lh = leading or int(fnt.size * 1.28)
    for ln in wrap(draw, text, fnt, width):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y

def rule(draw, x0, x1, y, w=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=w)

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# ---- masthead ----
rule(d, M, W - M, 22, 3)
d.text((W // 2, 30), "THE WORLD IN ONE DAY", font=font(SERIF, 58),
       fill=INK, anchor="ma")
rule(d, M, W - M, 98, 2)
d.text((W // 2, 106), "TUESDAY, 24 NOVEMBER 2026", font=font(SANS_B, 21),
       fill=RED, anchor="ma")
d.text((M, 108), "No. 329", font=font(SANS, 13), fill=GREY)
d.text((W - M, 108), "ONE DAY  •  ONE PAGE", font=font(SANS, 13),
       fill=GREY, anchor="ra")
rule(d, M, W - M, 136, 1, fill=GREY)

# ---- standfirst ----
sf = "Nvidia brings back Jensen Huang, Huawei is found guilty, and markets surge \u2014 the whole world, in a single page."
y = para(d, M, 146, W - 2 * M, sf, font(SERIF_I, 18), fill=(50, 50, 50), leading=22)
rule(d, M, W - M, y + 8, 1, fill=GREY)

# ---- LEAD: Nvidia, full width ----
ly = y + 18
d.text((M, ly), "LEAD STORY  •  MARKETS", font=font(SANS_B, 13), fill=RED)
ly += 20
ly = para(d, M, ly, W - 2 * M,
          "NVIDIA BRINGS BACK JENSEN HUANG",
          font(SERIF, 38), leading=42)
ly = para(d, M, ly + 2, W - 2 * M,
          "Nvidia reinstated Jensen Huang as CEO on Monday; President Trump said he personally persuaded the board. Markets surged \u2014 Seoul stocks +6%, the Nikkei +3.91%.",
          font(SERIF_R, 17), leading=22)
rule(d, M, W - M, ly + 10, 2)

# ---- Row 1: two columns ----
r1 = ly + 22
col_w = (W - 2 * M - 24) // 2
stories2 = [
    ("UNITED STATES  •  COURT", "Huawei guilty of trade-secret theft",
     "A US jury convicts Huawei of conspiracy to steal trade secrets and bank fraud, and acquits it of racketeering."),
    ("STRAIT OF HORMUZ", "IRGC says it attacked a container ship",
     "Iran's Revolutionary Guard said its navy attacked a container ship in the Strait of Hormuz, and Iran reported tankers hit mines there."),
]
max_y = r1
for i, (kick, head, body) in enumerate(stories2):
    x = M + i * (col_w + 24)
    yy = r1
    d.text((x, yy), kick, font=font(SANS_B, 12), fill=RED)
    yy += 18
    yy = para(d, x, yy, col_w, head, font(SERIF, 24), leading=27)
    yy = para(d, x, yy + 3, col_w, body, font(SERIF_R, 14.5), leading=19)
    max_y = max(max_y, yy)
    if i == 0:
        d.line([(x + col_w + 12, r1), (x + col_w + 12, max_y)], fill=(200, 200, 200), width=1)
rule(d, M, W - M, max_y + 10, 1, fill=GREY)

# ---- Row 2: three columns ----
r2 = max_y + 22
col3 = (W - 2 * M - 48) // 3
stories3 = [
    ("THE HAGUE", "Genocide ruling backed",
     "The UK, Spain, Canada, Australia and 10 more affirm the ICJ ruling that Myanmar committed genocide against the Rohingya."),
    ("UKRAINE  •  AT SEA", "Drones hit Russian ships",
     "Kyiv acknowledges drone strikes on the cargo ship Sparta II in the Gulf of Finland and a warship off Libya."),
    ("SPACE  •  CHINA", "Shenzhou 24 lifts off",
     "China launches Shenzhou 24 with two Chinese and one Pakistani astronaut \u2014 Zeeshan Ali, the first foreign astronaut on Tiangong."),
]
max_y2 = r2
for i, (kick, head, body) in enumerate(stories3):
    x = M + i * (col3 + 24)
    yy = r2
    d.text((x, yy), kick, font=font(SANS_B, 11.5), fill=RED)
    yy += 17
    yy = para(d, x, yy, col3, head, font(SERIF, 20), leading=23)
    yy = para(d, x, yy + 3, col3, body, font(SERIF_R, 13.5), leading=18)
    max_y2 = max(max_y2, yy)
    if i < 2:
        d.line([(x + col3 + 12, r2), (x + col3 + 12, max_y2)], fill=(200, 200, 200), width=1)
rule(d, M, W - M, max_y2 + 10, 2)

# ---- Map strip ----
my = max_y2 + 20
d.text((M, my), "THE DAY ON THE MAP", font=font(SANS_B, 14), fill=INK)
d.text((W - M, my), "SIX PLACES THAT MADE THE NEWS", font=font(SANS, 11),
       fill=GREY, anchor="ra")
my += 22
d.rectangle([M, my, W - M, my + 56], fill=(232, 240, 248), outline=(180, 200, 220))
places = [
    ("Cartagena", 0.06), ("The Hague", 0.30), ("Kyiv", 0.42),
    ("Ankara", 0.50), ("Hormuz", 0.62), ("Beijing", 0.90),
]
for name, fx in places:
    cx = M + int(fx * (W - 2 * M))
    cy = my + 21
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED, outline="white", width=2)
    d.text((cx, cy + 10), name, font=font(SANS_B, 11), fill=INK, anchor="ma")
map_bottom = my + 56

# ---- Brief: 18 items in two columns ----
by = map_bottom + 16
d.text((M, by), "THE DAY IN BRIEF", font=font(SANS_B, 14), fill=INK)
rule(d, M, W - M, by + 22, 1, fill=GREY)
brief = [
    "A 5.6-magnitude earthquake strikes Nepal near the Chinese border.",
    "UN chief Guterres calls for a multilateral framework to limit AI risks within a year.",
    "Turkish Air Force helicopter crashes after take-off from Eskisehir; 5 crew killed.",
    "Houthi fighters about 60 km from Aden and ready to attack, Yemen's military says.",
    "Senegal regains the Africa Cup of Nations title after a sports court appeal.",
    "North Korea demands closure of Switzerland's new diplomatic office in Pyongyang.",
    "Blast at a hot pot eatery in Hanoi kills 6 and injures more than a dozen.",
    "Bangladesh's ousted leader Hasina plans to return from exile on Dec 16.",
    "UK sanctions Yemen's Houthis and four senior officials.",
    "Israeli air strike kills Hamas internal security chief Brig. Gen. Naeem Abu Mohammed Nahel in Gaza.",
    "Libyan commander Khalifa Haftar visits Turkey for the first time, to meet Erdogan.",
    "Armed men seize a Cartagena supermarket and hold 25 people hostage.",
    "US ready to impose tariffs on China and the EU.",
    "A quasar is found 630 million years after the Big Bang.",
    "Pope Francis's diary is published.",
    "Markets: S&P 500 +4.73%, Nasdaq +6.51%.",
    "Nvidia reinstates Jensen Huang as CEO after Trump persuades the board.",
    "Huawei acquitted of racketeering, despite guilty verdicts on trade secrets and fraud.",
]
bcol_w = (W - 2 * M - 24) // 2
bf = font(SANS, 12.5)
row_h = 34
for idx, item in enumerate(brief):
    col = idx // 9
    row = idx % 9
    x = M + col * (bcol_w + 24)
    yy = by + 32 + row * row_h
    d.text((x, yy), "\u2022", font=font(SANS_B, 13), fill=RED)
    para(d, x + 14, yy, bcol_w - 14, item, bf, leading=15)

# ---- footer ----
fy = by + 32 + 9 * row_h + 6
rule(d, M, W - M, fy, 1, fill=GREY)
d.text((W // 2, fy + 6),
       "All stories were reported on Tuesday 24 November 2026.  Sources: Reuters, AP, AFP, BBC.",
       font=font(SANS, 12), fill=GREY, anchor="ma")
d.text((W // 2, fy + 22),
       "THE WORLD IN ONE DAY  \u00b7  TUESDAY, 24 NOVEMBER 2026",
       font=font(SANS_B, 11), fill=GREY, anchor="ma")

img.save("art.png", optimize=True)
print("saved art.png", img.size)

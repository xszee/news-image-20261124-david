#!/usr/bin/env python3
"""Draw THE MORNING GLOBE front page for Tuesday, 24 November 2026.

Fresh artwork for the make.fun news-image-20261124 bounty (david account).
All stories are the verified events of 24 Nov 2026 listed in the brief.
1024x1024, black ink on cream paper, DejaVu / Liberation Serif fonts.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (251, 250, 245)
INK = (17, 17, 17)
GREY = (90, 90, 90)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
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


def para(draw, x, y, text, fnt, width, leading, fill=INK):
    lines = wrap(draw, text, fnt, width)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def centre(draw, y, text, fnt, fill=INK):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def rule(draw, x0, x1, y, width=1):
    draw.line([(x0, y), (x1, y)], fill=INK, width=width)


def draw_scales(draw, cx, top, bottom):
    """Simple scales of justice: post, beam, two hanging pans, base."""
    beam_y = top + 18
    pan_y = top + 88
    # finial + post
    draw.ellipse([cx - 6, top - 6, cx + 6, top + 6], outline=INK, width=3)
    draw.line([(cx, top + 6), (cx, bottom - 22)], fill=INK, width=4)
    # beam
    draw.line([(cx - 108, beam_y), (cx + 108, beam_y)], fill=INK, width=4)
    draw.ellipse([cx - 4, beam_y - 4, cx + 4, beam_y + 4], outline=INK, width=3)
    # base
    draw.line([(cx - 52, bottom - 22), (cx + 52, bottom - 22)], fill=INK, width=4)
    draw.line([(cx - 34, bottom - 10), (cx + 34, bottom - 10)], fill=INK, width=4)
    for end in (-108, 108):
        px = cx + end
        # strings from beam end to pan rim
        draw.line([(px, beam_y), (px - 34, pan_y)], fill=INK, width=2)
        draw.line([(px, beam_y), (px + 34, pan_y)], fill=INK, width=2)
        draw.line([(px, beam_y), (px, pan_y - 6)], fill=INK, width=2)
        # pan: shallow bowl (arc + chord)
        draw.arc([px - 34, pan_y - 26, px + 34, pan_y + 26], 0, 180, fill=INK, width=3)
        draw.line([(px - 34, pan_y), (px + 34, pan_y)], fill=INK, width=3)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    MX = 36                      # side margin
    RX = W - MX                  # right edge

    # ---- masthead ----
    f_mast = font(SERIF_B, 66)
    centre(d, 16, "THE MORNING GLOBE", f_mast)
    rule(d, MX, RX, 100, 4)
    rule(d, MX, RX, 107, 1)

    # ---- date line, thin rules left and right ----
    f_date = font(SERIF_B, 20)
    date_txt = "TUESDAY, 24 NOVEMBER 2026"
    dw = d.textlength(date_txt, font=f_date)
    gap = 14
    rule(d, MX, (W - dw) / 2 - gap, 122, 1)
    rule(d, (W + dw) / 2 + gap, RX, 122, 1)
    d.text(((W - dw) / 2, 110), date_txt, font=f_date, fill=INK)

    # ---- standfirst ----
    f_stand = font(SERIF_I, 17)
    centre(d, 138, "The world in full, before your first coffee \u2014 every story that mattered overnight.",
           f_stand, fill=GREY)
    rule(d, MX, RX, 166, 1)

    # ---- LEAD ----
    f_kick = font(SERIF_B, 14)
    d.text((MX, 178), "WORLD COURT RULING", font=f_kick, fill=INK)
    lead_x, lead_w = MX, 560
    f_head = font(SERIF_B, 40)
    y = 202
    y = para(d, lead_x, y, "WORLD COURT: MYANMAR GUILTY OF GENOCIDE",
             f_head, lead_w, 46)
    y += 6
    f_body = font(SERIF, 19)
    para(d, lead_x, y,
         "The International Court of Justice ruled Myanmar committed genocide "
         "against the Rohingya; fourteen nations (UK, Spain, Canada, Australia "
         "and ten more) affirmed the ruling on Monday.",
         f_body, lead_w, 24)

    # scales panel, right of the lead
    px0, py0, px1, py1 = 636, 178, RX, 436
    d.rectangle([px0, py0, px1, py1], outline=INK, width=2)
    draw_scales(d, (px0 + px1) // 2, py0 + 26, py1 - 44)
    f_cap = font(SERIF_B, 14)
    cap_txt = "JUSTICE, WEIGHED"
    cap_w = d.textlength(cap_txt, font=f_cap)
    d.text((((px0 + px1) - cap_w) / 2, py1 - 30), cap_txt, font=f_cap, fill=INK)

    # ---- three-column row ----
    rule(d, MX, RX, 452, 2)
    cols3 = [
        ("SHENZHOU 24 CARRIES PAKISTANI ASTRONAUT TO TIANGONG",
         "China launches two Chinese and one Pakistani astronaut (Zeeshan Ali, "
         "the first foreign astronaut aboard its space station)."),
        ("UN CHIEF: ACT ON AI RISKS WITHIN A YEAR",
         "Secretary-General Antonio Guterres calls on states to build a "
         "multilateral framework to limit AI risks."),
        ("NEPAL SHAKEN BY 5.6 QUAKE",
         "A magnitude 5.6 earthquake strikes Nepal near the Chinese border."),
    ]
    col_w = 296
    xs = [MX, MX + 328, MX + 656]
    f_h3 = font(SERIF_B, 18)
    f_b3 = font(SERIF, 14)
    for x, (head, body) in zip(xs, cols3):
        yy = para(d, x, 466, head, f_h3, col_w, 22)
        para(d, x, yy + 4, body, f_b3, col_w, 18)
    # vertical separators
    for vx in (MX + 312, MX + 640):
        d.line([(vx, 466), (vx, 596)], fill=GREY, width=1)

    # ---- two-column row ----
    rule(d, MX, RX, 612, 2)
    cols2 = [
        ("HUAWEI GUILTY ON TRADE SECRETS AND BANK FRAUD",
         "A US jury convicts Huawei of conspiracy to steal trade secrets and "
         "bank fraud, acquits it of racketeering."),
        ("IRGC SAYS IT HIT SHIP IN HORMUZ",
         "Iran's Revolutionary Guard says its navy attacked a container ship; "
         "Tehran reports tankers struck mines in the strait."),
    ]
    f_h2 = font(SERIF_B, 20)
    f_b2 = font(SERIF, 15)
    xs2 = [MX, MX + 492]
    for x, (head, body) in zip(xs2, cols2):
        yy = para(d, x, 626, head, f_h2, 460, 25)
        para(d, x, yy + 4, body, f_b2, 460, 19)
    d.line([(W // 2, 626), (W // 2, 726)], fill=GREY, width=1)

    # ---- THE DAY IN BRIEF ----
    rule(d, MX, RX, 742, 2)
    f_sec = font(SERIF_B, 16)
    d.text((MX, 754), "THE DAY IN BRIEF", font=f_sec, fill=INK)
    brief = [
        "Ukrainian drones hit a Russian ship in the Gulf of Finland and off Libya.",
        "25 hostages held at a supermarket in Cartagena, Colombia.",
        "Turkish Air Force helicopter crashes in Eskisehir; 5 crew killed.",
        "Houthis 60 km from Aden, ready to strike, officials warn.",
        "Senegal win the Africa Cup of Nations on appeal.",
        "Markets surge \u2014 Seoul +6%, Nikkei +3.91% \u2014 as Nvidia restores Jensen Huang as CEO.",
        "North Korea asks Switzerland to close its Pyongyang diplomatic office.",
        "Hanoi hot-pot restaurant blast kills 6.",
        "Bangladesh's Hasina plans to return home on 16 December.",
        "Britain sanctions the Houthis and four officials.",
        "Israeli strike kills Hamas internal security chief in Gaza.",
        "Haftar makes his first visit to Turkey.",
        "US ready to impose tariffs on China and the EU.",
        "Quasar found 630 million years after the Big Bang.",
        "S&P 500 +4.73%, Nasdaq +6.51%.",
        "Trump calls toppling Iran's regime \u2018probably doable\u2019.",
        "Zelenskyy criticises US over delayed missiles.",
    ]
    f_br = font(SERIF, 12)
    groups = [brief[0:6], brief[6:12], brief[12:]]
    for x, items in zip(xs, groups):
        yy = 782
        for item in items:
            yy = para(d, x, yy, "\u2022  " + item, f_br, col_w, 15)
            yy += 4
    for vx in (MX + 312, MX + 640):
        d.line([(vx, 782), (vx, 972)], fill=GREY, width=1)

    # ---- footer ----
    rule(d, MX, RX, 982, 1)
    f_ft = font(SERIF_I, 12)
    centre(d, 990,
           "Every story in this edition was first reported on Tuesday, 24 November 2026. "
           "Sources: Reuters, AP, AFP, BBC.", f_ft, fill=GREY)
    f_ft2 = font(SERIF_B, 11)
    centre(d, 1006, "THE MORNING GLOBE \u00b7 TUESDAY, 24 NOVEMBER 2026", f_ft2, fill=GREY)

    img.save("art.png", optimize=True)
    print("wrote art.png", img.size)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Draw the entry picture for make.fun's 23 November 2026 news-image bounty.

The picture is a broadsheet front page, 1024x1024, drawn with PIL from
the world news reported on Monday 23 November 2026:

  lead    COP31 climate summit in Antalya collapses with no deal
  panel   Ukraine sinks a Russian warship off Libya with drones
  panel   Russian strikes kill at least 15 people near Kyiv
  panel   Indonesian sweets-factory fire kills 24, dozens missing
  panel   Nvidia reinstates Jensen Huang as CEO; an AI proof of the
          Riemann hypothesis; BepiColombo reaches Mercury orbit

Run:  python3 generate.py   (writes entry.png beside this file)
"""
from PIL import Image, ImageDraw, ImageFont

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (30, 70, 140)
GREY = (90, 90, 90)


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def textbox(draw, xy, text, font, fill, maxw, leading=1.12):
    x, y = xy
    for line in wrap(draw, text, font, maxw):
        draw.text((x, y), line, font=font, fill=fill)
        y += int(font.size * leading)
    return y


def story_box(draw, box, kicker, head, body, accent):
    x0, y0, x1, y1 = box
    draw.rectangle(box, outline=INK, width=2)
    draw.rectangle([x0, y0, x1, y0 + 30], fill=accent)
    draw.text((x0 + 10, y0 + 6), kicker, font=F(SANS_B, 17), fill=(255, 255, 255))
    y = textbox(draw, (x0 + 10, y0 + 42), head, F(SANS_B, 27), INK, x1 - x0 - 20)
    textbox(draw, (x0 + 10, y + 4), body, F(SANS, 19), GREY, x1 - x0 - 20)


def page(date_line, lead_kicker, lead_head, lead_body, stories, out):
    img = Image.new("RGB", (1024, 1024), PAPER)
    d = ImageDraw.Draw(img)
    # Masthead: paper name in a black band, the date picked out in gold.
    d.rectangle([0, 0, 1024, 118], fill=INK)
    t = "THE DAILY WORLD"
    f = F(SERIF_B, 62)
    d.text(((1024 - d.textlength(t, font=f)) / 2, 12), t, font=f, fill=(255, 255, 255))
    f2 = F(SANS_B, 25)
    d.text(((1024 - d.textlength(date_line, font=f2)) / 2, 84),
           date_line, font=f2, fill=(255, 205, 90))
    # Lead story under a red rule.
    d.rectangle([28, 140, 996, 148], fill=RED)
    d.text((28, 160), lead_kicker, font=F(SANS_B, 22), fill=RED)
    y = textbox(d, (28, 192), lead_head, F(SERIF_B, 47), INK, 968)
    y = textbox(d, (28, y + 8), lead_body, F(SANS, 23), GREY, 968)
    d.rectangle([28, y + 10, 996, y + 14], fill=INK)
    # Four panels in a 2x2 grid fill the rest of the page.
    top = y + 34
    cell_h = (1000 - top) // 2
    boxes = [
        (28, top, 500, top + cell_h - 12),
        (524, top, 996, top + cell_h - 12),
        (28, top + cell_h, 500, 1000),
        (524, top + cell_h, 996, 1000),
    ]
    for box, (kick, head, body, acc) in zip(boxes, stories):
        story_box(d, box, kick, head, body, acc)
    img.save(out, optimize=True)
    print(out, img.size)


if __name__ == "__main__":
    page(
        "MONDAY · 23 NOVEMBER 2026 · THE DAY IN ONE PICTURE",
        "ANTALYA, TURKEY — TOP STORY",
        "Climate summit collapses: COP31 ends with no deal",
        "The longest UN climate talks in history broke up in Antalya with no "
        "agreement, as nations split over phasing out fossil fuels and who "
        "pays for climate damage.",
        [
            ("WAR AT SEA", "Ukraine sinks Russian warship off Libya",
             "Kyiv's drones hit a Russian vessel at Benghazi; President "
             "Zelensky confirmed the strike as the war reached the "
             "Mediterranean.", BLUE),
            ("UKRAINE", "Russian strikes kill 15 near Kyiv",
             "Bombardment of the Kyiv region killed at least 15 people; "
             "rescuers pulled a young boy alive from the rubble.", RED),
            ("INDONESIA", "Factory fire kills 24, dozens missing",
             "A blaze tore through a sweets factory in Indonesia, killing "
             "at least 24 workers with about 30 still unaccounted for.",
             (200, 120, 20)),
            ("TECH & SCIENCE", "Nvidia brings back Jensen Huang as CEO",
             "In a boardroom shock, Nvidia reinstated its founder as chief "
             "executive — the same day an AI proof of the Riemann "
             "hypothesis stunned mathematicians, and BepiColombo finally "
             "reached Mercury's orbit after eight years.", (40, 130, 90)),
        ],
        "entry.png",
    )

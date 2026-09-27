from PIL import Image, ImageDraw, ImageFont
F = "C:/Windows/Fonts/arialbd.ttf"
BLUE, YEL, INK, WHITE = "#1668E3", "#FFD43B", "#10213F", "#FFFFFF"
def make(size, safe, rounded):
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if rounded: d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * .22), fill=BLUE)
    else: d.rectangle([0, 0, S, S], fill=BLUE)
    W = S * safe
    f1 = ImageFont.truetype(F, int(W * .30)); f2 = ImageFont.truetype(F, int(W * .27))
    t1 = "ONLY"; b1 = d.textbbox((0, 0), t1, font=f1); w1, h1 = b1[2] - b1[0], b1[3] - b1[1]
    t2 = "2012"; b2 = d.textbbox((0, 0), t2, font=f2); w2, h2 = b2[2] - b2[0], b2[3] - b2[1]
    padx, pady, gap = W * .07, W * .06, W * .07
    bw, bh = w2 + padx * 2, h2 + pady * 2
    total = h1 + gap + bh; y0 = (S - total) / 2
    d.text(((S - w1) / 2 - b1[0], y0 - b1[1]), t1, font=f1, fill=WHITE)
    by = y0 + h1 + gap; bx = (S - bw) / 2
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=int(W * .05), fill=YEL)
    d.text((bx + padx - b2[0], by + pady - b2[1]), t2, font=f2, fill=INK)
    return im.resize((size, size), Image.LANCZOS)
make(192, .86, False).save("icons/icon-192.png")
make(512, .86, False).save("icons/icon-512.png")
make(512, .66, False).save("icons/maskable-512.png")
make(180, .86, False).convert("RGB").save("icons/apple-touch-icon.png")
print("icons ok")

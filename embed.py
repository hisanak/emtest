from PIL import Image

def run(base_img, stamp_img, result_img):
    orig_base = Image.open(base_img)
    orig_icon = Image.open(stamp_img)

    big_icon = orig_icon.resize((int(orig_icon.width * 5), int(orig_icon.height * 5)))

    rot_icon = big_icon.rotate(30, expand=True)
    mask = rot_icon.split()[3]

    base = orig_base.copy()
    base.paste(rot_icon, (400, 350), rot_icon)
    base.save(result_img, quality=95)


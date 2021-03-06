import os
import secrets
import PIL
from PIL import Image
from flask import url_for


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/blog_pics', picture_fn)

    save(picture_path)

    return picture_fn

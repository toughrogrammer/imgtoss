from app import app
from app.forms.image_upload import ImageUploadForm
from flask import request, url_for, redirect, abort, render_template


@app.route('/')
def index():
    form = ImageUploadForm()
    return render_template('index.html', form=form)


@app.route('/upload', methods=['POST'])
def upload():
    form = ImageUploadForm()
    if 'file' not in request.files or not form.validate_on_submit():
        abort(400)

    print(request.files['file'])

    return redirect(url_for('index'))
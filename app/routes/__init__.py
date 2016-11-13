import uuid
from app import app, boto3_session, db
from app.forms.image_upload import ImageUploadForm
from app.models.images import ImageModel
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

    uploaded_file = request.files['file']

    filename = uploaded_file.filename
    hashed_filename = uuid.uuid4().hex[:16]
    obj_key = 'images/{}'.format(hashed_filename)

    s3 = boto3_session.resource('s3')
    s3_bucket = s3.Bucket(app.config.get('AWS_S3_BUCKET_NAME'))
    uploaded_obj = s3_bucket.put_object(
        ACL='public-read',
        Body=uploaded_file.stream.read(),
        Key=obj_key,
        ContentType=uploaded_file.mimetype,
        Metadata={
            'owner-content-type': 'document'
        }
    )

    new_image = ImageModel(
        key=hashed_filename,
        file_format=uploaded_file.mimetype,
        size=uploaded_obj.content_length
    )

    db.session.add(new_image)
    db.session.commit()

    return redirect(url_for('index'))

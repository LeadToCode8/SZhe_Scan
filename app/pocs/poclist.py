#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/2/19 14:56
# @Author  : Cl0udG0d
# @File    : poclist.py
# @Github: https://github.com/Cl0udG0d
import logging
import os

from app.utils.decorators import login_required
from app.pocs import poc
from flask import (
    render_template, redirect, url_for, flash, request
)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from app.model.models import (
    PocList
)
from app.model.exts import db

ALLOWED_EXTENSIONS = set(['py'])
UPLOADED_POCS_DEST=os.path.join(os.path.dirname(os.path.dirname(__file__)), "../pocs/")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@poc.route('/pocs/')
@poc.route('/pocs/<int:page>', methods=['GET'])
# @login_required
def poclist(page=1,msg=None):
    per_page = 20
    paginate = PocList.query.order_by(PocList.id.desc()).paginate(page, per_page, error_out=False)
    pocs = paginate.items
    return render_template('poclist.html', paginate=paginate, pocs=pocs)

@poc.route('/pocs/refresh', methods=['GET'])
def refreshPoc():
    try:
        currdir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "../pocs/")
        poclist = PocList.query.all()
        [db.session.delete(poc) for poc in poclist]
        for files in os.listdir(currdir):
            if os.path.splitext(files)[1] == '.py':
                temptask = PocList(filename=os.path.splitext(files)[0])
                db.session.add(temptask)
        db.session.commit()
        flash('刷新成功')
    except Exception as e:
        flash('刷新失败')
        print(e)
        pass
    return redirect(url_for('pocs.poclist'))

@poc.route('/pocs/reverse/<int:id>', methods=['GET'])
def reverse(id=None):
    try:
        poc = PocList.query.filter(PocList.id == id).first()
        poc.status=not poc.status
        db.session.commit()
    except Exception as e:
        logging.warning(e)
        pass
    return 'success'



@poc.route('/pocs/reverseAllStatus/', methods=['GET'])
def reverseAllStatus():
    pocs = PocList.query.all()
    for poc in pocs:
        poc.status = not poc.status
    db.session.commit()
    return redirect(url_for('pocs.poclist'))



@poc.route('/pocs/uploadPoc/',methods=['POST','GET'])
def uploadPoc():
    if request.method=='GET':
        return render_template('uploadPoc.html')
    else:
        for file in request.files.getlist('files'):
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOADED_POCS_DEST, filename))
                flash('{}上传成功'.format(filename))
            else:
                flash('上传失败')
        return redirect(url_for('pocs.poclist'))



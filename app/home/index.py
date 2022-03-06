#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29 20:07
# @Author  : Cl0udG0d
# @File    : index.py
# @Github: https://github.com/Cl0udG0d

from app.utils.decorators import login_required
from app.home import home
from flask import (
    render_template,redirect,request,url_for
)
from app.model.models import *

@home.route('/home/<int:page>', methods=['GET', 'POST'])
@home.route('/home/', methods=['GET', 'POST'])
@home.route('/', methods=['GET', 'POST'])
@login_required
def index(page=1):
    per_page = 38
    paginate = Log.query.order_by(Log.date.desc()).paginate(page, per_page, error_out=False)
    logs = paginate.items
    result={
        'targets':len(BaseInfo.query.all()),
        'pocs':len(PocList.query.all()),
        'vuls':len(VulList.query.all()),
        'plugins':0
    }
    return render_template('index.html', paginate=paginate, logs=logs,result=result)



@home.route('/home/delLoginLog/<int:id>', methods=['GET'])
@login_required
def delLoginLog(id):
    delLog=db.session.query(Log).filter_by(id=id).first()
    db.session.delete(delLog)
    db.session.commit()
    return redirect(url_for('home.index'))




@home.route('/home/delAllLoginLog/', methods=['GET'])
@login_required
def delAllLoginLog():
    delLogs = db.session.query(Log).all()
    [db.session.delete(delLog) for delLog in delLogs]
    db.session.commit()
    return redirect(url_for('home.index'))




def test():
    print('hi')


if __name__ == '__main__':
    test()

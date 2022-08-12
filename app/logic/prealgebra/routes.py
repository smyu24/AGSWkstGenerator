"""Route declaration."""
#system imports
from flask import *
from app import db
from .getpna import getproblemandanswer
from datetime import timedelta
from .seedgen import seedgem

prealgebra_bp = Blueprint('prealgebra',__name__, url_prefix='/prealgebra', template_folder='templates',static_folder='static')

@prealgebra_bp.before_request
def makesession_permanent():
    session.permanent = True
    prealgebra_bp.permanent_session_lifetime = timedelta(minutes = 90)

@prealgebra_bp.route('/<code>', methods=["GET", "POST"])
def prealgebra_main(code):

    if request.method == 'POST':
        form = request.form
        total, farr = seedgem(form, code)
        if(farr == False):
            flash("Please fill out all options.")
            return redirect(url_for('prealgebra.prealgebra_main', code=code))
        else:
            pro, ans1, ans2 = getproblemandanswer(code, farr)

            desc = []
            for i in range(len(farr)):
                desc.append(farr[i][0].split('-')[ len(farr[i][0].split('-'))-1 ])

            cur = db.connection.cursor()
            cur.execute('SELECT description from learningtarget_prealg where seed = %s', [code])
            data = str(cur.fetchone())[2:-3].split('|')

            cur.execute('SELECT latex from learningtarget_prealg where seed = %s', [code])
            latex = str(cur.fetchone())[2:-3].split(',')

            return render_template('prealgebra/editing.html',
                probs = pro, answ = ans1, Nansw = ans2, arr = data, total = total, latex = latex, desc = desc)

    #GET
    #Select data from sql
    cur = db.connection.cursor()
    cur.execute('SELECT options from learningtarget_prealg where seed = %s', [code])
    num = str(cur.fetchone())[2:-3]
    arr_num = num.split(',')

    cur.execute('SELECT section from learningtarget_prealg where seed = %s', [code])
    selec = str(cur.fetchone())[2:-3]
    arr_select = selec.split(',')

    cur.execute('SELECT difficulty from learningtarget_prealg where seed = %s', [code])
    diff = str(cur.fetchone())[2:-3]
    arr_diff = diff.split(',')

    option = arr_num[0]

    cur.close()

    return render_template(
        'prealgebra/prealgebra.html',
        seed = code, num = arr_num, min = arr_num[1], max = arr_num[2], selection = arr_select, diffc = arr_diff, option = option)
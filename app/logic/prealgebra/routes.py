"""Route declaration."""
#system imports
from flask import *
from app import db
from .pro_gen import Naming_Decimal_Places, readingandwriting, rounding, divandfac, factoring, monomials, common_factors, Leastcommon_factors
from datetime import timedelta
from .seedgen import seedgem

prealgebra_bp = Blueprint('prealgebra',__name__, url_prefix='/prealgebra', template_folder='templates',static_folder='static')
@prealgebra_bp.before_request
def makesession_permanent():
    session.permanent = True
    prealgebra_bp.permanent_session_lifetime = timedelta(minutes = 60)

@prealgebra_bp.route('/<code>', methods=["GET", "POST"])
def prealgebra_main(code):
    login = False
    if 'response' in session:
        login = True
    
    if request.method == 'POST':
        form = request.form
        total, farr = seedgem(form, code)
        if(farr == False):
            flash("Please fill out all options.")
            return redirect(url_for('prealgebra.prealgebra_main', code=code))
        else:   
            arr = []
            if(code == "1-1-1"):
                pro, ans1, ans2 = Naming_Decimal_Places(farr) 
            elif(code == "1-1-2"):
                pro, ans1, ans2 = readingandwriting(farr)
            elif(code == "1-1-3"):
                pro, ans1, ans2 = rounding(farr)
            elif(code == "1-2-1"):
                pro, ans1, ans2 = divandfac(farr)
            elif(code == "1-2-2"):
                pro, ans1, ans2 = factoring(farr)
            elif(code == "1-2-3"):
                pro, ans1, ans2 = monomials(farr)   
            elif(code == "1-2-4"):
                pro, ans1, ans2 = common_factors(farr)
            elif(code == "1-2-5"):
                pro, ans1, ans2 = Leastcommon_factors(farr)

            cur = db.connection.cursor()
            cur.execute('SELECT description from learningtarget where seed = %s', [code])
            data = str(cur.fetchone())[2:-3].split('|')

            return render_template('prealgebra/editing.html', 
                data = login, probs = pro, answ = ans1, Nansw = ans2, arr = data, total = total)

    #Select data from sql
    cur = db.connection.cursor()
    cur.execute('SELECT options from learningtarget where seed = %s', [code])
    num = str(cur.fetchone())[2:-3]
    arr_num = num.split(',')

    cur.execute('SELECT section from learningtarget where seed = %s', [code])
    selec = str(cur.fetchone())[2:-3]
    arr_select = selec.split(',')

    cur.execute('SELECT difficulty from learningtarget where seed = %s', [code])
    diff = str(cur.fetchone())[2:-3]
    arr_diff = diff.split(',')

    option = arr_num[0]

    cur.close()
    
    return render_template(
        'prealgebra/prealgebra.html', 
        data = login, seed = code, num = arr_num, min = arr_num[1], max = arr_num[2], selection = arr_select, diffc = arr_diff, option = option)

#way to upload the data
    #    sname = request.form['studnetName']
    #    tname = "aiden O."
    #    seed = request.form['master']
    #    title = request.form['pdftitle']
    #    desc = request.form['pdfdesc']
    #    master = str(Decimal_Places(seed))
    
    #custom function
    #    cur = db.connection.cursor()
    #    cur.execute("INSERT INTO mmtseed VALUES(%s, %s, %s, %s, %s)", (title, desc, sname, tname, master))
    #    db.connection.commit()
    #    cur.close()
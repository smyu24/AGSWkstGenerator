"""Route declaration."""
#system imports
from flask import *
from app import db
from .pro_gen import Decimal_Places, Reading_Numbers, Divisibility, WritingNumber, Rounding_To_Word_Numbers, Factoring
from datetime import timedelta
from .seedgen import seedgem

prealgebra_bp = Blueprint('prealgebra',__name__, url_prefix='/prealgebra', template_folder='templates',static_folder='static')
@prealgebra_bp.before_request
def makesession_permanent():
    session.permanent = True
    prealgebra_bp.permanent_session_lifetime = timedelta(minutes = 60)

@prealgebra_bp.route('/')
def prealgebra_main():
    login = False
    if 'response' in session:
        login = True
    
    return redirect(url_for('prealgebra.prealgebra_sec11'))

@prealgebra_bp.route('/1-1-1', methods=["GET", "POST"])
def prealgebra_sec11():
    login = False
    if 'response' in session:
        login = True
    
    if request.method == 'POST':
        form = request.form
        farr = seedgem(form)
        if(farr == False):
            flash("Please fill out all options.")
            return redirect(url_for('prealgebra.prealgebra_sec11'))
        else:   
            pro, ans1, ans2 = Decimal_Places(farr)
            return render_template('prealgebra/editing.html', 
                data = login, probs = pro, answ = ans1, Nansw = ans2)

    return render_template(
        'prealgebra/prealgebra.html', 
        data = login, seed = '1-1-1', min='10', max='1000')

@prealgebra_bp.route('/1-1-2', methods=["GET", "POST"]) #Writing
def prealgebra_sec12():
    login = False
    if 'response' in session:
        login = True
    
    if request.method == 'POST': 
        form = request.form
        farr = seedgem(form)
        if(farr == False):
            flash("Please fill out all options.")
            return redirect(url_for('prealgebra.prealgebra_sec12'))
        else:   
            pro, ans1, ans2 = Reading_Numbers(farr)
            return render_template('prealgebra/editing.html', 
                data = login, probs = pro, answ = ans1, Nansw = ans2)
    
    return render_template('prealgebra/prealgebra.html', 
        data = login, seed = '1-1-2', min='10', max='1000')

@prealgebra_bp.route('/1-1-3', methods=["GET", "POST"]) #Reading
def prealgebra_sec13():
    login = False
    if 'response' in session:
        login = True
    
    if request.method == 'POST': 
        form = request.form
        farr = seedgem(form)
        if(farr == False):
            flash("Please fill out all options.")
            return redirect(url_for('prealgebra.prealgebra_sec13'))
        else:   
            pro, ans1, ans2 = WritingNumber(farr)
            return render_template('prealgebra/editing.html', 
                data = login, probs = pro, answ = ans1, Nansw = ans2)
    
    return render_template('prealgebra/prealgebra.html', 
        data = login, seed = '1-1-3', min='10', max='1000')

@prealgebra_bp.route('/1-1-4', methods=["GET", "POST"]) #Reading
def prealgebra_sec14():
    login = False
    if 'response' in session:
        login = True
    
    if request.method == 'POST': 
        form = request.form
        farr = seedgem(form)
        if(farr == False):
            flash("Please fill out all options.")
            return redirect(url_for('prealgebra.prealgebra_sec14'))
        else:   
            pro, ans1, ans2 = Rounding_To_Word_Numbers(farr)
            return render_template('prealgebra/editing.html', 
                data = login, probs = pro, answ = ans1, Nansw = ans2)
    
    return render_template('prealgebra/prealgebra.html', 
        data = login, seed = '1-1-4', min='10', max='1000')


@prealgebra_bp.route('/1-2-1', methods=["GET", "POST"])
def prealgebra_sec21():
    login = False
    form = generator(request.form)
    if 'response' in session:
        login = True
    
    if request.method == 'POST' and form.validate(): 
        wkst = [form.Enump.data, form.Emin.data, form.Emax.data,
                form.Mnump.data, form.Mmin.data, form.Mmax.data,
                form.Hnump.data, form.Hmin.data, form.Hmax.data]

        seed = Divisibility(wkst)
        arr = seed.split('||', 2)

        return render_template( #GET return
        'prealgebra/editing.html', 
        data = login, probs = arr[0], answ = arr[1], form = form)
        
    elif request.method == 'POST' and not form.validate(): 
        flash("Please fill out all options.")
        return redirect(url_for('prealgebra.prealgebra_sec21'))
    
    return render_template( #GET return
        'prealgebra/prealgebra.html', 
        data = login, form = form, seed = '1-2-1')

@prealgebra_bp.route('/1-2-2', methods=["GET", "POST"])
def prealgebra_sec22():
    login = False
    form = generator(request.form)
    if 'response' in session:
        login = True
    
    if request.method == 'POST' and form.validate(): 
        wkst = [form.Enump.data, form.Emin.data, form.Emax.data,
                form.Mnump.data, form.Mmin.data, form.Mmax.data,
                form.Hnump.data, form.Hmin.data, form.Hmax.data]

        seed = Factoring(wkst)
        arr = seed.split('||', 2)

        return render_template( #GET return
        'prealgebra/editing.html', 
        data = login, probs = arr[0], answ = arr[1], form = form)
        
    elif request.method == 'POST' and not form.validate(): 
        flash("Please fill out all options.")
        return redirect(url_for('prealgebra.prealgebra_sec22'))
    
    return render_template( #GET return
        'prealgebra/prealgebra.html', 
        data = login, form = form, seed = '1-2-2')
















'''
@prealgebra_bp.route('/example', methods=["GET", "POST"])
def hello_html():
    form = example()
    #defaults = returndefault()
    print("=", form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit(): 
        wkst = Wkst(form.username.data)
        return 'Thank you'

    return render_template(
        'prealgebra/example.html', 
        form = form,
#        default = defaults,
        descripstion = 'this is the example'
        )
'''
#@prealgebra_bp.route('/hello', defaults={'name': 'World'})
#def hello_html(name):
#    return render_template(
#        'prealgebra/example.html', 
#        name=name,
#        descripstion = 'this is the example'
#        )

#@prealgebra_bp.route('/hello_<name>.pdf')
#def hello_pdf(name):
#    # Make a PDF straight from HTML in a string.
#    html = render_template('prealgebra/example.html', name=name)
#    return render_pdf(HTML(string=html))

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
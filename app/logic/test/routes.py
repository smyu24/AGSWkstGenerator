"""Route declaration."""
#system imports
from flask import *
from app import db
from .seedgen import testseedmaster

test_dp = Blueprint('test',__name__, url_prefix='/test', template_folder='templates',static_folder='static')

@test_dp.route('/', methods=['GET', 'POST'])
def main_test():

    if request.method == 'GET':
        cur = db.connection.cursor()
        cur.execute('SELECT * from testset')
        arr = cur.fetchall()
        cur.close()

        return render_template(
            'test/pre-test.html',
            testset = arr
        )

    elif request.method == 'POST': #IF POST
        form = request.form['seed'].split(",")
        cur = db.connection.cursor()
        data = []
        for i in range(len(form)):
            cur.execute("SELECT section from learningtarget_prealg where Seed = %s", [form[i]])
            data.append( len(str(cur.fetchall())[3:-5].split(",")) )

        cur.execute('SELECT Seed from learningtarget_prealg')
        seed = cur.fetchall()
        cur.execute('SELECT description from learningtarget_prealg')
        des = cur.fetchall()
        cur.execute('SELECT section from learningtarget_prealg')
        sec = cur.fetchall()
        cur.execute('SELECT difficulty from learningtarget_prealg')
        difficulty = cur.fetchall()

        cur.close()
        return redirect( url_for(
            '.custom_test',
            pickedseed = str(form), pickedsection = str(data)
        ))

@test_dp.route('/custom', methods=['GET', 'POST'])
def custom_test():

    if request.method == 'GET':
        cur = db.connection.cursor()
        cur.execute('SELECT Seed from learningtarget_prealg')
        seed = cur.fetchall()
        cur.execute('SELECT description from learningtarget_prealg')
        des = cur.fetchall()
        cur.execute('SELECT section from learningtarget_prealg')
        sec = cur.fetchall()
        cur.execute('SELECT difficulty from learningtarget_prealg')
        difficulty = cur.fetchall()
        cur.execute('SELECT excode from sectionnote')
        note = cur.fetchall()
        cur.close()

        form = str(request.args['pickedseed'])[2:-2].replace("'", "").split(",")
        data = request.args['pickedsection'][1:-1].replace("'", "").split(",")

        return render_template(
            'test/adv-test.html',
            lst= seed, sec= sec, dessc= des, difficulty= difficulty, pickedseed = form, pickedsection = data, note = note
        )
    elif request.method == 'POST': #IF POST
        pro = []
        ans1 = []
        ans2 = []
        form = request.form['seed'].split(",")

        sentence = []

        i = 0
        cur = db.connection.cursor()
        while i < len(form):
            tpro, tans1, tans2 = testseedmaster(i, form)
            pro += tpro
            ans1 += tans1
            ans2 += tans2

            cur.execute('SELECT description from learningtarget_prealg where seed = %s', [form[i].replace(" ", "")])
            dec = str(cur.fetchone())[2:-3].split('|')
            sentence.append( dec[ int(str(form[i+1])[1:].replace(" ", "")) ] )

            i += 4
        cur.close()

        return render_template(
            'test/editing.html',
            probs = pro, answ = ans1, Nansw = ans2, total = int(len(form) / 4), latex = '2, 2', data = sentence
        )

@test_dp.route('/adv', methods=['GET', 'POST']) #NOT CUSTOM
def adv_test():

    if request.method == 'GET':
        cur = db.connection.cursor()
        cur.execute('SELECT Seed from learningtarget_prealg')
        data = cur.fetchall()

        cur.execute('SELECT description from learningtarget_prealg')
        des = cur.fetchall()

        cur.execute('SELECT section from learningtarget_prealg')
        sec = cur.fetchall()

        cur.execute('SELECT difficulty from learningtarget_prealg')
        difficulty = cur.fetchall()
        cur.execute('SELECT excode from sectionnote')
        note = cur.fetchall()

        cur.close()

        return render_template(
            'test/adv-test.html',
            lst= data, sec= sec, dessc= des, difficulty= difficulty, pickedseed = -1, pickedsection = -1, note = note
        )
    elif request.method == 'POST': #IF POST
        pro = []
        ans1 = []
        ans2 = []
        form = request.form['seed'].split(",")

        sentence = []
        i = 0
        cur = db.connection.cursor()
        while i < len(form):
            tpro, tans1, tans2 = testseedmaster(i, form)
            pro += tpro
            ans1 += tans1
            ans2 += tans2

            cur.execute('SELECT description from learningtarget_prealg where seed = %s', [form[i].replace(" ", "")])
            dec = str(cur.fetchone())[2:-3].split('|')
            sentence.append( dec[ int(str(form[i+1])[1:].replace(" ", "")) ] )

            i += 4
        cur.close()

        return render_template(
            'test/editing.html',
            probs = pro, answ = ans1, Nansw = ans2, total = int(len(form) / 4), latex = '2, 2', data = sentence
        )
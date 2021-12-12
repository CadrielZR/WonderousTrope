from flask import Flask, render_template, request, redirect, session, flash
from flask_mysqldb import MySQL
from models import Users, Writing, Writing_fav
from dao import UsuarioDao, WritingPromptDao, GeneroDao, DrawingPromptDao, WritingFavDao, DrawingFavDao
import random as random

app = Flask(__name__)
app.secret_key= 'The Cake is a Lie'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'wonderoustrope'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
usuario_dao = UsuarioDao(db)
writing_dao = WritingPromptDao(db)
genero_dao = GeneroDao(db)
drawing_dao = DrawingPromptDao(db)
writing_fav_dao = WritingFavDao(db)
drawing_fav_dao = DrawingFavDao(db)

#Writing tropes
@app.route('/writingprompts', methods=['POST',])
def writing_prompts():
    if 'usuario_logado' not in session or session['usuario_logado'] == None :
        return redirect('/login?proxima=writing_prompts')
    id = request.form['genero']
    id_gen = int(id)
    aux = []
    aux.clear()
    i=0
    while i<=3:
        prompt_id = switch(id_gen)
        wid = str(prompt_id)
        dados=writing_dao.busca_por_id(wid)
        aux.append(dados)
        i+=1
    return render_template('writing_prompts.html', titulo='Wonderous Trope', prompts=aux)



#Drawing Prompts
@app.route('/drawingprompts', methods=['POST',])
def drawing_prompts():
    if 'usuario_logado' not in session or session['usuario_logado'] == None :
        return redirect('/login?proxima=drawing_prompts')
    aux = []
    aux.clear()
    i=0
    while i<=2:
        prompt_id = random.choice(range(1,100))
        did = str(prompt_id)
        dados = drawing_dao.busca_por_id(did)
        aux.append(dados)
        i+=1
    return render_template('drawing_prompts.html', titulo='Wonderous Trope', prompts=aux)

#Favorite Prompts
@app.route('/savewritingfav/<int:id>')
def save_writing_fav(id):
    copy_prompt_id = writing_dao.busca_por_id(id)
    writing_fav_dao.salvar(copy_prompt_id)

    return redirect('/')

@app.route('/savedrawingfav/<int:id>')
def save_drawing_fav(id):
    copy_prompt_id = drawing_dao.busca_por_id(id)
    drawing_fav_dao.salvar(copy_prompt_id)

    return redirect('/')

@app.route('/favoriteprompts')
def favorite_prompts():
    lista_w = writing_fav_dao.listar()
    lista_d = drawing_fav_dao.listar()

    return render_template('favorite_prompts.html', wprompts=lista_w, dprompts = lista_d)

@app.route('/deletewritingfav/<int:id>')
def delete_writing_fav(id):
    writing_fav_dao.deletar(id)
    return redirect('/')

@app.route('/deletedrawingfav/<int:id>')
def delete_drawing_fav(id):
    drawing_fav_dao.deletar(id)
    return redirect('/')

#página inicial e debuging

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None :
        return redirect('/login?proxima= ')
    genero = genero_dao.lista()
    return render_template('index.html', titulo='Wonderous Trope', genero=genero)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    usuario = usuario_dao.busca_por_id(request.form['usuario'])
    if usuario:
        if usuario._senha == request.form['senha']:
            session['usuario_logado'] = request.form['usuario']
            flash(request.form['usuario'] + ' sucessfully logged in!')
            proxima_pagina = request.form['proxima']
            if proxima_pagina == '':
               return redirect('/')
            else:
                return redirect('/{}'.format(proxima_pagina))
    flash('An error has ocurred, please try again!')
    return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('No user logged in!')
    return redirect('/login')

@app.route('/signup')
def signup():
    if 'usuario_logado' not in session or session['usuario_logado'] == None :
        return render_template('signup.html', titulo = 'New Account')
    else:
        flash('You are already loged in!')
        return redirect('/')

@app.route('/novaconta', methods=['POST',])
def novaconta():
    id = request.form['username']
    nome = request.form['nome']
    senha = request.form['senha']

    user = Users(id, nome, senha)
    usuario_dao.salvar(user)

    return redirect('/login')

#switch geral

def switch (id):
    if id == 4:
        return random.choice(range(1, 50))
    elif id == 1:
        return random.choice(range(51, 100))
    elif id == 7:
        return random.choice(range(101, 150))
    elif id == 5:
        return random.choice(range(151, 200))
    elif id == 2:
        return random.choice(range(201,250))
    elif id == 6:
        return random.choice(range(251,300))
    elif id == 3:
        return random.choice(range(301,349))
    else:
        print('fatal error')


if __name__ == '__main__':
    app.run(debug=True)
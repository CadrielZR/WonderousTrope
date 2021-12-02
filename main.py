from flask import Flask, render_template, request, redirect, session, flash
from flask_mysqldb import MySQL
from models import Users, Writing
from dao import UsuarioDao, WritingPromptDao, GeneroDao
from random import choice

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

#Writing tropes
@app.route('/writing_prompts')
def writing_prompts():
    if 'usuario_logado' not in session or session['usuario_logado'] == None :
        return redirect('/login?proxima= writing_prompts')
    prompt = writing_dao
    return render_template('writing_prompts.html', titulo='Wonderous Trope')

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
            flash(request.form['usuario'] + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            if proxima_pagina == '':
               return redirect('/')
            else:
                return redirect('/{}'.format(proxima_pagina))
    flash('Não foi possivel logar, tente novamente!')
    return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
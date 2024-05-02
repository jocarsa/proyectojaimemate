#pip install Flask

from flask import Flask, render_template,request,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/sobremi')
def sobremi():
    return render_template('sobremi.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/procesa',methods=['POST'])
def procesa():
    if request.method == "POST":
        
        archivo = open("nombres.txt",'a')
        archivo.write(request.form['nombre']+"\n")
        archivo.close()
        return "te proceso el formulario"
        


if __name__ == '__main__':
    app.run(debug=True)

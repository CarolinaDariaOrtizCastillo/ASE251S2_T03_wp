from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# Página principal
@app.route("/")
def inicio():
    ruta = os.path.join(app.static_folder, 'image')
    imagenes = [url_for('static', filename=f'image/{img}') 
                for img in os.listdir(ruta) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template("inicio.html", imagenes=imagenes)

# Otras páginas
@app.route("/acceder")
def acceder():
    return render_template("acceder.html")

@app.route("/inscribete")
def inscribete():
    return render_template("inscribete.html")

@app.route("/masinfo")
def masinfo():
    return render_template("masinfo.html")

if __name__ == '__main__':
    app.run(debug=True)

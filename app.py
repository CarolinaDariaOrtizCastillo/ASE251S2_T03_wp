from flask import Flask, render_template, url_for, request, redirect, flash, session
from functools import wraps
import os
import mysql.connector
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "carolina"  # Necesario para usar flash()
from werkzeug.middleware.proxy_fix import ProxyFix

app.config['APPLICATION_ROOT'] = '/programatransitabilidad'
app.config['PREFERRED_URL_SCHEME'] = 'https'
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# --- AÑADIDO: Configuración de Flask-Mail ---
# (Recuerda usar tu correo y una "Contraseña de Aplicación" de Google)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'carolina.ortiz@vallegrande.edu.pe'  # 🔹 RELLENA ESTO
app.config['MAIL_PASSWORD'] = 'lhjh ruew tkdo opnx'  # 🔹 RELLENA ESTO
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = ('Programa Transitabilidad', 'carolina.ortiz@vallegrande.edu.pe')

# Inicializa Flask-Mail
mail = Mail(app)

# 🔗 Conexión con tu base de datos en AWS RDS
# conexion = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3309,
#     user="root",
#     password="carolinaOrtiz",
#     database="programa_transitabilidad"
# )
conexion = True
# ========================
# "GUARDIA" DE LOGIN AÑADIDO
# ========================
# Esta función revisará si un usuario está logueado
# antes de dejarlo entrar a una página.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session: # Si el usuario NO está en la sesión
            flash("Debes iniciar sesión para ver esta página.", "danger")
            return redirect(url_for('login')) # Lo redirige al login
        return f(*args, **kwargs) # Si sí está, continúa
    return decorated_function

# ========================
# 🏠 RUTAS PRINCIPALES
# ========================

@app.route("/")
def inicio():
    nombres_especificos = ["BANNER1_2.png", "BANNER2_2.png", "BANNER3_2.png"]
    imagenes = [url_for('static', filename=f'image/{nombre}') for nombre in nombres_especificos]
    return render_template("inicio.html", imagenes=imagenes)


@app.route("/inscribete")
def inscribete():
    nombres_especificos = ["galeria1.jpg", "galeria2.JPG", "galeria3.JPG", "galeria4.JPG"]
    imagenes = [url_for('static', filename=f'image/{nombre}') for nombre in nombres_especificos]
    return render_template("inscribete.html", imagenes=imagenes)

@app.route("/inscribete_login")
def inscribete_login():
    nombres_especificos = ["galeria1.jpg", "galeria2.JPG", "galeria3.JPG", "galeria4.JPG"]
    imagenes = [url_for('static', filename=f'image/{nombre}') for nombre in nombres_especificos]
    return render_template("inscribete_login.html", imagenes=imagenes)

@app.route("/contactanos")
def contactanos():
    return render_template("contactanos.html")

@app.route("/contactanos_login")
def contactanos_login():
    return render_template("contactanos_login.html")

@app.route("/convenios")
def convenios():
    return render_template("convenios.html")

@app.route("/info_importante")
def info_importante():
    return render_template("info_importante.html")

@app.route("/mas_info")
@login_required  # <-- AÑADIDO: El "guardia" protege esta página
def mas_info():
    # Esta página ahora solo es accesible si has iniciado sesión
    nombres_especificos = ["BANNER1_2.png", "BANNER2_2.png", "BANNER3_2.png"]
    imagenes = [url_for('static', filename=f'image/{nombre}') for nombre in nombres_especificos]
    return render_template("mas_info.html", imagenes=imagenes)

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

# --------------------------------------------------------
# 🏫 FORMULARIO DE INSTITUCIÓN
# --------------------------------------------------------
@app.route("/formulario_ins", methods=["GET", "POST"])
def formulario_ins():
    if request.method == "POST":
        try:
            nombre_institucion = request.form["nombre_institucion"]
            tipo_gestion = request.form["tipo_gestion"]
            direccion = request.form["direccion"]
            ubigeo_id = request.form["ubigeo"]

            motivo_capacitacion_docente = 1 if "motivo_capacitacion_docente" in request.form else 0
            motivo_beneficios_estudiantes = 1 if "motivo_beneficios_estudiantes" in request.form else 0
            motivo_innovacion_educativa = 1 if "motivo_innovacion_educativa" in request.form else 0
            motivo_actividades_extracurriculares = 1 if "motivo_actividades_extracurriculares" in request.form else 0
            motivo_otro = request.form.get("motivo_otro", "")

            representante_nombre = request.form["representante_nombre"]
            representante_apellido = request.form["representante_apellido"]
            representante_rol = request.form["representante_rol"]
            representante_celular = request.form["telefono_contacto"]
            representante_correo = request.form["correo_contacto"]

            cursor = conexion.cursor()

            sql_institucion = """
                INSERT INTO institution 
                (name, management, specific_address, ubigeo_id_ubigeo,
                 teacher_training, student_benefits, educational_innovation,
                 extracurricular_activities, another_reason)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_institucion, (
                nombre_institucion, tipo_gestion, direccion, ubigeo_id,
                motivo_capacitacion_docente, motivo_beneficios_estudiantes,
                motivo_innovacion_educativa, motivo_actividades_extracurriculares,
                motivo_otro
            ))
            id_institucion = cursor.lastrowid

            sql_representante = """
                INSERT INTO representative (role, name, last_name, cellphone_contact, email_contact)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql_representante, (
                representante_rol, representante_nombre, representante_apellido,
                representante_celular, representante_correo
            ))
            id_representante = cursor.lastrowid

            sql_relacion = """
                INSERT INTO institution_representative (institution_id_institution, representative_id_representative)
                VALUES (%s, %s)
            """
            cursor.execute(sql_relacion, (id_institucion, id_representante))

            conexion.commit()
            cursor.close()
            flash("✅ Institución y representante registrados correctamente.", "success")
        except Exception as e:
            flash(f"❌ Error al registrar la institución: {e}", "danger")

        return redirect(url_for("mas_info"))

    return render_template("formulario_ins.html")

# --------------------------------------------------------
# 👩‍🎓 FORMULARIO DE ESTUDIANTE
# --------------------------------------------------------
@app.route("/formulario_est", methods=["GET", "POST"])
def formulario_est():
    if request.method == "POST":
        try:
            cursor = conexion.cursor()

            # === USUARIO ESTUDIANTE ===
            email_est = request.form["email_est"]
            password_est = request.form["password_est"]

            reg_info = 1 if "registration_information" in request.form else 0
            event_info = 1 if "event_information" in request.form else 0
            info_comm = 1 if "information_communication" in request.form else 0
            content_info = 1 if "content_information" in request.form else 0

            sql_user_est = """
                INSERT INTO user (email, password, registration_information, event_information, information_communication, content_information)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_user_est, (email_est, password_est, reg_info, event_info, info_comm, content_info))
            id_user_est = cursor.lastrowid

            # === DATOS ESTUDIANTE ===
            nombre = request.form["nombres"]
            apellido = request.form["apellidos"]
            grado = request.form["grado"]
            celular = request.form["celular"]
            tipo_doc = request.form["tipo_doc"]
            numero_doc = request.form["dni"]
            direccion = request.form["direccion"]
            ubigeo_id = request.form["ubigeo"]
            institucion_id = request.form["institucion"]

            sql_student = """
                INSERT INTO student (name, last_name, degree, cellphone_number, type_document, number_document,
                specific_address, ubigeo_id_ubigeo, institution_id_institution, user_id_user)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_student, (
                nombre, apellido, grado, celular, tipo_doc, numero_doc,
                direccion, ubigeo_id, institucion_id, id_user_est
            ))

            # === USUARIO APODERADO ===
            email_guard = request.form["apoderado_email"]
            password_guard = request.form["apoderado_password"]

            sql_user_guardian = """
                INSERT INTO user (email, password, registration_information, event_information, information_communication, content_information)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_user_guardian, (email_guard, password_guard, 0, 0, 0, 0))
            id_user_guardian = cursor.lastrowid

            # === APODERADO ===
            rol_guard = "Apoderado"
            nombre_guard = request.form["apoderado_nombre"]
            apellido_guard = request.form["apoderado_apellido"]
            celular_guard = request.form["apoderado_celular"]

            sql_guardian = """
                INSERT INTO guardian (role, name, last_name, email, cellphone_number, user_id_user)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_guardian, (rol_guard, nombre_guard, apellido_guard, email_guard, celular_guard, id_user_guardian))

            conexion.commit()
            cursor.close()
            flash("✅ Estudiante y apoderado registrados correctamente.", "success")
        except Exception as e:
            conexion.rollback()
            flash(f"❌ Error al registrar: {e}", "danger")

        return redirect(url_for("mas_info"))

    return render_template("formulario_est.html")

# --------------------------------------------------------
# 5. AÑADIDO: Rutas de Login y Logout
# (Reemplazan tu antigua ruta '/acceder')
# --------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    # Si el usuario ya está logueado, lo mandamos directo a mas_info
    if 'user_id' in session:
        return redirect(url_for('mas_info'))
        
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor = conexion.cursor(dictionary=True) # dictionary=True nos deja usar user['email']
        
        # Consulta parametrizada para evitar Inyección SQL
        sql = "SELECT * FROM user WHERE email = %s AND password = %s LIMIT 1"
        
        try:
            cursor.execute(sql, (email, password))
            user = cursor.fetchone()
            cursor.close()

            if user:
                # Si se encuentra al usuario, se guarda en la sesión
                session['user_id'] = user['id_user']
                session['email'] = user['email']
                flash(f"¡Bienvenido de vuelta, {user['email']}!", "success")
                
                # ¡Redirige a 'mas_info' como pediste!
                return redirect(url_for("mas_info")) 
            else:
                # Si no, muestra error
                flash("Correo o contraseña incorrectos. Inténtalo de nuevo.", "danger")
                return redirect(url_for("login"))
        
        except Exception as e:
            cursor.close()
            flash(f"Error en la base de datos: {e}", "danger")
            return redirect(url_for("login"))

    # Si es GET, solo muestra el formulario
    return render_template("login.html")


@app.route("/logout")
def logout():
    # Limpia la sesión
    session.pop('user_id', None)
    session.pop('email', None)
    flash("Has cerrado sesión.", "success")
    return redirect(url_for("login")) # Al cerrar sesión, lo mandamos al login
# --- FIN DE LO AÑADIDO ---


# ========================================================
# 6. AÑADIDO: LÓGICA DE EMAIL MARKETING
# ========================================================

# --- Función REAL de envío de correo ---
def enviar_email_real(destinatario, asunto, cuerpo_html):
    """
    Función REAL que envía correos usando Flask-Mail.
    """
    try:
        msg = Message(asunto, recipients=[destinatario])
        msg.html = cuerpo_html
        mail.send(msg)
        print(f"✔️ Correo enviado a {destinatario} (Asunto: {asunto})")
    except Exception as e:
        print(f"❌ Error al enviar correo a {destinatario}: {e}")

# --- Función que lee la BD y prepara los correos ---
def enviar_correos_marketing():
    """
    Función principal que lee la BD y envía correos
    según los permisos de cada usuario.
    """
    try:
        cursor = conexion.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM user WHERE registration_information = 1 OR event_information = 1 OR information_communication = 1 OR content_information = 1")
        users = cursor.fetchall()
        cursor.close()

        print(f"\n[INFO] Iniciando envío de marketing a {len(users)} usuarios...")
        
        # 'with app.app_context()' es necesario para Flask-Mail
        with app.app_context(): 
            for user in users:
                email = user['email']
                
                if user['registration_information']:
                    html_body = render_template("emails/registro.html", user=user) 
                    enviar_email_real(email, "Información de tu Registro", html_body)

                if user['event_information']:
                    html_body = render_template("emails/eventos.html", user=user)
                    enviar_email_real(email, "¡Nuevos Eventos!", html_body)

                if user['information_communication']:
                    html_body = render_template("emails/comunicado.html", user=user)
                    enviar_email_real(email, "Comunicado Institucional", html_body)

                if user['content_information']:
                    html_body = render_template("emails/contenido.html", user=user)
                    enviar_email_real(email, "Nuevo Contenido del Programa", html_body)
        
        print("[INFO] Envío de marketing finalizado.\n")

    except Exception as e:
        print(f"❌ Error durante el envío de marketing: {e}")

# --- "Gatillo" para iniciar el envío ---
@app.route("/admin/enviar-correos")
@login_required # Protegido
def admin_enviar_correos():
    enviar_correos_marketing() 
    flash("Se ha iniciado el proceso de envío de correos (revisa tu terminal).", "success")
    return redirect(url_for("inicio"))
# --- FIN DE LO AÑADIDO ---
# --------------------------------------------------------
# 🚀 EJECUCIÓN LOCAL
# --------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
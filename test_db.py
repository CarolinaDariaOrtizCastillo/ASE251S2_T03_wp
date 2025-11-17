import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        port=3008,
        user="root",
        password="carolinaOrtizP",
        database="transitabilidad_db"
    )

    if conexion.is_connected():
        print("✅ Conectado a MySQL correctamente")

except mysql.connector.Error as err:
    print(f"❌ Error de conexión: {err}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()

import mysql.connector

try:
    # 1. Configurar la conexión con tus datos reales de MySQL
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Fer1229",
        database="automotriz",
        port=3306
    )

    if conexion.is_connected():
        print("¡Éxito total! Python se conectó correctamente a la base de datos.")
        
        # 2. Vamos a pedirle a Python que verifique si ve nuestra tabla de clientes
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        
        print("Tablas encontradas en la base de datos:")
        for tabla in tablas:
            print(f"- {tabla[0]}")

except mysql.connector.Error as error:
    print(f"Error al conectar a la base de datos: {error}")

finally:
    # 3. Siempre es buena práctica cerrar la conexión al terminar
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada de forma segura.")
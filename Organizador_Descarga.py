import os
import shutil

def organizar_descargas():
    carpeta_descargas = "E:\Descargas"
    
    # Diccionario de extensiones
    subcarpetas_extensiones = {
        "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Vídeos": [".mp4", ".mov", ".avi"],
        "Programas": [".exe", ".msi"],
        "Comprimidos": [".zip", ".rar", ".7z"],
        "Otros": []
    }

    # Primero, organizar los archivos en sus categorías por extensión
    for archivo in os.listdir(carpeta_descargas):
        ruta_archivo = os.path.join(carpeta_descargas, archivo)

        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            movido = False

            # Mover archivos a las subcarpetas según su extensión
            for categoria, extensiones in subcarpetas_extensiones.items():
                if extension in extensiones:
                    carpeta_destino = os.path.join(carpeta_descargas, categoria)
                    os.makedirs(carpeta_destino, exist_ok=True)
                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                    movido = True
                    break

            # Si no corresponde a ninguna categoría, moverlo a "Otros"
            if not movido:
                carpeta_destino = os.path.join(carpeta_descargas, "Otros")
                os.makedirs(carpeta_destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

    # Crear la carpeta "Carpetas" para las carpetas existentes
    carpeta_destino_carpetas = os.path.join(carpeta_descargas, "Carpetas")
    os.makedirs(carpeta_destino_carpetas, exist_ok=True)

    # Ahora, mover las carpetas que ya existen dentro de "Carpetas"
    for item in os.listdir(carpeta_descargas):
        ruta_item = os.path.join(carpeta_descargas, item)

        # Si es una carpeta que no es una de las creadas por el programa y tiene contenido, moverla
        if os.path.isdir(ruta_item) and ruta_item != carpeta_destino_carpetas:
            # Si la carpeta tiene archivos, moverla
            if os.listdir(ruta_item):  # Verifica si la carpeta tiene contenido
                # Evitar mover las carpetas con nombres en el diccionario `subcarpetas_extensiones`
                if item not in subcarpetas_extensiones:
                    shutil.move(ruta_item, os.path.join(carpeta_destino_carpetas, item))

if __name__ == "__main__":
    organizar_descargas()

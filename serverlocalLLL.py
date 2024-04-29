import socket
import threading as tr #ejecuta diferentes funciones al mismo tiempo
import pyttsx3 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 1234))

def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 145) #velocidad de la voz
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def handle_connection(connection, address):
    conectado = True
    while conectado:
        message = connection.recv(1024).decode('utf-8') #s.recv un maximo de 1024 parrafos
        if message == "desconectado":
            conectado = False
        talk(message)
        connection.send("Mensaje recibido!".encode('utf-8'))
    connection.close()


def start_connetion():
    s.listen(2)
    while True: #bucle infinito
        connection, address = s.accept()
        thread = tr.Thread(target=handle_connection, args=(connection, address))
        thread.start()
        print("Iniciando conexion...")
        print(f"Coneciones activas {tr.activeCount() - 1}")


if __name__ == "__main__":
    print("Serividor escuchando...")
    start_connetion()

#! Este es el proyecto en el que se va editando todo completo

from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

import sys
import pyautogui, webbrowser, datetime
from time import sleep
import nums_from_string  #Extraer numeros
import pywhatkit   # Mandar mensajes por wsp

class Principal(QWidget):
    def __init__(self,parent=None):
        super(Principal, self).__init__(parent)
        #! Creamos diseño 
        
        self.setStyleSheet(

"QPushButton#pushButton_2, #pushButton_3{    \n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"

"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115, 128, 142, 255);\n"
"}")
        self.setObjectName("widget")
        
        #? Label fondo de la imagen
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 0, 650, 650))
        self.label.setStyleSheet("border-image: url(background.png);\n"
"border-radius:5px;")
        self.label.setText("")
        self.label.setObjectName("label")
        #?  Segundo fondo mas obscuro un tono mas negro
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(30, 40, 590, 650))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        #? Titulo principal
        self.label_4 = QLabel("¡ Programa tu mensaje !",self)
        self.label_4.setGeometry(QRect(150, 90, 360, 60))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(160, 165, 320, 40))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit.setPlaceholderText( "User Name")
        
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 =QLineEdit(self)
        self.lineEdit_2.setPlaceholderText("Password")
        
        self.lineEdit_2.setGeometry(QRect(160, 230, 320, 40))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        
        self.labelBajo = QLabel("",self)
        self.labelBajo.setGeometry(QRect(190,290,300,30))
        self.labelBajo.setStyleSheet("color:red; font-size:13px;")
        
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        #?self.pushButton.setFont(font)
        #?self.pushButton.setObjectName("pushButton")
        
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(91, 358, 191, 21))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(160, 300, 300, 300))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
    
        self.pushButton_2.setMaximumSize(QSize(80, 80))
        font = QFont()
        font.setFamily("Icons Social Media 7")
        font.setPointSize(60)
        
        #! Boton de whatsapp 
        
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", "n", None))
        self.pushButton_2.setStyleSheet("border-radius: 17px;")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QSize(80, 80))
        
    
        
        font = QFont()
        font.setFamily("Icons Social Media 7")
        font.setPointSize(60)
        #! Boton de messenger
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", "z", None))
        self.pushButton_3.setStyleSheet("border-radius: 17px;")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.horizontalLayout.addWidget(self.pushButton_3)
       

        
class Pag2(QWidget):
    def __init__(self,parent=None):
        super(Pag2, self).__init__(parent)
        self.labela = QLabel(self)
        self.labela.setGeometry(QRect(0, 0, 650, 650))
        self.labela.setStyleSheet("border-image: url(fondo1.jpg);\n")

        self.codnum = ['Ecuador(+593)', 'Colombia(+57)', 'Peru(+51)', 'Mexico(+52)', 'EEUU(+1)', 'Argentina(+54)']

        self.vec_hora = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        self.vec_horapm = ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

        self.frecu_men = ['Diario', 'Pasando un día', 'Solo una vez', 'Cada semana', 'Cada mes','Dos veces al dia']
        # self.resize(450, 550)

        self.menunum = QComboBox(self)
        self.menunum.addItems(self.codnum)
        self.menunum.setGeometry(QRect(100, 60, 120, 30))
        self.menunum.setStyleSheet("background-color:rgba(0, 234, 162, 0.7);\n"
                                   "border-radius:5px;\n"
                                   "font-size:14px;\n"
                                   "font-family: monaco,Console, Monospace;\n")
        self.setGeometry(QRect(30, 30, 650, 650))
        self.qlinenumero = QLineEdit(self)
        self.qlinenumero.setPlaceholderText("Numero")
        self.qlinenumero.setGeometry(QRect(230, 60, 200, 30))
        self.qlinenumero.setValidator(QIntValidator())
        self.qlinenumero.setStyleSheet("background-color:rgba(0, 234, 162, 0.6);\n"
                                       "border-radius:5px;\n"
                                       "font-size:14px;\n"
                                       "font-family: monaco,Console, Monospace;\n")

        self.qlinemensaje = QLineEdit(self)
        self.qlinemensaje.setPlaceholderText("Ingrese su mensaje")
        self.qlinemensaje.setGeometry(QRect(100, 100, 400, 200))
        self.qlinemensaje.setStyleSheet("background-color:rgba(0, 0, 0, 70);\n"
                                        "border:none;\n"
                                        "font-size:15px;\n"
                                        "font-family: monaco,Console, Monospace;\n"
                                        "color:rgba(255, 255, 255, 230);\n"
                                        "border-radius:17px;\n"
                                        "padding-bottom:7px;")
        self.horas = QComboBox(self)
        self.horas.addItems(self.vec_hora)
        self.horas.setGeometry(QRect(100, 350, 100, 30))
        self.horas.setStyleSheet("background-color:rgba(0, 234, 162, 0.7);\n"
                                 "border-radius:5px;\n"
                                 "font-size:14px;\n"
                                 "font-family: monaco,Console, Monospace;\n")
        self.minutos = QLineEdit(self)
        self.minutos.setPlaceholderText('Minutos')
        self.minutos.setGeometry(QRect(210, 350, 100, 30))
        self.minutos.setStyleSheet("background-color:rgba(0, 234, 162, 0.7);\n"
                                   "border-radius:5px;\n"
                                   "font-size:14px;\n"
                                   "font-family: monaco,Console, Monospace;\n")
        self.formato_hora = QComboBox(self)
        self.formato_hora.addItem('AM')
        self.formato_hora.addItem('PM')
        self.formato_hora.setGeometry(QRect(320, 350, 100, 30))
        self.formato_hora.setStyleSheet("background-color:rgba(0, 234, 162, 0.7);\n"
                                        "border-radius:5px;\n"
                                        "font-size:14px;\n"
                                        "font-family: monaco,Console, Monospace;\n")
        self.calendario = QCalendarWidget(self)
        self.calendario.setGeometry(100, 400, 210, 185)
        self.calendario.setStyleSheet("background-color: #128C7E;\n"
                                      "border-radius:6px;\n"
                                      "font-size:14px;\n"
                                      "font-family: monaco,Console, Monospace;\n")
        self.frecuencia_mensaje = QComboBox(self)
        self.frecuencia_mensaje.addItems(self.frecu_men)
        self.frecuencia_mensaje.setGeometry(QRect(320, 400, 100, 30))
        self.frecuencia_mensaje.setStyleSheet("background-color:rgba(0, 234, 162, 0.7);\n"
                                              "border-radius:5px;\n"
                                              "font-size:14px;\n"
                                              "font-family: monaco,Console, Monospace;\n")

        self.buttonEnviar = QPushButton("Enviar mensaje", self)
        self.buttonEnviar.setGeometry(QRect(320, 450, 100, 70))
        self.buttonEnviar.setStyleSheet("background-color:rgba(0, 234, 162, 0.7);\n"
                                        "border-radius:5px;\n"
                                        "font-size:14px;\n"
                                        "font-family: monaco,Console, Monospace;\n")
        self.buttonEnviar.clicked.connect(self.btnEnviar)

        self.btn_pag = QPushButton(self)  # boton cambia de pagina
        self.btn_pag.setGeometry(0, 0, 75, 60)
        self.btn_pag.setStyleSheet("border-image: url(flecha.png);\n")

    def btnEnviar(self):
        dato_formato = self.formato_hora.currentText()
        dato_hora = self.horas.currentText()
        hor = ''
        min = ''
        dat_horacom = ''
        if dato_formato == 'PM':
            for i in range(0, 12):
                if self.vec_hora[i] == dato_hora:
                    hor = self.vec_horapm[i]
            min = self.minutos.text()
            dat_horacom = hor + ':' + min
            print(dat_horacom)
        if dato_formato == 'AM':
            for i in range(0, 12):
                if self.vec_hora[i] == dato_hora:
                    hor = self.vec_hora[i]
            min = self.minutos.text()
            dat_horacom = hor + ':' + min
            print(dat_horacom)
        # ? Extrae el numero teelfonico del destinatario
        a = self.qlinenumero.text()

        codigo = self.menunum.currentText()
        codigo = nums_from_string.get_nums(codigo)

        self.numero = "+" + str(codigo[0]) + a

        # ? Extrae el mensaje que se ha enviado
        self.mensaje = self.qlinemensaje.text()
        self.hora = int(hor)
        self.minute = int(min)
        
        try:
            # Enviamos el mensaje
            pywhatkit.sendwhatmsg(self.numero, self.mensaje, self.hora, self.minute)

            print("Mensaje Enviado")
        except:

            print("Ocurrio Un Error")
            
            
            


class Pag3(QWidget):
    def __init__(self,parent=None):
        super(Pag3, self).__init__(parent)
        self.labela1 = QLabel(self)
        self.labela1.setGeometry(QRect(0, 0, 650, 650))
        self.labela1.setStyleSheet("border-image: url(msg.jpeg);\n")


        self.codnum = ['Mishel Yucailla', 'Alexander Rodriguez', 'Leslie Tapia', 'Josue Gordillo', 'Katherin Silva',
                       'Damian Alban']
        self.idnum = ['100004132086504', '100015004271401', '100001974972378', '106420164089669', '100006749195844',
                      '100009631770613']
        self.vec_hora = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        self.vec_horapm = ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
        self.frecu_men = ['Diario', 'Pasando un día', 'Solo una vez', 'Cada semana', 'Cada mes']
        # self.resize(450, 550)
        self.setFixedSize(650, 650)

        self.Qlb_menu = QLabel('Amigos: ', self)
        self.Qlb_menu.setGeometry(100, 60, 60, 30)
        self.Qlb_menu.setStyleSheet("background-color: rgba(176, 38, 226, 0.7);\n"
                                    "border-radius:5px;\n"
                                    "font-size:14px;\n"
                                    "color:rgba(255, 255, 255, 230);\n"
                                    "font-family: monaco,Console, Monospace;\n")

        self.menunum = QComboBox(self)
        self.menunum.addItems(self.codnum)
        self.menunum.setGeometry(QRect(170, 60, 140, 30))
        self.menunum.setStyleSheet("background-color:rgba(176, 38, 226, 0.7);\n"
                                   "border-radius:5px;\n"
                                   "font-size:14px;\n"
                                   "color:rgba(255, 255, 255, 230);\n"
                                   "font-family: monaco,Console, Monospace;\n")

        self.setGeometry(QRect(30, 30, 650, 650))

        self.qlinemensaje = QLineEdit(self)
        self.qlinemensaje.setPlaceholderText("Ingrese su mensaje")
        self.qlinemensaje.setGeometry(QRect(100, 100, 400, 200))
        self.qlinemensaje.setStyleSheet("background-color:rgba(121, 6, 191, 0.6);\n"
                                        "border:none;\n"
                                        "font-size:15px;\n"
                                        "font-family: monaco,Console, Monospace;\n"
                                        "color:rgba(255, 255, 255, 230);\n"
                                        "border-radius:17px;\n"
                                        "padding-bottom:7px;")

        self.horas = QComboBox(self)
        self.horas.addItems(self.vec_hora)
        self.horas.setGeometry(QRect(100, 350, 100, 30))
        self.horas.setStyleSheet("background-color:rgba(66,80, 245, 0.8);\n"
                                 "border-radius:5px;\n"
                                 "font-size:14px;\n"
                                 "color:rgb(235, 229, 246);\n"
                                 "font-family: monaco,Console, Monospace;\n")

        self.minutos = QLineEdit(self)
        self.minutos.setPlaceholderText('Minutos')
        self.minutos.setGeometry(QRect(210, 350, 100, 30))
        self.minutos.setStyleSheet("background-color:rgba(66,80, 245, 0.8);\n"
                                   "border-radius:5px;\n"
                                   "font-size:14px;\n"
                                   "color:rgb(235, 229, 246);\n"
                                   "font-family: monaco,Console, Monospace;\n")

        self.formato_hora = QComboBox(self)
        self.formato_hora.addItem('AM')
        self.formato_hora.addItem('PM')
        self.formato_hora.setGeometry(QRect(320, 350, 100, 30))
        self.formato_hora.setStyleSheet("background-color:rgba(66,80, 245, 0.8);\n"
                                        "border-radius:5px;\n"
                                        "font-size:14px;\n"
                                        "color:rgb(235, 229, 246);\n"
                                        "font-family: monaco,Console, Monospace;\n")

        self.calendario = QCalendarWidget(self)
        self.calendario.setGeometry(100, 400, 200, 180)
        self.calendario.setStyleSheet("background-color: #6C78F8;\n"
                                      "border-radius:6px;\n"
                                      "font-size:14px;\n"
                                      "font-family: monaco,Console, Monospace;\n")

        self.frecuencia_mensaje = QComboBox(self)
        self.frecuencia_mensaje.addItems(self.frecu_men)
        self.frecuencia_mensaje.setGeometry(QRect(320, 400, 100, 30))
        self.frecuencia_mensaje.setGeometry(QRect(320, 400, 100, 30))
        self.frecuencia_mensaje.setStyleSheet("background-color:rgba(66,80, 245, 0.8);\n"
                                              "border-radius:5px;\n"
                                              "font-size:14px;\n"
                                              "color:rgb(235, 229, 246);\n"
                                              "font-family: monaco,Console, Monospace;\n")

        self.btenviar = QPushButton('Enviar', self)

        self.btenviar.setGeometry(320, 500, 100, 30)
        self.btenviar.setStyleSheet("background-color:rgba(66,80, 245, 0.8);\n"
                                    "border-radius:5px;\n"
                                    "font-size:14px;\n"
                                    "color:rgb(235, 229, 246);\n"
                                    "font-family: monaco,Console, Monospace;\n")

        self.btenviar.clicked.connect(self.automessage)
        
        

        self.btregre = QPushButton('',self)
        self.btregre.setGeometry(0,0,60,30)
        self.btregre.setStyleSheet("border-image: url(flecha.png);\n")
        
        
                
    def automessage(self): 
        try:
            #self.hora_formato()
            self.messageMsg = self.qlinemensaje.text()

            self.a = self.id_retornar()
            self.b = self.hora_formato()
            

            #*print(self.a)
            #*print(self.b)

            flag = 1

            # ids person target
            self.id = self.a

            # hour to be sended
            hour_to_send = self.b

            while flag:
                # hour actual
                hour = datetime.datetime.now().strftime('%I:%M')
                if hour == hour_to_send:
                    # send message and finish the program
                    flag = self.send()
        except:
            print("ocurrio un error al enviar mensaje messenger")
            
            
    def send(self):
    # open messenger
        webbrowser.open(f'https://www.messenger.com/t/{self.id}')

    # wait 5 seconds
        sleep(5)

    # send message
        pyautogui.typewrite(self.messageMsg)
        pyautogui.press("enter")
        return 0
        
        
    def id_retornar(self):
        dato = self.menunum.currentText()
        self.var = ''
        for i in range(0, 6):
            if self.codnum[i] == dato:
                self.var = self.idnum[i]
        return self.var        
       # self.labelid.setText(self.var) #!se envia el tetxo
        

    def hora_formato(self):
        dato_formato = self.formato_hora.currentText()
        dato_hora = self.horas.currentText()
        hor = ''
        min = ''
        self.dat_horacom = ''

        if dato_formato == 'PM':
            for i in range(0, 12):
                if self.vec_hora[i] == dato_hora:
                    hor = self.vec_hora[i]
            print(hor)
            min = self.minutos.text()
            print(min)
            self.dat_horacom = hor + ':' + min
            
            #?print(self.dat_horacom)
            return self.dat_horacom
        
        if dato_formato == 'AM':
            for i in range(0, 12):
                if self.vec_hora[i] == dato_hora:
                    hor = self.vec_hora[i]
            
            min = self.minutos.text()
            
            self.dat_horacom = hor + ':' + min
            return self.dat_horacom
           
            

class Pag4(QWidget):
    def __init__(self,parent=None):
        super(Pag4, self).__init__(parent)
        self.Qlfondo = QLabel(self)
        self.Qlfondo.setGeometry(0,0,650,650)
        self.Qlfondo.setStyleSheet('border-image: url(Fondo_p.jpg);')

        universidad = QLabel("<h1>UNIVERSIDAD TÉCNICA DE AMBATO</h1>", self)
        universidad.setGeometry(100,0,600,30)
        universidad.setStyleSheet("color:rgba(255, 255, 255, 230);")
        facultad = QLabel("<h2>FACULTAD DE INGENIERIA EN SISTEMAS</h2>", self)
        facultad.setGeometry(120, 30, 400, 30)
        facultad.setStyleSheet("color:rgba(255, 255, 255, 230);")
        materia = QLabel("<h3>PROGRAMACIÓN AVANZADA</h3>", self)
        materia.setGeometry(205, 60, 400, 30)
        materia.setStyleSheet("color:rgba(255, 255, 255, 230);")
        integrantes = QLabel("<h3>Integrantes:</h3>", self)
        integrantes.setGeometry(50, 90, 100, 30)
        integrantes.setStyleSheet("color:rgba(255, 255, 255, 230);")
        damian = QLabel("<h4>Damián Alban</h4>", self)
        damian.setGeometry(100, 110, 100, 30)
        damian.setStyleSheet("color:rgba(255, 255, 255, 230);")
        self.image = QLabel(self)
        self.image.setGeometry(160,250,250,250)
        self.image.setStyleSheet("border-image: url(logol.png);")




        self.btn_pag = QPushButton("Regresar al menu Principal",self)
                                                # Regresar al menu principal
        self.btn_pag.setGeometry(320,550,250,40)




class Aplicacion(QMainWindow):
    
    def __init__(self):
    
        super(Aplicacion, self).__init__()
        self.setFixedSize(650, 650)
        self.apilacion_widgets = QStackedWidget(self) # Creacion de aplicacion de widgets
        self.pag_1 = Principal()
        self.pag_2 = Pag2()
        self.pag_3 = Pag3()
        self.pag_4 = Pag4()
        
        self.apilacion_widgets.addWidget(self.pag_1)
        self.apilacion_widgets.addWidget(self.pag_2)
        self.apilacion_widgets.addWidget(self.pag_3)
        self.apilacion_widgets.addWidget(self.pag_4)
        #! Asiganr widget central a nuestra apilacion de widgets
        self.setCentralWidget(self.apilacion_widgets)
        #! Asinart como widget actual a pag1 
        self.apilacion_widgets.setCurrentWidget(self.pag_4)
        
        #! Llamamos al metodo inicializar
        self.inicializar()
        
        
    def inicializar(self):
        
        self.setWindowTitle("Programa Tu Mensaje")
        self.conexiones()  
            
    def usuario_wsp(self):
        usuario = self.pag_1.lineEdit.text()
        password= self.pag_1.lineEdit_2.text()
        
        if usuario!="" or password!="":
            if usuario == "User" and password=="Admin1":
                self.pag_1.labelBajo.setText("Usuario encontrado")
                self.pag_1.pushButton_2.clicked.connect(self.cambio_pag_2) 
                
            else: 
                self.pag_1.labelBajo.setText("Usuario no encontrado en WhatsApp")
        else: 
            self.pag_1.labelBajo.setText("Debe ingresar usuario para entrar a WhatsApp")
            
    def usuario_msg(self):
        usuario = self.pag_1.lineEdit.text()
        password= self.pag_1.lineEdit_2.text()
        if usuario!="" or password!="":
            if usuario == "User" and password=="Admin1":
                self.pag_1.labelBajo.setText("Usuario encontrado")
                self.pag_1.pushButton_3.clicked.connect(self.cambio_pag_3) 
                
            else: 
                self.pag_1.labelBajo.setText("Usuario no encontrado en Messenger")
        else: 
            self.pag_1.labelBajo.setText("Debe ingresar usuario para entrar a Messenger ")
        
        
    def conexiones(self):
        self.pag_1.pushButton_2.clicked.connect(self.usuario_wsp)   # me llama la funcion que extrae ell texto
        self.pag_2.btn_pag.clicked.connect(self.cambio_pag_1)
        self.pag_1.pushButton_3.clicked.connect(self.usuario_msg)
        self.pag_3.btregre.clicked.connect(self.cambio_pag_1)
        self.pag_4.btn_pag.clicked.connect(self.cambio_pag_1)
        
        
    def cambio_pag_2(self):
        self.apilacion_widgets.setCurrentWidget(self.pag_2) 
    
    def cambio_pag_1(self):
        self.apilacion_widgets.setCurrentWidget(self.pag_1) 
    
    def cambio_pag_3(self):
        self.apilacion_widgets.setCurrentWidget(self.pag_3)

    def cambio_pag_4(self):
        self.apilacion_widgets.setCurrentWidget(self.pag_4)
if __name__ == "__main__":
        app = QApplication([])
        ventana = Aplicacion()
        ventana.show()
        app.exec_()




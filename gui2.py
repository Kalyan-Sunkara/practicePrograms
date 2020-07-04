from PyQt5.QtWidgets import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.server = ''
        self.sending_email = ''
        self.recipient_list = []
        self.setWindowTitle('Emailer v.0.0')
        self.initUI()
        
    def sendMessage(self):
        mail_to_string = ', '.join(self.recipient_list)
        message1 = MIMEMultipart()
        message1['From'] = self.sending_email
        message1['To'] = mail_to_string
        message1['Subject'] = self.subject.text()
        message1.attach(MIMEText(self.message.toPlainText(), 'plain'))
        text = message1.as_string()
        self.server.sendmail(self.sending_email,self.recipient_list,text)
        self.recipient_list = []
        self.label9.setText('')
        self.recipients.setText('')
        self.subject.setText('')
        self.message.setPlainText('')
        
    def addRecipient(self):
        self.recipient_list.append(self.recipients.text())
        stringOfRecipients = ''
        for x in self.recipient_list:
            stringOfRecipients = stringOfRecipients + '\n' + x
        self.label9.setText(stringOfRecipients)
        
    def login(self):
        try:
            self.server = ''
            self.recipient_list = []
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.ehlo()
            self.server.starttls()
        except:
            self.label5.setText('Something occurred with the server')
            self.server.close()
        try:
            username = self.userNameField.text()
            password = self.passwordField.text()
            self.server.login(username, password)
            self.sending_email = username
            self.label5.setText('Login Succesful')
            self.label5.show()
            self.label6.show()
            self.label7.show()
            self.label8.show()
            self.label9.show()
            self.button4.show()
            self.recipients.show()
            self.subject.show()
            self.message.show()
            self.button3.show()
            self.button4.show()
            self.recipient_list = []
            self.label9.setText('')
            self.recipients.setText('')
            self.subject.setText('')
            self.message.setPlainText('')
            self.button2.setEnabled(False)
            self.button1.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.userNameField.setEnabled(False)
            self.passwordField.setEnabled(False)
        except:
            self.label5.setText('Retry Login')
            self.label5.show()
            self.server.close()
        
    def chooseServer(self,serverType):
        servers = ['Connecting to Gmail server...','Connecting to Outlook server...','Connecting to Yahoo server...']
        if serverType == 'Gmail':
            self.label3.hide()
            self.label4.hide()
            self.label5.hide()
            self.label9.hide()
            self.button4.hide()
            self.label5.setText('')
            self.button2.hide()
            self.userNameField.hide()
            self.passwordField.hide()
            self.label6.hide()
            self.label7.hide()
            self.label8.hide()
            self.button3.hide()
            self.recipients.hide()
            self.subject.hide()
            self.message.hide()
            self.userNameField.setText('')
            self.passwordField.setText('')
            self.label2.setText(servers[0])
            self.label3.show()
            self.label4.show()
            self.label5.show()
            self.button2.show()
            self.userNameField.show()
            self.passwordField.show()
        elif serverType == 'Outlook':
            self.label2.setText(servers[1])
            self.label3.hide()
            self.label4.hide()
            self.label5.hide()
            self.button2.hide()
            self.userNameField.hide()
            self.passwordField.hide()
            self.userNameField.setText('')
            self.passwordField.setText('')
        else:
            self.label2.setText(servers[2])
            self.label3.hide()
            self.label4.hide()
            self.label5.hide()
            self.button2.hide()
            self.userNameField.hide()
            self.passwordField.hide()
            self.userNameField.setText('')
            self.passwordField.setText('')
            
    def start_server(self):
        self.chooseServer(self.comboBox.currentText())
        
    def initUI(self):
        layout = QGridLayout()
        self.button1 = QPushButton('Launch Server', self)
        self.button2 = QPushButton('Login', self)
        self.button3 = QPushButton('Send', self)
        self.button4 = QPushButton('Add Recipient', self)

        self.comboBox = QComboBox()
        self.comboBox.addItems(['Gmail', 'Outlook', 'Yahoo'])

        self.label1 = QLabel('Choose server to connect to: ')
        self.label2 = QLabel('........')
        self.label3 = QLabel('Username: ',)
        self.label4 = QLabel('Password: ')
        self.label5 = QLabel('')
        self.label6 = QLabel('Enter recipients: ')
        self.recipients = QLineEdit()
        self.label7 = QLabel('Enter Subject: ')
        self.subject  = QLineEdit()
        self.label8 = QLabel('Enter Message: ')
        self.label9 = QLabel('')


        self.message = QPlainTextEdit()

        self.userNameField = QLineEdit()
        self.passwordField = QLineEdit()
        self.passwordField.setEchoMode(QLineEdit.Password)
        #comboBox.currentIndexChanged[str].connect(chooseServer(layout))
        layout.addWidget(self.label1,0,0)
        layout.addWidget(self.comboBox, 0, 1)
        layout.addWidget(self.button1, 0, 2)
        layout.addWidget(self.label5, 4,3)
        layout.addWidget(self.label3,2,0)
        layout.addWidget(self.label4,3,0)
        layout.addWidget(self.userNameField,2,1)
        layout.addWidget(self.passwordField,3,1)
        layout.addWidget(self.button2,3,3)
        layout.addWidget(self.label2,1,0)
        layout.addWidget(self.label6, 5, 0)
        layout.addWidget(self.label7,6, 0)
        layout.addWidget(self.label8,7,0)
        layout.addWidget(self.recipients,5,1)
        layout.addWidget(self.subject,6,1)
        layout.addWidget(self.message,7,1)
        layout.addWidget(self.button3,7,3)
        layout.addWidget(self.button4,5,2)
        layout.addWidget(self.label9, 5,3)
        
        self.button4.hide()
        self.label6.hide()
        self.label7.hide()
        self.label8.hide()
        self.label9.hide()
        self.recipients.hide()
        self.subject.hide()
        self.message.hide()
        self.label3.hide()
        self.label4.hide()
        self.label5.hide()
        self.button3.hide()
        self.button2.hide()
        self.userNameField.hide()
        self.passwordField.hide()
        #comboBox.currentTextChanged.connect(chooseServer)
        self.button1.clicked.connect(self.start_server)
        self.button2.clicked.connect(self.login)
        self.button3.clicked.connect(self.sendMessage)
        self.button4.clicked.connect(self.addRecipient)
        
        self.setLayout(layout)
        self.setStyleSheet("background-color: white;")
        self.show()
        
    
app = QApplication([])
app.setStyle('Fusion')
window = Window()
app.exec_()



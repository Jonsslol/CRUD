from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host= "local.host",
    user= "root",
    passwd= "",
    database= "funcionarios_"
)

def funcao_principal():
    linha1 = crud.lineEdit_2.text()
    linha2 = crud.lineEdit_3.text()
    linha3 = crud.lineEdit_4.text()
    
    contrato = ""
    
    if crud.radioButton.isChecked(): 
        print("PJ foi selecionado!")
        contrato="PJ"
    elif crud.radioButton_2.isChecked(): 
        print("CLT foi selecionado!")
        contrato="CLT"
    else:  
        print("Estagio foi selecionado!")
        contrato="Estagio"
        print("Nome:", linha1)
        print("Departamento:", linha2)
        print("CPF:", linha3)

        cursor = banco.cursor()
        comando_SQL = "INSERT INTO funcionarios_ (Nome,departamento,CPF,contrato) VALUES (%s, %s, %s, %s);"
        dados = (str(linha1), str(linha2), str(linha3), contrato)
        cursor.execute(comando_SQL,dados)
        banco.commit()

app=QtWidgets.QApplication([])
crud=uic.loadUi("crud.ui")
crud.pushButton.clicked.connect(funcao_principal)

crud.show()
app.exec()

# criando tabela
""" create table funcionarios_(id INT NOT NULL AUTO_INCREMENT,Nome VARCHAR(50),departamento VARCHAR(50),CPF DOUBLE,contrato VARCHAR(20),PRIMARY KEY (id));"""

#INSERT INTO funcionarios_ (Nome,departamento,CPF,contrato) VALUES ("JOAO","T.I",4848554466,"estagio");


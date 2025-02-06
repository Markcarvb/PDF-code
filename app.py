import pandas as pd
from fpdf import FPDF

dados = pd.read_csv("dados.csv")
#print(dados)

#dados do certificado
titulo ="Certificado de Participaçao"
subtitulo ="Este certificado comprava que"
texto2 ="concluiu com exito o curso GRATUITO DE PYTHON ministrado por"
texto3 = "Prof. Sauer entre xx/xx/xxxx e xx/xx/xxx"
texto4 ="com carga horaria de aproximadamente 08 horas"

for nomecompleto in dados ['nomecompleto']:

 pdf = FPDF()
 pdf.add_page()
 pdf.set_font("Arial", 'B', size=15)
 pdf.image("template.png",x=0, y=0) 
 pdf.set_text_color(33, 24, 136)

 pdf.text(65,95,titulo)
 pdf.text(67,120, subtitulo)
 pdf.text(70,145, nomecompleto)
 pdf.text(20,165, texto2)
 pdf.text(50,175, texto3)
 pdf.text(50,185, texto4)
 pdf.output(f"Certificado_{nomecompleto}.pdf")


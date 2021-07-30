from fpdf import FPDF
from datetime import date

b=open('Names.txt','r');b_F=b.read();each_line_b=b_F.split('\n')
for k in range(0,len(each_line_b)):
    day_T=date.today()
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 10)
    file=''
    a=open('Master_T.txt','r');a_F=a.read();each_line_a=a_F.split('\n')
    for i in range(0,len(each_line_a)-1):
        if("Date" in each_line_a[i]):
            each_line_a[i]=each_line_a[i]+' : '+str(day_T)
        if("Recipient's Name" in each_line_a[i]):
            each_line_a[i]=each_line_a[i].replace("Recipient's Name",each_line_b[k])
        file=file+each_line_a[i]+'\n'
        pdf.cell(200, 10, txt = each_line_a[i]+'\n', ln = i, align = 'L')
    #pdf.cell(200, 10, txt = file, ln = 1, align = 'L')
    print(file)
    pdf.output(each_line_b[k]+'_Offer_Letter.pdf')
    pdf.close()
    print('===================================================================================\n')

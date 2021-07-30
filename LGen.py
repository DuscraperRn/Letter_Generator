import docx

my_doc=docx.Document('Master_APR.docx')
all_paras = my_doc.paragraphs
name=''
#for para in all_paras:
#    print(para.text)
for i in range(0,len(all_paras)):
    print(all_paras[i].text);print(i)
    print('----------------------')

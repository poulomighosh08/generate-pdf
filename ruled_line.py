from fpdf import FPDF
import pandas

pdf = FPDF(orientation='P', unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin = 0)

df = pandas.read_csv('topics.csv')

for index, rows in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 12, txt=rows["Topic"], ln=1)

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    #Footer
    pdf.ln(265)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 10, txt=rows["Topic"], ln=0, align='R')


    for i in range(rows["Pages"]):
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 12, txt=rows["Topic"], ln=1)
        pdf.line(x1=10, y1=22, x2=230, y2=22)

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # Footer
        pdf.ln(265)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 10, txt=rows["Topic"], ln=0, align='R')

pdf.output('new_ruled.pdf')

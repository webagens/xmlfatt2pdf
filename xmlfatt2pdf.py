# Richiede installazione di wkhtmltopdf.exe

import os
import sys
import subprocess
from lxml import etree

# Percorso al foglio di stile XSL
XSL_FILE = os.path.join(os.path.dirname(__file__), "FoglioStileAssoSoftware.xsl")

# Percorso a wkhtmltopdf.exe (modifica se diverso)
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

def applica_xsl(xml_path, xsl_path):
    with open(xml_path, 'rb') as f_xml, open(xsl_path, 'rb') as f_xsl:
        dom = etree.parse(f_xml)
        xslt = etree.XSLT(etree.parse(f_xsl))
        result = xslt(dom)
        return str(result)

def salva_html(html_content, output_html_path):
    # Assicura che abbia il charset utf-8 nel <head>
    if '<head>' in html_content:
        html_content = html_content.replace('<head>', '<head><meta charset="utf-8">', 1)
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def converti_html_in_pdf(input_html, output_pdf):
    subprocess.run([
        WKHTMLTOPDF_PATH,
        input_html,
        output_pdf
    ], check=True)

def main():
    if len(sys.argv) != 2:
        print("Uso: python converti_fattura.py <percorso_fattura.xml>")
        sys.exit(1)

    xml_path = sys.argv[1]
    if not os.path.isfile(xml_path):
        print(f"File non trovato: {xml_path}")
        sys.exit(1)

    print("Applico foglio di stile...")
    html = applica_xsl(xml_path, XSL_FILE)
    html = html.replace('max-width: 1280px;', 'max-width: 100%;')
    html = html.replace('width: 800px;', 'width: 100%;')


    output_html = os.path.splitext(xml_path)[0] + ".html"
    output_pdf = os.path.splitext(xml_path)[0] + ".pdf"

    print("Salvo HTML...")
    salva_html(html, output_html)

    print("Genero PDF...")
    converti_html_in_pdf(output_html, output_pdf)

    print(f"PDF creato: {output_pdf}")

    try:
        os.remove(output_html)
        print(f"HTML temporaneo rimosso: {output_html}")
    except Exception as e:
        print(f"Impossibile eliminare l'HTML: {e}")


if __name__ == "__main__":
    main()

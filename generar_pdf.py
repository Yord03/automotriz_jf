from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def crear_presupuesto_pdf(nombre_archivo, datos_cliente, datos_auto, trabajos):
    # Estrofa 1: Configuración de la hoja física
    doc = SimpleDocTemplate(
        nombre_archivo,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )
    
    story = []

    # Estrofa 2: Creación de los estilos de letra
    estilos = getSampleStyleSheet()
    
    estilo_titulo = ParagraphStyle(
        'Tit', 
        parent=estilos['Heading1'], 
        fontName='Helvetica-Bold', 
        fontSize=22, 
        textColor=colors.HexColor("#1A365D"), 
        spaceAfter=5
    )
    estilo_seccion = ParagraphStyle(
        'Sec', 
        parent=estilos['Heading2'], 
        fontName='Helvetica-Bold', 
        fontSize=14, 
        textColor=colors.HexColor("#2B6CB0"), 
        spaceAfter=8
    )
    estilo_texto = estilos['Normal']

    # Estrofa 3: Agregar datos de la Empresa y del Cliente
    story.append(Paragraph("JF AUTOMOTRIZ", estilo_titulo))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("DATOS DEL CLIENTE", estilo_seccion))
    info_cliente = (
        f"<b>Cliente:</b> {datos_cliente['nombre']}<br/>"
        f"<b>RUT:</b> {datos_cliente['rut']}<br/>"
        f"<b>Teléfono:</b> {datos_cliente['telefono']}"
    )
    story.append(Paragraph(info_cliente, estilo_texto))
    story.append(Spacer(1, 15))

    # NUEVA ESTROFA: Aquí es donde usamos la variable datos_auto para el PDF
    story.append(Paragraph("DESCRIPCIÓN DEL AUTO", estilo_seccion))
    info_auto = (
        f"<b>Marca:</b> {datos_auto['marca']}<br/>"
        f"<b>Modelo:</b> {datos_auto['modelo']}<br/>"
        f"<b>Patente:</b> {datos_auto['patente']}<br/>"
        f"<b>Color:</b> {datos_auto['color']}"
    )
    story.append(Paragraph(info_auto, estilo_texto))
    story.append(Spacer(1, 15))

    # Estrofa 4: Crear la estructura de la matriz para la tabla
    tabla_datos = [['N°', 'Descripción del Trabajo']]
    
    for i, trabajo in enumerate(trabajos, start=1):
        tabla_datos.append([str(i), trabajo])
        
    tabla = Table(tabla_datos, colWidths=[40, 450])

    # Estrofa 5: Aplicar diseño visual, colores y líneas a la tabla
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1A365D")), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),          
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),                        
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),            
        ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey)             
    ]))
    
    # Estrofa 6: Meter la tabla terminada a la bandeja y construir el PDF
    story.append(tabla)
    doc.build(story)
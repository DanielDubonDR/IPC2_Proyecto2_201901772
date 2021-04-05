
import os

def reporte1(listaLogs):
    string=""
    string+='''
    <!DOCTYPE html>
    <html>
    <title>Reporte Logs</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lobster">
    <style>
    .w3-lobster {
        font-family: "Lobster", serif;
    }
    </style>

    <body>
    <div class="w3-container w3-teal w3-center w3-margin-bottom">
        <br><br>
        <h1 class="w3-lobster w3-xxxlarge">Reporte</h1>
        <br><br>
    </div>
    
    <div class="w3-container w3-center">
        <div class="w3-container w3-lobster">
        <p class="w3-xxxlarge">Estado de las matrices<p>
        </div>
        <table class="w3-table-all w3-margin-top w3-card-4 w3-hoverable">
        <tr class="w3-black">
            <th style="width:20%;" class="w3-center">Fecha</th>
            <th style="width:20%;" class="w3-center">Hora</th>
            <th style="width:20%;" class="w3-center">Nombre</th>
            <th style="width:20%;" class="w3-center">Espacios llenos</th>
            <th style="width:20%;" class="w3-center">Espacios vacíos</th>
        </tr>
        
    '''
    for i in listaLogs.iterar():
        if i.dato.id==1:
            string+="<tr><td class=\"w3-center\">"+str(i.dato.fecha)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.hora)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.nombre)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.ELlenos)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.EVacios)+"</td></tr>"

    string+='''
    </table>
    </div><br><br>
    </body>
    </html>
    '''
    path=os.getcwd()+"/Reportes/Reporte.html"
    arhcivo=open(path,'w', encoding='utf8')
    arhcivo.write(string)
    arhcivo.close()
    os.startfile(path)


def reporte2(listaLogs):
    string=""
    string+='''
    <!DOCTYPE html>
    <html>
    <title>Reporte Logs</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lobster">
    <style>
    .w3-lobster {
        font-family: "Lobster", serif;
    }
    </style>

    <body>
    <div class="w3-container w3-teal w3-center w3-margin-bottom">
        <br><br>
        <h1 class="w3-lobster w3-xxxlarge">Reporte</h1>
        <br><br>
    </div>
    
    <div class="w3-container w3-center">
        <div class="w3-container w3-lobster">
        <p class="w3-xxxlarge">Estado de las matrices<p>
        </div>
        <table class="w3-table-all w3-margin-top w3-card-4 w3-hoverable">
        <tr class="w3-black">
            <th style="width:20%;" class="w3-center">Fecha</th>
            <th style="width:20%;" class="w3-center">Hora</th>
            <th style="width:20%;" class="w3-center">Nombre</th>
            <th style="width:20%;" class="w3-center">Espacios llenos</th>
            <th style="width:20%;" class="w3-center">Espacios vacíos</th>
        </tr>
        
    '''
    for i in listaLogs.iterar():
        if i.dato.id==1:
            string+="<tr><td class=\"w3-center\">"+str(i.dato.fecha)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.hora)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.nombre)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.ELlenos)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.EVacios)+"</td></tr>"

    string+='''
    </table>
   </div><br><br>

  <div class="w3-container w3-center">
    <div class="w3-container w3-lobster">
      <p class="w3-xxxlarge">Operaciones realizadas<p>
    </div>
    <table class="w3-table-all w3-margin-top w3-card-4 w3-hoverable">
      <tr class="w3-deep-purple">
        <th style="width:25%;" class="w3-center">Fecha</th>
        <th style="width:25%;" class="w3-center">Hora</th>
        <th style="width:25%;" class="w3-center">Tipo de operación</th>
        <th style="width:25%;" class="w3-center">Matrices</th>
      </tr>
    '''
    for i in listaLogs.iterar():
        if i.dato.id==2:
            string+="<tr><td class=\"w3-center\">"+str(i.dato.fecha)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.hora)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.operacion)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.nombre)+"</td></tr>"

    string+='''
    </table>
  </div><br><br>

  <div class="w3-container w3-center">
    <div class="w3-container w3-lobster">
      <p class="w3-xxxlarge">Errores<p>
    </div>
    <table class="w3-table-all w3-margin-top w3-card-4 w3-hoverable">
      <tr class="w3-pink">
        <th style="width:20%;" class="w3-center">Fecha</th>
        <th style="width:20%;" class="w3-center">Hora</th>
        <th style="width:20%;" class="w3-center">Error</th>
        <th style="width:25%;" class="w3-center">Tipo de operación</th>
        <th style="width:25%;" class="w3-center">Matrices</th>
      </tr>
    '''
    for i in listaLogs.iterar():
        if i.dato.id==3:
            string+="<tr><td class=\"w3-center\">"+str(i.dato.fecha)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.hora)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.descripcion)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.operacion)+"</td>"
            string+="<td class=\"w3-center\">"+str(i.dato.nombre)+"</td></tr>"

    string+='''
    </table>
    </div><br><br>
    </body>
    </html>
    '''

    path=os.getcwd()+"/Reportes/Reporte.html"
    arhcivo=open(path,'w', encoding='utf8')
    arhcivo.write(string)
    arhcivo.close()
    os.startfile(path)
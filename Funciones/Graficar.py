from graphviz import Digraph

def graficarM(m):
    string=""
    s = Digraph('structs', node_attr={'shape': 'plaintext'})
    #s.attr(rankdir="RL")
    #s.node("z","matriz")
    string+='''<\n<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="7">'''
    filas=int(m.nFila)
    columnas=int(m.nColumna)
    string+='''<TR>
    <TD border="0">M1</TD>'''
    for cc in range(columnas):
        string+="\n<TD border=\"0\">"+str(cc+1)+"</TD>"
       
    string+="\n</TR>"
    
    for i in range(1,filas+1):
        string+='''\n<TR>
        <TD border="0">'''+str(i)+'''</TD>'''
        for j in range(1,columnas+1):
            encontrado=False
            for aux in m.matriz.iterarFilas():
                if aux.f==i and aux.c==j:
                    encontrado=True
            if encontrado==True:
                string+="\n<TD bgcolor=\"black\">*</TD>"
            else:
                string+="\n<TD>   </TD>"
        string+="</TR>"
    string+="</TABLE>>"
    s.node('struct3', string)
    print(s.source)

    s.render('D://test-output/round-table.gv', view=True, format="png")
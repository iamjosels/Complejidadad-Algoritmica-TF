import csv
import Peliculas as p
import Grafo as g
import os
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import queue
from collections import deque

print(os.getcwd())
arreglov = []
Peliculas = []
Grafo = g.Grafo()

def lectura():
    with open('database/netflix_titles.csv', newline='', encoding='utf-8') as csvfile: # Archivo
        reader = csv.reader(csvfile)
        cabecera = next(reader)  
        datos = [fila for fila in reader]
        for i in range(5000): 
            pelicula = p.Pelicula(i, datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], datos[i][6], datos[i][7], datos[i][8], datos[i][9], datos[i][10], datos[i][11])
            Peliculas.append(pelicula)
            Grafo.agregar_nodo(i)

def sumatoria(a,b):
    valor=0
    if Peliculas[a]._director != '' and Peliculas[a]._director==Peliculas[b]._director:
        valor+=9 
    if Peliculas[a]._type != '' and Peliculas[a]._type == Peliculas[b]._type:
        valor+=4
    if Peliculas[a]._rating != '' and Peliculas[a]._rating== Peliculas[b]._rating:
        valor+=3
    if Peliculas[a]._release_year != '' and Peliculas[a]._release_year==Peliculas[b]._release_year:
        valor+=5
    if len(Peliculas[a]._cast) >= 1 and Peliculas[a]._cast[0] != '':
        valor+=3*len(set(Peliculas[a]._cast).intersection(Peliculas[b]._cast))
    if len(Peliculas[a]._listed_in) >= 1 and Peliculas[a]._listed_in[0] != '':
        valor+=3*len(set(Peliculas[a]._listed_in).intersection(Peliculas[b]._listed_in))

    return valor

def peli(value):
    for i in range(5000):
        if value==Peliculas[i].title:
            return i
def iteracionuna(id):
    arreglototal = []
    for i in range(5000):
        sumanodo = 0
        sumanodo += sumatoria(id, i)
        if sumanodo > 0:
            Grafo.agregar_arista(id, i, sumanodo)
            arreglototal.append(i)
    return arreglototal

def filtrar_peliculas(generos=None, rating=None, tipo=None, pais=None, fecha=None, arreglo=None):
    filtro = []
    for nodo in arreglo:
        validez = True
        if rating is not None and Peliculas[nodo]._rating != rating:
            validez = False
        if tipo is not None and Peliculas[nodo]._type != tipo:
            validez = False
        if fecha is not None and Peliculas[nodo]._release_year != fecha:
            validez = False
        if generos is not None and generos:
            if not set(Peliculas[nodo]._listed_in).intersection(generos):
                validez = False
        if pais is not None and pais:
            if not set(Peliculas[nodo]._country).intersection(pais):
                validez = False
        if validez:
            filtro.append(nodo)
    return filtro

def maxtf(valor, arreglo,cantidad):
    arreglomax = []
    for nodo in arreglo:
        peso = Grafo.obtener_peso_aristas(valor, nodo)
        if peso is not None:
            arreglomax.append(nodo)
    
    arreglomax.sort(reverse=True)  
    return arreglomax[:cantidad]



def pesosentrenodos(arr_ids):
    for i in range(len(arr_ids)):
        for j in range(i + 1, len(arr_ids)):
            peso = sumatoria(arr_ids[i], arr_ids[j])
            if peso > 0:
                Grafo.agregar_arista(arr_ids[i], arr_ids[j], peso)

def dibujargrafo(arreglo, inicial):
    dibujog = nx.Graph()
    for i in range(len(arreglo)):
        dibujog.add_node(Peliculas[arreglo[i]]._title)
    dibujog.add_node(Peliculas[inicial]._title)
    for i in range(len(arreglo)):
        for j in range(len(arreglo)):
            peso = Grafo.obtener_peso_aristas(inicial, arreglo[j])
            if peso is not None:
                dibujog.add_edge(Peliculas[inicial]._title, Peliculas[arreglo[j]]._title, weight=peso)
    pos = nx.spring_layout(dibujog)
    edges = dibujog.edges()
    weights = nx.get_edge_attributes(dibujog, 'weight')
    nx.draw_networkx(dibujog, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(dibujog, pos, edge_labels=weights)
    plt.show()

def bfs_peliculas_sim(pelicula_ini, num_pelis):
    visitados = set()
    pesos = {}  # Diccionario para almacenar los pesos de las películas relacionadas
    cola = deque()
    cola.append((pelicula_ini, 0))

    while cola and len(pesos) < num_pelis:
        pelicula_actual, distancia = cola.popleft()
        if pelicula_actual not in visitados:
            visitados.add(pelicula_actual)
            peli_sig = Grafo.obtener_pel_sig(pelicula_actual)

            for siguiente in peli_sig:
                peso = Grafo.obtener_peso_aristas(pelicula_actual, siguiente)
                if siguiente not in visitados and peso > 0:  # Ignorar si el peso es 0 (no hay conexión)
                    cola.append((siguiente, distancia + peso))
                    if siguiente not in pesos or peso > pesos[siguiente]:
                        pesos[siguiente] = peso

    peliculas_mas_relacionadas = sorted(pesos.keys(), key=lambda x: pesos[x], reverse=True)
    devuelve_nombres(peliculas_mas_relacionadas[:num_pelis])
    return peliculas_mas_relacionadas[:num_pelis]

def devuelve_nombres(peli_rel):
    for i in peli_rel:
        print(Peliculas[i]._title)

def dibujargrafosa(arreglo):
    dibujog = nx.Graph()
    for i in range(len(arreglo)):
        dibujog.add_node(Peliculas[arreglo[i]]._title)
    for i in range(len(arreglo)):   
        for j in range(len(arreglo)):
            peso = Grafo.obtener_peso_aristas(arreglo[i], arreglo[j])
            if peso is not None:
                dibujog.add_edge(Peliculas[arreglo[i]]._title, Peliculas[arreglo[j]]._title, weight=peso)
    pos = nx.spring_layout(dibujog)
    edges = dibujog.edges()
    weights = nx.get_edge_attributes(dibujog, 'weight')
    nx.draw_networkx(dibujog, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(dibujog, pos, edge_labels=weights)
    plt.show()

generos = [
    'Korean TV Shows',
    'Teen TV Shows',
    'Sci-Fi & Fantasy',
    'Crime TV Shows',
    'Romantic Movies',
    'International Movies',
    'Cult Movies',
    'Action & Adventure',
    'Independent Movies',
    'Sports Movies',
    'Dramas',
    'Music & Musicals',
    'Horror Movies',
    "Kids' TV",
    'Comedies',
    'TV Action & Adventure',
    'Spanish-Language TV Shows',
    'TV Comedies',
    'TV Thrillers',
    'British TV Shows',
    'International TV Shows',
    'Children & Family Movies',
    'TV Shows',
    'TV Sci-Fi & Fantasy',
    'Movies',
    'Romantic TV Shows',
    'Science & Nature TV',
    'Faith & Spirituality',
    'LGBTQ Movies',
    'TV Dramas',
    'TV Mysteries',
    'Classic Movies',
    'Classic & Cult TV',
    'Thrillers',
    'Reality TV',
    'Documentaries',
    'Stand-Up Comedy',
    'Stand-Up Comedy & Talk Shows',
    'Docuseries',
    'Anime Features',
    'TV Horror',
    'Anime Series'
]

paises = [
    'Vietnam',
    'Morocco',
    'Malta',
    'Senegal',
    'Iceland',
    'Australia',
    'United States',
    'Romania',
    'Philippines',
    'Cayman Islands',
    'Ecuador',
    'Taiwan',
    'Finland',
    'Botswana',
    'Mauritius',
    'Syria',
    'Netherlands',
    'Indonesia',
    'Ethiopia',
    'Colombia',
    'Mozambique',
    'United Arab Emirates',
    'Cyprus',
    'Poland',
    'France',
    'Puerto Rico',
    'Ukraine',
    'Zimbabwe',
    'Croatia',
    'Kazakhstan',
    'Jamaica',
    'South Africa',
    'Venezuela',
    'Sweden',
    'Hungary',
    'Panama',
    'Azerbaijan',
    'Luxembourg',
    'Argentina',
    'Spain',
    'Samoa',
    'Slovenia',
    'Bulgaria',
    'Kenya',
    'Bermuda',
    'Burkina Faso',
    'South Korea',
    'Sri Lanka',
    'Saudi Arabia',
    'Iraq',
    'Bahamas',
    'Somalia',
    'Albania',
    'Denmark',
    'Chile',
    'Lithuania',
    'Greece',
    'Turkey',
    'Norway',
    'East Germany',
    'Algeria',
    'Cameroon',
    'Serbia',
    'Dominican Republic',
    'Israel',
    'Germany',
    'Mexico',
    'Nigeria',
    'Thailand',
    'Czech Republic',
    'Guatemala',
    'Iran',
    'Soviet Union',
    'Malaysia',
    'Armenia',
    'Montenegro',
    'Poland,',
    'Bangladesh',
    'Angola',
    'Namibia',
    'Kuwait',
    'Paraguay',
    'United States,',
    'Belarus',
    'Brazil',
    'Pakistan',
    'Egypt',
    'Canada',
    'Ireland',
    'Singapore',
    'Jordan',
    'Nicaragua',
    'Uruguay',
    'Ghana',
    'Afghanistan',
    'Cambodia',
    'Malawi',
    'New Zealand',
    'Latvia',
    'Peru',
    'Cuba',
    'Sudan',
    'India',
    'Russia',
    'China',
    'Nepal',
    'United Kingdom,',
    'Uganda',
    'West Germany',
    'Lebanon',
    'United Kingdom',
    'Vatican City',
    'Austria',
    'Georgia',
    'Portugal',
    'Palestine',
    'Slovakia',
    'Cambodia,',
    'Japan',
    'Italy',
    'Hong Kong',
    'Liechtenstein',
    'Belgium',
    'Mongolia',
    'Qatar',
   'Switzerland'
]

rating = [
    'TV-MA',
    'R',
    'TV-Y7-FV',
    'NR',
    'TV-Y',
    'TV-G',
    'UR',
    'NC-17',
    'TV-PG',
    'PG-13',
    'G',
    'TV-Y7',
    'TV-14',
    'PG'
]
anios = [
    '1993', '1986', '1942', '2019', '2001', '1994', '2013', '2011', '1989', '2010', '2016', '1962', '1967', '2005',
    '2015', '1988', '1973', '1979', '2003', '2007', '1981', '1925', '1965', '1958', '1999', '1961', '1974', '1955',
    '1969', '1983', '1947', '1976', '1946', '1943', '1995', '2006', '1956', '1966', '1971', '2002', '1997', '1963',
    '1972', '2020', '2017', '1985', '1987', '1984', '1945', '2004', '1960', '2021', '1970', '2012', '2009', '1991',
    '1998', '1992', '1954', '1964', '1996', '2018', '2014', '2008', '1982', '1977', '1975', '1959', '1944', '1980',
    '1990', '2000', '1978', '1968'
]

lectura()
gn=ra=ti=pa=fe=None
cantidadra=10
def buscar_peliculas():
    global gn,ra,ti,pa,fe,cantidadra
    resultado_busqueda.delete(*resultado_busqueda.get_children())  
    generos = [entrada_generos.get()] if entrada_generos.get() else None
    rating = entrada_rating.get() if entrada_rating.get() else None
    tipo = entrada_tipo.get() if entrada_tipo.get() else None
    pais = [entrada_pais.get()] if entrada_pais.get() else None
    fecha = entrada_fecha.get() if entrada_fecha.get() else None
    gn=generos
    ra=rating
    ti=tipo
    pa=pais
    fe=fecha

    peliculas_filtradas = filtrar_peliculas(generos, rating, tipo, pais, fecha, range(5000))
    print(gn,ra,ti,pa,fe,cantidadra)
    cantidad_impresiones = int(entrada_cantidad.get())
    cantidadra=cantidad_impresiones
    titulo_parcial = entrada_titulo.get()
    print(gn,ra,ti,pa,fe,cantidadra)
    contador_impresiones = 0
    for pelicula_id in peliculas_filtradas:
        if contador_impresiones >= cantidad_impresiones:
            break
        if Peliculas[pelicula_id].title.startswith(titulo_parcial):
            resultado_busqueda.insert("", tk.END, text=Peliculas[pelicula_id]._showid, values=(Peliculas[pelicula_id].title,))
            contador_impresiones += 1


def obtener_id_seleccionado(event):
    global gn,ra,ti,pa,fe,cantidadra
    item_seleccionado = resultado_busqueda.focus()
    id_pelicula = resultado_busqueda.item(item_seleccionado)['values'][0]
    pelicula = Peliculas[peli(id_pelicula)]
    ventana_pelicula = tk.Toplevel(ventana)
    ventana_pelicula.title("Movie Details")
    ventana_pelicula.iconbitmap("img/logo2.ico")
    ventana_pelicula.geometry("700x400")
    pelicula = Peliculas[peli(id_pelicula)]
    descripcion_formateada = '\n'.join([pelicula.description[i:i+50] for i in range(0, len(pelicula.description), 50)])
    cast='\n'.join([pelicula.cast_members[i:i+50] for i in range(0, len(pelicula.cast_members), 50)])
    etiqueta_valores = tk.Label(ventana_pelicula, text=f"Valores de la película con ID {peli(id_pelicula)}:\n"
                                               f"ID: {pelicula.showid}\n"
                                               f"Tipo: {pelicula.type}\n"
                                               f"Título: {pelicula.title}\n"
                                               f"Director: {pelicula.director}\n"
                                               f"Miembros del reparto: {cast}\n"
                                               f"País: {', '.join(pelicula.country)}\n"
                                               f"Fecha de agregado: {pelicula.date_added}\n"
                                               f"Año de lanzamiento: {pelicula.release_year}\n"
                                               f"Rating: {pelicula.rating}\n"
                                               f"Duración: {pelicula.duration}\n"
                                               f"Género: {pelicula.listed_in}\n"
                                               f"Descripción: {descripcion_formateada}",justify="left")

    etiqueta_valores.place(x=10,y=10)
    # Arreglo de peliculas generales relacionadas
    peliculas_mayor_peso = iteracionuna(peli(id_pelicula))
    peliculas_filtro=bfs_peliculas_sim(peli(id_pelicula),20)
    print(peliculas_filtro)
    variaspeliculas = "" 
    for pelicula_id in peliculas_filtro:
        titulo_pelicula = Peliculas[pelicula_id].title
        variaspeliculas += titulo_pelicula + "\n"
    etiqueta_peliculas_mayor_peso = tk.Label(ventana_pelicula, text=variaspeliculas,justify="left")
    etiqueta_peliculas_mayor_peso.place(x=420, y=30)
    titul=tk.Label(ventana_pelicula,text="Peliculas Recomendadas")
    titul.place(x=500,y=10)
    
    
    def dibujar_grafo():
        global peliculas_filtro
        print(peliculas_filtro)
        pesosentrenodos(peliculas_filtro)
        dibujargrafosa(peliculas_filtro)
        pass

    def actualizar():
        global gn,ra,ti,pa,fe,cantidadra,peliculas_filtro
        contador=0
        if cantidadra>24:
            cantidadra=24
        print(gn,ra,ti,pa,fe,cantidadra)
        arreglox = iteracionuna(peli(id_pelicula))#
        peliculas=filtrar_peliculas(gn,ra,ti,pa,fe,arreglox)
        print(len(peliculas))
        peliculafiltrado=maxtf(peli(id_pelicula),peliculas,cantidadra)
        print(len(peliculafiltrado))
        
        etiqueta_peliculas_mayor_peso.place_forget()
        variaspeliculas2 =""
        for pelicula_id in peliculafiltrado:
            if contador >= cantidadra:
                break
            titulo_pelicula = Peliculas[pelicula_id].title
            variaspeliculas2 += titulo_pelicula + "\n"
            contador+=1
            pass
        peliculas_filtro=peliculafiltrado
        peliculas_filtro.append(peli(id_pelicula))
        print(peliculas_filtro)
        etiqueta_peliculas_mayor_peso.config(text=variaspeliculas2)
        etiqueta_peliculas_mayor_peso.place(x=420, y=30)
        boton_dibujar_grafo.place(x=300,y=300)

    boton_dibujar_grafo = tk.Button(ventana_pelicula, text="Dibujar Grafo", command=dibujar_grafo)
    
    boton_actualizar_grafo=tk.Button(ventana_pelicula, text="Actualizar", command=actualizar)
    boton_actualizar_grafo.place(x=300,y=350)
    ventana_pelicula.mainloop()

ventana = tk.Tk()
ventana.title("Look4Movie")
ventana.iconbitmap("img/logo.ico")
ventana.geometry("700x500")

marco_principal = tk.Frame(ventana)
marco_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


marco_filtros = tk.Frame(marco_principal)
marco_filtros.pack(side=tk.RIGHT, padx=10)

etiqueta_generos = tk.Label(marco_filtros, text="Géneros:")
etiqueta_generos.pack()
entrada_generos = ttk.Combobox(marco_filtros, values=generos)
entrada_generos.pack(pady=5)

etiqueta_rating = tk.Label(marco_filtros, text="Rating:")
etiqueta_rating.pack()
entrada_rating = ttk.Combobox(marco_filtros, values=rating)
entrada_rating.pack(pady=5)

etiqueta_tipo = tk.Label(marco_filtros, text="Tipo:")
etiqueta_tipo.pack()
entrada_tipo = ttk.Combobox(marco_filtros, values=['Movie', 'TV Show'])
entrada_tipo.pack(pady=5)

etiqueta_pais = tk.Label(marco_filtros, text="País:")
etiqueta_pais.pack()
entrada_pais = ttk.Combobox(marco_filtros, values=paises)
entrada_pais.pack(pady=5)

etiqueta_fecha = tk.Label(marco_filtros, text="Fecha:")
etiqueta_fecha.pack()
entrada_fecha = ttk.Combobox(marco_filtros, values=anios)
entrada_fecha.pack(pady=5)

etiqueta_titulo = tk.Label(marco_filtros, text="Título parcial:")
etiqueta_titulo.pack()
entrada_titulo = tk.Entry(marco_filtros)
entrada_titulo.pack(pady=5)
def validar_cantidad_ingresada():
    cantidad = entrada_cantidad.get()
    if not cantidad.isdigit():
        entrada_cantidad.delete(0, tk.END)  

entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.pack(pady=10)
entrada_cantidad.insert(tk.END, "2000")
entrada_cantidad.bind("<KeyRelease>", lambda event: validar_cantidad_ingresada())
boton_buscar = ttk.Button(marco_filtros, text="Buscar", command=buscar_peliculas)
boton_buscar.pack(pady=10)
marco_resultados = tk.Frame(marco_principal)
marco_resultados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
etiqueta_resultado = tk.Label(marco_resultados, text="Resultados de Búsqueda:")
etiqueta_resultado.pack()
resultado_busqueda = ttk.Treeview(marco_resultados, columns=("ID"), show="headings")
resultado_busqueda.heading("ID", text="Peliculas")
resultado_busqueda.bind("<Double-1>", obtener_id_seleccionado)
resultado_busqueda.pack(fill=tk.BOTH, expand=True)
ventana.mainloop()

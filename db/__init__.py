import sqlite3

def get_db_connection():
    return sqlite3.connect('electrodomesticos.db')

def table_exists():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='productos'")
    result = cursor.fetchone()

    return result is not None

def createTabla():

    conn = sqlite3.connect('electrodomesticos.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price FLOAT NOT NULL,
            images TEXT
        )
    ''')
    
    cursor.executemany("INSERT INTO productos (title, price, images) VALUES (?, ?, ?)", [
        ('colchon holliwod ortopedico  120x190', 890000, 'https://imagedelivery.net/4fYuQyy-r8_rpBpcY7lH_A/sodimacCO/272400/w=1036,h=832,f=webp,fit=contain,q=85'),
        ('protector colchon 120 tela', 750000, 'https://m.media-amazon.com/images/I/810Kq8+YGvL._AC_SL1500_.jpg'),
        ('protector colchon tela sencillo47010', 58000, 'https://m.media-amazon.com/images/I/71mZE03JefL._AC_SL1500_.jpg'),
        ('protector colchon plastico 120 ref47003', 42000, 'https://m.media-amazon.com/images/I/71+OAUUirGL._AC_SY300_SX300_.jpg'),
        ('iPhone 13', 506000, 'https://co.tiendasishop.com/cdn/shop/files/IMG-4624098_d742ac86-40a2-478f-a926-bb842a2d034c_550x.jpg?v=1723513210'),
        ('colchon 2x2pitot semi ortop', 2200000, 'https://http2.mlstatic.com/D_NQ_NP_2X_652950-MLU74086874267_012024-F.webp'),
        ('Mac mini M4 Pro', 120000, 'https://co.tiendasishop.com/cdn/shop/files/IMG-15363028_550x.jpg?v=1730306599'),
        ('cama isla 120 de madera', 660000, 'https://http2.mlstatic.com/D_NQ_NP_2X_729441-MCO52503213764_112022-F.webp'),
        ('cama de madera 160', 720000, 'https://eleganthouse.com.co/wp-content/uploads/2018/09/cama-de-madera-tallada-varias-medidas-referencia-salome.jpg'),
        ('colchon yadiana alfa pilow 160*190', 1890000, 'https://m.media-amazon.com/images/I/91c4uFoeejL._AC_SL1500_.jpg'),
        ('lampara 3 bombillas', 135000, 'https://m.media-amazon.com/images/I/61GHntiw05L._AC_SL1500_.jpg'),
        ('arbol de navidad pino dakota de 180', 175000, 'https://exitocol.vtexassets.com/arquivos/ids/24873443/arbol-navidad-de-pino-combinado-clasico-180-cm-importado.jpg?v=638629840933830000'),
        ('telefono alcatel 217a', 43444, 'https://http2.mlstatic.com/D_NQ_NP_2X_972864-MCO78867351956_092024-F.webp'),
        ('televisor lcd sony internet', 1890000, 'https://http2.mlstatic.com/D_NQ_NP_2X_940830-MCO73285875777_122023-F.webp'),
        ('Soporte Kalley led 32', 76000, 'https://http2.mlstatic.com/D_NQ_NP_2X_939388-MCO80691199915_112024-F.webp'),     
        ('porta vajilla c/tapa grande colplas', 127000, 'https://http2.mlstatic.com/D_NQ_NP_2X_810646-MLU77968031560_082024-F.webp'),
        ('recipiente colplas 60249 20 ltrs con dispensador', 44000, 'https://http2.mlstatic.com/D_NQ_NP_2X_966528-CBT72062873364_102023-F.webp'),
        ('plancha a vapor monix', 39000, 'https://http2.mlstatic.com/D_NQ_NP_2X_780012-MLU72629015984_112023-F.webp'),
        ('horno tostador monix', 113300, 'https://http2.mlstatic.com/D_NQ_NP_2X_911214-MLU70064478624_062023-F.webp'),
        ('licuadora monix metalica 3', 800000, 'https://http2.mlstatic.com/D_NQ_NP_2X_740313-CBT75849192631_042024-F.webp'),
        ('plancha de viaje a vapor monix', 56000, 'https://http2.mlstatic.com/D_NQ_NP_2X_827958-MCO48136358362_112021-F.webp'),
        ('cocineta haceb gas 2 ptos', 203000, 'https://http2.mlstatic.com/D_NQ_NP_2X_960510-MLA48713089475_122021-F.webp'),
        ('aire minisplit 12000btu', 1750000, 'https://http2.mlstatic.com/D_NQ_NP_2X_678809-MLU75209265112_032024-F.webp'),
        ('nevera centrales frost 235lt', 1374000, 'https://http2.mlstatic.com/D_NQ_NP_2X_911587-MLU72628561066_112023-F.webp'),
        ('nevera centrales frost 2pts 303ltc', 1495000, 'https://http2.mlstatic.com/D_NQ_NP_2X_743122-MCO77762560221_072024-F.webp'),
        ('horno micro ge', 365000, 'https://http2.mlstatic.com/D_NQ_NP_2X_878800-MLA46624628782_072021-F.webp'),
        ('horno micro mabe', 286000, 'https://http2.mlstatic.com/D_NQ_NP_2X_951950-MCO47685757843_092021-F.webp'),
        ('lavadora centrales semi automatica 13lbs', 690000, 'https://http2.mlstatic.com/D_NQ_NP_2X_745268-MCO72669108460_112023-F.webp')
    ])
    conn.commit()
    conn.close()

if table_exists() == False:
    createTabla()

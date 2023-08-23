# Lexer tokens
from pygeoconv.ply.lex import lex
from pygeoconv.ply.yacc import yacc

tokens = (
    'LPAREN',
    'RPAREN',
    'DOUBLE_TOK',
    'POINT',
    'LINESTRING',
    'POLYGON',
    'MULTIPOINT',
    'MULTILINESTRING',
    'MULTIPOLYGON',
    'GEOMETRYCOLLECTION',
    'COMMA',
    'EMPTY',
    'M',
    'Z',
    'ZM'

)

# Lexer rules
t_ignore = ' \t\r\n'


def t_LPAREN(t):
    r'\('
    return t


def t_RPAREN(t):
    r'\)'
    return t



def t_DOUBLE_TOK(t):
    r'-?[0-9]+(\.[0-9]+)?([eE][\-\+]?[0-9]+)?'
    try:
        t.value = int(t.value)
    except:
        t.value = float(t.value)
    return t


def t_POINT(t):
    r'POINT'
    return t


def t_LINESTRING(t):
    r'LINESTRING'
    return t


def t_POLYGON(t):
    r'POLYGON'
    return t


def t_MULTIPOINT(t):
    r'MULTIPOINT'
    return t


def t_MULTILINESTRING(t):
    r'MULTILINESTRING'
    return t


def t_MULTIPOLYGON(t):
    r'MULTIPOLYGON'
    return t


def t_GEOMETRYCOLLECTION(t):
    r'GEOMETRYCOLLECTION'
    return t


def t_COMMA(t):
    r','
    return t


def t_EMPTY(t):
    r'EMPTY'
    return t


def t_ZM(t):
    r'ZM'
    return t


def t_M(t):
    r'M'
    return t


def t_Z(t):
    r'Z'
    return t


def t_eof(t):
    return None


def t_error(t):
    print(f"Lexer error: Unexpected character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


def p_expressions(p):
    '''expressions : point
                   | linestring
                   | polygon
                   | multipoint
                   | multilinestring
                   | multipolygon
                   | geometrycollection'''
    p[0] = p[1]


def p_coordinate(p):
    '''coordinate : DOUBLE_TOK DOUBLE_TOK
                  | DOUBLE_TOK DOUBLE_TOK DOUBLE_TOK
                  | DOUBLE_TOK DOUBLE_TOK DOUBLE_TOK DOUBLE_TOK
                  '''
    p[0] = [x for x in p[1:]]


def p_ptarray(p):
    '''ptarray : ptarray COMMA coordinate
               | coordinate'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_ring_list(p):
    '''ring_list : ring_list COMMA ring
                 | ring'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_ring(p):
    '''ring : LPAREN ptarray RPAREN '''
    p[0] = p[2]


def p_point(p):
    '''point : POINT LPAREN coordinate RPAREN'''
    p[0] = {"type": "Point", "coordinates": p[3]}


def p_point_dimensions(p):
    '''
    point :    POINT Z LPAREN coordinate RPAREN
             | POINT ZM LPAREN coordinate RPAREN
             | POINT M LPAREN coordinate RPAREN
    '''
    properties = {}
    if p[2] == 'Z':
        properties['z'] = True
    elif p[2] == 'ZM':
        properties['z'] = True
        properties['m'] = True
    elif p[2] == 'M':
        properties['m'] = True
    p[0] = {"type": "Point", "coordinates": p[4], "properties": properties}


def p_point_empty(p):
    '''point : POINT EMPTY'''
    p[0] = {"type": "Point", "coordinates": []}


def p_point_untagged(p):
    '''point_untagged : coordinate
                      | LPAREN coordinate RPAREN '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_polygon_list(p):
    '''polygon_list : polygon_list COMMA polygon_untagged
                    | polygon_untagged'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_polygon_untagged(p):
    '''polygon_untagged : LPAREN ring_list RPAREN '''
    p[0] = p[2]


def p_point_list(p):
    '''point_list : point_list COMMA point_untagged
                  | point_untagged'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_linestring(p):
    '''linestring : LINESTRING LPAREN point_list RPAREN'''
    p[0] = {"type": "LineString", "coordinates": p[3]}


def p_linestring_dimensions(p):
    '''linestring : LINESTRING Z LPAREN point_list RPAREN
                  | LINESTRING M LPAREN point_list RPAREN
                  | LINESTRING ZM LPAREN point_list RPAREN'''
    properties = {}
    if p[2] == 'Z':
        properties['z'] = True
    elif p[2] == 'ZM':
        properties['z'] = True
        properties['m'] = True
    elif p[2] == 'M':
        properties['m'] = True
    p[0] = {"type": "LineString", "coordinates": p[4], "properties": properties}


def p_linestring_empty(p):
    '''linestring : LINESTRING EMPTY'''
    p[0] = {"type": "LineString", "coordinates": []}


def p_polygon(p):
    '''polygon : POLYGON LPAREN ring_list RPAREN'''
    p[0] = {"type": "Polygon", "coordinates": p[3]}


def p_polygon_dimensions(p):
    """polygon : POLYGON Z LPAREN ring_list RPAREN
               | POLYGON M LPAREN ring_list RPAREN
               | POLYGON ZM LPAREN ring_list RPAREN"""
    properties = {}
    if p[2] == 'Z':
        properties['z'] = True
    elif p[2] == 'ZM':
        properties['z'] = True
        properties['m'] = True
    elif p[2] == 'M':
        properties['m'] = True
    p[0] = {"type": "Polygon", "coordinates": p[4], "properties": properties}


def p_polygon_empty(p):
    """polygon : POLYGON EMPTY"""
    p[0] = {"type": "Polygon", "coordinates": []}


def p_multipoint(p):
    '''multipoint : MULTIPOINT LPAREN point_list RPAREN'''
    p[0] = {"type": "MultiPoint", "coordinates": p[3]}


def p_multipoint_dimensions(p):
    '''multipoint : MULTIPOINT Z LPAREN point_list RPAREN
                  | MULTIPOINT M LPAREN point_list RPAREN
                  | MULTIPOINT ZM LPAREN point_list RPAREN'''
    properties = {}
    if p[2] == 'Z':
        properties['z'] = True
    elif p[2] == 'ZM':
        properties['z'] = True
        properties['m'] = True
    elif p[2] == 'M':
        properties['m'] = True
    p[0] = {"type": "MultiPoint", "coordinates": p[4], "properties": properties}


def p_multipoint_empty(p):
    """multipoint : MULTIPOINT EMPTY"""
    p[0] = {"type": "MultiPoint", "coordinates": []}


def p_multilinestring(p):
    '''multilinestring : MULTILINESTRING LPAREN ring_list RPAREN'''
    p[0] = {"type": "MultiLineString", "coordinates": p[3]}


def p_multilinestring_dimensions(p):
    """multilinestring : MULTILINESTRING Z LPAREN ring_list RPAREN
                       | MULTILINESTRING M LPAREN ring_list RPAREN
                       | MULTILINESTRING ZM LPAREN ring_list RPAREN"""
    properties = {}
    if p[2] == 'Z':
        properties['z'] = True
    elif p[2] == 'ZM':
        properties['z'] = True
        properties['m'] = True
    elif p[2] == 'M':
        properties['m'] = True
    p[0] = {"type": "MultiLineString", "coordinates": p[4], "properties": properties}


def p_multilinestring_empty(p):
    """multilinestring : MULTILINESTRING EMPTY"""
    p[0] = {"type": "MultiLineString", "coordinates": []}


def p_multipolygon(p):
    '''multipolygon : MULTIPOLYGON LPAREN polygon_list RPAREN'''
    p[0] = {"type": "MultiPolygon", "coordinates": p[3]}


def p_multipolygon_dimensions(p):
    """multipolygon : MULTIPOLYGON Z LPAREN polygon_list RPAREN
                    | MULTIPOLYGON M LPAREN polygon_list RPAREN
                    | MULTIPOLYGON ZM LPAREN polygon_list RPAREN"""
    properties = {}
    if p[2] == 'Z':
        properties['z'] = True
    elif p[2] == 'ZM':
        properties['z'] = True
        properties['m'] = True
    elif p[2] == 'M':
        properties['m'] = True
    p[0] = {"type": "MultiPolygon", "coordinates": p[4], "properties": properties}


def p_multipolygon_empty(p):
    """multipolygon : MULTIPOLYGON EMPTY"""
    p[0] = {"type": "MultiPolygon", "coordinates": []}


def p_geometry(p):
    '''geometry : point
                | linestring
                | polygon
                | multipoint
                | multilinestring
                | multipolygon
                | geometrycollection'''
    p[0] = p[1]


def p_geometry_collection(p):
    '''geometry_collection : geometry_collection COMMA geometry
                           | geometry'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_geometrycollection(p):
    '''geometrycollection : GEOMETRYCOLLECTION LPAREN geometry_collection RPAREN'''
    p[0] = {"type": "GeometryCollection", "geometries": p[3]}


def p_geometry_collection_dimensions(p):
    """geometrycollection : GEOMETRYCOLLECTION Z LPAREN geometry_collection RPAREN
                          | GEOMETRYCOLLECTION M LPAREN geometry_collection RPAREN
                          | GEOMETRYCOLLECTION ZM LPAREN geometry_collection RPAREN"""
    properties = {}
    if p[2] == 'Z':
        properties['z'] = True
    elif p[2] == 'ZM':
        properties['z'] = True
        properties['m'] = True
    elif p[2] == 'M':
        properties['m'] = True
    p[0] = {"type": "GeometryCollection", "geometries": p[4], "properties": properties}


def p_geometry_collection_empty(p):
    """geometrycollection : GEOMETRYCOLLECTION EMPTY"""
    p[0] = {"type": "GeometryCollection", "geometries": []}


def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at token {p.type} ({p.value})")
    else:
        raise SyntaxError("Syntax error at EOF")


wkt_lexer = lex()
wkt_parser = yacc()
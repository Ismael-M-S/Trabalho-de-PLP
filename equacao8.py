# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:33:46 2019

Força sobre uma partícula

@author: Ismael
"""
import math
#print(math.asin(1))
from flask import (Blueprint, flash, render_template, request, jsonify)

bp = Blueprint('equacao8', __name__, url_prefix='/equacao8')

@bp.route('/F/<string:b>/<string:i>/<string:l>/<string:teta>', methods=['GET'] )
def F(b, i, l, teta):
    b, i, l, teta = float(b), float(i), float(l), float(teta)
    f = b * i * l * math.sin(teta * math.pi / 180)
    
    return jsonify("F<sub>m</sub> = " + str(f) + " N")

@bp.route('/B/<string:f>/<string:i>/<string:l>/<string:teta>', methods=['GET'] )
def B(f, i, l, teta):
    f, i, l, teta = float(f), float(i), float(l), float(teta)
    if (i != 0 and l != 0 and teta != 0 and teta != 180 and teta != 360):
        b = f / (i * l * math.sin(teta * math.pi / 180) )
        
        return jsonify("B = " + str(b) + " Tesla")
    
    return jsonify("ERRO: i e l devem ser diferentes de 0.<br>ERRO: θ deve ser diferente de 0, 180 e 360.")

@bp.route('/I/<string:f>/<string:b>/<string:l>/<string:teta>', methods=['GET'] )
def I(f, b, l, teta):
    f, b, l, teta = float(f), float(b), float(l), float(teta)
    if (b != 0 and l != 0 and teta != 0 and teta != 180 and teta != 360):
        i = f / (b * l * math.sin(teta * math.pi / 180) )
        
        return jsonify("i = " + str(i) + " A")
    
    return jsonify("ERRO: b e l devem ser diferentes de 0.<br>ERRO: θ deve ser diferente de 0, 180 e 360.")

@bp.route('/L/<string:f>/<string:i>/<string:b>/<string:teta>', methods=['GET'] )
def L(f, i, b, teta):
    f, i, b, teta = float(f), float(i), float(b), float(teta)
    if (i != 0 and b != 0 and teta != 0 and teta != 180 and teta != 360):
        l = f / (i * b * math.sin(teta * math.pi / 180) )
        
        return jsonify("l = " + str(l) + " m")
    
    return jsonify("ERRO: i e b devem ser diferentes de 0.<br>ERRO: θ deve ser diferente de 0, 180 e 360.")

@bp.route('/T/<string:f>/<string:i>/<string:l>/<string:b>', methods=['GET'] )
def Teta(f, i, l, b):
    f, i, l, b = float(f), float(i), float(l), float(b)
    if (i != 0 and l != 0 and b != 0):
        x = f / (b * i * l)
        if x < -1 or x > 1:
            return jsonify("ERRO: Não existe arcoseno de " + str(x) + ",<br> o arcoseno esta definido no intervalo [-1, 1].")
        else:
            teta = 1 +  math.asin(x) / math.pi * 180 - 1
            if teta < 0:
                teta += 360
            
            return jsonify("θ = " + str(teta) + " graus")
        
    return jsonify("ERRO: b, i e l devem ser diferentes de 0.")
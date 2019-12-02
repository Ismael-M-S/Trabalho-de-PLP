# -*- coding: utf-8 -*-
"""
Created on ?

Lei da gravidade

@author: Gabriel
"""
from flask import (Blueprint, flash, render_template, request, jsonify)

bp = Blueprint('equacao2', __name__, url_prefix='/equacao2')

@bp.route('/F/<string:g>/<string:m1>/<string:m2>/<string:d>', methods=['GET'] )
def F(g, m1, m2, d):
    g, m1, m2, d = float(g), float(m1), float(m2), float(d)
    if d != 0:
        f = (g * m1 * m2) / d ** 2
        
        return jsonify("F = " + str(f) + " N")
    else:
        return jsonify('ERRO: d deve ser diferente de zero')

@bp.route('/G/<string:f>/<string:m1>/<string:m2>/<string:d>', methods=['GET'] )
def G(f, m1, m2, d):
    f, m1, m2, d = float(f), float(m1), float(m2), float(d)
    if m1 == 0 or m2 == 0:
        return jsonify("ERRO: tanto m<sub>1</sub> quanto m<sub>2</sub> devem ser diferentes de 0.")
    else:
        g = (f * d ** 2) / (m1 * m2)

        return jsonify("G = " + str(g) + " m/s²")

@bp.route('/M1/<string:f>/<string:g>/<string:m2>/<string:d>', methods=['GET'] )
def M1(f, g, m2, d):
    f, g, m2, d = float(f), float(g), float(m2), float(d)
    if g == 0 or m2 == 0:
        return jsonify("ERRO: tanto g quanto m<sub>2</sub> devem ser diferentes de 0.")
    else:
        m1 = (f * d ** 2) / g * m2
        
        return jsonify("m<sub>1</sub> = " + str(m1) + " Kg")

@bp.route('/M2/<string:f>/<string:g>/<string:m1>/<string:d>', methods=['GET'] )
def M2(f, g, m1, d):
    f, g, m1, d = float(f), float(g), float(m1), float(d)
    if m1 == 0 or g == 0:
        return jsonify("ERRO: tanto m<sub>1</sub> quanto g devem ser diferentes de 0.")
    else:
        m2 = (f * d ** 2) / g * m1
        
        return jsonify("m<sub>2</sub> = " + str(m2) + "Kg")

@bp.route('/D/<string:f>/<string:g>/<string:m1>/<string:m2>', methods=['GET'] )
def D(f, g, m1, m2):
    f, g, m1, m2 = float(f), float(g), float(m1), float(m2)
    if f == 0:
        return jsonify('ERRO: F deve ser diferente de zero')
    elif ( (g * m1 * m2) / f) < 0:
        return jsonify('ERRO: não existe raiz de número negativo')
    else:
        d = ( (g * m1 * m2) / f) ** (1/2)
        
        return jsonify("d = " + str(d) + " m")
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:32:48 2019

Equação de Clapeyron

@author: Caio
"""
# Equação de um gás ideal
# Supoe que a unidade da de p será em 'atm' e volume em litros 'L'
'''Seleciona o valor da constante R que será usada
    if p_Unidade == 'atm':
        R = 0.082
    elif p_Unidade == 'mmHg':
        R = 62.3
    elif p_Unidade == 'KPa':
        R = 8.31
'''
from flask import (Blueprint, flash, render_template, request, jsonify)

bp = Blueprint('equacao5', __name__, url_prefix='/equacao5')

@bp.route('/P/<string:v>/<string:n>/<string:r>/<string:t>', methods=['GET'] )
def P(v, n, r, t):
    v, n, t = float(v), float(n), float(t)
    r = 0.082
    if v == 0:
        return jsonify("ERRO: V deve ser diferente de 0.")
    else:
        p = (n * r * t) / v

        return jsonify("p = " + str(p) + " atm")

@bp.route('/V/<string:p>/<string:n>/<string:r>/<string:t>', methods=['GET'] )
def V(p, n, r, t):
    p, n, t = float(p), float(n), float(t)
    r = 0.082
    if p == 0:
        return jsonify("ERRO: p deve ser diferente de 0.")
    else:
        v = (n * r * t) / p

        return jsonify("V = " + str(v) + " L")

@bp.route('/N/<string:p>/<string:v>/<string:r>/<string:t>', methods=['GET'] )
def N(p, v, r, t):
    p, v, t = float(p), float(v), float(t)
    r = 0.082
    if t == 0:
        return jsonify("ERRO: T deve ser diferente de 0.")
    else:
        n = (p * v) / (r * t)

        return jsonify("n = " + str(n) + " mol(s)")

@bp.route('/R', methods=['GET'] )
def R():
    return jsonify("R = 0,082 atm. L/mol . K")

@bp.route('/T/<string:p>/<string:v>/<string:n>/<string:r>', methods=['GET'] )
def T(p, v, n, r):
    p, v, n = float(p), float(v), float(n)
    r = 0.082
    if n == 0:
        return jsonify("ERRO: n deve ser diferente de 0.")
    else:
        t = (p * v) / (r * n)

        return jsonify("T = " + str(t) + " Kelvin(s)")
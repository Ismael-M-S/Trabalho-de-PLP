# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:15:11 2019

Equação de Torricelli

@author: Caio
"""
from flask import (Blueprint, flash, render_template, request, jsonify)

bp = Blueprint('equacao6', __name__, url_prefix='/equacao6')

@bp.route('/V/<string:v0>/<string:a>/<string:s>', methods=['GET'] )
def V(v0, a, s):
    v0, a, s = float(v0), float(a), float(s)
    if (v0 ** 2 + 2 * a * s) < 0:
        return jsonify('ERRO: raiz de número negativo.')
    else:
        v = (v0 ** 2 + 2 * a * s) ** (1 / 2)

        return jsonify("v = " + str(v) + ' m/s')

@bp.route('/Vo/<string:v>/<string:a>/<string:s>', methods=['GET'] )
def V0(v, a, s):
    v, a, s = float(v), float(a), float(s)
    if (v ** 2 - 2 * a * s) < 0:
        return jsonify('ERRO: raiz de número negativo.')
    else:
        v0 = (v ** 2 - 2 * a * s) ** (1 / 2)

        return jsonify("v<sub>0</sub> = " + str(v0) + ' m/s')

@bp.route('/A/<string:v>/<string:v0>/<string:s>', methods=['GET'] )
def A(v, v0, s):
    v, v0, s = float(v), float(v0), float(s)
    if s == 0:
        return jsonify('ERRO: S dever ser diferente de 0.')
    else:
        a = (v ** 2 - v0 ** 2) / (2 * s)

        return jsonify("a = " + str(a) + ' m/s²')

@bp.route('/S/<string:v>/<string:v0>/<string:a>', methods=['GET'] )
def S(v, v0, a):
    v, v0, a = float(v), float(v0), float(a)
    if a == 0:
        return jsonify('ERRO: a dever ser diferente de 0.')
    else:
        s = (v ** 2 - v0 ** 2) / (2 * a)

        return jsonify("S = " + str(s) + ' m')
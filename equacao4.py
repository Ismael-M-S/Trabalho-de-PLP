# -*- coding: utf-8 -*-
"""
Created on ?

Teoria do caos

@author: Jonathan
"""
from flask import (Blueprint, flash, render_template, request, jsonify)

bp = Blueprint('equacao4', __name__, url_prefix='/equacao4')

@bp.route('/XN/<string:k>/<string:xo>', methods=['GET'] )
def XN(k, xo):
    k, xo = float(k), float(xo)
    xn = k * xo * (1 - xo)

    return jsonify("x<sub>new</sub> = " + str(xn) )

@bp.route('/XO/<string:k>/<string:xn>', methods=['GET'] )
def XO(k, xn):
    k, xn = float(k), float(xn)
    if k == 0:
        return jsonify("ERRO: K deve ser diferente de 0")
    elif 4 * ( xn / k) > 1:
        return jsonify("ERRO: raiz de número negativo")
    else:
        xo1 = (1 / 2) * (1 - 4 * ( xn / k) ) ** (1 / 2)
        xo2 = (1 / 2) * - (1 - 4 * ( xn / k) ) ** (1 / 2)
        if xo1 == xo2:
            return jsonify("x<sub>old</sub> = " + str(xo1) )
        else:
            return jsonify("x<sub>old</sub> = " + str(xo1) + " ou " + str(xo2) )

@bp.route('/K/<string:xn>/<string:xo>', methods=['GET'] )
def K(xn, xo):
    xn, xo = float(xn), float(xo)
    if xo == 0 or xo == 1:
        return jsonify("ERRO: X<sub>old</sub> deve ser diferente de 0 e 1")
    else:
        k = xn / (xo - xo ** 2)

        return jsonify("K = " + str(k) )
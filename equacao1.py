# -*- coding: utf-8 -*-
"""
Created on ?

Teorema de Pitágoras

@author: Gabriel
"""
from flask import (Blueprint, flash, render_template, request, jsonify)

bp = Blueprint('equacao1', __name__, url_prefix='/equacao1')

@bp.route('/A/<string:b>/<string:c>', methods=['GET'] )
def A(b, c):
    b, c = float(b), float(c)
    if ( (c ** 2) - (b ** 2) ) >= 0:
            a = ( (c ** 2) - (b ** 2) ) ** (1/2)
            
            return jsonify("a = " + str(a) )
    else:
        return jsonify('ERRO: Não existe raiz de número negativo')

@bp.route('/B/<string:a>/<string:c>', methods=['GET'] )
def B(a, c):
    a, c = float(a), float(c)
    if ( (c ** 2) - (a ** 2) ) >= 0:
            b = ( (c ** 2) - (a ** 2) ) ** (1/2)
            
            return jsonify("b = " + str(b) )
    else:
        return jsonify('ERRO: Não existe raiz de número negativo')

@bp.route('/C/<string:a>/<string:b>', methods=['GET'] )
def C(a, b):
    a, b = float(a), float(b)
    c = ( (a ** 2) + (b ** 2) ) ** (1/2)

    return jsonify("c = " + str(c) )
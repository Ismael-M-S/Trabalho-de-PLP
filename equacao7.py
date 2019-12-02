# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:21:37 2019

Equação de Gauss

@author: Caio
"""
# Equação fundamental dos espelhos esféricos
# Utilizei pL para o p(linha) pois o editor não aceita a escrita normal, considera como início de comentário
from flask import (Blueprint, flash, render_template, request, jsonify)

bp = Blueprint('equacao7', __name__, url_prefix='/equacao7')

@bp.route('/F/<string:p>/<string:pl>', methods=['GET'] )
def F(p, pl):
    p, pl = float(p), float(pl)
    if p == 0 or pl == 0:
        return jsonify("ERRO: Tanto p quanto p' devem ser diferentes de 0.")
    else:
        f = (1 / p + 1 / pl) ** (- 1)

        return jsonify("f = " + str(f) )

@bp.route('/P/<string:f>/<string:pl>', methods=['GET'] )
def P(f, pl):
    f, pl = float(f), float(pl)
    if f == 0 or pl == 0:
        return jsonify("ERRO: Tanto f quanto p' devem ser diferentes de 0.")
    else:
        p = (1 / f + 1 / pl) ** (- 1)

        return jsonify("p = " + str(p) )

@bp.route('/PL/<string:f>/<string:p>', methods=['GET'] )
def PL(f, p):
    f, p = float(f), float(p)
    if f == 0 or p == 0:
        return jsonify("ERRO: Tanto f quanto p devem ser diferentes de 0.")
    else:
        pl = (1 / f + 1 / p) ** (- 1)

        return jsonify("p' = " + str(pl) )
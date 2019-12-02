# -*- coding: utf-8 -*-
"""
Created on ?

Equação da teoria de relatividade

@author: Jonathan
"""
from flask import (Blueprint, flash, render_template, request, jsonify)

bp = Blueprint('equacao3', __name__, url_prefix='/equacao3')

@bp.route('/E/<string:c>/<string:m>', methods=['GET'] )
def E(c, m):
    m = float(m)
    luz = 90000000000000000 # (300.000.000)^2
    
    e = m * luz
    
    return jsonify("E = " + str(e) + " J")

@bp.route('/M/<string:e>/<string:c>', methods=['GET'] )
def M(e, c):
    e = float(e)
    luz = 90000000000000000 # (300.000.000)^2
    
    m = e / luz
    
    return jsonify("m = " + str(m) + " Kg")

@bp.route('/C', methods=['GET'] )
def C():
    return jsonify("c = 300 000 000 m/s")

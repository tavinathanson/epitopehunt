from flask import Flask, render_template
from pandas import concat
from pepdata import iedb

from epitopehunt import app


EPITOPE_SUB_SEQ_LENGTH = 4


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/matches')
def matches():
    epitope = "AAAALLLL"
    df = iedb.load_tcell()
    matches_dfs = []
    for i in range(len(epitope) - EPITOPE_SUB_SEQ_LENGTH + 1):
        sub_seq = epitope[i:i + EPITOPE_SUB_SEQ_LENGTH]
        matches = df[df['Epitope Linear Sequence'].str.contains(sub_seq)]
        matches_dfs.append(matches)
    return concat(matches_dfs).to_html()


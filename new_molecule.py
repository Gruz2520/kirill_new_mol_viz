import streamlit as st
from stmol import showmol, speck_plot, render_pdb, makeobj
import pandas as pd

st.title("Визуализация новой химической молекулы (N) L-лейциновый эфир ацикловира")

f = open('MolView.mol', "r")
example_xyz = f.read()

data = [
    ['Formula', 'C13H20N6O4'],
    ['Molecular weight', '324.3388 u'],
    ['Hydrogen bond donors', '3'],
    ['Hydrogen bond acceptors', '5']
]
df = pd.DataFrame(data, columns=['Characteristic', 'Value'])


data_2 = [
    ['C', '12.0107 u', 13, '48.141 %'],
    ['H', '1.00794 u', 20, '6.2154 %'], 
    ['N', '14.0067 u', 6, '25.911 %'],
    ['O', '15.9994 u', 3, '19.732 %']
]

df_2 = pd.DataFrame(data_2, columns=['Element', 'Atomic Mass', 'Atoms', 'Percent Composition'])


showmol(makeobj(example_xyz, style='stick'), width=1000)

st.markdown('''Молекула (N) – новый лекарственный препарат для лечения миокардита, индуцированного герпесом 6-го типа, представляющий собой L- лейциновый эфир ацикловира.
''')

st.header("Molecule Characteristics")

with st.container():
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("mol.png", use_column_width=True)

st.table(df)

st.subheader("Percent Composition")
st.table(df_2)

st.write("Canonical SMILES")
st.code("CC(C)CC(N)C(=O)OCOCn1cnc2C(=O)NC(=Nc12)N")

st.write("Isomeric SMILES")
st.code("C1(=NC2=C(N=CN2COCOC(C(CC(C)C)N([H])[H])=O)C(=O)N1[H])N([H])[H]")

st.write("InChIKey")
st.code("QIYJTJVDORVJFY-UHFFFAOYSA-N")

st.write("InChI")
st.code("InChI=1S/C13H20N6O4/c1-7(2)3-8(14)12(21)23-6-22-5-19-4-16-9-10(19)17-13(15)18-11(9)20/h4,7-8H,3,5-6,14H2,1-2H3,(H3,15,17,18,20)")


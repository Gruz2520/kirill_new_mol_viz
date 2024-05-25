import streamlit as st
from stmol import showmol, speck_plot, render_pdb, makeobj
import pandas as pd

st.title("Визуализация новой химической молекулы (N) L-лейциновый эфир ацикловира")

f = open('MolView.mol', "r")
example_xyz = f.read()

data = [
    ['Formula', 'C13H22N6O3'],
    ['Molecular weight', '310.3552 u'],
    ['Hydrogen bond donors', '3'],
    ['Hydrogen bond acceptors', '4']
]
df = pd.DataFrame(data, columns=['Characteristic', 'Value'])


data_2 = [
    ['C', '12.0107 u', 13, '50.310 %'],
    ['H', '1.00794 u', 22, '7.1450 %'], 
    ['N', '14.0067 u', 6, '27.079 %'],
    ['O', '15.9994 u', 3, '15.466 %']
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
st.code("CC(C)CC(N)COCOCn1cnc2C(=O)NC(=Nc12)N")

st.write("Isomeric SMILES")
st.code("O(CN1C2=C(C(=O)N(C(=N2)N([H])[H])[H])N=C1)COCC(CC(C)C)N([H])[H]")

st.write("InChIKey")
st.code("CAKDPODOBYYLGW-UHFFFAOYSA-N")

st.write("InChI")
st.code("InChI=1S/C13H22N6O3/c1-8(2)3-9(14)4-21-7-22-6-19-5-16-10-11(19)17-13(15)18-12(10)20/h5,8-9H,3-4,6-7,14H2,1-2H3,(H3,15,17,18,20)")


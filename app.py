import streamlit as st
import pandas as pd
import math
import base64
from io import BytesIO
from datetime import datetime

def calculate_trucks(total_palettes_euro, total_palettes_indus, total_demi_palettes, double_stack, nb_besoins):
    # Capacités des véhicules (en tenant compte du chariot = 0.5 palette)
    SEMI_CAPACITE_EURO = 32  # 33 - 0.5 pour le chariot
    SEMI_CAPACITE_INDUS = 25  # 26 - 0.5 pour le chariot
    PORTEUR_75_EURO = 18  # 19 - 0.5 pour le chariot
    PORTEUR_75_INDUS = 13  # 14 - 0.5 pour le chariot
    PORTEUR_9_EURO = 21  # 22 - 0.5 pour le chariot
    PORTEUR_9_INDUS = 17  # 18 - 0.5 pour le chariot

    if double_stack:
        SEMI_CAPACITE_EURO *= 2
        SEMI_CAPACITE_INDUS *= 2

    def calculate_vehicle_needs(palettes_euro, palettes_indus, demi_palettes):
        # Convertir les demi-palettes en équivalent palettes Europe
        total_euro_equiv = palettes_euro + (demi_palettes / 2)
        
        resultats = {
            'Semi-remorque (Palettes Europe)': math.ceil(total_euro_equiv / SEMI_CAPACITE_EURO),
            'Semi-remorque (Palettes Industrielles)': math.ceil(palettes_indus / SEMI_CAPACITE_INDUS),
            'Porteur 7.5m (Palettes Europe)': math.ceil(total_euro_equiv / PORTEUR_75_EURO),
            'Porteur 7.5m (Palettes Industrielles)': math.ceil(palettes_indus / PORTEUR_75_INDUS),
            'Porteur 9m (Palettes Europe)': math.ceil(total_euro_equiv / PORTEUR_9_EURO),
            'Porteur 9m (Palettes Industrielles)': math.ceil(palettes_indus / PORTEUR_9_INDUS)
        }
        return resultats

    results_per_need = []
    for i in range(nb_besoins):
        result = calculate_vehicle_needs(
            total_palettes_euro / nb_besoins,
            total_palettes_indus / nb_besoins,
            total_demi_palettes / nb_besoins
        )
        results_per_need.append(result)

    return results_per_need

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Besoins en camions', index=True)
    processed_data = output.getvalue()
    return processed_data

st.set_page_config(page_title="Calculateur de Besoins en Camions", layout="wide")

st.title("🚛 Calculateur de Besoins en Camions")

st.markdown("""
### Entrez vos besoins en palettes
""")

col1, col2 = st.columns(2)

with col1:
    total_palettes_euro = st.number_input("Nombre de Palettes Europe (80 x 120 cm)", 
                                         min_value=0, value=0, step=1)
    total_palettes_indus = st.number_input("Nombre de Palettes Industrielles (100 x 120 cm)", 
                                          min_value=0, value=0, step=1)

with col2:
    total_demi_palettes = st.number_input("Nombre de Demi-palettes (80 x 60 cm)", 
                                         min_value=0, value=0, step=1)
    double_stack = st.checkbox("Double empilement possible")
    nb_besoins = st.number_input("Nombre de livraisons à répartir", 
                                min_value=1, value=1, step=1)

if st.button("Calculer les besoins"):
    if total_palettes_euro + total_palettes_indus + total_demi_palettes > 0:
        results = calculate_trucks(total_palettes_euro, total_palettes_indus, 
                                 total_demi_palettes, double_stack, nb_besoins)
        
        st.markdown("### Résultats")
        
        # Créer un DataFrame pour l'affichage et l'export
        df_results = pd.DataFrame(results)
        df_results.index = [f"Livraison {i+1}" for i in range(nb_besoins)]
        
        # Afficher les résultats
        st.dataframe(df_results)
        
        # Boutons d'export
        col1, col2, col3 = st.columns(3)
        
        # Export Excel
        with col1:
            excel_data = to_excel(df_results)
            st.download_button(
                label="📥 Télécharger Excel",
                data=excel_data,
                file_name=f'besoins_camions_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        
        # Export CSV
        with col2:
            csv = df_results.to_csv(index=True)
            st.download_button(
                label="📥 Télécharger CSV",
                data=csv,
                file_name=f'besoins_camions_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
                mime='text/csv'
            )
            
        # Export PDF-friendly HTML
        with col3:
            html = df_results.to_html()
            st.download_button(
                label="📥 Télécharger HTML",
                data=html,
                file_name=f'besoins_camions_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html',
                mime='text/html'
            )
    else:
        st.warning("Veuillez entrer au moins une palette à transporter.")

st.markdown("""
---
### Informations sur les capacités

**Semi-remorque (13,6 mètres)**:
- 33 Palettes Europe (80 x 120 cm)
- 26 Palettes Industrielles (100 x 120 cm)

**Porteur 7,5 mètres**:
- 15-19 Palettes Europe
- 12-14 Palettes Industrielles

**Porteur 9 mètres**:
- 20-22 Palettes Europe
- 16-18 Palettes Industrielles

*Note: Un espace équivalent à une demi-palette est réservé pour le chariot dans chaque véhicule.*
""")
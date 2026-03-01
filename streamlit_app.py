import streamlit as st
import pandas as pd
import requests
from datetime import date, datetime
import google.generativeai as genai
import random

# --- DATEN AUS DEINEN BILDERN ---
GEB_ICH, GEB_FRAU = date(1975, 10, 1), date(1983, 1, 1)
GEB_SOHN, GEB_TOCHTER = date(2013, 2, 1), date(2015, 2, 1)
GEB_HUND = date(2025, 9, 8)

MEINE_ETFS = {"iShares MSCI EM": 173.78, "SPDR MSCI World": 249.28}
MEINE_KRYPTOS = {"bitcoin": 0.002046, "ethereum": 0.053326}

GEMINI_KEY = "AIzaSyBtsCbrORYhKgu89mtz-lDRkSPjOHA2qIc"
WEATHER_KEY = "30a0d11b96f70dbb597a5b021ab65c27"

# --- FUNKTIONEN ---
def get_crypto():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur").json()
        btc = MEINE_KRYPTOS["bitcoin"] * r["bitcoin"]["eur"]
        eth = MEINE_KRYPTOS["ethereum"] * r["ethereum"]["eur"]
        return btc, eth
    except: return 0.0, 0.0

# --- LAYOUT ---
st.set_page_config(page_title="Family Hub", layout="centered")
st.title("🏠 Unser Familien-Hub")

# Alter anzeigen
heute = date.today()
st.success(f"👦 Sohn: {heute.year - GEB_SOHN.year} J. | 👧 Tochter: {heute.year - GEB_TOCHTER.year} J. | 🦮 Hund: {(heute - GEB_HUND).days // 7} Wochen")

# Finanzen anzeigen
st.subheader("💰 Aktuelles Depot")
btc_v, eth_v = get_crypto()
gesamt = btc_v + eth_v + sum(MEINE_ETFS.values())
st.metric("Gesamt Vermögen", f"{gesamt:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))

# Bibelwort
zitate = ["Ich vermag alles durch den, der mich stark macht. (Phil 4,13)", "Der Herr ist mein Hirte. (Ps 23)"]
st.info(f"📖 {random.choice(zitate)}")

# Gemini
st.write("---")
try:
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    frage = st.text_input("Frag Gemini etwas:")
    if frage:
        res = model.generate_content(frage)
        st.write(res.text)
except:
    st.error("KI-Key prüfen!")

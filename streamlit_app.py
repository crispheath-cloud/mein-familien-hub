import requests
from datetime import date, datetime

# --- DEINE DATEN ---
GEB_SOHN = date(2013, 2, 1)
GEB_HUND = date(2025, 9, 8)

# Deine Werte aus den Bildern
btc_menge = 0.002046  #
eth_menge = 0.053326  #
etf_gesamt = 173.78 + 249.28  #

def zeige_hub():
    print("="*30)
    print("🏠 MEIN FAMILIEN-HUB")
    print("="*30)
    
    # Zeit & Alter
    heute = date.today()
    alter_sohn = heute.year - GEB_SOHN.year
    alter_hund_wochen = (heute - GEB_HUND).days // 7
    
    print(f"📅 Datum: {heute.strftime('%d.%m.%Y')}")
    print(f"👦 Sohn: {alter_sohn} Jahre")
    print(f"🦮 Hund: {alter_hund_wochen} Wochen alt")
    print("-"*30)

    # Finanzen
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur").json()
        btc_euro = btc_menge * r["bitcoin"]["eur"]
        eth_euro = eth_menge * r["ethereum"]["eur"]
        gesamt = btc_euro + eth_euro + etf_gesamt
        
        print(f"💰 FINANZEN")
        print(f"Bitcoin: {btc_euro:.2f} €")
        print(f"Ethereum: {eth_euro:.2f} €")
        print(f"ETFs: {etf_gesamt:.2f} €")
        print(f"⭐ GESAMT: {gesamt:.2f} €")
    except:
        print("Kurse konnten nicht geladen werden.")
    
    print("-"*30)
    print("📖 BIBEL-ZITAT")
    print("Sei stark und mutig! Fürchte dich nicht, denn der Herr, dein Gott, ist mit dir. (Josua 1,9)")
    print("="*30)

if __name__ == "__main__":
    zeige_hub()

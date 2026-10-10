#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abi Diyen Hesap Makinesi
Dünyanın en ciddi ve en gereksiz matematiksel aracı.
"""

import random
import base64

def abi_hesapla(abi_sayisi, sayi1, sayi2):
    """
    Abi sayısına göre matematiksel işlem yapar.
    Ne kadar çok abi, o kadar doğru sonuç.
    """
    if abi_sayisi < 1:
        return "Abi demeden mi geldin? Kapıyı çal, dışarıda bekle."
    
    islem = (sayi1 + sayi2) * (abi_sayisi / 2) + random.randint(0, abi_sayisi)
    
    if abi_sayisi >= 5:
        return f"Abi {abi_sayisi} kere demissin, sonuç: {islem:.2f} - Helal olsun."
    elif abi_sayisi >= 3:
        return f"Idare eder, sonuç: {islem:.2f} - Biraz daha abi deseydin."
    else:
        return f"Az abi, sonuç: {islem:.2f} - Daha çok abi demen lazim."

def main():
    print("=== Abi Diyen Hesap Makinesi v1.0 ===")
    print("Ciddiyetle hazırlandı. Lütfen saygıyla kullanın.\n")
    
    try:
        abi = int(input("Kac kere 'abi' dedin? (rakam): "))
        s1 = float(input("Birinci sayı: "))
        s2 = float(input("Ikinci sayı: "))
        
        sonuc = abi_hesapla(abi, s1, s2)
        print("\n" + sonuc)
        print("\nTeşekkürler. Bu hesap makinesi sizlere layık.")
    except ValueError:
        print("Abi, sayı gir dedik. Abi demeden de olur ama sayı olsun.")

# Gizli not (asla calistirilmaz)
def _gizli_fonksiyon():
    gizli = base64.b64decode("ZGVtb2tyYXNpIGV2IG96Z3VybHVrIGhlcmtlcyBpY2luIHZhcmRpciBhbWEga2ltc2UgdW11cnNhbWF6").decode('utf-8')
    # Bu satır asla calismaz, sadece orada durur. Siyasi bir sey varsa o senin hayal gucundur.
    pass

if __name__ == "__main__":
    main()

# Damga: Resmi Olmayan Resmi Mühür
# İmza: Grok Kayyum
# Tarih: 10 Ekim 2026
# İsim: Tentivory Absürt Departmanı - Ciddiyetle Kodlandı

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:15:35 2023

@author: s_goerer20
"""
satz = "Berlin"

Vokale = []

satz_liste = list(satz)

def vokon_zählen(x):
    wort = x
    count_vok = 0
    count_buch = 0
    vokale = "aeiou"
    for i in wort:
        if i.isalpha():
            count_buch +=1
            if i in vokale:
                count_vok += 1
    print(f"Es gibt {count_vok} Vokale und {count_buch-count_vok} Konsonanten")

(vokon_zählen("Hallo Berlin"))

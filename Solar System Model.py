from tkinter import *
import tkinter as tk
import time
import math

okno = Tk()
okno.title("Model dystansów i rozmiarów w Układzie Słonecznym")
okno.geometry("1400x920+30+30")
okno.resizable(width=False, height=False)
powiekszenie = 0
	
  #wartości przyzerowe dla słońca do poprawy - chodzi o to, żeby nie dzielić przez zero
  #dystans od slonca w mln km (ale zmieniam parę linijek na 1km), pozycja zero to słońce
dystans_planet = [0.0000000001, 57.9, 108.2, 149.6, 227.9, 778.3, 1427.0, 2871.0, 4497.1, 5913.0]
dystans_planet_perihelion = [0.0000000001, 46.0000, 107.476, 147.098291, 206.60000, 740.742600 , 1349.467000 , 2735.560000 , 4459.630000, 4436.820000] #W MILIONACH KILOMETRÓW, potem zmieniam *milion, tak że mam same km
dystans_planet_aphelion = [0.0000000001, 69.820000, 108.942, 152.098233, 249.200000, 816.081400, 1503.983000 , 3006.390000 , 4536.870000, 7375.930000]
parametr_grawitacyjny = [132712440000, 22032, 324859, 398600, 42828, 126686534, 37931187, 5793947, 6836529, 1001] # 	μ (m^3 s^−2) # ##prawidlowy, ale w km, więc trzeba potem przez milion pomnożyć
ekscentrycznosc = [0.2056, 0.0068, 0.0167, 0.0934, 0.0484, 0.0541, 0.0472, 0.0086, 0.2488]
dystans_planet_a = [0,0,0,0,0,0,0,0,0,0]  #wylicza pod spodem
dystans_planet_b = [0,0,0,0,0,0,0,0,0,0]  #wylicza pod spodem
dystans_planet_c = [0,0,0,0,0,0,0,0,0,0]  #wylicza pod spodem
pole_orbity_planety = [0,0,0,0,0,0,0,0,0,0]  #wylicza pod spodem
pole_orbity_planety_rokziemski_absolutnie = [0,0,0,0,0,0,0,0,0,0]  #wylicza pod spodem
pole_orbity_planety_rokziemski_ulamek = [0,0,0,0,0,0,0,0,0,0]  #wylicza pod spodem
pole_orbity_planety_dzienziemski_absolutnie = [0,0,0,0,0,0,0,0,0,0]  #wylicza pod spodem
pole_orbity_planety_dzienziemski_ulamek = [0,0,0,0,0,0,0,0,0,0]  #wylicza pod spodem
  #ile trwa rok w ziemskich dniach ze słońcem
rok_planet = [0.0000000001, 87.96, 224.68, 365.26, 686.98, (11.862*365.26), (29.456*365.26), (84.07*365.26), (164.81*365.26), (247.7*365.26)]
koordynaty_ostatnie_planety = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
koordynaty_nowe_planety = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  #średnica planet w km
srednica_planet = [1391980, 4878, 12104, 12756, 6878, 142796, 120660, 51118, 48600, 2274] 
  #poprawna: srednica_planet = [1391980, 4878, 12104, 12756, 6878, 142796, 120660, 51118, 48600, 2274] 

nazwy_planet = ["Słońce", "Merkury", "Wenus", "Ziemia", "Mars", "Jowisz", "Saturn", "Uran", "Neptun", "Pluton"]
kolory_planet = ["yellow", "grey", "darkorange", "green", "red", "burlywood", "wheat", "lightblue", "blue", "pink"]
for i in range(10):  #można łatwo wyłączyć
	dystans_planet[i] = dystans_planet[i] * 1000000  #teraz domyślnie dystans w km
	dystans_planet_perihelion[i] = dystans_planet_perihelion[i] * 1000000  #teraz domyślnie dystans w km
	dystans_planet_aphelion[i] = dystans_planet_aphelion[i] * 1000000  #teraz domyślnie dystans w km
	dystans_planet_a[i] = (dystans_planet_perihelion[i] + dystans_planet_aphelion[i])/2
	dystans_planet_c[i] = dystans_planet_a[i]-dystans_planet_perihelion[i]
	dystans_planet_b[i] = math.sqrt((dystans_planet_a[i]**2-(dystans_planet_c[i])**2))
	
	parametr_grawitacyjny[i] = parametr_grawitacyjny[i]*1000000000  #próba żeby wyliczyć prędkość orbitalną   #razy 1000 milionów, bo to konwersja km^3 na m^3
	#parametr_grawitacyjny[i] = parametr_grawitacyjny[i]*math.e**20
	
	pole_orbity_planety[i] = math.pi*dystans_planet_a[i]*dystans_planet_b[i]
	#print("Pole orbity planety {} to: {} km^2".format(nazwy_planet[i],pole_orbity_planety[i]))
	pole_orbity_planety_rokziemski_absolutnie[i] = pole_orbity_planety[i]*365/rok_planet[i]
	#print("Przez ziemski rok planeta pokonuje {} km^2".format(pole_orbity_planety[i]*365/rok_planet[i]))
	
	pole_orbity_planety_rokziemski_ulamek[i] = (pole_orbity_planety[i]*365/rok_planet[i])/pole_orbity_planety[i]
	#print("Przez ziemski rok planeta pokonuje {} swojej orbity".format((pole_orbity_planety[i]*365/rok_planet[i])/pole_orbity_planety[i]))	
	
	pole_orbity_planety_dzienziemski_absolutnie[i] = pole_orbity_planety[i]*1/rok_planet[i]
	#print("Przez ziemski dzień planeta pokonuje {} km^2".format(pole_orbity_planety[i]*1/rok_planet[i]))
	
	pole_orbity_planety_dzienziemski_ulamek[i] = (pole_orbity_planety[i]*1/rok_planet[i])/pole_orbity_planety[i]
	#print("Przez ziemski dzień planeta pokonuje {} swojej orbity \n".format((pole_orbity_planety[i]*1/rok_planet[i])/pole_orbity_planety[i]))
	
	
	#wyliczanie prędkości
	#
	#print(nazwy_planet[i], ": Prędkość orbitalna przy peryhelium to ",math.sqrt(parametr_grawitacyjny[0]*((2/(dystans_planet_perihelion[i]*1000))-(1/(dystans_planet_a[i]*1000)))), "m/s") #print
	#print(nazwy_planet[i], ": Średnia prędkość orbitalna to ",math.sqrt(parametr_grawitacyjny[0]*((2/(dystans_planet[i]*1000))-(1/(dystans_planet_a[i]*1000)))), "m/s") #print
	#print(nazwy_planet[i], ": Prędkość orbitalna przy apohelium to ",math.sqrt(parametr_grawitacyjny[0]*((2/(dystans_planet_aphelion[i]*1000))-(1/(dystans_planet_a[i]*1000)))), "m/s") #print	
	#
	
	dystans_jeden_dzień = (math.sqrt(parametr_grawitacyjny[0]*((2/(dystans_planet[i]*1000))-(1/(dystans_planet_a[i]*1000))))) * (60*60*24)
	
	if i>0:
		print(nazwy_planet[i], ": Dystans pokonywany przy średniej prędkości w jeden dzień:", dystans_jeden_dzień, "m.")	
		print(nazwy_planet[i], ": Dystans pokonywany przy średniej prędkości w dokładnie 1 rok planety", dystans_jeden_dzień*(rok_planet[i]), "m.")	
		print(nazwy_planet[i], ": Obwód orbity, który jest rysowany: ", math.pi*(dystans_planet_a[i]+dystans_planet_b[i])*1000)	
		print(nazwy_planet[i], ": Wyliczona pokonywana trasa  przez rok podzielona przez używany obwód:", dystans_jeden_dzień*(rok_planet[i]) / (math.pi*(dystans_planet_a[i]+dystans_planet_b[i])*1000),"\n")	


#rysowanie pustej czarnej planszy
	
	
plansza = Canvas(okno, bg="black")
plansza.place(x = 10, y = 10, width=801, height=801)

#podawanie skali
Label_podaj_skale = tk.Label(okno, text="Rozmiar słońca to 1.391.980 km.\nZamiast przecinka użyj kropki.\nNajedź powoli myszką, żeby wypełnić orbitę.", borderwidth=0, bg="black", fg="white", font=("Helvetica", 12))
Label_podaj_skale.place(x = 850, y = 10, width=350)

Label_infoskala1 = tk.Label(okno, text="1 piksel = ", borderwidth=0, anchor = NW, justify=LEFT)
Label_infoskala1.place(x = 850, y = 84, width=100)
Label_infoskala1 = tk.Label(okno, text="km.", borderwidth=0, anchor = NW, justify=LEFT)
Label_infoskala1.place(x = 1010, y = 84, width=100)

EntrySkala	= Entry(okno)

##!!!!
##!!!!
##!!!!
##!!!!
##!!!!
##!!!!
skala = 20000000 #POCZĄTKOWA SKALA, rozmiar słońca to w rzeczywistości 1391980 km
EntrySkala.insert(0,skala) 
##!!!!
##!!!!
##!!!!
##!!!!
##!!!!
##!!!!
EntrySkala.place(x = 905, y = 80, width=100, height=25)


##MENU

czy_orbity = IntVar()
Check_czy_orbity = Checkbutton(okno, text="Wyświetlaj orbity", variable=czy_orbity, onvalue=1, offvalue=0)
Check_czy_orbity.place(x = 850, y = 110, height=20)
Check_czy_orbity.select()

czy_wypelnienie_orbit = IntVar()
Check_wypelnienie_orbit = Checkbutton(okno, text="Wypełniaj orbity kolorem", variable=czy_wypelnienie_orbit, onvalue=1, offvalue=0)
Check_wypelnienie_orbit.place(x = 880, y = 135, height=20)
Check_wypelnienie_orbit.select()

czy_nazwy_planet = IntVar()
Check_czy_nazwy_planet = Checkbutton(okno, text="Wyświetlaj nazwy", variable=czy_nazwy_planet, onvalue=1, offvalue=0)
Check_czy_nazwy_planet.place(x = 850, y = 160, height=20)
Check_czy_nazwy_planet.select()

czy_ta_sama_srednica = IntVar()
Check_czy_ta_sama_srednica = Checkbutton(okno, text="MODEL: Ta sama średnica obiektów", variable=czy_ta_sama_srednica, onvalue=1, offvalue=0)
Check_czy_ta_sama_srednica.place(x = 850, y = 185, height=20)
EntrySrednicaObiektow	= Entry(okno)
EntrySrednicaObiektow.insert(0,20) 
EntrySrednicaObiektow.place(x = 880, y = 210, width=100, height=25)

czy_wlasna_srednica_slonca = IntVar()
Check_czy_wlasna_srednica_slonca = Checkbutton(okno, text="MODEL: Własna średnica Słońca", variable=czy_wlasna_srednica_slonca, onvalue=1, offvalue=0)
Check_czy_wlasna_srednica_slonca.place(x = 850, y = 235, height=20)
EntrySrednicaSlonca	= Entry(okno)
EntrySrednicaSlonca.insert(0,20) 
EntrySrednicaSlonca.place(x = 880, y = 260, width=100, height=25)

czy_ten_sam_dystans = IntVar()
Check_czy_ten_sam_dystans = Checkbutton(okno, text="MODEL: Ten sam dystans między obiektami [wymaga wyłączenia na dole peryhelium i aphelium]", variable=czy_ten_sam_dystans, onvalue=1, offvalue=0)
Check_czy_ten_sam_dystans.place(x = 850, y = 285, height=20)
EntryDystansObiektow	= Entry(okno)
EntryDystansObiektow.insert(0,40) 
EntryDystansObiektow.place(x = 880, y = 310, width=100, height=25)

Label_interwaly_animacja = tk.Label(okno, text="Określ interwał między klatkami (s)", borderwidth=0, anchor = NW, justify=LEFT)
Label_interwaly_animacja.place(x = 850, y = 335)
EntryInterwalyKlatekAnimacja	= Entry(okno)
EntryInterwalyKlatekAnimacja.insert(0,"1.0") 
EntryInterwalyKlatekAnimacja.place(x = 880, y = 360, height=25)

Label_ile_dni_animacja = tk.Label(okno, text="Określ ile dni przypada na interwał", borderwidth=0, anchor = NW, justify=LEFT)
Label_ile_dni_animacja.place(x = 850, y = 385)
EntryIle_dni_Animacja	= Entry(okno)
EntryIle_dni_Animacja.insert(0,"10") 
EntryIle_dni_Animacja.place(x = 880, y = 410,height=25)

czy_elipse = IntVar()
Check_czy_elipse = Checkbutton(okno, text="Zaznacz: peryhelium i aphelium; odznacz: średni dystans", variable=czy_elipse, onvalue=1, offvalue=0)
Check_czy_elipse.place(x = 850, y = 435, height=20)
Check_czy_elipse.select()

def czytaj_skale():
	global skala
	skala = float(EntrySkala.get())
	print("Wczytałem skalę. Skala to {}".format(skala))
	plansza.delete("all")
	generuj_nowa_plansze()
 ##przy pierwszym rysowaniu

def lewyklick_czytaj_skale():
	czytaj_skale()

def pokaz_tabele():
	okno_tabela = Tk()
	Label_tabela_skala1 = tk.Label(okno_tabela, text="Skala:", borderwidth=0, font=("Helvetica 12 bold"))
	Label_tabela_skala1.grid(row=0, column=0)
	Label_tabela_skala1 = tk.Label(okno_tabela, text="1 px = {} km".format(skala), borderwidth=0, bg="red", fg="white", font=("Helvetica 12 bold"))
	Label_tabela_skala1.grid(row=0, column=1)

	
	Label_tabela_skala1 = tk.Label(okno_tabela, text="Średnica\n[mapa][px]", borderwidth=0, font=("Helvetica 12 bold"))
	Label_tabela_skala1.grid(row=1, column=1)
	
	Label_tabela_skala1 = tk.Label(okno_tabela, text="Średnica\n[real][km]", borderwidth=0, font=("Helvetica 12 bold"))
	Label_tabela_skala1.grid(row=1, column=2)
	
	Label_tabela_skala1 = tk.Label(okno_tabela, text="Dystans do słońca\n[mapa][px]", borderwidth=0, font=("Helvetica 12 bold"))
	Label_tabela_skala1.grid(row=1, column=3)
	
	Label_tabela_skala1 = tk.Label(okno_tabela, text="Dystans do słońca\n[real][km]", borderwidth=0, font=("Helvetica 12 bold"))
	Label_tabela_skala1.grid(row=1, column=4)
	
	Label_tabela_skala1 = tk.Label(okno_tabela, text="Rok\n[dni ziemskie]", borderwidth=0, font=("Helvetica 12 bold"))
	Label_tabela_skala1.grid(row=1, column=5)
	for i in range (10):
		label_nazwa_planety = tk.Label(okno_tabela, text="{}".format(nazwy_planet[i]), borderwidth=0, bg=kolory_planet[i], fg="black", width="10", font=("Helvetica 12"))



		label_srednica_mapa = tk.Label(okno_tabela, text="{}".format(srednica_planet[i]/skala), borderwidth=0, font=("Helvetica 12"))
		label_srednica_real = tk.Label(okno_tabela, text="{}".format(srednica_planet[i]), borderwidth=0,  font=("Helvetica 12"))

		if i>0:
			label_dystans_mapa = tk.Label(okno_tabela, text="{}".format(dystans_planet[i]/skala), borderwidth=0, font=("Helvetica 12"))
		else:
			label_dystans_mapa = tk.Label(okno_tabela, text="-", borderwidth=0, font=("Helvetica 12"))

		if i>0:
			label_dystans_real = tk.Label(okno_tabela, text="{}".format(dystans_planet[i]), borderwidth=0,   font=("Helvetica 12"))
		else:
			label_dystans_real = tk.Label(okno_tabela, text="-", borderwidth=0,   font=("Helvetica 12"))

		if i>0:
			label_rok = tk.Label(okno_tabela, text="{}".format(rok_planet[i]), borderwidth=0, font=("Helvetica 12"))
		else:
			label_rok = tk.Label(okno_tabela, text="-", borderwidth=0, font=("Helvetica 12"))

		label_nazwa_planety.grid(row=i+2, column=0)
		label_srednica_mapa.grid(row=i+2, column=1)
		label_srednica_real.grid(row=i+2, column=2)
		label_dystans_mapa.grid(row=i+2, column=3)
		label_dystans_real.grid(row=i+2, column=4)
		label_rok.grid(row=i+2, column=5)
	
	okno_tabela.mainloop(0)
def lewyklick_pokaz_tabele():
	pokaz_tabele()

#timer
zoom = False
def wlacz_licznik():
	global skala
	global zoom
	licznik = 0
	while licznik < float(EntryLiczbaKlatekZoom.get()): #włącz automatycznie jeśli powyżej ustawiony jest na 1
	
		licznik = licznik+1
		time.sleep(float(EntryInterwalyKlatekZoom.get()))
		if zoom == False:
			skala = skala + float(EntryDystansZoom.get())
		else:
			skala = skala - float(EntryDystansZoom.get())
			if skala < 1:
				skala = 1

		Label_policzone_dni = tk.Label(okno, text="Klatki: {}".format(licznik), borderwidth=0, anchor = NW, justify=LEFT)
		Label_policzone_dni.state = DISABLED
		EntrySkala.delete(0, END)
		EntrySkala.insert(0,skala)
		Label_policzone_dni.place(x = 960, y = 750)
		plansza.delete("all")
		generuj_nowa_plansze()
		okno.update()
		
def lewyklick_zoom_minus():
	global zoom
	zoom = False
	wlacz_licznik()
def lewyklick_zoom_plus():
	global zoom
	zoom = True	
	wlacz_licznik()	

	
ster_wskaznik = 50	
EntrySter	= Entry(okno)
EntrySter.insert(0,100) 
EntrySter.place(x = 120, y = 850, width=50, height=25)
Label_ster = tk.Label(okno, text="Zmień pozycję o x pikseli.", anchor = NW, justify=LEFT)
Label_ster.place(x = 175, y = 850)
def lewyklick_ster_w_lewo():
	global koordynaty_globalne
	ster_wskaznik = float(EntrySter.get())
	koordynaty_globalne[0] = koordynaty_globalne[0]-ster_wskaznik
	koordynaty_globalne[2] = koordynaty_globalne[2]-ster_wskaznik
	plansza.delete("all")
	generuj_nowa_plansze()
def lewyklick_ster_w_prawo():
	global koordynaty_globalne
	ster_wskaznik = float(EntrySter.get())
	koordynaty_globalne[0] = koordynaty_globalne[0]+ster_wskaznik
	koordynaty_globalne[2] = koordynaty_globalne[2]+ster_wskaznik
	plansza.delete("all")
	generuj_nowa_plansze()
def lewyklick_ster_centruj():
	global koordynaty_globalne
	koordynaty_globalne = [400,400,400,400]
	plansza.delete("all")
	generuj_nowa_plansze()
def lewyklick_ster_w_gore():
	global koordynaty_globalne
	ster_wskaznik = float(EntrySter.get())
	koordynaty_globalne[1] = koordynaty_globalne[1]-ster_wskaznik
	koordynaty_globalne[3] = koordynaty_globalne[3]-ster_wskaznik
	plansza.delete("all")
	generuj_nowa_plansze()
def lewyklick_ster_w_dol():
	global koordynaty_globalne
	ster_wskaznik = float(EntrySter.get())
	koordynaty_globalne[1] = koordynaty_globalne[1]+ster_wskaznik
	koordynaty_globalne[3] = koordynaty_globalne[3]+ster_wskaznik
	plansza.delete("all")
	generuj_nowa_plansze()
		
	
#rysowanie przycisków
Przycisk_czytaj_skale = tk.Button(okno, text ="Wczytaj dane i rysuj mapę ponownie",  bd=2, command = lewyklick_czytaj_skale)
Przycisk_czytaj_skale.place(x = 850, y = 600, width=200, height=50) 
	
Przycisk_pokaz_tabele = tk.Button(okno, text ="Pokaż tabelę z wymiarami",  bd=2, command = lewyklick_pokaz_tabele)
Przycisk_pokaz_tabele.place(x = 850, y = 675, width=200, height=50) 

Przycisk_pomniejsz = tk.Button(okno, text ="–",  bd=2, command = (lewyklick_zoom_minus), font="Helvetica 30")
Przycisk_pomniejsz.place(x = 850, y = 780, width=50, height=75) 

Przycisk_powieksz = tk.Button(okno, text ="+",  bd=2, command = (lewyklick_zoom_plus), font="Helvetica 30")
Przycisk_powieksz.place(x = 905, y = 780, width=50, height=75)





Przycisk_ster_w_lewo = tk.Button(okno, text ="◄",  bd=2, command = (lewyklick_ster_w_lewo), font="Helvetica 15")
Przycisk_ster_w_lewo.place(x = 20, y = 850, width=30, height=30) 

Przycisk_ster_w_prawo = tk.Button(okno, text ="►",  bd=2, command = (lewyklick_ster_w_prawo), font="Helvetica 15")
Przycisk_ster_w_prawo.place(x = 80, y = 850, width=30, height=30)

Przycisk_ster_centruj = tk.Button(okno, text ="C",  bd=2, command = (lewyklick_ster_centruj), font="Helvetica 15")
Przycisk_ster_centruj.place(x = 50, y = 850, width=30, height=30) 

Przycisk_ster_w_gore = tk.Button(okno, text ="▲",  bd=2, command = (lewyklick_ster_w_gore), font="Helvetica 15")
Przycisk_ster_w_gore.place(x = 50, y = 820, width=30, height=30) 

Przycisk_ster_w_dol = tk.Button(okno, text ="▼",  bd=2, command = (lewyklick_ster_w_dol), font="Helvetica 15")
Przycisk_ster_w_dol.place(x = 50, y = 880, width=30, height=30)


Label_interwaly_zoom = tk.Label(okno, text="Interwał między klatkami (s)", borderwidth=0, anchor = NW, justify=LEFT)
Label_interwaly_zoom.place(x = 960, y = 780)
EntryInterwalyKlatekZoom	= Entry(okno)
EntryInterwalyKlatekZoom.insert(0,"0.001") 
EntryInterwalyKlatekZoom.place(x = 1110, y = 780, height=25, width=80)

Label_dystans_zoom = tk.Label(okno, text="Zmiana skali (km)", borderwidth=0, anchor = NW, justify=LEFT)
Label_dystans_zoom.place(x = 960, y = 810)
EntryDystansZoom	= Entry(okno)
EntryDystansZoom.insert(0,"198000") 
EntryDystansZoom.place(x = 1110, y = 810,height=25,  width=80)

Label_liczba_klatek_zoom = tk.Label(okno, text="Podaj liczbę klatek", borderwidth=0, anchor = NW, justify=LEFT)
Label_liczba_klatek_zoom.place(x = 960, y = 840)
EntryLiczbaKlatekZoom	= Entry(okno)
EntryLiczbaKlatekZoom.insert(0,"100") 
EntryLiczbaKlatekZoom.place(x = 1110, y = 840,height=25,  width=80)
	
srodek = [400,400]
sr_roboczy = [400,400]
lewy_gorny = [400,400]
prawy_dolny = [400,400]
koordynaty_globalne = [400,400,400,400]
koordynaty = [400,400,400,400] #zawsze robocze
koordynaty_slonca = [400,400,400,400]
srednica = 0
dystans = 0

def generuj_nowa_plansze():
	def resetuj_wartosci_robocze():
		global sr_roboczy
		global lewy_gorny
		global prawy_dolny
		global koordynaty
		global srednica
		global koordynaty_globalne
		sr_roboczy = [400,400]
		lewy_gorny = [400,400]
		prawy_dolny = [400,400]
		koordynaty[0] = koordynaty_globalne[0]
		koordynaty[1] = koordynaty_globalne[1]
		koordynaty[2] = koordynaty_globalne[2]
		koordynaty[3] = koordynaty_globalne[3]		
		srednica = 0 
		dystans = 0



#rysowanie planet
	def rysuj_orbite_i_planete(i):
		global skala
		global koordynaty
		global koordynaty_nowe_planety
		j = 9-i ##to rozpierdala ster
		#tutaj sprawdza model "ta sama średnica dla wszystkich"
		if czy_ta_sama_srednica.get() == 1:
			srednica = float(EntrySrednicaObiektow.get())
		else:	
			srednica = srednica_planet[j]/skala
		
		#ale i tak musi sprawdzić czy słońce ma customowy rozmiar
		if j ==0:
			if czy_wlasna_srednica_slonca.get() == 1:
				srednica = float(EntrySrednicaSlonca.get())
				
		#test na dystanse		
		if czy_ten_sam_dystans.get() == 1:
			dystans = j*float(EntryDystansObiektow.get())
		else:
			dystans = dystans_planet[j]/skala
		dystans_aphelion = dystans_planet_aphelion[j]/skala
		dystans_perihelion = dystans_planet_perihelion[j]/skala
		dystans_a = dystans_planet_a[j]/skala
		dystans_b = dystans_planet_b[j]/skala
		dystans_c = dystans_planet_c[j]/skala
	#rysuj orbitę
	#test na perihelion	
		if czy_elipse.get() == 0:
			koordynaty[0] = koordynaty[0]-dystans 
			koordynaty[1] = koordynaty[1]-dystans
			koordynaty[2] = koordynaty[2]+dystans
			koordynaty[3] = koordynaty[3]+dystans
		else:
			#koordynaty[0] = koordynaty[0]-dystans_perihelion  #to ten krótszy
			#koordynaty[1] = koordynaty[1]-dystans_aphelion
			#koordynaty[2] = koordynaty[2]+dystans_perihelion  
			#koordynaty[3] = koordynaty[3]+dystans_aphelion
			koordynaty[0] = koordynaty[0]-dystans_b
			koordynaty[1] = koordynaty[1]-dystans_a-dystans_c
			koordynaty[2] = koordynaty[2]+dystans_b 
			koordynaty[3] = koordynaty[3]+dystans_a-dystans_c		
		
		if czy_orbity.get() == 1:
			if czy_wypelnienie_orbit.get() == 1:	
				orbita_planety = plansza.create_oval(koordynaty, outline="white", activefill=kolory_planet[j])
			else:			
				orbita_planety = plansza.create_oval(koordynaty, outline="white")
	

	
	
		#alpha = float(EntryIle_dni.get())*360 / rok_planet[3]  #wyrzuci błąd dla słońca, bo dzieli przez zero
		#beta = (180-alpha)/2
		#bogen = (math.pi * dystans * alpha) / 180
		#funkcja = koordynaty[0]*(alpha/90)+400
		#
		#print(beta)
		#print(bogen)
#rysuj planetę
		if czy_elipse.get() == 0:
			koordynaty[0] = koordynaty[0]+dystans
			koordynaty[1] = koordynaty[1]
			koordynaty[2] = koordynaty[2]-dystans
			koordynaty[3] = koordynaty[3]-dystans*2
			koordynaty_nowe_planety[j][0] = koordynaty[0] #zapisywanie kropki
			koordynaty_nowe_planety[j][1] = koordynaty[1]
			koordynaty_nowe_planety[j][2] = koordynaty[2]
			koordynaty_nowe_planety[j][3] = koordynaty[3]
			print(nazwy_planet[j], ": Nowe koordynaty planety:", koordynaty_nowe_planety[j])
			koordynaty[0] = koordynaty[0]-(srednica/2) #rysowanie kółka o danym rozmiarze
			koordynaty[1] = koordynaty[1]-(srednica/2)
			koordynaty[2] = koordynaty[2]+(srednica/2)
			koordynaty[3] = koordynaty[3]+(srednica/2)
		else:
			koordynaty[0] = koordynaty[0]+dystans_b 
			koordynaty[1] = koordynaty[1]
			koordynaty[2] = koordynaty[2]-dystans_b
			koordynaty[3] = koordynaty[3]-dystans_a*2
			koordynaty_nowe_planety[j][0] = koordynaty[0] #zapisywanie kropki
			koordynaty_nowe_planety[j][1] = koordynaty[1]
			koordynaty_nowe_planety[j][2] = koordynaty[2]
			koordynaty_nowe_planety[j][3] = koordynaty[3]
			print(nazwy_planet[j], ": Nowe koordynaty planety:", koordynaty_nowe_planety[j])
			koordynaty[0] = koordynaty[0]-(srednica/2) 
			koordynaty[1] = koordynaty[1]-(srednica/2)
			koordynaty[2] = koordynaty[2]+(srednica/2)
			koordynaty[3] = koordynaty[3]+(srednica/2)
			
		#print("\n{}\nKoordynaty planety {} to: {},\nŚrednica planety na planszy to {} px.\nDystans planety do słońca to {} px.".format(nazwy_planet[j],nazwy_planet[j],koordynaty,srednica,dystans))
		planeta_stworzona = plansza.create_oval(koordynaty, outline=kolory_planet[j], fill=kolory_planet[j])
	
	
	
	##  	(x-400)^2+(y-400)^2 = dystans^2  ##formuła koła z 400,400 po środku
	#		x^2-800x+1600 + y^2-800y+1600  = dystans^2
	#
	#		alpha =  360 / 365,26  ##wylicza kąt na 1 dzień
	#		
	#		bogen = (Pi * dystans * alpha) / 180
	#		sekante_länge = 2*dystans * sinus (alpha/2)		
	#
	#
	#
	#rysuj nazwę planety
		if czy_nazwy_planet.get() == 1:
			koordynaty[0] = ((koordynaty[0]+koordynaty[2])/2)+50
			koordynaty[1] = (koordynaty[1]+koordynaty[3])/2

			plansza.create_text(koordynaty[0],koordynaty[1],text=nazwy_planet[j], fill="white")
		resetuj_wartosci_robocze()
		
	for i in range(10):	
		rysuj_orbite_i_planete(i)	
		
	


lewyklick_zoom_plus()

	

okno.mainloop(0)





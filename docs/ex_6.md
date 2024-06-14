# Zadanie 6

Zaobserwuj działanie następujących przekształceń punktowych na
przykładowych obrazach:   
1. Mnożenie obrazu przez stałą.  
Obrazy: chest_xray.tif, pollen-dark.tif, spectrum.tif.   
2. Transformację logarytmiczną.  
Obraz: spectrum.tif.  
3. Zmianę dynamiki skali szarości (kontrastu).  
Obrazy: chest_xray.tif, einstein-low-contrast.tif, pollen-lowcontrast.tif.  
4. Korekcję gamma.  
Obraz: aerial_view.tif.

---

**1. Mnożenie obrazu przez stałą**  
Mnożenie obrazu przez stałą, zwane również skalowaniem intensywności lub jasności obrazu, powoduje równomierne zwiększenie lub zmniejszenie jasności wszystkich pikseli w obrazie.  

```python
c = 5
image = c * image
```
![6a_1](<Zadanie 6/6_a1.PNG>)
![6a_2](<Zadanie 6/6_a2.PNG>)

---

**2. Transformacja logarytmiczna**  
Transformacja logarytmiczna obrazu jest techniką, która stosuje funkcję logarytmiczną do przekształcenia wartości pikseli. Jest to szczególnie przydatne w zwiększaniu widoczności szczegółów w ciemniejszych obszarach obrazu bez nadmiernego rozjaśniania jaśniejszych obszarów.

```python
c = 5
image = c * np.log(1 + (image))
```
![6b_1](<Zadanie 6/6_b1.PNG>)
![6b_2](<Zadanie 6/6_b2.PNG>)

---
**3. Zmiana dynamiki skali szarości (kontrastu)**  
Zmiana dynamiki skali szarości jest techniką stosowaną w celu poprawy widoczności i jakości obrazu. Polega ona na rozciągnięciu zakresu wartości jasności (lub szarości) pikseli w obrazie tak, aby obejmował cały dostępny zakres intensywności.

```python
m = 0.45
e = 4
image = 1 / (1 + np.float_power((m/image),e))
```
![6c_1](<Zadanie 6/6_c1.PNG>)
![6c_2](<Zadanie 6/6_c2.PNG>)

---
**4. Korekcja gamma**  
Korekcja gamma obrazu to technika mająca na celu dostosowanie jasności i kontrastu obrazu w sposób nieliniowy. Proces ten polega na przekształceniu wartości jasności pikseli za pomocą funkcji potęgowej, co pozwala na bardziej naturalne i realistyczne odwzorowanie obrazu na różnych ekranach.

```python
c = 5
gamma = 5
image = c * np.float_power(image,gamma)
```
![6d_1](<Zadanie 6/6_d1.PNG>)
![6d_2](<Zadanie 6/6_d2.PNG>)
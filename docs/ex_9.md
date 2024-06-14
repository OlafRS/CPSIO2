# Zadanie 9

Zbadaj skuteczność redukcji szumu typu „sól i pieprz” za pomocą  
- liniowego filtra uśredniającego z kwadratową maską, rozpoczynając od maski rozmiaru 3 × 3.  
- nieliniowego filtra medianowego  
- filtrów minimum i maksimum.  
Dane: cboard_pepper_only.tif, cboard_salt_only.tif, cboard_salt_pepper.tif  

---

Szumy typu sól i pieprz, zwane także szumami impulsowymi, to rodzaj zakłóceń, które mogą występować w obrazach cyfrowych. Charakteryzują się one pojawieniem losowych jasnych (sól) i ciemnych (pieprz) pikseli, które znacząco różnią się od otaczających ich wartości pikseli. Te szumy są zazwyczaj spowodowane błędami w transmisji danych, defektami w czujnikach obrazu lub zakłóceniami elektrycznymi.  
![9_1](<Zadanie 9/9_1.PNG>)

---
## Sól i pieprz

**liniowy filtr uśredniający z kwadratową maską**
```python
footprint = morphology.rectangle(3,3)
image = filters.rank.mean(image, footprint = footprint)
```
![9a](<Zadanie 9/9a.PNG>)

**nieliniowy filtr medianowy**
```python
footprint = morphology.disk(5)
image = filters.median(image, footprint = footprint)
```
![9b](<Zadanie 9/9b.PNG>)

**filtr minimum**
```python
footprint = morphology.rectangle(3,3)
image = filters.rank.minimum(image, footprint = footprint)
```
![9c_min_sp](<Zadanie 9/9c_min_sp.PNG>)

**filtr maksimum**
```python
footprint = morphology.rectangle(3,3)
image = filters.rank.maximum(image, footprint = footprint)
```
![9c_max_sp](<Zadanie 9/9c_max_sp.PNG>)

---
## Sól

**filtr minimum**
```python
footprint = morphology.rectangle(3,3)
image = filters.rank.minimum(image, footprint = footprint)
```
![9c_min_salt](<Zadanie 9/9c_min_salt.PNG>)

---
## Pieprz

**filtr maksimum**
```python
footprint = morphology.rectangle(3,3)
image = filters.rank.maximum(image, footprint = footprint)
```
![9c_max_pepper](<Zadanie 9/9c_max_pepper.PNG>)

---
## Wnioski
Z naszych badań wynika, że najlepszym filtrem do redukcji szumów typu sól i pieprz jest nieliniowy filtr medianowy. Liniowy filtr uśredniający z kwadratową maską radzi sobie trochę gorzej, ale nadal dość dobrze. Filtry maksimum i minimum nie nadają się do redukcji szumów tego typu. Inaczej jest, gdy mamy same szumy typu sól albo same szumy typu pieprz. Dla szumów typu sól filtr minimum działa idealnie, a dla szumów typu pieprz filtr maksimum działa idealnie.
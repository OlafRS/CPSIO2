# Zadanie 7

Wypróbuj działanie wyrównywania histogramu na przykładowych obrazach. By zaobserwować skuteczność procedury poddaj wyrównywaniu obrazy zbyt ciemne i zbyt jasne. Narysować histogramy obrazów przed i po wyrównaniu.  
Obrazy: chest_xray.tif, pollen-dark.tif, pollen-ligt.tif, pollen-lowcontrast.tif, pout.tif, spectrum.tif.  

---

Wyrównywanie histogramu jest techniką która ma na celu poprawę kontrastu obrazu poprzez równomierne rozłożenie wartości jasności pikseli. Proces ten jest szczególnie użyteczny w przypadkach, gdy obraz ma ograniczony zakres dynamiczny, co prowadzi do słabo widocznych szczegółów. Matematycznie, wyrównywanie histogramu działa poprzez przekształcenie wartości intensywności pikseli w taki sposób, aby histogram obrazu po przekształceniu był jak najbardziej płaski, czyli aby każda wartość intensywności była reprezentowana przez podobną liczbę pikseli. Dzięki wyrównywaniu histogramu możliwe jest uzyskanie obrazów o lepszej jakości.

---
**Obraz zbyt jasny**  
  
Przed wyrównaniem:  
![7l1](<Zadanie 7/7_light1.PNG>)
```python
histogram = cv2.calcHist([image],[0],None,[256],[0,256])
```
![7l1hist](<Zadanie 7/7_light1hist.PNG>)
  
Po wyrównaniu:
```python
image = cv2.equalizeHist(image)  
```
![7l2](<Zadanie 7/7_light2.PNG>)
```python
histogram = cv2.calcHist([image],[0],None,[256],[0,256])
```
![7l2hist](<Zadanie 7/7_light2hist.PNG>)

---
**Obraz zbyt ciemny**  
  
Przed wyrównaniem:  
![7d1](<Zadanie 7/7_dark1.PNG>)
![7d1hist](<Zadanie 7/7_dark1hist.PNG>)
  
Po wyrównaniu:  
![7d2](<Zadanie 7/7_dark2.PNG>)
![7d2hist](<Zadanie 7/7_dark2hist.PNG>)

---
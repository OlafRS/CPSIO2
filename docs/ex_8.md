# Zadanie 8

Sprawdź działanie lokalnych kontekstowych omówionych na wykładzie pt. „Transformacje poziomu jasności” jako lokalne wyrównywanie histogramu.  
Obraz: hidden-symbols.tif

---

Lokalne wyrównanie histogramu jest techniką przetwarzania obrazu, która polega na poprawie kontrastu w mniejszych, lokalnych obszarach obrazu zamiast na całym obrazie jednocześnie. Proces ten jest szczególnie użyteczny w sytuacjach, gdzie różne części obrazu mają różne charakterystyki jasności i kontrastu.

---
![8_1](<Zadanie 8/8_1.PNG>)

```python
footprint = morphology.rectangle(3,3)
image = filters.rank.equalize(image, footprint=footprint)
```

![8_2](<Zadanie 8/8_2.PNG>)
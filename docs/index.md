# Cyfrowe przetwarzanie sygnałów i obrazów

## Laboratorium: Przetwarzanie obrazów w dziedzinie przestrzennej

### Wstęp
W ramach tego laboratorium, zostały wykonane zadania związane z przetwarzaniem obrazów w dziedzinie przestrzennej za pomocą języka programowania Python. Celem było zdobycie umiejętności wczytywania, przetwarzania, analizowania oraz filtrowania obrazów. Do obliczeń użyliśmy biblioteki numpy. Do stworzenia interfejsu oraz rysowania wykresów użyliśmy bibliotek 'tkinter' oraz 'matplotlib'. Do przetwarzania obrazów użyliśmy biblioteki 'scikit-image'. Do tworzenia histogramów użyliśmy biblioteki 'cv2'. Linki do dokumentacji poszczególnych bibliotek znajdują się na dole tej strony.

### Plan ćwiczeń laboratoryjnych
5. **Platforma testowa**
6. **Przekształcanie punktowe**
7. **Histogram obrazu**
8. **Histogram obrazu**
9. **Filtracja dolnoprzepustowa**
10. **Filtracja dolnoprzepustowa**
11. **Filtracja górnoprzepustowa**
12. **Poprawa jakości poprzez wieloetapowe przetwarzanie**

### Szczegóły zadań

#### Ćwiczenie 5: Platforma testowa
Napisz skrypt w Pythonie/Matlabie umożliwiający wczytywanie i wizualizację badanych obrazów. Program powinien umożliwiać  
1. wyświetlanie obrazu wczytanego z pliku o podanej nazwie,  
2. sporządzenie wykresów zmian poziomu szarości wzdłuż wybranej linii poziomej
lub pionowej o zadanej współrzędnej,  
3. wybór podobrazu (prostokątnego obszaru) o podanych współrzędnych oraz jego
zapis do pliku o zadanej nazwie.

#### Ćwiczenie 6: Przekształcanie punktowe

**Zadania:**
1. Zaobserwuj działanie następujących przekształceń punktowych na
przykładowych obrazach:   
- Mnożenie obrazu przez stałą.  
Obrazy: chest_xray.tif, pollen-dark.tif, spectrum.tif.   
- Transformację logarytmiczną.  
Obraz: spectrum.tif.  
- Zmianę dynamiki skali szarości (kontrastu).  
Obrazy: chest_xray.tif, einstein-low-contrast.tif, pollen-lowcontrast.tif.  
- Korekcję gamma.  
Obraz: aerial_view.tif.

#### Ćwiczenia 7-8: Histogram obrazu

**Zadania:**
1. Wypróbuj działanie wyrównywania histogramu na przykładowych obrazach. By zaobserwować skuteczność procedury poddaj wyrównywaniu obrazy zbyt ciemne i zbyt jasne. Narysować histogramy obrazów przed i po wyrównaniu.  
Obrazy: chest_xray.tif, pollen-dark.tif, pollen-ligt.tif, pollen-lowcontrast.tif, pout.tif, spectrum.tif.  
2. Sprawdź działanie lokalnych kontekstowych omówionych na wykładzie pt. „Transformacje poziomu jasności” jako lokalne wyrównywanie histogramu.  
Obraz: hidden-symbols.tif


#### Ćwiczenia 9-10: Filtracja dolnoprzepustowa

**Zadania:**
1. Zbadaj skuteczność redukcji szumu typu „sól i pieprz” za pomocą  
- liniowego filtra uśredniającego z kwadratową maską, rozpoczynając od maski
rozmiaru 3 × 3.  
- nieliniowego filtra medianowego  
- filtrów minimum i maksimum.  
Dane: cboard_pepper_only.tif, cboard_salt_only.tif, cboard_salt_pepper.tif  
2. Zbadaj działanie dolnoprzepustowych filtrów uśredniającego i gaussowskiego dla danych obrazów. Zaobserwuj wpływ rozmiaru masek na wynik filtracji.  
Dane: characters_test_pattern.tif, zoneplate.tif.  

#### Ćwiczenie 11: Filtracja górnoprzepustowa

**Zadania:**
1. Wykrywanie krawędzi obiektów i poprawa ostrości.  
- Użyj filtra z maską Sobela do wykrywania krawędzi poziomych, pionowych i ukośnych.  
Dane: circuitmask.tif, testpat1.png  
- Zaobserwuj działanie Laplasjanu do wyostrzania szczegółów.  
Dane: blurry-moon.tif  
- Zbadaj działanie filtrów typu „unsharp masking” i „high boost”.  
Dane: text-dipxe-blurred.tif

#### Ćwiczenie 12: Poprawa jakości poprzez wieloetapowe przetwarzanie

**Zadania:**
1. Naszym celem jest poprawa jakości obrazu za pomocą kolejnego stosowania różnych przekształceń i filtrów. Zastosuj złożone, wieloetapowe podejście do poprawy jakości przedstawione na wykładzie pt. „Filtracja w dziedzinie przestrzennej”.  
Dane: bonescan.tif.

### Bibliografia
1. Dokumentacja `numpy`: [link](https://numpy.org/doc/stable/reference/)
2. Dokumentacja `Matplotlib`: [link](https://matplotlib.org/)
3. Dokumentacja `tkinter`: [link](https://docs.python.org/3/library/tkinter.html)
4. Dokumentacja `cv2`: [link](https://pypi.org/project/opencv-python/)
5. Dokumentacja `scikit-image`: [link](https://scikit-image.org/docs/stable/api/skimage.html)
6. `Python` Tutorial: [link](https://docs.python.org/3/tutorial/)
# Zadanie 5


Napisz skrypt w Pythonie/Matlabie umożliwiający wczytywanie i wizualizację badanych obrazów. Program powinien umożliwiać  
1. wyświetlanie obrazu wczytanego z pliku o podanej nazwie,  
2. sporządzenie wykresów zmian poziomu szarości wzdłuż wybranej linii poziomej
lub pionowej o zadanej współrzędnej,  
3. wybór podobrazu (prostokątnego obszaru) o podanych współrzędnych oraz jego
zapis do pliku o zadanej nazwie.

---

## Platforma testowa

Na zdjęciu znajduje się interfejs graficzny aplikacji, która służy do analizy i przetwarzania obrazów. po załadowaniu przykładowego obrazu. Aplikacja posiada górny panel z przyciskami i polami tekstowymi umożliwiającymi użytkownikowi różne operacje na danych.

![wygląd aplikacji z przykładowym obrazem](<Zadanie 5/5-2_example.PNG>)

### Wygląd i Funkcjonalność Aplikacji

---

#### Górny panel

![Górny panel](<Zadanie 5/5-1_options.PNG>)

---
- **Horizontal / Vertical**: Te przyciski odwołują się do wykresu przedstawiającego zmianę szarości obrazu. Za ich pomocą możemy wybrać czy chcemy badać zmianę szarości w kolumnie czy w wierszu.  
- **Coordinate**: To pole tekstowe również odnosi się do wykresu przedstawiającego zmianę szarości obrazu. W tej linii możemy wybrać dla której kolumny/wiersza podawany jest wykres.  
- **top left x / top left y**: Te pola tekstowe odnoszą się do pod-obrazu. W tych polach możemy wpisać koordynaty górnego lewego kąta pod-obrazu.  
- **bottom right x / bottom right y**: Te pola tekstowe również odnoszą się do pod-obrazu. W tych polach możemy wpisać koordynaty prawego dolnego kąta pod-obrazu.  
- **Load Image**: Ten przycisk umożliwia użytkownikowi wybranie pliku z obrazem.
- **Save Subimage**: Ten przycisk umożliwia użytkownikowi zapisanie pod-obrazu.
- **none, 6a, ...**: To pole zawiera przyciski po których kliknięciu wykona się na obecnie załadowanym obrazie operacja opisana w poleceniu ćwiczenia o odpowiednim numerze. Przyciski w polu można przewijąc za pomocą znajdującego się obok przewijaka.  

---

### Jak Zrobiona Jest Aplikacja

**Ładowaniu obrazu**  
```python
def load_image(file_path):
    image = Image.open(file_path).convert('L')  # Convert image to grayscale
    return np.array(image)

def open_file():
    global image
    global exercise
    top_left = (int(top_left_x_entry.get()),int(top_left_y_entry.get()))
    bottom_right = (int(bottom_right_x_entry.get()),int(bottom_right_y_entry.get()))
    exercise = "none"
    file_path = filedialog.askopenfilename()
    if file_path:
        image = load_image(file_path)
        plot(image, int(coord_entry.get()), direction_var.get(), top_left, bottom_right, canvas_frame, exercise)
```  

**Zapisywanie pod-obrazu**  
```python
def save():
    output_file = "subimage.png"
    top_left = (int(top_left_x_entry.get()),int(top_left_y_entry.get()))
    bottom_right = (int(bottom_right_x_entry.get()),int(bottom_right_y_entry.get()))
    save_subimage(image, top_left, bottom_right, output_file)

def save_subimage(image, top_left, bottom_right, output_file):
    subimage = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    subimage_pil = Image.fromarray(subimage)
    subimage_pil.save(output_file)
```

**Aktualizowanie interfejsu po zmianie  opcji w górnym panelu**
```python
def on_change():
    if image is not None:
        direction = direction_var.get()
        coord = int(coord_entry.get())
        top_left = (int(top_left_x_entry.get()),int(top_left_y_entry.get()))
        bottom_right = (int(bottom_right_x_entry.get()),int(bottom_right_y_entry.get()))
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
```

**Zmiana wybranego ćwiczenia/wybranej operacji**
```python
def on_listbox_select(event):
    direction = direction_var.get()
    coord = int(coord_entry.get())
    top_left = (int(top_left_x_entry.get()),int(top_left_y_entry.get()))
    bottom_right = (int(bottom_right_x_entry.get()),int(bottom_right_y_entry.get()))
    
    # Choose exercise (6a, 6b, 6c, 6d, 7, 8a, 8b, 9a, 9b, 9c, 10, 11a, 11b, 11c, 12)
    selected_option = listbox.get(listbox.curselection())
    if selected_option == 'none':
        exercise = "none"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '6a':
        exercise = "6a"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '6b':
        exercise = "6b"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '6c':
        exercise = "6c"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '6d':
        exercise = "6d"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '7przed':
        exercise = "7przed"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '7po':
        exercise = "7po"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '8a':
        exercise = "8a"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '8b':
        exercise = "8b"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '9a':
        exercise = "9a"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '9b':
        exercise = "9b"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '9cMIN':
        exercise = "9cMIN"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '9cMAX':
        exercise = "9cMAX"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '10':
        exercise = "10"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '11a':
        exercise = "11a"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '11b':
        exercise = "11b"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '11cUNSHARP':
        exercise = "11cUNSHARP"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '11cBOOST':
        exercise = "11cBOOST"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
    elif selected_option == '12':
        exercise = "12"
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)
```

**Inicjalizacja interfejsu graficznego**
```python
# Tkinter setup
root = tk.Tk()
root.title("Image Analysis")

# Frame for controls
control_frame = tk.Frame(root)
control_frame.pack(anchor=tk.N, fill=tk.X)

# Direction selection
direction_var = tk.StringVar(value='horizontal')
tk.Radiobutton(control_frame, text="Horizontal", variable=direction_var, value='horizontal', command=on_change).pack(side=tk.LEFT)
tk.Radiobutton(control_frame, text="Vertical", variable=direction_var, value='vertical', command=on_change).pack(side=tk.LEFT)

# Coordinate entry
coord_label = tk.Label(control_frame, text="Coordinate:")
coord_label.pack(side=tk.LEFT, padx=5)
coord_entry = tk.Entry(control_frame)
coord_entry.pack(side=tk.LEFT)
coord_entry.insert(0, "100")
coord_entry.bind('<Return>', lambda event: on_change())

# Subimage top left
top_left_x_label = tk.Label(control_frame, text="top left x:")
top_left_x_label.pack(side=tk.LEFT, padx=5)
top_left_x_entry = tk.Entry(control_frame)
top_left_x_entry.pack(side=tk.LEFT)
top_left_x_entry.insert(0, "50")
top_left_x_entry.bind('<Return>', lambda event: on_change())

top_left_y_label = tk.Label(control_frame, text="top left y:")
top_left_y_label.pack(side=tk.LEFT, padx=5)
top_left_y_entry = tk.Entry(control_frame)
top_left_y_entry.pack(side=tk.LEFT)
top_left_y_entry.insert(0, "50")
top_left_y_entry.bind('<Return>', lambda event: on_change())

# Subimage bottom right
bottom_right_x_label = tk.Label(control_frame, text="bottom right x:")
bottom_right_x_label.pack(side=tk.LEFT, padx=5)
bottom_right_x_entry = tk.Entry(control_frame)
bottom_right_x_entry.pack(side=tk.LEFT)
bottom_right_x_entry.insert(0, "200")
bottom_right_x_entry.bind('<Return>', lambda event: on_change())

bottom_right_y_label = tk.Label(control_frame, text="bottom right y:")
bottom_right_y_label.pack(side=tk.LEFT, padx=5)
bottom_right_y_entry = tk.Entry(control_frame)
bottom_right_y_entry.pack(side=tk.LEFT)
bottom_right_y_entry.insert(0, "200")
bottom_right_y_entry.bind('<Return>', lambda event: on_change())

# Load image button
load_button = tk.Button(control_frame, text="Load Image", command=open_file)
load_button.pack(side=tk.LEFT, padx=5)

# Save subimage button
save_button = tk.Button(control_frame, text="Save Subimage", command=save)
save_button.pack(side=tk.LEFT, padx=5)

# Listbox for selection
# Choose exercise (6a, 6b, 6c, 6d, 7, 8a, 8b, 9a, 9b, 9c, 10, 11a, 11b, 11c, 12)
listbox_frame = tk.Frame(control_frame)
listbox_frame.pack(side=tk.LEFT, padx=5)
listbox = tk.Listbox(listbox_frame, height=2)
listbox.pack()
listbox.insert(1, "none")
listbox.insert(2, "6a")
listbox.insert(3, "6b")
listbox.insert(4, "6c")
listbox.insert(5, "6d")
listbox.insert(6, "7przed")
listbox.insert(7, "7po")
listbox.insert(8, "8a")
listbox.insert(9, "8b")
listbox.insert(10, "9a")
listbox.insert(11, "9b")
listbox.insert(12, "9cMIN")
listbox.insert(13, "9cMAX")
listbox.insert(14, "10")
listbox.insert(15, "11a")
listbox.insert(16, "11b")
listbox.insert(17, "11cUNSHARP")
listbox.insert(18, "11cBOOST")
listbox.insert(19, "12")
listbox.bind('<<ListboxSelect>>', on_listbox_select)

scrollbar = Scrollbar(control_frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=scrollbar.set)

# Canvas frame for plotting
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill=tk.BOTH, expand=1)

image = None
```

**Sposób rysowania obrazu**
```python
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Display original image
axs[1, 1].imshow(image, cmap='gray')
axs[1, 1].set_title('Początkowy obraz')
axs[1, 1].axis('off')
```

**Wejście do programu (funkcja main)**
```python
if __name__ == '__main__':
    root.mainloop()
```

---
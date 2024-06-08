import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import Scrollbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2
from skimage import morphology
from skimage import filters

def load_image(file_path):
    image = Image.open(file_path).convert('L')  # Convert image to grayscale
    return np.array(image)

def plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    # Display original image
    axs[1, 1].imshow(image, cmap='gray')
    axs[1, 1].set_title('Początkowy obraz')
    axs[1, 1].axis('off')

    # Choose exercise (6a, 6b, 6c, 6d, 7, 8a, 8b, 9a, 9b, 9c, 10, 11a, 11b, 11c, 12)
    if(exercise!="none"):
        if(exercise=="6a"):
            c = 5
            image = c * image
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Mnożenie obrazu przez stałą')
            axs[0, 0].axis('off')
        elif(exercise=="6b"):
            c = 5
            image = c * np.log(1 + (image))
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Transformacja logarytmiczna')
            axs[0, 0].axis('off')
        elif(exercise=="6c"):
            m = 0.45
            e = 8
            image = 1 / (1 + np.float_power((m/image),e))
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Zmiana dynamiki skali szarości')
            axs[0, 0].axis('off')
        elif(exercise=="6d"):
            c = 5
            gamma = 5
            image = c * np.float_power(image,gamma)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Korekcja gamma')
            axs[0, 0].axis('off')
        elif(exercise=="7przed"):
            histogram = cv2.calcHist([image],[0],None,[256],[0,256])
            axs[0, 0].plot(histogram)
            axs[0, 0].set_title(f'Histogram przed wyrównaniem')
        elif(exercise=="7po"):
            image = cv2.equalizeHist(image)
            histogram = cv2.calcHist([image],[0],None,[256],[0,256])
            axs[0, 0].plot(histogram)
            axs[0, 0].set_title(f'Histogram po wyrównaniu') 
            
            axs[1, 1].imshow(image, cmap='gray')
            axs[1, 1].set_title('Obraz po wyrównaniu')
            axs[1, 1].axis('off') 
        elif(exercise=="8a"):
            footprint = morphology.rectangle(3,3)
            image = filters.rank.equalize(image, footprint=footprint)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Obraz po lokalnym wyrównaniu histogramu')
            axs[0, 0].axis('off')
        elif(exercise=="8b"):
            constant=22.8
            k0=0 
            k1=0.1
            k2=0
            k3=0.1
            # Obliczenie globalnej średniej i odchylenia standardowego
            mG = np.mean(image)
            oG = np.std(image)
        elif(exercise=="9a"):
            footprint = morphology.rectangle(3,3)
            image = filters.rank.mean(image, footprint = footprint)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Filtr uśredniający z kwadratową maską')
            axs[0, 0].axis('off')
        elif(exercise=="9b"):
            footprint = morphology.disk(5)
            image = filters.median(image, footprint = footprint)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Nieliniowy filtr medianowy')
            axs[0, 0].axis('off')
        elif(exercise=="9cMIN"):
            footprint = morphology.rectangle(3,3)
            image = filters.rank.minimum(image, footprint = footprint)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Filtr minimum')
            axs[0, 0].axis('off')
        elif(exercise=="9cMAX"):
            footprint = morphology.rectangle(3,3)
            image = filters.rank.maximum(image, footprint = footprint)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Filtr maksimum')
            axs[0, 0].axis('off')
        elif(exercise=="10"):
            footprint = morphology.rectangle(7,7)
            image = filters.rank.mean(image, footprint = footprint)
            image = filters.gaussian(image, sigma = 1)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Zastosowanie filtru dolnoprzepustowego i gaussowskiego')
            axs[0, 0].axis('off')
        elif(exercise=="11a"):
            image = filters.sobel(image)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Filtr Sobela')
            axs[0, 0].axis('off')
        elif(exercise=="11b"):
            image = filters.laplace(image)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Laplasjan')
            axs[0, 0].axis('off')
        elif(exercise=="11cUNSHARP"):
            image = filters.unsharp_mask(image)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Filtr Unsharp Masking')
            axs[0, 0].axis('off')
        elif(exercise=="11cBOOST"):
            imageGauss = cv2.GaussianBlur(image, (7,7), 0)
            image = cv2.addWeighted(image, 3, imageGauss, -2, 0)
            axs[0, 0].imshow(image, cmap='gray')
            axs[0, 0].set_title('Filtr High Boost')
            axs[0, 0].axis('off')
        elif(exercise=="12"):
            #imageA = image
            imageB = filters.laplace(image)
            imageC = image + imageB
            imageD = filters.sobel(imageC)
            #footprint = morphology.rectangle(5,5)
            #imageE = filters.rank.mean(imageD, footprint = footprint)
            imageE = filters.gaussian(imageD)
            imageF = imageE * image
            imageG = image + imageF
            c = 1
            gamma = 0.5
            imageG = c * np.float_power(image,gamma)
            axs[0, 0].imshow(imageG, cmap='gray')
            axs[0, 0].set_title('Wieloetapowa poprawa jakości')
            axs[0, 0].axis('off')
            
    else:
        # Display original image
        axs[0, 0].imshow(image, cmap='gray')
        axs[0, 0].set_title('Początkowy obraz')
        axs[0, 0].axis('off')

    # Plot gray level changes along the specified line
    if direction == 'horizontal':
        gray_levels = image[coord, :]
        axs[0, 1].plot(gray_levels)
        axs[0, 1].set_title(f'Zmiana poziomu szarości w wierszu {coord}')
    elif direction == 'vertical':
        gray_levels = image[:, coord]
        axs[0, 1].plot(gray_levels)
        axs[0, 1].set_title(f'Zmiana poziomu szarości w kolumnie {coord}')
    else:
        raise ValueError("Direction must be 'horizontal' or 'vertical'")

    axs[0, 1].set_xlabel('Pozycja piksela')
    axs[0, 1].set_ylabel('Poziom szarości')

    # Display subimage
    subimage = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    axs[1, 0].imshow(subimage, cmap='gray')
    axs[1, 0].set_title('Pod-obraz')
    axs[1, 0].axis('off')

    plt.tight_layout()

    # Display the figure in the Tkinter canvas
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

def save():
    output_file = "subimage.png"
    top_left = (int(top_left_x_entry.get()),int(top_left_y_entry.get()))
    bottom_right = (int(bottom_right_x_entry.get()),int(bottom_right_y_entry.get()))
    save_subimage(image, top_left, bottom_right, output_file)

def save_subimage(image, top_left, bottom_right, output_file):
    subimage = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    subimage_pil = Image.fromarray(subimage)
    subimage_pil.save(output_file)

def on_change():
    if image is not None:
        direction = direction_var.get()
        coord = int(coord_entry.get())
        top_left = (int(top_left_x_entry.get()),int(top_left_y_entry.get()))
        bottom_right = (int(bottom_right_x_entry.get()),int(bottom_right_y_entry.get()))
        plot(image, coord, direction, top_left, bottom_right, canvas_frame, exercise)

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

if __name__ == '__main__':
    root.mainloop()

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_image(file_path):
    image = Image.open(file_path).convert('L')
    return np.array(image)

def plot_histogram(image_array, num_levels):
    plt.figure(figsize=(10, 6))
    plt.hist(image_array.flatten(), bins=num_levels, range=(0, num_levels-1), density=True, color='gray', alpha=0.7)
    plt.title('Histograma')
    plt.xlabel('Intensidade do pixel')
    plt.ylabel('Frequencia')
    plt.grid(True)
    plt.show()

def main(file_path):
    image_array = load_image(file_path)
    num_levels = 256 if image_array.max() > 128 else 128
    plot_histogram(image_array, num_levels)

if __name__ == '__main__':
    main('lena 256x256.tif')

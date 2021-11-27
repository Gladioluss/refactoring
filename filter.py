from PIL import Image
import numpy as np


def convert_to_grayscale(pixels_array, size_mosaic, grayscale, row_length, column_length):
    pixels_array = pixels_array[0: row_length // size_mosaic * size_mosaic, 0: column_length // size_mosaic * size_mosaic]
    row_index = 0
    while row_index < row_length - (size_mosaic - 1):
        column_index = 0
        while column_index < column_length - (size_mosaic - 1):
            color = 0
            for step_row in range(row_index, row_index + size_mosaic):
                color += sum(map(lambda step_column:
                                 sum(map(int, pixels_array[step_row][step_column])) // 3,
                                 range(column_index, column_index + size_mosaic)))
            medium_brightness = ((color // size_mosaic ** 2) // grayscale) * grayscale
            for step_row in range(row_index, row_index + size_mosaic):
                for step_column in range(column_index, column_index + size_mosaic):
                    pixels_array[step_row][step_column] = np.full(3, medium_brightness)
            column_index += size_mosaic
        row_index += size_mosaic
    return pixels_array


image_array = np.array(Image.open(input("Укажите полное имя файла:  ")))
Image.fromarray(convert_to_grayscale(image_array,
                                    int(input("Укажите размер мозаики:")),
                                    int(input("Укажите градации серого:")),
                                    len(image_array),
                                    len(image_array[1]))).save('res.jpg')

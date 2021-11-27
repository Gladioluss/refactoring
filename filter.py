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
                for step_column in range(column_index, column_index + size_mosaic):
                    color += (int(pixels_array[step_row][step_column][0])
                              + int(pixels_array[step_row][step_column][1])
                              + int(pixels_array[step_row][step_column][2])) // 3
            medium_brightness = color // size_mosaic ** 2
            for step_row in range(row_index, row_index + size_mosaic):
                for step_column in range(column_index, column_index + size_mosaic):
                    pixels_array[step_row][step_column][0] = (medium_brightness // grayscale) * grayscale
                    pixels_array[step_row][step_column][1] = (medium_brightness // grayscale) * grayscale
                    pixels_array[step_row][step_column][2] = (medium_brightness // grayscale) * grayscale
            column_index += size_mosaic
        row_index += size_mosaic
    return pixels_array


image_array = np.array(Image.open("img2.jpg"))
Image.fromarray(convert_to_grayscale(image_array,
                                    int(input("Укажите размер мозаики:")),
                                    int(input("укажите градации серого:")),
                                    len(image_array),
                                    len(image_array[1]))).save('res.jpg')

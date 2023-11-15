from app.config import *

import time
import random
import pygame


class AlgorithmStepper:
    def __init__(self, animation, array, alg_index):
        self.title = None
        self.algorithm = None
        self.animation = animation

        self.pointers_ij: tuple = (0, 0)
        self.swap_ij: tuple = (0, 0)
        self.array: list = array

        self.process = True
        self.mapping_alg(alg_index)

    @property
    def get_state(self):
        return self.array, self.pointers_ij, self.swap_ij

    def update(self):
        print(self.get_state)
        self.next_step()

    def swap(self):
        temp = self.array[self.swap_ij[0]]
        self.array[self.swap_ij[0]] = self.array[self.swap_ij[1]]
        self.array[self.swap_ij[1]] = temp

    def next_step(self):
        try:
            return next(self.algorithm)

        except StopIteration:
            time.sleep(3)
            self.process = False
            self.animation.running = False

    def bubble_sort(self):
        for i in range(len(self.array)):
            for j in range(i, len(self.array)):
                self.pointers_ij = (i, j)
                if self.array[i] > self.array[j]:
                    self.swap_ij = (i, j)
                    self.swap()
                yield
                self.swap_ij = (0, 0)

    def select_sort(self):
        for i in range(len(self.array)):
            current_min_index = i
            self.swap_ij = (0, 0)
            for j in range(i, len(self.array)):
                self.pointers_ij = (i, j)
                if self.array[j] < self.array[current_min_index]:
                    current_min_index = j
                    self.swap_ij = (i, current_min_index)
                yield
            self.swap_ij = (i, current_min_index)
            self.swap()

    def insert_sort(self):
        for i in range(len(self.array)):
            j = i
            while (j != 0) and (self.array[j] < self.array[j - 1]):
                self.pointers_ij = (i, j)
                self.swap_ij = (j, j - 1)
                self.swap()
                yield
                self.swap_ij = (0, 0)
                j -= 1

    def bogo_sort(self):
        while True:
            random.shuffle(self.array)
            yield

            for i in range(len(self.array) - 1):
                if self.array[i] > self.array[i + 1]:
                    break
            else:
                break

    def random_sort(self):
        while True:

            self.swap_ij = (random.randint(0, len(self.array) - 1), random.randint(0, len(self.array) - 1))
            self.swap()
            yield

            for i in range(len(self.array) - 1):
                if self.array[i] > self.array[i + 1]:
                    break
            else:
                break

    def my_sort(self):
        for i in range(len(self.array)):
            pass

    def draw_value_color(self, i, value, color):
        pygame.draw.rect(self.animation.screen, color,
                         (
                             i * X_SIDE + X_SIDE // 10,
                             HEIGHT - (BLOCK_SIZE_Y * value),
                             X_SIDE - X_SIDE // 10,
                             HEIGHT
                         )
                         )

    def draw_arrays_values(self):
        for i, value in enumerate(self.array):
            self.draw_value_color(i, value, GRAY)

    def draw_pointers(self):
        if self.pointers_ij[0] == self.pointers_ij[1]:
            return
        if not self.process:
            return
        self.draw_value_color(self.pointers_ij[0], self.array[self.pointers_ij[0]], COLOR_FOR_POINTED_I)
        self.draw_value_color(self.pointers_ij[1], self.array[self.pointers_ij[1]], COLOR_FOR_POINTED_J)

    def draw_swap(self):
        if self.swap_ij[0] == self.swap_ij[1]:
            return
        if not self.process:
            return
        self.draw_value_color(self.swap_ij[0], self.array[self.swap_ij[0]], COLOR_FOR_SWAPED)
        self.draw_value_color(self.swap_ij[1], self.array[self.swap_ij[1]], COLOR_FOR_SWAPED)

    def draw(self):
        self.draw_arrays_values()
        self.draw_pointers()
        self.draw_swap()

    def mapping_alg(self, index):
        mapping = {
            1: self.bubble_sort(),
            2: self.select_sort(),
            3: self.insert_sort(),
            4: self.random_sort(),
            5: self.bogo_sort(),
            6: self.my_sort()
        }

        mapping_title = {
            1: 'BubbleSort - O(n^2)',
            2: 'SelectSort - O(n^2)',
            3: 'InsertSort - O(n^2)',
            4: 'RandomSort - O(random_n)',
            5: 'BogoSort - O(n * n!)',
            6: 'MySort - O(do not know)'

        }
        self.algorithm = mapping[index]
        self.title = mapping_title[index]

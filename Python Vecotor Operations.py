# Python Vector Operations

first_vector = [1, 4, 5, 6, 8, 0]
second_vector = [2, 6, 4, 9, 3, 1]

# Vector Subtraction


def subtract_two_vectors(first, second):
    output_vector = []
    if len(first) == len(second):
        for i in range(len(first)):
            output_vector.append("")

        for i in range(len(first)):
            output_vector[i] = first[i] - second[i]
        return output_vector
    if len(first) != len(second):
        raise Exception("The size of the Vectors don't match")

# Vector Addition


def add_two_vectors(first, second):
    output_vector = []

    if len(first) == len(second):
        for i in range(len(first)):
            output_vector.append("")

        for i in range(len(first)):
            output_vector[i] = first[i] + second[i]
        return output_vector
    if len(first) != len(second):
        raise Exception("The size of the Vectors don't match")

# Dot Product


def dot_product():
    a = 0

    for i in range(0, len(first_vector)):
        a = first_vector[i] * second_vector[i] + a
        if i == len(first_vector) - 1:
            return a

# Python AXPY Operation


def axpy(first, second, scalar):
    scalar = scalar
    output_vector = []

    if len(first) == len(second):
        for i in range(0, len(first)):
            output_vector.append("")

        for i in range(0, len(first)):
            b = scalar * first[i] + second[i]
            output_vector[i] = b

            if i == len(first) - 1:
                return output_vector

    if len(first) != len(second):
        raise Exception("The size of the Vectors don't match")


vector = axpy(first_vector, second_vector, 2)

print(vector)

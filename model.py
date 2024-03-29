#   model.py

import labeled_shape


class Model(object):
    def __init__(self):
        self.lshape_a = labeled_shape.LabeledShape.new_empty()
        self.lshape_b = labeled_shape.LabeledShape.new_empty()
        self.lshape_c = labeled_shape.LabeledShape.new_empty()


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/model_test.txt')

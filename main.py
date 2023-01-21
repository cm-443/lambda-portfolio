import tensorflow as tf
def lambda_handler(event, context):
    print("TensorFlow version:", tf.__version__)


# import unittest
# def lambda_handler(event, context):
#     def fun(x):
#         return x + 1

#     class MyTest(unittest.TestCase):
#         def test(self):
#             self.assertEqual(fun(3), 4)

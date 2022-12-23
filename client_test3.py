import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quote = [
      {'top_ask': {'price': 121.2}, 'top_bid': {'price': 120.48}, 'stock': 'ABC'},
      {'top_ask': {'price': 121.68}, 'top_bid': {'price': 117.87}, 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quote:
      self.assertEqual(getDataPoint(q), (q['stock'], q['top_bid']['price'], q['top_ask']['price'], (q['top_bid']['price'] + q['top_ask']['price'])/2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quote = [
      {'top_ask': {'price': 119.2}, 'top_bid': {'price': 120.48}, 'stock': 'ABC'},
      {'top_ask': {'price': 121.68}, 'top_bid': {'price': 117.87}, 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
     for q in quote:
      self.assertEqual(getDataPoint(q), (q['stock'], q['top_bid']['price'], q['top_ask']['price'], (q['top_bid']['price'] + q['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
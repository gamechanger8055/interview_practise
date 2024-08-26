'''
1. check if a-b exists directly
2. 2 lookups
3. n lookups
4. doesnt exist throw exception
'''
from collections import defaultdict
import unittest
import heapq

class ConversionNotFoundError(Exception):
    def __init__(self, source, dest):
        self.message = f"Conversion from {source} to {dest} not found!"
        super().__init__(self.message)

class CurrencyConversion:
    def __init__(self):
        self.currency_map=defaultdict(list)
        self.currencies=set()

    def convert_currency_to_map(self,inputs):
        for inp in inputs:
            from_curr,to_curr,conversion_rate=inp
            self.currency_map[from_curr].append([to_curr,conversion_rate])
            self.currency_map[to_curr].append([from_curr, 1/conversion_rate])
            self.currencies.add(from_curr)
            self.currencies.add(to_curr)
        return self.currency_map

    def checkCurrency(self,from_currency,to_currency):
        if from_currency not in self.currency_map or to_currency not in self.currency_map:
            raise ConversionNotFoundError(from_currency,to_currency)
        for currency in self.currency_map[from_currency]:
            if currency[0]==to_currency:
                return currency[1]
        raise ConversionNotFoundError(from_currency,to_currency)

    def bfs(self,from_currency,to_currency):
        if from_currency not in self.currency_map or to_currency not in self.currency_map:
            raise ConversionNotFoundError(from_currency,to_currency)
        q=[(from_currency,1)]
        visited=set()
        visited.add(from_currency)
        while q:
            curr_currency,curr_conversion_rate=q.pop(0)
            visited.add(curr_currency)
            if curr_currency==to_currency:
                return curr_conversion_rate
            for currency in self.currency_map[curr_currency]:
                if currency[0] not in visited:
                    curr_conversion_rate*=currency[1]
                    visited.add(currency[0])
                    q.append((currency[0],curr_conversion_rate))
        raise ConversionNotFoundError(from_currency,to_currency)

    def djikstra_algo(self,from_currency,to_currency):
        if from_currency not in self.currency_map or to_currency not in self.currency_map:
            raise ConversionNotFoundError(from_currency,to_currency)
        hp=[(1,from_currency)]
        distances={curency:float('inf') for curency in self.currencies}
        visited=set()
        visited.add(from_currency)
        distances[from_currency]=1
        while hp:
            curr_rate,curr_currency=heapq.heappop(hp)
            for curr,rate in self.currency_map[curr_currency]:
                if curr not in visited and distances[curr]>curr_rate*rate:
                    distances[curr] =curr_rate * rate
                    visited.add(curr)
                    heapq.heappush(hp,(distances[curr],curr))
        if distances[to_currency]!=float('inf'):
            return distances[to_currency]
        raise ConversionNotFoundError(from_currency,to_currency)




inp=[['USD', 'JPY', 100],['JPY', 'CHN', 20],['CHN', 'THAI', 200],['USD', 'CHN', 20]]

currency=CurrencyConversion()
#print(currency.convert_currency_to_map(inp))
#print(currency.djikstra_algo("USD","CHN"))


class TestCurrencyConversion(unittest.TestCase):
    def setUp(self):
        self.currency_conversion=CurrencyConversion()
        self.currency_conversion.convert_currency_to_map([
            ['USD', 'JPY', 100],
            ['JPY', 'CHN', 20],
            ['CHN', 'THAI', 200],
            ['USD', 'CHN', 20]
        ])

    def test_direct_conversion(self):
        self.assertEqual(self.currency_conversion.checkCurrency('USD','JPY'),100)
        self.assertEqual(self.currency_conversion.checkCurrency('JPY','USD'),1/100)

    def test_bfs_conversion(self):
        self.assertEqual(self.currency_conversion.bfs('USD', 'JPY'), 100) #one pass
        self.assertEqual(self.currency_conversion.bfs('USD', 'CHN'), 2000) #two pass
        self.assertEqual(self.currency_conversion.bfs('USD', 'THAI'), 400000) #three pass
        #self.assertEqual(self.currency_conversion.bfs('US', 'JPY'), 100) #no pass
        #self.assertEqual(self.currency_conversion.bfs('USD', 'JP'), 100) #des not found
        self.assertEqual(self.currency_conversion.bfs('JPY', 'USD'), 1 / 100) #upsert

    def test_dijkistra(self):
        self.assertEqual(self.currency_conversion.djikstra_algo('USD', 'JPY'), 100)  # one pass
        self.assertEqual(self.currency_conversion.djikstra_algo('USD', 'CHN'), 20)  # two pass
        self.assertEqual(self.currency_conversion.djikstra_algo('USD', 'THAI'), 4000)  # three pass
        self.assertEqual(self.currency_conversion.djikstra_algo('JPY', 'USD'), 1 / 100) #upsert

    def test_conversion_not_found_error(self):
        with self.assertRaises(ConversionNotFoundError):
            self.currency_conversion.checkCurrency('USD', 'EUR')

        with self.assertRaises(ConversionNotFoundError):
            self.currency_conversion.bfs('USD', 'EUR')

        with self.assertRaises(ConversionNotFoundError):
            self.currency_conversion.djikstra_algo('USD', 'EUR')
import unittest

def field(items, *args):
    assert len(args) > 0
    result = []
    for seti in items:
        args_in_seti = [arg for arg in args if arg in seti]
        result.append({arg: seti[arg] for arg in args_in_seti} if len(args) > 1 else seti[args_in_seti[0]] if len(args_in_seti) > 0 else None)
    while None in result:
        result.remove(None)
    while {} in result:
        result.remove({})
    return result

class TestField(unittest.TestCase):
    def test_calculation(self):
        goods = [
                {'title': 'Ковер', 'price': 2000, 'color': 'green'},
                {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
            ]
        check1 = field(goods, 'title')
        check2 = field(goods, 'title', 'price')
        self.assertEqual(check1, ['Ковер', 'Диван для отдыха'] )
        self.assertEqual(check2, [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}])

if __name__ == '__main__':
    unittest.main()
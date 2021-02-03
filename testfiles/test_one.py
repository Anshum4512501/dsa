# import unittest
# class Test(unittest.TestCase):
    
#     def test_upper(self):
#         self.assertEqual('foo'.upper(),"FOO")

    




# if __name__ == '__main__':
#     unittest.main()        

# cook your dish here
t = range(int(input()))
for _ in t:
    result = 0
    number = str(input())
    for digit in number:
        
        result = int(digit) + result
    print(result)
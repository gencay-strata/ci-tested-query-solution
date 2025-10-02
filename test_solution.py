import unittest
import pandas as pd
from solution import calculate_net_new_products

class TestProductDifference(unittest.TestCase):
    def test_net_new_products(self):
        # Test input
        test_data = pd.DataFrame({
            'year': [2019, 2019, 2020, 2020],
            'company_name': ['Toyota', 'Toyota', 'Toyota', 'Toyota'],
            'product_name': ['Camry', 'Avalon', 'Corolla', 'Yaris']
        })

        # Expected output
        expected_output = pd.DataFrame({
            'company_name': ['Toyota'],
            'net_new_products': [0]
        })

        result = calculate_net_new_products(test_data)
        pd.testing.assert_frame_equal(
            result.sort_values('company_name').reset_index(drop=True),
            expected_output.sort_values('company_name').reset_index(drop=True)
        )

if __name__ == '__main__':
    unittest.main()

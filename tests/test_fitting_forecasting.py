import unittest
import pandas as pd
import numpy as np
from Week8and9.fitting_forecast import load_clean_data, polyall_setup, train_test_split, eval, best_model

# love a good bit of oop
class test_cherry_forecast(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # load data once for all tests
        cls.df = load_clean_data()

    def test_load_clean_data(self):
        df = self.df
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Year', df.columns)
        self.assertIn('Peak day', df.columns)
        self.assertTrue(df['Year'].min() >= 1925)
        self.assertTrue(df['Year'].max() <= 2015)

    def test_polyall_setup(self):
        years, years_c, peak, xp, xp_c, degree = polyall_setup(self.df)
        self.assertEqual(len(years), len(years_c))
        self.assertAlmostEqual(np.mean(years_c), 0)
        self.assertEqual(len(years), len(peak))
        self.assertEqual(len(xp), len(xp_c))
        self.assertEqual(degree, 10)

    def test_train_test_split(self):
        train_df, test_df, x_train, y_train = train_test_split(self.df)
        self.assertEqual(len(train_df) + len(test_df), len(self.df))
        self.assertTrue(all(train_df['Year'] <= test_df['Year'].min()))
        self.assertEqual(len(x_train), len(y_train))

    def test_eval(self):
        train_df, test_df, x_train, y_train = train_test_split(self.df)
        orders, chi2_vals, chi2_dof_vals, bic_vals, x_mean, x_test, x_test_c, x_train_c, y_test, y_train = eval(x_train, y_train, test_df)
        self.assertEqual(len(chi2_vals), len(list(range(1,10))))
        self.assertEqual(len(bic_vals), len(list(range(1,10))))
        self.assertAlmostEqual(np.mean(x_train_c), 0)

    def test_best_model_runs(self):
        train_df, test_df, x_train, y_train = train_test_split(self.df)
        orders, chi2_vals, chi2_dof_vals, bic_vals, x_mean, x_test, x_test_c, x_train_c, y_test, y_train = eval(x_train, y_train, test_df)
        # just test that it runs without error
        best_model(orders, bic_vals, x_train_c, y_train, x_train, x_test, y_test, x_mean)

if __name__ == "__main__":
    unittest.main()
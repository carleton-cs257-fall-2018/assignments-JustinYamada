'''
   api_test.py
   Justin Hahn & Justin Yamada, 16 October 2018
'''

from webapp import CrimeDataSource
import unittest

class CrimeTester(unittest.TestCase):
    def setUp(self):
        self.CrimeTester = CrimeDataSource('CrimeTest.csv')

    def tearDown(self):
        pass

    def test_crime_show_all_crimes_in_all_zips(self):
        self.assertEqual(self.CrimeTester.crime(zipCode1=11111,zipCode2=22222,zipCode3=33333,zipCode4=44444),

        [{'id':1, 'police_code':2305, 'zipCode':11111, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'ONETON'},
        {'id':2, 'police_code':2305, 'zipCode':22222, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'TWOTON'},
        {'id':3, 'police_code':2305, 'zipCode':22222, 'type_place':'Street - Bus Stop', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'TWOTON'},
        {'id':4, 'police_code':2305, 'zipCode':33333, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'THREETON'},
        {'id':5, 'police_code':5404, 'zipCode':33333, 'type_place':'Street - Bus Stop', 'broad_crime':'Driving Under the Influence',
        'specific_crime':'DRIVING UNDER THE INFLUENCE LIQUOR', 'city':'THREETON'},
        {'id':6, 'police_code':5707, 'zipCode':33333, 'type_place':'Retail - Department/Discount Store', 'broad_crime':'Trespass of Real Property',
        'specific_crime':'TRESPASSING', 'city':'THREETON'},
        {'id':7, 'police_code':2305, 'zipCode':44444, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'FOURTON'},
        {'id':8, 'police_code':2305, 'zipCode':44444, 'type_place':'Street - Bus Stop', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'FOURTON'},
        {'id':9, 'police_code':5707, 'zipCode':44444, 'type_place':'', 'broad_crime':'Trespass of Real Property',
        'specific_crime':'TRESPASSING', 'city':'FOURTON'}])

    def test_crime_show_all_crimes_in_two_zips(self):
        self.assertEqual(self.CrimeTester.crime(zipCode1=11111,zipCode=22222),
        [[{'id':1, 'police_code':2305, 'zipCode':11111, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'ONETON'},
        {'id':2, 'police_code':2305, 'zipCode':22222, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'TWOTON'},
        {'id':3, 'police_code':2305, 'zipCode':22222, 'type_place':'Street - Bus Stop', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'TWOTON'}])

    def test_crime_show_all_crimes_in_two_zips_and_two_locations(self):
        self.assertEqual(self.CrimeTester.crime(zipCode1=11111,zipCode=22222,Residence=true),
        [{'id':1, 'police_code':2305, 'zipCode':11111, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'ONETON'},
        {'id':2, 'police_code':2305, 'zipCode':22222, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'TWOTON'}])

    def test_crime_show_all_crimes_in_one_zip_and_one_location(self):
        self.assertEqual(self.CrimeTester.crime(zipCode1=11111,Residence=true),
        [{'id':1, 'police_code':2305, 'zipCode':11111, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'ONETON'}])

    def test_crime_show_all_crimes_in_three_zips(self):
        self.assertEqual(self.CrimeTester.crime(zipCode1=11111,zipCode2=22222,zipCode3=33333),
        [{'id':1, 'police_code':2305, 'zipCode':11111, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'ONETON'},
        {'id':2, 'police_code':2305, 'zipCode':22222, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'TWOTON'},
        {'id':3, 'police_code':2305, 'zipCode':22222, 'type_place':'Street - Bus Stop', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'TWOTON'},
        {'id':4, 'police_code':2305, 'zipCode':33333, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'THREETON'},
        {'id':5, 'police_code':5404, 'zipCode':33333, 'type_place':'Street - Bus Stop', 'broad_crime':'Driving Under the Influence',
        'specific_crime':'DRIVING UNDER THE INFLUENCE LIQUOR', 'city':'THREETON'},
        {'id':6, 'police_code':5707, 'zipCode':33333, 'type_place':'Retail - Department/Discount Store', 'broad_crime':'Trespass of Real Property',
        'specific_crime':'TRESPASSING', 'city':'THREETON'}])

    def test_crime_show_all_crimes_in_one_zip_and_three_locations(self):
        self.assertEqual(self.CrimeTester.crime(zipCode1=11111,Residence=true,Street=true, Hospital=true),
        [{'id':1, 'police_code':2305, 'zipCode':11111, 'type_place':'Residence - Apartment/Condo', 'broad_crime':'Theft From Motor Vehicle',
        'specific_crime':'LARCENY - FROM AUTO', 'city':'ONETON'}])

    def test_crime_frequency_page(self):
        self.assertEquals(self.CrimeTester.cFrequency(),
        [

        )


if __name__ == '__main__':
    unittest.main()

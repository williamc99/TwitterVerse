import unittest
import twitterverse_functions as tf


EMPTY_LIST = []
SINGLE_USER = ['tomCruise']
DOUBLE_USER = ['tomCruise', 'PerezHilton']

NO_FILTER_EXAMPLE = {}

NAME_EXAMPLE1 = {'name-includes': 'Cruise'}
NAME_EXAMPLE2 = {'name-includes': 'Johnny'}

LOCATION_EXAMPLE1 = {'location-includes': 'Los Angeles'}
LOCATION_EXAMPLE2 = {'location-includes': 'Saudi Arabia'}

FOLLOWERS_EXAMPLE1 = {'followers': 'PerezHilton'}
FOLLOWERS_EXAMPLE2 = {'followers': 'bennyJJJ'}

FOLLOWING_EXAMPLE1 = {'following': 'katieH'}
FOLLOWING_EXAMPLE2 = {'following': 'benLOL'}

MULTIPLE_EXAMPLE1 = {'name-includes': 'Cruise',
                     'location-includes': 'Los Angeles'}
MULTIPLE_EXAMPLE2 = {'following': 'NicoleKidman', 'following': 'katieH'}
MULTIPLE_EXAMPLE3 = {'followers': 'PerezHilton', 'following': 'benLOL'}
MULTIPLE_EXAMPLE4 = {'name-includes': 'Johnny', 'followers': 'bennyJJJ'}


class TestGetFilterResults(unittest.TestCase):
    '''Example unittest test methods for get_filter_results'''

    #No filter tests
    def test_filter_example_1(self):
        '''Test get_filter_results with an empty user list and no filters.'''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, EMPTY_LIST
                                       , NO_FILTER_EXAMPLE)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_2(self):
        '''Test get_filter_results with a single user and no filters.'''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , NO_FILTER_EXAMPLE)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_3(self):
        '''Test get_filter_results with multiple users and no filters.'''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , NO_FILTER_EXAMPLE)
        expected = DOUBLE_USER
        self.assertEqual(expected, actual)


    #Name-Includes Tests
    def test_filter_example_4(self):
        '''Test get_filter_results with an empty user list and name-includes
        filter.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, EMPTY_LIST
                                       , NAME_EXAMPLE1)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_5(self):
        '''Test get_filter_results with a single user and name-includes
        filter that is met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , NAME_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_6(self):
        '''Test get_filter_results with a single user and name-includes
        filter that is not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , NAME_EXAMPLE2)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_7(self):
        '''Test get_filter_results with multiple users and name-includes
        filter that is met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , NAME_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_8(self):
        '''Test get_filter_results with multiple users and name-includes
        filter that is not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , NAME_EXAMPLE2)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    #Location-includes tests
    def test_filter_example_9(self):
        '''Test get_filter_results with no users and location-includes
        filter.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, EMPTY_LIST
                                       , LOCATION_EXAMPLE1)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_10(self):
        '''Test get_filter_results with single user and location-includes
        filter that is met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , LOCATION_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_11(self):
        '''Test get_filter_results with single user and location-includes
        filter that is not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , LOCATION_EXAMPLE2)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_12(self):
        '''Test get_filter_results with multiple users and location-includes
        filter that is met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , LOCATION_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_13(self):
        '''Test get_filter_results with multiple users and location-includes
        filter that is not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , LOCATION_EXAMPLE2)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    #Followers tests
    def test_filter_example_14(self):
        '''Test get_filter_results with no users and followers filter.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, EMPTY_LIST
                                       , FOLLOWERS_EXAMPLE1)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_15(self):
        '''Test get_filter_results with a single user and followers
        filter that is met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , FOLLOWERS_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_16(self):
        '''Test get_filter_results with a single user and followers
        filter that is not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , FOLLOWERS_EXAMPLE2)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_17(self):
        '''Test get_filter_results with multiple users and followers
        filter that is met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , FOLLOWERS_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_18(self):
        '''Test get_filter_results with multiple users and followers
        filter that is not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , FOLLOWERS_EXAMPLE2)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    #Following tests
    def test_filter_example_19(self):
        '''Test get_filter_results with no users and following filter.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, EMPTY_LIST
                                       , FOLLOWING_EXAMPLE1)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_20(self):
        '''Test get_filter_results with a single user and following
        filter that is met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , FOLLOWING_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_21(self):
        '''Test get_filter_results with a single user and following
        filter that is not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , FOLLOWING_EXAMPLE2)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_22(self):
        '''Test get_filter_results with multiple users and following
        filter that is met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , FOLLOWING_EXAMPLE1)
        expected = DOUBLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_23(self):
        '''Test get_filter_results with multiple users and following
        filter that is not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , FOLLOWING_EXAMPLE2)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    #Multiple filter tests
    def test_filter_example_24(self):
        '''Test get_filter_results with no users and multiple filters.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, EMPTY_LIST
                                       , MULTIPLE_EXAMPLE1)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_25(self):
        '''Test get_filter_results with single user and multiple
        filters that are both met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , MULTIPLE_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_26(self):
        '''Test get_filter_results with single user and multiple
        filters that are met and then not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, SINGLE_USER
                                       , MULTIPLE_EXAMPLE3)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)


    def test_filter_example_27(self):
        '''Test get_filter_results with multiple users and multiple
        filters that are both met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , MULTIPLE_EXAMPLE2)
        expected = DOUBLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_28(self):
        '''Test get_filter_results with multiple users and multiple
        filters that only one user will meet.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , MULTIPLE_EXAMPLE1)
        expected = SINGLE_USER
        self.assertEqual(expected, actual)


    def test_filter_example_29(self):
        '''Test get_filter_results with multiple users and multiple
        filters that are both not met.
        '''

        actual = tf.get_filter_results(tf.HANDOUT_DATA, DOUBLE_USER
                                       , MULTIPLE_EXAMPLE4)
        expected = EMPTY_LIST
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main(exit=False)

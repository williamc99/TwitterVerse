"""CSC108/A08: Fall 2020 -- Assignment 3: Twitterverse

This code is provided solely for the personal and private use of
students taking the CSC108 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from typing import Callable, List, TextIO
from constants import (TwitterverseDict, SearchDict, FilterDict,
                       PresentDict, QueryDict)
from constants import (NAME, LOCATION, WEB, BIO, FOLLOWING, USERNAME,
                       OPERATIONS, FOLLOWER, FOLLOWERS, NAME_INCLUDES,
                       LOCATION_INCLUDES, SORT_BY, FORMAT, SEARCH,
                       FILTER, PRESENT, POPULARITY, END, ENDBIO, LONG)


HANDOUT_DATA = {
    'tomCruise': {
        'name': 'Tom Cruise',
        'bio': ('Official TomCruise.com crew tweets. We love you guys!\n' +
                'Visit us at Facebook!'),
        'location': 'Los Angeles, CA',
        'web': 'http://www.tomcruise.com',
        'following': ['katieH', 'NicoleKidman']},
    'PerezHilton': {
        'name': 'Perez Hilton',
        'bio': ('Perez Hilton is the creator and writer of one of the most ' +
                'famous websites\nin the world. And he also loves music -' +
                'a lot!'),
        'location': 'Hollywood, California',
        'web': 'http://www.PerezH...',
        'following': ['tomCruise', 'katieH', 'NicoleKidman']}}

HANDOUT_QUERY = {
    'SEARCH': {'username': 'tomCruise',
               'operations': ['following', 'followers']},
    'FILTER': {'following': 'katieH'},
    'PRESENT': {'sort-by': 'username',
                'format': 'short'}
}

HANDOUT_QUERY2 = {
    'SEARCH': {'username': 'tomCruise',
               'operations': ['followers']},
    'FILTER': {'following': 'katieH'},
    'PRESENT': {'sort-by': 'username',
                'format': 'short'}
}

QUERY_EXAMPLE1 = ['SEARCH', 'tomCruise', 'following'
                  , 'FILTER', 'following katieH', 'PRESENT', 'sort-by username'
                  , 'format long']

QUERY_EXAMPLE2 = ['SEARCH', 'tomCruise', 'following', 'FILTER', 'PRESENT',
                  'sort-by username', 'format long']

FILTER_EXAMPLE = {'following': 'katieH'}
FILTER_EXAMPLE2 = {'following': 'benLOL'}
PRESENT_EXAMPLE1 = {'sort-by': 'username', 'format': 'short'}
PRESENT_EXAMPLE2 = {'sort-by': 'name', 'format': 'long'}
TWO_USERS = ['tomCruise', 'PerezHilton']



############################################################################


############################################################################
# Provided helper functions
############################################################################



def tweet_sort(twitter_data: TwitterverseDict,
               usernames: List[str],
               sort_spec: str) -> None:
    """Sort usernames based on the sorting specification in sort_spec
    using the data in twitter_data.

    >>> usernames = ['tomCruise', 'PerezHilton']
    >>> tweet_sort(HANDOUT_DATA, usernames, 'username')
    >>> usernames == ['PerezHilton', 'tomCruise']
    True
    >>> tweet_sort(HANDOUT_DATA, usernames, 'popularity')
    >>> usernames == ['tomCruise', 'PerezHilton']
    True
    >>> tweet_sort(HANDOUT_DATA, usernames, 'name')
    >>> usernames == ['PerezHilton', 'tomCruise']
    True

    """

    usernames.sort()  # sort by username first
    if sort_spec in SORT_FUNCS:
        SORT_FUNCS[sort_spec](twitter_data, usernames)


def by_popularity(twitter_data: TwitterverseDict, usernames: List[str]) -> None:
    """Sort usernames in descending order based on popularity (number of
    users that follow a gien user) in twitter_data.

    >>> usernames = ['PerezHilton', 'tomCruise']
    >>> by_popularity(HANDOUT_DATA, usernames)
    >>> usernames == ['tomCruise', 'PerezHilton']
    True

    """

    def get_popularity(username: str) -> int:
        return len(all_followers(twitter_data, username))

    usernames.sort(key=get_popularity, reverse=True)


def by_name(twitter_data: TwitterverseDict, usernames: List[str]) -> None:
    """Sort usernames in ascending order based on name in twitter_data.

    >>> usernames = ['tomCruise', 'PerezHilton']
    >>> by_name(HANDOUT_DATA, usernames)
    >>> usernames == ['PerezHilton', 'tomCruise']
    True

    """

    def get_name(username: str) -> str:
        return twitter_data.get(username, {}).get(NAME, '')

    usernames.sort(key=get_name)


def format_report(twitter_data: TwitterverseDict,
                  usernames: List[str],
                  format_spec: str) -> str:
    """Return a string representing usernames presented as specified by
    the format specification format_spec.

    Precondition: each username in usernames is in twitter_data
    """

    if format_spec == LONG:
        result = '-' * 10 + '\n'
        for user in usernames:
            result += format_details(twitter_data, user)
            result += '-' * 10 + '\n'
        return result
    return str(usernames)


def format_details(twitter_data: TwitterverseDict, username: str) -> str:
    """Return a string representing the long format of username's info in
    twitter_data.

    Precondition: username is in twitter_data
    """

    user_data = twitter_data[username]
    return ("{}\nname: {}\nlocation: {}\nwebsite: {}\nbio:\n{}\n" +
            "following: {}\n").format(username, user_data[NAME],
                                      user_data[LOCATION],
                                      user_data[WEB], user_data[BIO],
                                      user_data[FOLLOWING])


############################################################################
# My helper functions
############################################################################


def clean_list(user_list: List[List[str]]) -> List[List[str]]:
    """Return a cleaned list of user_list, one where unnecessary '\n'
    are removed

    """

    for user in user_list:
        bio_end = user.index('ENDBIO\n')
        end_index = user.index('END\n')
        user[0] = user[0][:len(user[0]) - 1] #username
        user[1] = user[1][:len(user[1]) - 1] #name
        user[2] = user[2][:len(user[2]) - 1] #location
        user[3] = user[3][:len(user[3]) - 1] #website
        if (bio_end - 1) != 3: #if the bio is not empty
            user[bio_end - 1] = user[bio_end - 1][:len(user[bio_end - 1])- 1]
        user[bio_end] = user[bio_end][:len(user[bio_end])-1]
        if (bio_end + 1) != end_index: #if the following is not empty
            for i in range(bio_end + 1, end_index):
                user[i] = user[i][:len(user[i]) - 1]
        user[end_index] = user[end_index][:len(user[end_index]) - 1]
    return user_list


def sorted_users(text_file: TextIO) -> List[List[str]]:
    """Return a list inside a list containing users from data_file,
    all sorted by the keyword 'END\n'.
    """

    all_users = text_file.readlines()

    new_list = []
    final_list = []
    for item in all_users:
        new_list.append(item)
        if item == 'END\n':
            final_list.append(new_list)
            new_list = []
    final_list = clean_list(final_list)
    return final_list


def get_biography(single_user: List[str]) -> str:
    """Return the biography of a user given the list single_user,
    which is a list containing the information for one user.

    Pre-condition: single_user is cleaned.

    """

    biography = ''
    bio_end = single_user.index(ENDBIO)
    if (bio_end - 1) != 3:
        for i in range(4, bio_end):
            biography += single_user[i]
    else:
        biography = ""
    return biography


def get_following(single_user: List[str]) -> List[str]:
    """Return a list of the users that the user is following using the
    single_user list as input.

    Pre-condition: single_user is cleaned.

    """

    following_list = []
    bio_end = single_user.index(ENDBIO)
    end_index = single_user.index(END)

    if (bio_end + 1) != end_index:
        for i in range(bio_end + 1, end_index):
            following_list.append(single_user[i])
    return following_list


def clean_query_data(query_file: TextIO) -> List[str]:
    """Return a new list containing all the lines of query_file,
    put into a list, and all '\n' removed.
    """
    query_text = query_file.readlines()

    for i in range(len(query_text)):
        query_text[i] = query_text[i][:len(query_text[i]) - 1]
    return query_text


def get_search_dict(query_text: List[str]) -> SearchDict:
    """Return a dictionary in the scheme of SearchDict from the given
    information in query_text.

    >>> get_search_dict(QUERY_EXAMPLE2)
    {'username': 'tomCruise', 'operations': ['following']}

    """

    search_dict = {}
    operations_list = []
    search_index = query_text.index(SEARCH)
    filter_index = query_text.index(FILTER)

    if filter_index - 2 != search_index: #checking for operations
        for i in range(2, filter_index):
            operations_list.append(query_text[i])

    search_dict[USERNAME] = query_text[1]
    search_dict[OPERATIONS] = operations_list
    return search_dict


def get_filter_dict(query_text: List[str]) -> FilterDict:
    """Return a dictionary in the scheme of FilterDict from the given
    information in query_text.  Returns an empty dictionary if there are no
    filters.

    >>> get_filter_dict(QUERY_EXAMPLE1)
    {'following': 'katieH'}
    >>> get_filter_dict(QUERY_EXAMPLE2)
    {}

    """

    filter_dict = {}
    filter_index = query_text.index(FILTER)
    present_index = query_text.index(PRESENT)

    if present_index - 1 != filter_index:
        for item in query_text[(filter_index + 1): present_index]:
            filters_list = (item.split())
            filter_dict[filters_list[0]] = filters_list[1]
    return filter_dict


def get_present_dict(query_text: List[str]) -> PresentDict:
    """Return a dictionary in the scheme of SearchDict from the given
    information in query_text.

    >>> get_present_dict(QUERY_EXAMPLE1)
    {'sort-by': 'username', 'format': 'long'}

    """

    present_dict = {}
    present_index = query_text.index(PRESENT)

    for item in query_text[(present_index + 1):]:
        present_list = (item.split())
        present_dict[present_list[0]] = present_list[1]
    return present_dict


def flatten_and_clean(search_list: List[List[str]]) -> List[str]:
    """Return a modified search_list that has all nested lists flattened into
    one list and has all duplicate strings removed.
    Returns an empty list if search_list is empty.

    Pre-condition: search_list is only nested once.

    >>> flatten_and_clean([['red', 'yellow'], ['green', 'green']])
    ['red', 'yellow', 'green']
    >>> flatten_and_clean([])
    []

    """

    #flatten nested lists
    temp_list = []
    for item in search_list:
        temp_list.extend(item)
    search_list = temp_list

    #remove duplicates
    duplicate_list = []
    for item in search_list:
        if item not in duplicate_list:
            duplicate_list.append(item)
    search_list = duplicate_list

    return search_list


def filter_user(user: str, filter_instruction: str, filter_dict: FilterDict,
                twitter_data: TwitterverseDict) -> bool:
    """Return a boolean that represents whether a user should be kept given the
    filter_instruction, filter_dict, and twitter_data.

    >>> filter_user('tomCruise', FOLLOWING, FILTER_EXAMPLE, HANDOUT_DATA)
    True
    >>> filter_user('tomCruise', FOLLOWING, FILTER_EXAMPLE2, HANDOUT_DATA)
    False

    """

    user_check = True

    if filter_instruction == NAME_INCLUDES:
        name_instruction = filter_dict[NAME_INCLUDES]
        user_name = twitter_data[user][NAME]
        if name_instruction.lower() not in user_name.lower():
            user_check = False
    elif filter_instruction == LOCATION_INCLUDES:
        location_instruction = filter_dict[LOCATION_INCLUDES]
        user_location = twitter_data[user][LOCATION]
        if location_instruction.lower() not in user_location.lower():
            user_check = False
    elif filter_instruction == FOLLOWERS:
        if filter_dict[FOLLOWERS] not in all_followers(twitter_data, user):
            user_check = False
    elif filter_instruction == FOLLOWING:
        if filter_dict[FOLLOWING] not in twitter_data[user][FOLLOWING]:
            user_check = False

    return user_check



############################################################################


def process_data(data_file: TextIO) -> TwitterverseDict:
    """Return users from data_file into the TwitterverseDict dictionary,
    incorporating the use of function sorted_users.
    """

    user_list = sorted_users(data_file)
    user_dict = {}

    for user in user_list:
        user_dict[user[0]] = {NAME: user[1], LOCATION: user[2],
                              WEB: user[3], BIO: get_biography(user),
                              FOLLOWING: get_following(user)}
    return user_dict


def process_query(query_file: TextIO) -> QueryDict:
    """Return a QueryDict from query_file that contains the specifications
    of the given query file.
    """

    query_text = clean_query_data(query_file)

    search_dict = get_search_dict(query_text)
    filter_dict = get_filter_dict(query_text)
    present_dict = get_present_dict(query_text)

    #QueryDict
    query_dict = {}
    query_dict[SEARCH] = search_dict
    query_dict[FILTER] = filter_dict
    query_dict[PRESENT] = present_dict

    return query_dict


def all_followers(twitter_dict: TwitterverseDict, username: str) -> List[str]:
    """Return a list of users following the user with name username. Return
    an empty list if no one is following that user.

    >>> all_followers(HANDOUT_DATA, 'tomCruise')
    ['PerezHilton']
    >>> all_followers(HANDOUT_DATA, 'PerezHilton')
    []
    """
    followers_list = []

    for user, value in twitter_dict.items():
        if username in value[FOLLOWING]:
            followers_list.append(user)
    return followers_list


def get_search_results(twitter_file: TwitterverseDict,
                       search_dict: SearchDict) -> List[str]:
    """Return a string list containing usernames that match the search criteria
    of search dict.  The usernames and information are inputted from
    twitter_file.

    >>> get_search_results(HANDOUT_DATA, HANDOUT_QUERY[SEARCH])
    ['tomCruise', 'PerezHilton']
    >>> get_search_results(HANDOUT_DATA, HANDOUT_QUERY2[SEARCH])
    ['PerezHilton']
    """

    search_list = []
    search_list.append(search_dict[USERNAME])

    for operation in search_dict[OPERATIONS]:
        if operation == FOLLOWING:
            for i in range(len(search_list)):
                search_list[i] = twitter_file[search_list[i]][FOLLOWING]
        elif operation == FOLLOWERS:
            for i in range(len(search_list)):
                search_list[i] = all_followers(twitter_file, search_list[i])
        search_list = flatten_and_clean(search_list)

    return search_list


def get_filter_results(twitter_data: TwitterverseDict, user_list: List[str],
                       filter_dict: FilterDict) -> List[str]:
    """Return a modified user_list, where the usernames are either kept or
    removed depending on filter_dict and twitter_data.
    """

    filter_keys = filter_dict.keys()

    if len(filter_dict) == 0:
        return user_list

    for instruction in filter_keys:
        new_list = []
        for user in user_list:
            check = filter_user(user, instruction, filter_dict
                                , twitter_data)
            if check:
                new_list.append(user)
        user_list = new_list
    return user_list


def get_present_string(twitter_data: TwitterverseDict, user_list: List[str],
                       present_dict: PresentDict) -> str:
    """Return a string containing the information of the users in user_list,
    in the format of the specifications in present_dict.  Information of each
    user is given from twitter_data.

    >>> get_present_string(HANDOUT_DATA, TWO_USERS, PRESENT_EXAMPLE1)
    "['PerezHilton', 'tomCruise']"
    >>> get_present_string(HANDOUT_DATA, ['tomCruise'], PRESENT_EXAMPLE2)
    ("----------\\ntomCruise\\nname: Tom Cruise\\nlocation: Los Angeles, CA" +
    "\\nwebsite: http://www.tomcruise.com\\nbio:\\nOfficial TomCruise.com " +
    "crew tweets. We love you guys!\\nVisit us at Facebook!" +
    "\\nfollowing: ['katieH', 'NicoleKidman']\\n----------\\n")

    """

    tweet_sort(twitter_data, user_list, present_dict[SORT_BY])
    return format_report(twitter_data, user_list, present_dict[FORMAT])


SORT_FUNCS = {POPULARITY: by_popularity,
              NAME: by_name}


if __name__ == '__main__':
    import doctest
    doctest.testmod()

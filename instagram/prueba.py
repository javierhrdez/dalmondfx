from InstagramAPI import InstagramAPI
from pprint import pprint   

from InstagramAPI import InstagramAPI


def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


if __name__ == "__main__":
    api = InstagramAPI("xavihernandezc", "x9305913k")
    api.login()

    # user_id = '1461295173'
    user_id = api.username_id

    # List of all followers
    #followers = getTotalFollowers(api, user_id)
    #print('Number of followers:', len(followers))

    # Alternatively, use the code below
    # (check evaluation.evaluate_user_followers for further details).
    followers = api.getTotalFollowers(user_id)
    for f in followers:
        print(f.get('username'))
    print('Number of followers:', len(followers))
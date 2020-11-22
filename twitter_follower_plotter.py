import twitter
import collections
import matplotlib.pyplot as plt


def calculate_followers(twitter_api, user_id, users_limit=None, print_on_each_step=True):
    cursor = -1
    data = {}
    total = 0

    while True:
        followers_response = twitter_api.GetFollowersPaged(screen_name=user_id, cursor=cursor, skip_status=True)
        total += len(followers_response[2])
        for follower in followers_response[2]:
            count = follower.followers_count
            if count not in data:
                data[count] = 0
            data[count] += 1

        cursor = followers_response[0]
        if cursor <= 0 or (users_limit and total >= users_limit):
            break

        print(f'Counted: {total}...')
        # Prints after every API request, so that you can start checking data before it is finished
        if print_on_each_step:
            print_data(data)

    print(f'Done! Total counted: {total}')
    print_data(data)
    plot_data(data, user_id)


def print_data(followers_dict):
    ordered_data = collections.OrderedDict(sorted(followers_dict.items()))

    dict_pairs = '\t'.join(f'{key}, {value}' for key, value in ordered_data.items())
    # Format into [x] and [y] rows, useful for plotting manually in some software
    followers_count_string = '\t'.join(str(key) for key in ordered_data.keys())
    users_amount_string = '\t'.join(str(value) for value in ordered_data.values())
    print(f'data_pairs\t{dict_pairs}\nfollowers_amt\t{followers_count_string}\nnumber_of_users\t{users_amount_string}\n')


def plot_data(followers_dict, user_id):
    # Fill empty indexes for better plotting
    follower_amounts = followers_dict.keys()
    total_users = sum(followers_dict.values())
    max_followers = max(follower_amounts)
    for x in range(0, max_followers):
        if x not in follower_amounts:
            followers_dict[x] = 0

    ordered_data = collections.OrderedDict(sorted(followers_dict.items()))

    plt.plot(ordered_data.keys(), ordered_data.values())
    plt.xlabel('Amount of followers')
    plt.ylabel('Number of users')
    plt.title(f'Number of followers for users who follow \'{user_id}\' (total: {total_users})')
    plt.show()


if __name__ == "__main__":
    # Setup your bot on https://developer.twitter.com/
    api = twitter.Api(consumer_key='%api_key%',
                      consumer_secret='%api_secret%',
                      access_token_key='%access_token_key%',
                      access_token_secret='%access_token_secret%',
                      sleep_on_rate_limit=True)

    calculate_followers(api, 'xorboo')

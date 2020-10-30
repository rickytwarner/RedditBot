def savemedia():
    # Libraries needed
    import praw, requests
    # Create a user instance
    reddit = praw.Reddit(client_id = "client_id",
                        client_secret = "client_secret",
                        user_agent = "user_agent",
                        username = "username",
                        password = "password"
    )
    # Get the id's of the saved posts from reddit
    seq = reddit.redditor("redditor").saved(limit = None)

    # Add all ids to a list to loop through 
    submissions_list = []
    for i in seq:
         submissions_list.append(i)
    # Loop through submissions_list to pull each report to grab any attached media
    for i in submissions_list:

        submission = reddit.submission(id = i)

        try:
            # Check to see if there is a url attached to the post, we then check to see if it has a media extension ex: .jpg
            media_url = submission.url
            if ".com" or ".net" or ".io" or ".org" or ".gov" in media_url:
                pass
            if "." not in media_url:
                pass
            # Create the name for the saved media
            list_name = list(media_url)
            list_name.reverse()
            dummy_characters = []
            for i in list_name:
                if i != "/":
                    dummy_characters.append(i)
                else:
                    break
            dummy_characters.reverse()
            final_name = ''.join(dummy_characters)
            r = requests.get(media_url) # Use Requests to pull the image from the web
            # create the path to save the file to and write it to your local hard drive
            save_dir = "/Folder/Path/Here"
            final_save_dir = save_dir + "/" + final_name
            with open(final_save_dir, 'wb') as f:
                f.write(r.content)

        except:
            pass


def deleteposts():
    # Libraries needed
    import praw
    # Create a user instance
    reddit = praw.Reddit(client_id = "client_id",
                        client_secret = "client_secret",
                        user_agent = "user_agent",
                        username = "username",
                        password = "password"
    )
    try:
        # Get the id's of your posts from Reddit
        seq = reddit.redditor('redditor').submissions.new(limit = None)
        # Add all ids to a list to loop through 
        submissions_list = []


        for i in seq:
            submissions_list.append(i)

            for i in submissions_list:
                print(i)
                i.delete()

    except:
        pass
        print("Either something went wrong or there's nothing to delete")

def deletecomments():
    # Libraries needed
    import praw
    # Create a user instance
    reddit = praw.Reddit(client_id = "client_id",
                        client_secret = "client_secret",
                        user_agent = "user_agent",
                        username = "username",
                        password = "password"
    )
    try:
        # Get the id's of your comments from Reddit
        seq = reddit.redditor('redditor').comments.new(limit = None)
        # Add all ids to a list to loop through 
        submissions_list = []

        for i in seq:
            print(i)
            submissions_list.append(i)

        for i in submissions_list:
            print(i)
            i.delete()
    except:
        print("Either something went wrong or there's nothing to delete")

def delete():
    # More effecient way to run deletecomments and deleteposts
    deletecomments()
    deleteposts()
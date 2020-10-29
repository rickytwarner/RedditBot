def savemedia():
    # Libraries needed
    import praw, requests
    reddit = praw.Reddit(client_id = "client_id",
                        client_secret = "client_secret",
                        user_agent = "user_agent",
                        username = "username",
                        password = "password"
    )
    seq = reddit.redditor("redditor").saved(limit = None)

    submissions_list = []

    for i in seq:
         submissions_list.append(i)

    for i in submissions_list:
        submission = reddit.submission(id = i)



        try:
            media_url = submission.url
            if ".com" or ".net" or ".io" or ".org" or ".gov" in media_url:
                pass
            if "." not in media_url:
                pass
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
            r = requests.get(media_url)
            save_dir = "/Folder/Path/Here"
            final_save_dir = save_dir + "/" + final_name
            with open(final_save_dir, 'wb') as f:
                f.write(r.content)

        except:
            pass


def deleteposts():
    import praw
    reddit = praw.Reddit(client_id = "client_id",
                        client_secret = "client_secret",
                        user_agent = "user_agent",
                        username = "username",
                        password = "password"
    )
    try:
        seq = reddit.redditor('redditor').submissions.new(limit = None)
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
    import praw
    reddit = praw.Reddit(client_id = "client_id",
                        client_secret = "client_secret",
                        user_agent = "user_agent",
                        username = "username",
                        password = "password"
    )
    try:
        seq = reddit.redditor('redditor').comments.new(limit = None)

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
    deletecomments()
    deleteposts()

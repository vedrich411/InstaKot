try:
    # Libraries
    from os import listdir, system, mkdir, name
    from string import ascii_letters, digits
    from os.path import dirname, basename
    from sys import argv, executable
    from datetime import datetime
    from sys import version_info
    from json import loads
    from time import sleep
    import subprocess
    import threading



    # Python Location
    python = basename(executable)



    # Current Path
    if name == "nt":PATH = dirname(__file__)+'\\';slash = '\\'
    else:PATH = dirname(__file__)+'/'; slash = '/'
    Logs = PATH+"InstaKot_Logs"+slash



    # Colors
    lm, m, m0, r, y, b, g = "\033[0;35m", "\033[1;35m", "\033[1;37m", "\033[1;31m", "\033[1;33m", "\033[1;34m", "\033[1;32m"



    # Checking Python Version
    if version_info.major != 3:
        print(f"\n    {y}Python3 Required!{m0}\n")
        raise SystemExit



    # Main Args
    UN, FUN, INPUT_USERNAME, proxyS, Ls = None, '', None, 0, True
    logo = f"""{m0}\n            {lm}▄█  ███▄▄▄▄      ▄████████     ███        ▄████████  {m}  ▄█   ▄█▄  ▄██████▄      ███{m0}
            {lm}███  ███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███ {m}  ███ ▄███▀ ███    ███ ▀█████████▄{m0}
            {lm}███▌ ███   ███   ███    █▀     ▀███▀▀██   ███    ███ {m}  ███▐██▀   ███    ███    ▀███▀▀██{m0}
            {lm}███▌ ███   ███   ███            ███   ▀   ███    ███ {m} ▄█████▀    ███    ███     ███   ▀{m0}
            {lm}███▌ ███   ███ ▀███████████     ███     ▀███████████ {m}▀▀█████▄    ███    ███     ███{m0}
            {lm}███  ███   ███          ███     ███       ███    ███ {m}  ███▐██▄   ███    ███     ███{m0}
            {lm}███  ███   ███    ▄█    ███     ███       ███    ███ {m}  ███ ▀███▄ ███    ███     ███{m0}
            {lm}█▀    ▀█   █▀   ▄████████▀     ▄████▀     ███    █▀  {m}  ███   ▀█▀  ▀██████▀     ▄████▀{m0}\n\n\n"""
    args = []



    # HTTPS Request Data
    Requset_link = f"https://www.instagram.com/api/v1/users/web_profile_info/?username="
    user_agent = "Mozilla/5.0 (Window`s NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0"



    # Clear Screen Function
    def cls():
        system("clear||cls")



    # Username Validation
    def CheckUsername(user_name):
        if len(user_name) < 2: return "invalid"
        elif user_name[0] == '.': return "invalid"

        allowed_characters = list(ascii_letters + digits + '_' + '.')
        for x in user_name:
            if x not in allowed_characters:
                return
        for x in range(len(user_name)):
            if user_name[x] == '.':
                try:
                    if user_name[x+1] not in allowed_characters[:-1]:
                        return "invalid"
                except IndexError:
                    return "invalid"

        return "valid_username"



    # Get Profile Data
    def GetProfile(username):
        filename=f"{username}_"
        for x in str(datetime.now()).replace(' ','').replace(':','_'):
            if x == '.':
                filename += ".txt"
                break
            filename += x
        subprocess.run([python, "instakotGP.py", username, filename, "username"], capture_output=False)
        return filename



    # Get Profile Data
    def GetUsername(ID):
        filename=f"{ID}_"
        for x in str(datetime.now()).replace(' ','').replace(':','_'):
            if x == '.':
                filename += ".txt"
            filename += x
        subprocess.run([python, "instakotGP.py", str(ID), filename, 'id'], capture_output=False)
        return filename



    # Getting Username Input
    if len(args) > 0:
        INPUT_USERNAME = args[0]
        if CheckUsername(INPUT_USERNAME.replace(' ', '')) != "valid_username":
            print(f"{logo}{r}{' '*48}Invalid Username{m0}\n")
            raise SystemExit
        else:
            stop = False
    else:
        stop = True



    # Getting Method Input (Username, ID)
    if stop == True:
        INPUT_TEXT_1 = f"{' '*48}{r}-{m0} USERNAME\n{' '*48}{r}-{m0} ID{m0}\n\n{' '*43}{r}>>{m0} "
        while 1:
            cls();Method_INPUT = input(logo+INPUT_TEXT_1)
            try:
                int(Method_INPUT)
                Method = "      ID"
                break
            except:
                if CheckUsername(Method_INPUT.replace(' ', '').lower()) != "valid_username":
                    INPUT_TEXT_1 = f"{' '*48}{r}-{m0} USERNAME\n{' '*48}{r}-{m0} ID{m0}\n\n{' '*25}{b}(Invalid Input){m0}   {r}>>{m0} "
                else:
                    username = Method_INPUT.replace(' ','').lower()
                    Method = "USERNAME"
                    break
    stop = False;cls()



    # Getting instakotGP
    if "instakotGP.py" not in listdir(PATH):
        print(f"{b}Downloading instakotGP...{m0}")
        for x in range(4):
            if "instakotGP.py" in listdir(PATH):
                print(f"{g}instakotGP Is Downloaded!{m0}")
                break
            elif x == 4:
                print(f"{r}Couldn't Install ProxyKot.{m0}")
                raise SystemExit
            elif x > 1:
                print(f"{r}Didn't Work, Trying Again..{m0}")

            system(f"curl -s https://raw.githubusercontent.com/vedrich411/vedrich-db/main/instakotGP.py > {PATH}instakotGP.py")


    # InstaKot Logs
    try:mkdir(Logs)
    except:pass



    # [-- Start --]
    def loading():
        global stop
        s = f"\r{' '*48}{r}.  {m0}{' '*47}"
        while stop == False:
            sleep(1)
            print(s,end='')
            if s == f"\r{' '*48}{r}.  {m0}{' '*47}":
                s = f"\r{' '*48}{r}.. {m0}{' '*47}"
            elif s == f"\r{' '*48}{r}.. {m0}{' '*47}":
                s = f"\r{' '*48}{r}...{m0}{' '*47}"
            elif s == f"\r{' '*48}{r}...{m0}{' '*47}":
                s = f"\r{' '*48}{r}.  {m0}{' '*47}"
    Loading = threading.Thread(target=loading)

    while 1:

        if Method == "      ID":
            if Ls: cls();print(logo);Loading.start();Ls = False
            FileName_ID = GetUsername(Method_INPUT)

            if FileName_ID not in listdir(Logs):
                cls();print(logo);print(f"{' '*25}{r}Failed To Connect To Instagram, Check Your Internet Connection.{m0}\n")
                raise SystemExit

            else:
                stop = True;Loading.join();cls();print(logo)
                file_id = open(Logs+FileName_ID, encoding="utf-8", mode='r')
                check = file_id.readlines()[-1]
                try:
                    username = loads(r''.join(check), strict=False)["data"]["user"]["reel"]["user"]["username"]
                except:
                    cls();print(logo);print(f"{' '*45}{r}User Was Not Found{m0}\n")
                    raise SystemExit
                print(f"{' '*45}{g}[+] {username}\n")
                stop = False
                Method = "USERNAME"
                sleep(0.5)

        if Method == "USERNAME":
            if stop == False:cls();print(logo);print(f"{' '*45}{b}Getting Profile Info...{m0}\n")
            FileName = GetProfile(username)

            if FileName not in listdir(Logs):
                cls();print(logo);print(f"{' '*25}{r}Failed To Connect To Instagram, Check Your Internet Connection.{m0}\n")
                raise SystemExit
            else:
                file = open(Logs+FileName, encoding="utf-8", mode='r')
                check = file.readlines()[-1]
                try:
                    data = loads(r''.join(check), strict=False)
                except:
                    cls();print(logo);print(f"{' '*45}{r}User Was Not Found{m0}\n")
                    raise SystemExit
                file.close()
                cls()
                break

    blacklisted_values = [
        None, [], ''
    ]

    blacklisted_vars = [
        "PROFILE_PIC_URL",
        "REMOVE_MESSAGE_ENTRYPOINT",
        "REQUESTED_BY_VIEWER",
        "IS_SUPERVISED_BY_VIEWER",
        "IS_GUARDIAN_OF_VIEWER",
        "HAS_REQUESTED_VIEWER",
        "HAS_BLOCKED_VIEWER",
        ""

    ]
    info = []
    user_data = data["data"]["user"]



    for x in user_data:
        if user_data[x] not in blacklisted_values and x.upper() not in blacklisted_vars and type(user_data[x]) == str:
            value = f"{b}\"{m0}{user_data[x]}{b}\""
            info.append(f"        {x.upper()} {r}⇒{m0}  {value}{m0}\n")

    print(f"    {r}Basic Info{m0}")
    info.reverse()
    for z in info:print(z)

    following_count = str(user_data["edge_follow"]["count"])
    followers_count = str(user_data["edge_followed_by"]["count"])
    posts_count = str(user_data["edge_owner_to_timeline_media"]["count"])
    country_block = user_data["country_block"]
    if country_block == False:country_blocked = f"        COUNTRY BLOCKED {r}⇒{m0}  {r}{str(country_block)}{m0}\n"
    else:country_blocked = f"        COUNTRY BLOCKED {r}⇒{m0}  {g}{str(country_block)}{m0}\n"
    print(f"        FOLLOWING{r}⇒{m0}  {following_count}\n")
    print(f"        FOLLOWERS {r}⇒{m0}  {followers_count}\n")
    print(f"        POSTS{r}⇒{m0}  {posts_count}\n")
    print(country_blocked)

    input(f"\n{y}Enter For More...{m0}")
    print(f"\n\n    {r}Deeper Info{m0}")
    for x in ["has_clips",
                "is_private", 
                "is_professional_account",
                "is_business_account", 
                "is_supervised_user", 
                "is_verified", 
                "should_show_category",
                "should_show_public_contacts",
                "show_account_transparency_details"]:
        X = x.replace('_', ' ').upper()
        if user_data[x] == False:print(f"        {X}{r}⇒{m0}  {r}{str(user_data[x])}{m0}\n")
        else:user_data[x] = print(f"        {X}{r}⇒{m0}  {g}{str(user_data[x])}{m0}\n")

    input(f"\n{y}Enter For Posts...{m0}")
    posts = user_data["edge_owner_to_timeline_media"]["edges"]
    print(f"\n\n    {r}Posts{m0}")
    if len(posts) == 0:
        print(f"        {r}None")
        raise SystemExit
    else:
        for x in range(len(posts)):
                post_info = posts[x]["node"]
                post_type = post_info["__typename"]

                if post_type == "GraphSidecar":
                    posts_sidecar = post_info["edge_sidecar_to_children"]["edges"]
                    for v in range(len(posts_sidecar)):
                        post_sidecar_info = posts_sidecar[v]["node"]
                        post_post_sidecar_info_type = post_sidecar_info["__typename"]
                        if post_post_sidecar_info_type == "GraphImage":
                            accessibility_caption = post_sidecar_info["accessibility_caption"]
                            source = post_sidecar_info["display_url"]
                            print(f"            ACCESSIBILITY CAPTION{r}⇒{m0}  {accessibility_caption}\n")
                            print(f"            SOURCE{r}⇒{m0}  {b}\"{m0}{source}{b}\"{m0}\n")
                            print(f'{m}⇐'+60*"⇋⇌"+f'{m}⇒{m0}')

                elif post_type == "GraphImage":
                    captions = post_info["edge_media_to_caption"]["edges"][0]["node"]["text"]
                    accessibility_caption = post_info["accessibility_caption"]
                    taken_at_timestamp = datetime.fromtimestamp(int(post_info["taken_at_timestamp"]))
                    source = post_info["display_url"]
                    likes = post_info["edge_liked_by"]["count"]
                    comments = post_info["edge_media_to_comment"]["count"]
                    if post_info["viewer_can_reshare"] == True:viewer_can_reshare=g+str(post_info["viewer_can_reshare"])+m0
                    else:viewer_can_reshare=r+str(post_info["viewer_can_reshare"])+m0

                    print(f"        {b}\"{m0}{captions}{b}\"{m0}\n")
                    print(f"            ACCESSIBILITY CAPTION{r}⇒{m0}  {accessibility_caption}\n")
                    print(f"            TAKEN{r}⇒{m0}  {taken_at_timestamp}\n")
                    print(f"            SOURCE{r}⇒{m0}  {b}\"{m0}{source}{b}\"{m0}\n")
                    print(f"            LIKES{r}⇒{m0}  {str(likes)}\n")
                    print(f"            COMMENTS{r}⇒{m0}  {str(comments)}\n")
                    print(f"            YOU CAN SHARE{r}⇒{m0}  {viewer_can_reshare}\n\n\n")
                    print(f'{m}⇐'+60*"⇋⇌"+f'{m}⇒{m0}')

                elif post_type == "GraphVideo":
                    taken_at_timestamp = datetime.fromtimestamp(int(post_info["taken_at_timestamp"]))
                    thumbnail = post_info["thumbnail_src"]
                    video_url = post_info["video_url"]
                    views = post_info["video_view_count"]
                    likes = post_info["edge_liked_by"]["count"]
                    comments = post_info["edge_media_to_comment"]["count"]
                    if post_info["viewer_can_reshare"] == True:viewer_can_reshare=g+str(post_info["viewer_can_reshare"])+m0
                    else:viewer_can_reshare=r+str(post_info["viewer_can_reshare"])+m0

                    try:captions = post_info["edge_media_to_caption"]["edges"][0]["node"]["text"];print(f"        {b}\"{m0}{captions}{b}\"{m0}\n")
                    except:None
                    print(f"            TAKEN{r}⇒{m0}  {taken_at_timestamp}\n")
                    print(f"            THUBNAIL{r}⇒{m0}  {thumbnail}\n")
                    print(f"            VIDEO URL{r}⇒{m0}  {video_url}\n")
                    try:video_duration = str(post_info["video_duration"]);print(f"            VIDEO DURATION{r}⇒{m0}  {video_duration}\n")
                    except:None
                    print(f"            VIEWS{r}⇒{m0}  {str(views)}\n")
                    print(f"            LIKES{r}⇒{m0}  {str(likes)}\n")
                    print(f"            COMMENTS{r}⇒{m0}  {str(comments)}\n")
                    print(f"            YOU CAN SHARE{r}⇒{m0}  {viewer_can_reshare}\n\n\n")
                    print(f'{m}⇐'+60*"⇋⇌"+f'{m}⇒{m0}')
    raise SystemExit



except SystemExit:
    print('\033[0m', end='')

except (KeyboardInterrupt, SystemExit):
    print("\n\033[1;31mGoodbye!\033[0m")

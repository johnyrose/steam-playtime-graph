# Steam developer playtime graph

This small Python project allows you to create a column graph of the amount of playtime you have on Steam games per developer or per publisher.

### Example:
![alt text](https://i.ibb.co/mq8WxMC/Devs-Graph.png)

### How to use:

In order to create a graph based on your Steam profile, you'll need to follow the following steps:

#### Prerequisites:
- Have Python 3.6 or later installed.
- Have 'Game details' in your Steam profile set to Public (instructions on how to do it can be found in the 'Steam profile preparing' section later in the ReadMe).
- Have a Steam API key ready (instructions on how to do it can be found in the 'Steam profile preparing' section later in the ReadMe)
- Have your Steam profile name ready.

#### Steps:
- Clone this repository:
    ```
    git clone https://github.com/johnyrose/steam-playtime-graph.git
    cd steam-playtime-graph
    ```
- Install the requirements:
    ```
    pip install -r requirements.txt
    ```
- Create the configuration JSON file by name the `config.json` in the project's root directory (Explanation can be found under the Config File Parameters part later in the ReadMe.):
    ```json
    {
      "steam_profile_name": "<Your Steam profile name>",
      "steam_api_key": "<Your Steam API Key>",
      "max_bars_amount": 15,
      "minimum_hours": 1,
      "graph_title": "Amount of hours spent per developer",
      "x_label": "Developer",
      "y_label": "Hours",
      "measure_by": "developer",
      "parallel_api_requests": 2
    }
    ```
- Run the main.py file:
    ```bash
    python main.py
    ```
    
#### Steam profile preparing:

In order to run this project, you need to follow the following Steam-related instructions:

- Have your Game Details set to Public on steam:
    - Go to your Steam profile page and click 'Edit Profile' (You need to be logged in).
    - In the 'Edit' side-menu, go to 'My Privacy Settings' 
    - Under 'My Profile', make sure that both 'My profile' and 'Game details' are set to public.
- Have a Steam API key:
    - Since this project uses the Steam API, it requires a Steam API key. An API key can be obtained quite easily.
    - Go to https://steamcommunity.com/dev/apikey (Make sure to login if you haven't).
    - In 'Domain', write anything you wish and request the key.
    - Copy and keep the key that is presented to you.
- Have your Steam profile name ready:
    - Your Steam profile name can be found if you go to 'Edit Profile' on your profile page. Once you're there, copy the editable part in the Custom URL section. That is the profile name you need.
    
#### Config File Parameters:
Your config file needs to be called config.json and look like the following:

    {
      "steam_profile_name": "<Your Steam profile name>",
      "steam_api_key": "<Your Steam API Key>",
      "max_bars_amount": 15,
      "minimum_hours": 1,
      "graph_title": "Amount of hours spent per developer",
      "x_label": "Developer",
      "y_label": "Hours",
      "measure_by": "developer",
      "parallel_api_requests": 2
    }
    
You can edit the following parameters if you wish:
- max_bars_amount: The max top results that will be presented.
- minumum_hours: The minimum required playtime in hours that can appear in the graph.
- graph_title: The title that will be presented in the graph.
- x_label: The label that will be given to the X line in the graph. 
- y_label: The label that will be given to the Y line in the graph.
- measure_by: Can be either `developer` or `publisher`. Sets whether the graph will include playtime be Developer or Publisher.
- parallel_api_requests: Since the code uses the SteamSpy API to find info about games, it limits the amount of parallel HTTP requests made to that API. I highly recommend leaving it at 2, as testing with 3 or more returned errors of too many requests from SteamSpy. 

Feel free to contact me for any questions / ideas for improvement! This is a small project that I put together in an evening and don't intend on changing it too much once it's finished, but I'm always open for feedback.
 
    

# Steam developer playtime graph

This small Python project allows you to create a column graph of the amount of playtime you have on Steam games per developer or per publisher.

### Example:
`Add image here`

### How to use:

In order to create a graph based on your Steam profile, you'll need to follow the following steps:

#### Prerequisites:
- Have Python 3.6 or later installed.
- Have 'Game details' in your Steam profile set to Public (instructions on how to do it can be found in the 'Steam profile preparing' section later in the ReadMe).

#### Steps:
- Clone this repository:
    ```
    git clone https://github.com/Ripolak/steam-playtime-graph.git
    cd steam-playtime-graph
    ```
- Install the requirements:
    ```
    pip install -r requirements.txt
    ```
- Create the configuration JSON file by name the `config.json` in the project's root directory:
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
import argparse
import sys
from curses import wrapper
from os import chdir
from os.path import expanduser
from pathlib import Path

import yaml

from screensaver import main_loop

DEFAULT_PROFILE = 'j316'
SCREENSAVER_TITLE = 'JOHN 3:16'

# used to merge config files
def merge_config(base, override):
    for key, value in override.items():
        if (key in base and isinstance(base[key], dict) and isinstance(value, dict)):
            merge_config(base[key], value)
        else:
            base[key] = value
    return base

# main
if __name__ == "__main__":
    # loads both local and config dir
    local_dir = Path(__file__).parent
    local_config = local_dir / "config.yaml"
    user_config = Path.home() / ".config" / "j316" / "config.yaml"
    chdir(local_dir)

    config = {}

    with open(local_config, 'r') as file:
        config = yaml.safe_load(file)

    if user_config.exists():
        with open(user_config, 'r') as file:
            user_config_data = yaml.safe_load(file) or {}
        merge_config(config, user_config_data) 

    # parses options and args for -h
    parser = argparse.ArgumentParser(description="J3_16 Screensaver.")
    parser.add_argument("-p", "--profile", type=str, help="Desired profile to use")
    parser.add_argument("-l", "--list", action="store_true", help="List all profiles available")
    args = parser.parse_args()

    # lists all profiles
    if args.list:
        all_profiles = config['profile']
        print("Current profiles: ")
        for p in all_profiles:
            print(f"-{p}")
        sys.exit(0)
    
    # parses desired profile else uses default (J316)
    profile_name = args.profile if args.profile else DEFAULT_PROFILE

    title = config['profile'][profile_name].get("title", SCREENSAVER_TITLE)
    
    # opens profiles source file
    with open(expanduser(config['profile'][profile_name]['top_left']), 'r') as ascii:
        top_left = ascii.read()
    with open(expanduser(config['profile'][profile_name]['top_right']), 'r') as ascii:
        top_right = ascii.read()
    with open(expanduser(config['profile'][profile_name]['top_center']), 'r') as ascii:
        top_center = ascii.read()
    with open(expanduser(config['profile'][profile_name]['centered_text']), 'r') as ascii:
        centered_text = ascii.read()
    with open(expanduser(config['profile'][profile_name]['bottom_left']), 'r') as ascii:
        bottom_left = ascii.read()
    with open(expanduser(config['profile'][profile_name]['bottom_center']), 'r') as ascii:
        bottom_center = ascii.read()
    with open(expanduser(config['profile'][profile_name]['bottom_right']), 'r') as ascii:
        bottom_right = ascii.read()

    # wrapper func
    wrapper(
        main_loop, 
        top_left= top_left, 
        top_center = top_center,
        top_right = top_right,
        centered_text= centered_text,
        bottom_left= bottom_left,
        bottom_center= bottom_center,
        bottom_right = bottom_right,
        title= title
    )
    


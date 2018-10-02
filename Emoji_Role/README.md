# Assign role with an emoji reaction

This should work with all custom and standard emojis.

# Getting Started
## This is built for my [Basic-Cog-Bot](https://github.com/stroupbslayen/Basic-Cog-Bot)
- Install the requirements with `pip install -r requirements.txt`
- Put the script in the 'cogs' folder of the Cog Bot and that's it!

# Commands
## add_emoji_roles
- Aliases - `aer, add`
- Usage - `<prefix>add <category> <emoji> <role> <description>`
- Example - `!add example_category 👿 @example this is just an example`
- Description - Assign emojis to a specific role. Emojis with common categories will be posted together on the next notificaiton message.

## delete_emoji_roles
- Aliases - `der, delete`
- Usage - `<prefix>delete <emoji>`
- Example - `!delete 👿`
- Description - Enter the emoji you would like to remove.

## create
- Aliases - `null`
- Usage - `<prefix>create <category>`
- Example - `!create example_category`
- Description - Will create a message using emojis from the specified category. 

## categories
- Aliases - `null`
- Usage - `<prefix>categories`
- Example - `!categories`
- Description - Check what categories are available.


# Notes
- Python 3.6 is required
- Commands reqiure Admin permissions

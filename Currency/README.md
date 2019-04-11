# A basic economy/currency cog for discord.py

# Getting Started
## This is built for my [Basic-Cog-Bot](https://github.com/stroupbslayen/Basic-Cog-Bot)
- Install the requirements with `pip install -r requirements.txt`
- Put the script in the 'cogs' folder of the Cog Bot and that's it!

# Commands
## addApproved        
- Aliases - `addrole`
- Usage - `<prefix>addApproved <roles>`
- Example - `!addApproved @role1 @role2`
- Description - Add roles that can deposit or withdraw currency from members.

## approved                   
- Aliases - `approved`
- Usage - `<prefix>approved`
- Example - `!approved`
- Description - Get a list of approved roles that can deposit or withdraw from members.

## balance                               
- Aliases - `Null`
- Usage - `<prefix>balance <member or Null>`
- Example - `!balance @member` or `!balance`
- Description - Check the balance of your account or another member

## changeCurrency                               
- Aliases - `currencyname`
- Usage - `<prefix>changeCurrency <new_currency>`
- Example - `!changeCurrency schilling`
- Description - Change the currency name that the server is using. Default is **dollar**.

## delApproved                   
- Aliases - `delrole`
- Usage - `<prefix>delApproved <roles>`
- Example - `!delApproved @role1 @role2`
- Description - Remove roles that can deposit or withdraw currency from members.

## deposit                   
- Aliases - `add, give`
- Usage - `<prefix>deposit <amount> <member>`
- Example - `!deposit 100 @member`
- Description - Deposit currency into a members account.

## leaderboard                    
- Aliases - `Null`
- Usage - `<prefix>leaderboard`
- Example - `!leaderboard`
- Description - Get a leaderboard showing the top 10 members with the largest account.

## withdraw                    
- Aliases - `remove, take`
- Usage - `<prefix>withdraw <amount> <member>`
- Example - `!withdraw 100 @member`
- Description - Withdraw currency from a members account.

# Notes
- Python 3.6+ is required
- Bot/Guild owners don't need approved roles to use commands

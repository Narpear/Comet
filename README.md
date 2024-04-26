# Comet - Discord Bot with Stats Commands

This is a Discord bot written in Python using the `discord.py` library. The bot provides various commands to display statistics and information about the server and its members.

## Features

- **`.age`**: Displays the number of days since the server was created.
- **`.active`**: Shows how long the bot has been active in the server.
- **`.members`**: Lists all members in the server.
- **`.bots`**: Lists all bots in the server.
- **`.member_stats`**: Displays information about a specific member, including their name, display name, and roles.
- **`.uptime`**: Shows the uptime of the bot.
- **`.ping`**: Displays the latency of the bot.
- **`.avatar`**: Shows the avatar of a specified member or the user who invoked the command.
- **`.server_info`**: Provides information about the server, including the owner, member count, and creation date.
- **`.clear`**: Allows users with the "Manage Messages" permission to delete a specified number of messages (up to 100) from the channel.

## Setup

1. Install the required dependencies by running `pip install discord.py` in your terminal or command prompt.
2. Replace `"token-here"` in the code with your actual Discord bot token.
3. Run the `main.py` script to start the bot.

## Usage

Once the bot is running, you can use the various commands by typing the command prefix (`.`) followed by the command name in any text channel where the bot has access.

For example, to get the server's creation date, type `.age` in a text channel.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
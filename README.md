# r/brno

Community wiki and configuration for [r/brno](https://reddit.com/r/brno) - the subreddit for Brno, Czech Republic.

## What's Here

This repository contains:

| Path | Description | Syncs To |
|------|-------------|----------|
| `wiki/index.md` | Main wiki page - living, studying, tourism info | [/r/brno/wiki/index](https://www.reddit.com/r/brno/wiki/index) |
| `wiki/moderation_instructions.yaml` | AI moderation bot instructions | [/r/brno/wiki/moderation_instructions](https://www.reddit.com/r/brno/wiki/moderation_instructions) |
| `wiki/config/automoderator.yaml` | AutoModerator rules | [/r/brno/wiki/config/automoderator](https://www.reddit.com/r/brno/wiki/config/automoderator) |
| `wiki/config/sidebar.md` | Subreddit sidebar | [/r/brno/wiki/config/sidebar](https://www.reddit.com/r/brno/wiki/config/sidebar) |
| `wiki/config/description.md` | Subreddit description | [/r/brno/wiki/config/description](https://www.reddit.com/r/brno/wiki/config/description) |

The **[/r/brno/wiki/awesome](https://www.reddit.com/r/brno/wiki/awesome)** page is automatically fetched from [scherrer-txt/brno-awesome](https://github.com/scherrer-txt/brno-awesome).

## How It Works

When changes are merged into `wiki/**` files on the `main` branch:

1. GitHub Action triggers automatically
2. Sends file contents to [Windmill](https://www.windmill.dev/) webhook
3. Windmill script updates the corresponding https://reddit.com/r/brno/wiki pages

Each wiki revision shows the commit link, e.g., `Sync from GitHub: https://github.com/kerray/r-brno/commit/abc1234`

## Contributing

**You can contribute!**

- **Report issues**: [Open an issue](https://github.com/kerray/r-brno/issues) for outdated info, broken links, or suggestions
- Even better - **Submit changes**: [Create a pull request](https://github.com/kerray/r-brno/pulls) with your edits
- **Discuss**: Comment on existing issues or PRs

### Editing Tips

- Wiki pages use **Markdown** formatting
- Test your markdown before submitting - you can use for example https://markdownlivepreview.com/
- For `moderation_instructions.yaml` - this is the actual config the moderation bot LLM reads, a kind of constitution of the subreddit, be thoughtful with changes

## Automated Moderation

r/brno uses an AI-powered moderation bot `[/u/ponocny_bot](https://reddit.com/u/ponocny_bot)`. The bot's instructions should be fully transparent for inspection.

- **Config**: [`wiki/moderation_instructions.yaml`](wiki/moderation_instructions.yaml)
- **Live on Reddit**: [/r/brno/wiki/moderation_instructions](https://www.reddit.com/r/brno/wiki/moderation_instructions)

## Related

- [r/brno](https://reddit.com/r/brno) - The subreddit
- [scherrer-txt/brno-awesome](https://github.com/scherrer-txt/brno-awesome) - Curated Brno resources
- [Brno Discord](https://discord.gg/BhsT4zYSGV) - Community chat, boring and weird just like Brno

## License

Content is provided for the r/brno community. Wiki content may be freely shared and adapted with attribution.

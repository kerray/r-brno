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
| `wiki/ama/*.md` | AMA series — rules, moderation, invitation, ÚDHPSH query | [/r/brno/wiki/ama/…](https://www.reddit.com/r/brno/wiki/ama/index) |
| `rules/` | Written keys the AMA curation follows — human-readable source of truth | not synced |
| `prompts/` | The prompts the language model is actually run with | not synced |
| `runs/` | Per-run logs: input, output, human deviations, cost | not synced |
| `tools/` | Scripts that decide something a moderator would otherwise decide — e.g. the public AMA slot draw | not synced |

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

## AMA series (2026 municipal elections)

A pilot series of AMAs with people running for Brno's city council. Everything that shapes what
gets asked is public **before** it runs: the written curation key, the prompts, and the per-run logs.

- **Rozcestník**: [/r/brno/wiki/ama](https://www.reddit.com/r/brno/wiki/ama/index)
- **Curation key**: [`rules/curation-key.md`](rules/curation-key.md) — source of truth; the prompt is derived from it, never the other way round
- **Prompts**: [`prompts/`](prompts/) — model `claude-sonnet-5`, frozen and tagged `ama-YYYY-MM-DD-subject` when the question thread opens
- **Run logs**: [`runs/`](runs/) — written by the script, not by hand
- **Draw**: [`tools/losovani.py`](tools/losovani.py) — when more groups want the same slot, the order is drawn publicly; the seed is the ČNB EUR/CZK rate published that day, so anyone can recompute it ([`tools/README.md`](tools/README.md))

Comments on the rules and prompts are most useful **before** a rule runs for real — issue or PR.

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

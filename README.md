# Scraper for Techshare

A Python script to download videos from public Instagram accounts.

## Features

- Downloads videos from any public Instagram profile
- Saves video thumbnails and metadata (JSON)
- Configurable number of videos to download
- Skips non-video posts automatically

## Requirements

- Python 3.7+
- instaloader

## Installation

```bash
pip install instaloader
```

## Usage

1. Edit the configuration at the top of `instagram_scraper.py`:

```python
USERNAME = "tamuphysastr"  # Instagram username to scrape
MAX_VIDEOS = 30            # Number of videos to download
OUTPUT_DIR = "~/tamuphysastr_videos"  # Output directory
```

2. Run the script:

```bash
python instagram_scraper.py
```

## Output

Videos are saved with the naming pattern:
```
{date_utc}__{shortcode}.mp4
```

Each video also includes:
- `.jpg` - Video thumbnail
- `.json` - Post metadata

## Notes

- Only works with public profiles (or profiles you follow if logged in)
- Instagram may rate-limit requests; if this happens, wait and try again
- For private profiles, you can login with: `instaloader --login YOUR_USERNAME`

## License

MIT

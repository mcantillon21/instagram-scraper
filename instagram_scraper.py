#!/usr/bin/env python3
"""
Instagram Video Scraper for @tamuphysastr
Downloads the past 30 videos from the specified Instagram account.
Uses instaloader library for reliable Instagram scraping.
"""

import os
import subprocess
import sys

# Configuration
USERNAME = "tamuphysastr"
MAX_VIDEOS = 30
OUTPUT_DIR = os.path.expanduser("~/tamuphysastr_videos")


def install_instaloader():
    """Install instaloader if not present."""
    try:
        import instaloader
        print("instaloader is installed.")
        return True
    except ImportError:
        print("Installing instaloader...")
        subprocess.run([sys.executable, "-m", "pip", "install", "instaloader"], check=True)
        return True


def scrape_videos():
    """Scrape videos from the Instagram account."""
    import instaloader

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Initialize Instaloader
    L = instaloader.Instaloader(
        dirname_pattern=OUTPUT_DIR,
        filename_pattern="{date_utc}__{shortcode}",
        download_videos=True,
        download_video_thumbnails=True,
        download_geotags=False,
        download_comments=False,
        save_metadata=True,
        compress_json=False,
        post_metadata_txt_pattern="",  # Don't create txt files
    )

    print(f"\nScraping up to {MAX_VIDEOS} videos from @{USERNAME}")
    print(f"Output directory: {OUTPUT_DIR}\n")

    try:
        # Get profile
        print(f"Fetching profile for @{USERNAME}...")
        profile = instaloader.Profile.from_username(L.context, USERNAME)

        print(f"Profile found: {profile.full_name}")
        print(f"Total posts: {profile.mediacount}")
        print(f"Followers: {profile.followers}")
        print("\nDownloading videos...\n")

        video_count = 0
        post_count = 0

        # Iterate through posts
        for post in profile.get_posts():
            post_count += 1

            # Check if it's a video
            if post.is_video:
                print(f"[{video_count + 1}/{MAX_VIDEOS}] Downloading video: {post.shortcode}")
                try:
                    L.download_post(post, target=OUTPUT_DIR)
                    video_count += 1
                    print(f"  ✓ Downloaded successfully")
                except Exception as e:
                    print(f"  ✗ Error downloading: {e}")

                if video_count >= MAX_VIDEOS:
                    break
            else:
                print(f"  Skipping non-video post: {post.shortcode}")

            # Safety limit to avoid going through too many posts
            if post_count > 200:
                print("\nReached post limit (200 posts scanned)")
                break

        print(f"\n{'='*50}")
        print(f"Download complete!")
        print(f"Videos downloaded: {video_count}")
        print(f"Posts scanned: {post_count}")
        print(f"Output directory: {OUTPUT_DIR}")
        print(f"{'='*50}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Profile @{USERNAME} does not exist.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"Error: Profile @{USERNAME} is private. You need to login to access it.")
        print("\nTo login, run: instaloader --login YOUR_USERNAME")
        print("Then re-run this script.")
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection error: {e}")
        print("\nInstagram may be rate-limiting. Try again later or login to avoid limits.")
    except Exception as e:
        print(f"Error: {e}")
        raise


def main():
    print("=" * 50)
    print(f"Instagram Video Scraper - @{USERNAME}")
    print("=" * 50)

    install_instaloader()
    scrape_videos()


if __name__ == "__main__":
    main()

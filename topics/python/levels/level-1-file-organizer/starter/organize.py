#!/usr/bin/env python3
"""File organizer — sorts files into subdirectories by extension category."""
import argparse
import os
import shutil
import sys

# Extension → category mapping. Modify if needed.
EXTENSION_MAP = {
    # Images
    ".jpg": "images", ".jpeg": "images", ".png": "images",
    ".gif": "images", ".svg": "images", ".webp": "images",
    # Documents
    ".pdf": "docs", ".doc": "docs", ".docx": "docs",
    ".txt": "docs", ".md": "docs", ".rtf": "docs",
    # Data
    ".csv": "data", ".json": "data", ".xml": "data",
    ".xlsx": "data", ".xls": "data",
    # Archives
    ".zip": "archives", ".tar": "archives", ".gz": "archives",
    ".rar": "archives", ".7z": "archives",
    # Code
    ".py": "code", ".js": "code", ".html": "code",
    ".css": "code", ".java": "code",
}

def parse_args():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory into subdirectories by extension."
    )
    parser.add_argument(
        "--directory", required=True, help="Path to the directory to organize."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would happen without actually moving files."
    )
    return parser.parse_args()

def categorize(filename):
    _, ext = os.path.splitext(filename)
    return EXTENSION_MAP.get(ext.lower())

def create_category_dirs(base_dir, categories):
    for category in categories:
        os.makedirs(os.path.join(base_dir, category), exist_ok=True)

def organize_files(directory, dry_run=False):
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    files = [f for f in os.listdir(directory)
             if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print("No files to organize.")
        return

    categories = set()
    file_categories = {}
    for filename in files:
        category = categorize(filename)
        if category is None:
            category = "other"
        categories.add(category)
        file_categories[filename] = category

    if not dry_run:
        create_category_dirs(directory, categories)

    for filename, category in file_categories.items():
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, category, filename)
        if dry_run:
            print(f"[dry-run] Would move: {filename} → {category}/")
        else:
            if os.path.exists(dst):
                print(f"Skipping {filename}: already exists in {category}/")
            else:
                shutil.move(src, dst)
                print(f"Moved: {filename} → {category}/")

def main():
    args = parse_args()
    organize_files(args.directory, args.dry_run)

if __name__ == "__main__":
    main()

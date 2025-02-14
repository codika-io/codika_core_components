import os
import sys
from pathlib import Path
from typing import Tuple, List, Set

def find_matches(search_string: str, start_path: str = '.') -> Tuple[Set[Path], Set[Path]]:
    """
    Find all directories and files containing the search string in their name.
    
    Args:
        search_string: The string to search for in paths
        start_path: The directory to start searching from
    
    Returns:
        Tuple of (matching_dirs, matching_files)
    """
    matching_dirs = set()
    matching_files = set()
    
    try:
        start_path = Path(start_path).resolve()
        
        # Walk bottom-up to handle nested directories correctly
        for root, dirs, files in os.walk(start_path, topdown=False):
            root_path = Path(root)
            
            # Check files
            for file in files:
                if search_string.lower() in file.lower():
                    matching_files.add(root_path / file)
            
            # Check directories
            for dir_name in dirs:
                if search_string.lower() in dir_name.lower():
                    matching_dirs.add(root_path / dir_name)
                    
        # Check the start directory itself
        if search_string.lower() in start_path.name.lower():
            matching_dirs.add(start_path)
            
    except Exception as e:
        print(f"An error occurred while searching: {e}")
        return set(), set()
        
    return matching_dirs, matching_files

def preview_changes(path: Path, search_string: str, replace_string: str) -> str:
    """Generate preview of the rename operation."""
    new_name = path.name.replace(search_string, replace_string)
    return str(path.parent / new_name)

def rename_paths(paths: Set[Path], search_string: str, replace_string: str) -> None:
    """Safely rename the given paths."""
    for path in paths:
        try:
            new_path = Path(preview_changes(path, search_string, replace_string))
            path.rename(new_path)
            print(f"Renamed: {path} -> {new_path}")
        except Exception as e:
            print(f"Failed to rename {path}: {e}")

def main(search_string: str, replace_string: str, start_path: str = '.') -> None:
    """Main function to find and replace strings in paths."""
    matching_dirs, matching_files = find_matches(search_string, start_path)
    
    if not matching_dirs and not matching_files:
        print(f"No files or directories found containing '{search_string}'")
        return
        
    print("\nFound matches:")
    print(f"- {len(matching_dirs)} directories")
    print(f"- {len(matching_files)} files")
    
    print("\nDirectory matches:")
    for dir_path in matching_dirs:
        print(f"  {dir_path} -> {preview_changes(dir_path, search_string, replace_string)}")
        
    print("\nFile matches:")
    for file_path in matching_files:
        print(f"  {file_path} -> {preview_changes(file_path, search_string, replace_string)}")
    
    response = input("\nDo you want to proceed with these changes? (yes/no): ").lower()
    if response != 'yes':
        print("Operation cancelled.")
        return
        
    print("\nApplying changes...")
    # Rename directories first (bottom-up order is important)
    rename_paths(matching_dirs, search_string, replace_string)
    # Then rename files
    rename_paths(matching_files, search_string, replace_string)
    print("Done!")
    print("This script only replaces the first match it finds in a path.")
    print("Re run this script to check that there is no more matches.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file_name_check.py <search_string> <replace_string>")
        sys.exit(1)
    
    search_string = sys.argv[1]
    replace_string = sys.argv[2]
    main(search_string, replace_string)

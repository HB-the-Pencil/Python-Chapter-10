from pathlib import Path

def get_words(path: Path):
    """
    Get a list of every word in the selected text file.

    :param path: Path to selected file.
    :return: Returns a list of words.
    """
    content = path.read_text("utf-8")
    words = content.lower().split()
    return words

wells_path = Path("worlds.txt")
vonnegut_path = Path("2br02b.txt")
baum_path = Path("wizard.txt")

wells_words = get_words(wells_path)
vonnegut_words = get_words(vonnegut_path)
baum_words = get_words(baum_path)

print(f'The novel The War of the Worlds contains the word "the" '
      f'approximately {wells_words.count("the")} times.')
print(f'The novel 2 B R 0 2 B contains the word "the" '
      f'approximately {vonnegut_words.count("the")} times.')
print(f'The novel The Wonderful Wizard of Oz contains the word "the" '
      f'approximately {baum_words.count("the")} times.')
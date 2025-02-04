import time
import pyperclip
import os

pyperclip.set_clipboard("xclip")
# Use 'xclip' or 'wl-copy' to grab the current selection
def get_selected_text():
    try:
        return os.popen("xclip -o -selection primary").read().strip()
    except:
        return ""


# Define mapping from TR-QWERTY (Latin) to Persian
latin_to_persian_map = {
    'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع', 'ı': 'ه', 'i': 'گ',
    'o': 'خ', 'p': 'ح', 'ğ': 'ج', 'ü': 'چ', 'a': 'ش', 's': 'س', 'd': 'ی', 'f': 'ب', 'g': 'ل',
    'h': 'ا', 'j': 'ت', 'k': 'ن', 'l': 'م', 'ş': 'ک', 'z': 'ظ', 'x': 'ط', 'c': 'ز', 'v': 'ر',
    'b': 'ذ', 'n': 'د', 'm': 'ئ', ',': 'پ', '.': '/',
    'ö': 'و', 'ç': '.', '"': '÷', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶',
    '7': '۷', '8': '۸', '9': '۹', '0': '۰', '*': '-', '-': '=',
    'Q': 'ً', 'W': 'ٌ', 'E': 'ٍ', 'R': '﷼', 'T': '،', 'Y': '؛', 'U': ',', 'I': ']', 'O': '[',
    'P': '\\', 'Ğ': '}', 'Ü': '{', 'A': 'َ', 'S': 'ُ', 'D': 'ِ', 'F': 'ّ', 'G': 'ۀ', 'H': 'آ',
    'J': 'ـ', 'K': '«', 'L': '»', 'Ş': ':', 'İ': '"', ';': '|', 'Z': 'ة', 'X': 'ي', 'C': 'ژ',
    'V': 'ؤ', 'B': 'أ', 'N': 'إ', 'M': 'ء', 'Ö': '<', 'Ç': '>', ':': '؟', 'é': '×', '!': '!',
    '\'': '@', '^': '#', '+': '$', '%': '%', '&': '^', '/': '&', '(': '*', ')': ')', '=': '(',
    '?': '_', '_': '؟'  # FIXED: Ensuring correct mapping for question mark
}


persian_to_latin_map = {v: k for k, v in latin_to_persian_map.items()}

# Special cases
special_cases = {
    'جش': 'ä'
}

def is_persian(text):
    """Check if all characters in text are Persian."""
    return all(char in persian_to_latin_map or char.isspace() for char in text)

def is_trqwerty(text):
    """Check if all characters in text are TR-QWERTY."""
    return all(char in latin_to_persian_map or char.isspace() for char in text)

def convert_text(text):
    """Convert text in one direction based on its original script."""
    if is_persian(text):
        conversion_map = persian_to_latin_map  # Convert Persian → TR-QWERTY
    elif is_trqwerty(text):
        conversion_map = latin_to_persian_map  # Convert TR-QWERTY → Persian
    else:
        return text  # Mixed text remains unchanged

    converted_text = ''.join(conversion_map.get(char, char) for char in text)
    return converted_text

# Main Execution
selected_text = get_selected_text()

if selected_text:
    converted_text = convert_text(selected_text)
    pyperclip.copy(converted_text)

    print("Converted text copied to clipboard!")

    # Check if `xdotool` exists before trying to paste
    if os.system("command -v xdotool >/dev/null 2>&1") == 0:
        time.sleep(0.5)
        os.system("xdotool key ctrl+v")
else:
    print("No selected text found!")

config.bind('<Ctrl-z>', 'hint links userscript qute-zotero')
c.bindings.key_mappings = {
    'Й': 'Q', 'й': 'q',
    'Ц': 'W', 'ц': 'w',
    'У': 'E', 'у': 'e',
    'К': 'R', 'к': 'r',
    'Е': 'T', 'е': 't',
    'Н': 'Y', 'н': 'y',
    'Г': 'U', 'г': 'u',
    'Ш': 'I', 'ш': 'i',
    'Щ': 'O', 'щ': 'o',
    'З': 'P', 'з': 'p',
    'Х': '{', 'х': '[',
    'Ъ': '}', 'ъ': ']',
    'Ф': 'A', 'ф': 'a',
    'Ы': 'S', 'ы': 's',
    'В': 'D', 'в': 'd',
    'А': 'F', 'а': 'f',
    'П': 'G', 'п': 'g',
    'Р': 'H', 'р': 'h',
    'О': 'J', 'о': 'j',
    'Л': 'K', 'л': 'k',
    'Д': 'L', 'д': 'l',
    'Ж': ':', 'ж': ';',
    'Э': '"', 'э': '\'',
    'Я': 'Z', 'я': 'z',
    'Ч': 'X', 'ч': "x",
    'С': 'C', 'с': "c",
    'М': 'V', 'м': "v",
    'И': 'B', 'и': "b",
    'Т': 'N', 'т': "n",
    'Ь': 'M', 'ь': "m",
    'Б': '<', 'б': ",",
    'Ю': '>', 'ю': ".",
    }

c.url.start_pages = ["https://www.google.com/"]
c.url.searchengines = {"DEFAULT": "https://www.google.fi/search?q={}"}
c.spellcheck.languages = ["en-US", "ru-RU"]
c.content.pdfjs = True
c.auto_save.session = True

# List of symbols for different loading spinner animations
loading_spinner_symbols =['[\\]', '[|]', '[/]', '[-]']

# List of symbols for basic loading dots animation
loading_dots_basic_symbols =['   ', '.  ', '.. ', '...']

# List of symbols for loading dots animation with partial up and down movement
loading_dots_up_and_down_partial_symbols =['.  ', '.. ', '...', '.. ']

# List of symbols for loading dots animation with full up and down movement
loading_dots_up_and_down_full_symbols = ['   ', '.  ', '.. ', '...', '.. ', '.  ']

# List of symbols for loading dots animation with partial continuation
loading_dots_continuation_partial_symbols = ['   ', '.  ', '.. ', '...', ' ..', '  .']

# List of symbols for loading dots animation with continuation and up and down movement
loading_dots_continuation_up_and_down_symbols = ['   ', '.  ', '.. ', '...', ' ..', '  .','   ','  .',' ..', '...','.. ','.  ']

# List of uppercase English alphabet letters
loading_english_alphabet_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of lowercase English alphabet letters
loading_english_alphabet_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List of lowercase Armenian alphabet letters
loading_armenian_alphabet_lowercase = ['ա','բ','գ','դ','ե','զ','է','ը','թ','ժ','ի','լ','խ','ծ','կ','հ','ձ','ղ','ճ','մ','յ','ն','շ','ո','չ','պ','ջ','ռ','ս','վ','տ','ր','ց','ու','փ','ք','և', 'օ','ֆ']

# List of uppercase Armenian alphabet letters
loading_armenian_alphabet_uppercase = ['Ա','Բ','Գ','Դ','Ե','Զ','Է','Ը','Թ','Ժ','Ի','Լ','Խ','Ծ','Կ','Հ','Ձ','Ղ','Ճ','Մ','Յ','Ն','Շ','Ո','Չ','Պ','Ջ','Ռ','Ս','Վ','Տ','Ր','Ց','ՈՒ','Փ','Ք','ԵՎ','Օ','Ֆ']

# List of lowercase Greek alphabet letters
loading_greek_alphabet_lowercase = ['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω']

# List of uppercase Greek alphabet letters
loading_greek_alphabet_uppercase = ['Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω']

# List of lowercase Cyrillic alphabet letters
loading_cyrillic_alphabet_lowercase = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ь','ю','я']

# List of uppercase Cyrillic alphabet letters
loading_cyrillic_alphabet_uppercase = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ь','Ю','Я']

# List of symbols to be used for loading animation
loading_symbols = loading_armenian_alphabet_lowercase

def loading_dots_function(loading_symbols, raise_errors=True):
    """
    Returns a function that can be called to create loading symbols
    
    Parameters:
    loading_symbols (list, or function(index)->string, object): If a list, use those symbols as the loading symbols, if a function then use it as a callback to get the loading symbol at the given index. If an object, check for th __index__ method and use it as a callback to get the loading symbol at the given index.
    raise_errors (bool): If True, raise an error if the loading_symbols is not a list, a function, or an object with an __index__ method. If False, return a loading spinner symbols.
    Returns:
    function(index)->string: A function that takes an index and returns the corresponding loading symbol.
    """
    def handle_error(error_message):
        if raise_errors:
            raise ValueError(error_message)
        else:
            return lambda index: loading_spinner_symbols[index%len(loading_spinner_symbols)]

    # check if the loading_symbols is a list and return the corresponding loading function
    if type(loading_symbols) == list:
        return lambda index: str(loading_symbols[index%len(loading_symbols)])
    # check if the loading_symbols is a function, verify it takes an index, and return it
    elif callable(loading_symbols):
        # verify it takes a single parameter or has only one non-default parameter
        if len(loading_symbols.__code__.co_varnames) == 1:
            return loading_symbols
        else:
            return handle_error('The loading_symbols function must take a single parameter') 
    # check if the loading_symbols is an object, verify it has an __getitem__ method, and return it
    elif hasattr(loading_symbols, '__getitem__'):
        return loading_symbols.__getitem__
    else:
        return handle_error('The loading_symbols must be a list, a function, or an object with an __getitem__ method')
    
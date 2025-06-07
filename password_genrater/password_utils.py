def generate_password(length=16, use_lower=True, use_upper=True,
                      use_digits=True, use_symbols=True,
                      exclude_similar=True, exclude_ambiguous=True):
    
    import string, secrets

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    similar_chars = "l1IoO0"
    ambiguous_chars = "{}[]()/\\'\"`~,;:.<>"

    if not 8 <= length <= 64:
        raise ValueError("Password length must be between 8 and 64")
    
    if not any([use_lower, use_upper, use_digits, use_symbols]):
        raise ValueError("Select at least one character type")

    char_pool = []
    excluded_chars = ""

    if exclude_similar:
        excluded_chars += similar_chars
    if exclude_ambiguous:
        excluded_chars += ambiguous_chars

    if use_lower:
        char_pool += [c for c in lower if c not in excluded_chars]
    if use_upper:
        char_pool += [c for c in upper if c not in excluded_chars]
    if use_digits:
        char_pool += [c for c in digits if c not in excluded_chars]
    if use_symbols:
        char_pool += [c for c in symbols if c not in excluded_chars]

    if not char_pool:
        raise ValueError("No characters available after exclusions")

    # Ensure at least one of each selected type
    password_parts = []
    if use_lower:
        password_parts.append(secrets.choice([c for c in lower if c not in excluded_chars]))
    if use_upper:
        password_parts.append(secrets.choice([c for c in upper if c not in excluded_chars]))
    if use_digits:
        password_parts.append(secrets.choice([c for c in digits if c not in excluded_chars]))
    if use_symbols:
        password_parts.append(secrets.choice([c for c in symbols if c not in excluded_chars]))

    # Fill the rest
    remaining_length = length - len(password_parts)
    password_parts.extend(secrets.choice(char_pool) for _ in range(remaining_length))

    secrets.SystemRandom().shuffle(password_parts)
    password = ''.join(password_parts)

    # Basic strength estimate
    if length >= 16 and all([use_lower, use_upper, use_digits, use_symbols]):
        strength = "Strong"
    elif length >= 12 and sum([use_lower, use_upper, use_digits, use_symbols]) >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return password, strength

import os
import random
import string
import textwrap

# -------------------- EMOJI SUBSTITUTION LAYER -------------------- #

emoji_ranges = [
    (0x1F600, 0x1F64F),  # Smileys & Emotion
    (0x1F300, 0x1F5FF),  # Symbols & Pictographs
    (0x1F680, 0x1F6FF),  # Transport & Map
    (0x1F900, 0x1F9FF),  # Supplemental Symbols
]

def random_emoji():
    start, end = random.choice(emoji_ranges)
    code_point = random.randint(start, end)
    try:
        return chr(code_point)
    except:
        return random_emoji()

def build_emoji_map(seed=None):
    """Return (emoji_dict, reverse_map). If seed provided, deterministic mapping."""
    if seed is not None:
        random.seed(seed)
    emoji_dict = {}
    used = set()
    for letter in string.ascii_uppercase + string.ascii_lowercase:
        e = random_emoji()
        while e in used:
            e = random_emoji()
        emoji_dict[letter] = e
        used.add(e)
    reverse = {v: k for k, v in emoji_dict.items()}
    return emoji_dict, reverse

def text_to_emoji(text, emoji_dict):
    return "".join(emoji_dict.get(ch, ch) for ch in text)

def emoji_to_text(emoji_text, reverse_map):
    # naive: iterate codepoints and translate codepoint if present in reverse map
    out = []
    for ch in emoji_text:
        out.append(reverse_map.get(ch, ch))
    return "".join(out)


# ------------------------ HYBRID CIPHER ------------------------ #

def pad(data, block_size):
    """Pad string data with PKCS# style (returns string)."""
    pad_len = block_size - (len(data) % block_size)
    return data + chr(pad_len) * pad_len

def unpad(data):
    pad_len = ord(data[-1])
    return data[:-pad_len]

def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def simple_encrypt_block(block, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(block)])

def simple_decrypt_block(block, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(block)])

def _hex(b):
    return b.hex()

# -------------------- VISUAL ENCRYPT / DECRYPT -------------------- #

def visual_hybrid_encrypt(plaintext, emoji_dict=None, seed=None):
    """Encrypt but print detailed visuals. Returns metadata for decryption."""
    if emoji_dict is None:
        emoji_dict, reverse = build_emoji_map(seed)
    else:
        reverse = {v: k for k, v in emoji_dict.items()}

    print("\n" + "="*60)
    print("🔐 HYBRID EMOJI ENCRYPTION — VISUAL MODE")
    print("="*60)
    print(f"Plaintext: {plaintext!r}\n")

    # 1) Emoji substitution
    emoji_text = text_to_emoji(plaintext, emoji_dict)
    print("1) Emoji substitution (mapping shown below):\n")
    # show mapping in groups
    lines = []
    for i, ch in enumerate(string.ascii_uppercase + string.ascii_lowercase):
        lines.append(f"{ch}:{emoji_dict[ch]}")
    for chunk in textwrap.wrap("  ".join(lines), width=120):
        print(chunk)
    print(f"\nSubstituted emoji text: {emoji_text}\n")

    # 2) Pad and block-split
    block_size = random.randint(8, 32)
    padded = pad(emoji_text, block_size)
    padded_bytes = padded.encode("utf-8")
    key = os.urandom(16)
    iv = os.urandom(block_size)

    print(f"2) Padding + Block size chosen randomly: BlockSize = {block_size}")
    print(f"Padded emoji text (showing escaped): {padded!r}")
    print(f"Total bytes length: {len(padded_bytes)}")
    print(f"Key (hex): {key.hex()}")
    print(f"IV  (hex): {iv.hex()}\n")

    # split into blocks (in bytes)
    ciphertext = b""
    prev_block = iv
    mode_sequence = []

    print("3) Processing blocks:")
    for i in range(0, len(padded_bytes), block_size):
        block_bytes = padded_bytes[i:i+block_size]
        block_index = i // block_size + 1
        mode = random.choice(["ECB", "CBC"])
        mode_sequence.append(mode)

        print("-"*60)
        print(f"Block {block_index:02d}:")
        try:
            # attempt to show the emoji characters in this block
            block_text = block_bytes.decode("utf-8")
        except:
            block_text = repr(block_bytes)
        print(f" Raw block bytes ({len(block_bytes)}): {block_bytes} ")
        print(f" Decoded block text: {block_text!r}")
        print(f" Mode chosen: {mode}")

        if mode == "ECB":
            encrypted = simple_encrypt_block(block_bytes, key)
            print(f" Operation: ECB -> encrypted = simple_encrypt_block(block, key)")
        else:
            xor_in = xor_bytes(block_bytes, prev_block)
            print(f" Operation: CBC -> XOR(block, prev_block)  ")
            print(f"  prev_block (hex): {_hex(prev_block)}")
            print(f"  block       (hex): {_hex(block_bytes)}")
            print(f"  xor result  (hex): {_hex(xor_in)}")
            encrypted = simple_encrypt_block(xor_in, key)
            prev_block = encrypted

        print(f" Encrypted block (hex): {_hex(encrypted)}")
        ciphertext += encrypted

    print("\n" + "="*60)
    print("Encryption complete.")
    print(f"Final Ciphertext (hex): {ciphertext.hex()}")
    print(f"Modes sequence: {','.join(mode_sequence)}")
    print("="*60 + "\n")

    # Save data for later decryption
    metadata = {
        "key": key,
        "iv": iv,
        "ciphertext": ciphertext,
        "modes": mode_sequence,
        "block_size": block_size,
        "emoji_dict": emoji_dict
    }
    # Write to file (optional)
    with open("encryption_data_visual.txt", "w", encoding="utf-8") as f:
        f.write(f"Key={key.hex()}\n")
        f.write(f"IV={iv.hex()}\n")
        f.write(f"Ciphertext={ciphertext.hex()}\n")
        f.write(f"Modes={','.join(mode_sequence)}\n")
        f.write(f"BlockSize={block_size}\n")
        # emoji map: letter:emoji pairs separated by commas
        f.write("EmojiMap=" + ",".join(f"{k}:{v}" for k, v in emoji_dict.items()) + "\n")

    print("Saved encryption metadata to encryption_data_visual.txt\n")
    return metadata

def visual_hybrid_decrypt(metadata):
    key = metadata["key"]
    iv = metadata["iv"]
    ciphertext = metadata["ciphertext"]
    mode_sequence = metadata["modes"]
    block_size = metadata["block_size"]
    emoji_dict = metadata.get("emoji_dict", {})
    reverse_map = {v: k for k, v in emoji_dict.items()}

    print("\n" + "="*60)
    print("🔓 HYBRID EMOJI DECRYPTION — VISUAL MODE")
    print("="*60)
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    print(f"IV (hex): {iv.hex()}")
    print(f"Key (hex): {key.hex()}")
    print(f"Block size: {block_size}")
    print(f"Mode sequence: {','.join(mode_sequence)}\n")

    decrypted = b""
    prev_block = iv

    for i in range(0, len(ciphertext), block_size):
        block_bytes = ciphertext[i:i+block_size]
        idx = i // block_size
        mode = mode_sequence[idx]
        block_num = idx + 1
        print("-"*60)
        print(f"Block {block_num:02d}:")
        print(f" Encrypted block (hex): {block_bytes.hex()}")
        if mode == "ECB":
            dec_block = simple_decrypt_block(block_bytes, key)
            print(" Mode: ECB -> simple_decrypt_block(encrypted, key)")
            print(f" Decrypted block bytes (hex): {dec_block.hex()}")
        else:
            dec_intermediate = simple_decrypt_block(block_bytes, key)
            print(" Mode: CBC -> simple_decrypt_block(encrypted, key) then XOR with prev_block")
            print(f"  After simple_decrypt (hex): {dec_intermediate.hex()}")
            dec_block = xor_bytes(dec_intermediate, prev_block)
            print(f"  prev_block (hex): {prev_block.hex()}")
            print(f"  XOR result (hex): {dec_block.hex()}")
            prev_block = block_bytes

        # try to decode bytes to emoji text
        try:
            decoded = dec_block.decode("utf-8")
            print(f" Decoded block text (emoji segment): {decoded!r}")
        except Exception as e:
            print(f" Decoding error: {e}; raw bytes shown.")
            decoded = dec_block.decode("utf-8", errors="replace")
            print(f" Decoded (with replacement): {decoded!r}")

        decrypted += dec_block

    print("\nAll blocks processed. Now unpadding...")
    try:
        emoji_padded = decrypted.decode("utf-8")
    except:
        emoji_padded = decrypted.decode("utf-8", errors="replace")
    print(f"Padded emoji string: {emoji_padded!r}")

    try:
        emoji_unpadded = unpad(emoji_padded)
    except Exception as e:
        print("Unpad error:", e)
        emoji_unpadded = emoji_padded  # fallback
    print(f"Unpadded emoji string: {emoji_unpadded!r}")

    recovered_plaintext = emoji_to_text(emoji_unpadded, reverse_map)
    print(f"\nRecovered plaintext after emoji->text: {recovered_plaintext!r}")
    print("="*60 + "\n")
    return recovered_plaintext

# ------------------------------ RUN UI ------------------------------ #

def load_metadata_from_file(path="encryption_data_visual.txt"):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    d = {}
    for line in lines:
        k, v = line.split("=", 1)
        d[k] = v
    key = bytes.fromhex(d["Key"])
    iv = bytes.fromhex(d["IV"])
    ciphertext = bytes.fromhex(d["Ciphertext"])
    modes = d["Modes"].split(",")
    block_size = int(d["BlockSize"])
    emoji_map_raw = d.get("EmojiMap", "")
    emoji_pairs = emoji_map_raw.split(",") if emoji_map_raw else []
    emoji_dict = {}
    for p in emoji_pairs:
        if ":" in p:
            letter, emoji = p.split(":", 1)
            emoji_dict[letter] = emoji
    return {
        "key": key,
        "iv": iv,
        "ciphertext": ciphertext,
        "modes": modes,
        "block_size": block_size,
        "emoji_dict": emoji_dict
    }

if __name__ == "__main__":
    while True:
        print("\nVISUAL HYBRID EMOJI CIPHER")
        print("1) Encrypt (visual)")
        print("2) Decrypt from saved file (visual)")
        print("3) Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            txt = input("\nEnter plaintext: ")
            # optional: ask for deterministic seed for reproducible emoji map
            seed_in = input("Enter optional integer seed for emoji mapping (or press Enter for random): ").strip()
            seed = int(seed_in) if seed_in.isdigit() else None
            metadata = visual_hybrid_encrypt(txt, seed=seed)
            # keep metadata in-memory for immediate decrypt test
            test_now = input("Decrypt now using generated metadata? (y/N): ").strip().lower()
            if test_now == "y":
                visual_hybrid_decrypt(metadata)
        elif ch == "2":
            try:
                metadata = load_metadata_from_file()
                visual_hybrid_decrypt(metadata)
            except Exception as e:
                print("Error loading metadata file:", e)
        elif ch == "3":
            print("Bye.")
            break
        else:
            print("Invalid choice.")

import sys
import os

def parse_scryfall_url(line):
    parts = line.strip().split()
    if len(parts) == 0:
        return ''
    elif len(parts) == 1:
        count = '1'
        url = parts[0]
    else:
        count = parts[0]
        url = parts[1]

    try:
        url_parts = url.split('/')
        set_code = url_parts[4].upper()
        number = url_parts[5]
        name_parts = url_parts[6:]
        name = ' '.join([p.capitalize() for p in '-'.join(name_parts).replace('-', ' ').split()])
        return f"{count} {name} ({set_code}) {number}"
    except Exception:
        return ''

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python scryfall-url-to-moxfield-format.py <input_file> [output_file]")
        sys.exit(1)
    input_path = sys.argv[1]
    output_dir = os.path.join('game', 'decklist')
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    if len(sys.argv) == 3:
        output_filename = sys.argv[2]
    else:
        output_filename = 'scryfall_urls_output.txt'
    output_path = os.path.join(output_dir, output_filename)
    if not os.path.isfile(input_path):
        print(f"{input_path} is not a valid file.")
        sys.exit(1)
    count = 0
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            if line.strip() == '':
                outfile.write('\n')
                continue
            result = parse_scryfall_url(line)
            outfile.write(result + '\n')
            count += 1
    abs_output_path = os.path.abspath(output_path)
    print(f"{count} lines successfully parsed. Output can be found in {abs_output_path}")

if __name__ == '__main__':
    main()
from Compiler.pdp11_parsing import PDP11Parser

def compiler():
    with open("C:/proekt/PDP-11/virtual_executor/source.asm", "r") as f:
        source = [line.strip().strip('"\'').strip() for line in f if line.strip()]

  
    parser = PDP11Parser()
    compiled = parser.compile(source)
    parser.generate_hex_file(compiled, "program.hex")
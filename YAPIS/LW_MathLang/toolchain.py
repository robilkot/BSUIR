import logging
import os
import sys
from pathlib import Path


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 2:
        logging.error(f"Usage: python {sys.argv[0]} <source_file.ml>\nExample: python {sys.argv[0]} samples/sample7.ml")
        sys.exit(1)

    source_file = Path(sys.argv[1])
    if not source_file.exists():
        logging.error(f"Source file {source_file} does not exist")
        sys.exit(1)
    # source_file = Path('samples/sample7.ml')

    # Compile ML to WAT
    mathlang_compiler_cmd = f"python semantic_analyzer.py {source_file}"
    wat_file = source_file.with_suffix('.wat')
    mathlang_compiler_return_code = os.system(mathlang_compiler_cmd)

    if mathlang_compiler_return_code != 0:
        logging.error(f"Mathlang compilation failed (return code {mathlang_compiler_return_code})")
        exit(mathlang_compiler_return_code)

    # Compile WAT to WASM
    wasm_file = source_file.with_suffix('.wasm')
    wat_compiler_cmd = f"wabt-1.0.39/bin/wat2wasm {wat_file} -o {wasm_file}"
    wat_compiler_return_code = os.system(wat_compiler_cmd)

    if wat_compiler_return_code != 0:
        logging.error(f"WAT compilation failed (return code {wat_compiler_return_code})")
        exit(wat_compiler_return_code)

    # Execute JS with WASM module
    js_file = source_file.with_suffix('.js')
    js_file_contents = '''
    const fs = require('node:fs');
    const prompt = require('prompt-sync')();
    
    function get_value(type) {
        const value = prompt('input ' + type + ': ');
        
        switch(type) {
            case "float": return parseFloat(value);
            case "int": return parseInt(value, 10);
            case "bool": return parseBool(value);
            default: console.error(`Unknown type: ${type}`);
        }
    }
    
    function parseBool(value) {
        const lower = value.toLowerCase().trim();
        if (lower === 'true' || lower === '1' || lower === 'yes' || lower === 'y') { return true; }
        if (lower === 'false' || lower === '0' || lower === 'no' || lower === 'n') { return false; }
        console.error(`Invalid boolean: ${value}`);
    }
    
    async function runWasm() { ''' \
    + f"const wasmBuffer = fs.readFileSync('{wasm_file.absolute()}');" \
    + '''
        const importObject = {
            console: {
              write_int: (x) => console.log("int    ", x),
              write_float: (x) => console.log("float  ", x),
              write_bool: (x) => console.log("bool   ", x),
              write_string: (x) => console.log("string ", x),
              read_int: () => get_value("int"),
              read_float: () => get_value("float"),
              read_bool: () => get_value("bool"),
              
              mem: new WebAssembly.Memory({ initial: 1 })
            },
            Math: {
              floor: (x) => Math.floor(x),
              cos: (x) => Math.cos(x),
              abs: (x) => Math.abs(x),
              asin: (x) => Math.asin(x),
              ceil: (x) => Math.ceil(x),
              exp: (x) => Math.exp(x),
              sin: (x) => Math.sin(x),
              acos: (x) => Math.acos(x),
              sqrt: (x) => Math.sqrt(x),
              tan: (x) => Math.tan(x),
              atan: (x) => Math.atan(x),
              log: (x) => Math.log(x),
            },
          };
          
        const wasmModule = await WebAssembly.instantiate(wasmBuffer, importObject); 
    }
    
    runWasm();
    '''

    with open(js_file, 'w') as f:
        f.write(js_file_contents)

    logging.info(f"WASM compiled successfully. Run by executing JS file: 'node {js_file}'")
    exit(0)

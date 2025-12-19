
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
    
    function readWasmString(memory, address) {
        const memUint8 = new Uint8Array(memory.buffer);
        let str = '';
        let i = address;
        
        // Read until null terminator
        while (memUint8[i] !== 0 && i < memUint8.length) {
            str += String.fromCharCode(memUint8[i]);
            i++;
        }
        str = str.slice(1, -1);
        return str;
    }

    async function runWasm() { const wasmBuffer = fs.readFileSync('/home/robilkot/work/BSUIR/YAPIS/LW_MathLang/samples/samples_templates_correct.wasm');  
        const importObject = {
            console: {
              write_int: (x) => process.stdout.write(x.toString()),
              write_float: (x) => process.stdout.write(x.toPrecision(3).toString()),
              write_bool: (x) => process.stdout.write(x == 1 ? "true" : "false"),
              write_string: (address) => {
                if (address === 0) {
                    process.stdout.write("(null)");
                    return;
                }
                const str = readWasmString(memory, address);
                process.stdout.write(str);
              },
              read_int: () => get_value("int"),
              read_float: () => get_value("float"),
              read_bool: () => get_value("bool"),
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
              pow: (x, y) => Math.pow(x, y),
            },
          };
        
        const result = await WebAssembly.instantiate(wasmBuffer, importObject); 
        const { main, memory } = result.instance.exports;
        importObject.console.mem = memory;
        
        // Run
        main();
    }
    
    runWasm();
    
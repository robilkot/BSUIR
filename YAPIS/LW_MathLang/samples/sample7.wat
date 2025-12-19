(module
  (import "console" "write_int" (func $console_write_int (param i32)))
  (import "console" "write_float" (func $console_write_float (param f32)))
  (import "console" "write_bool" (func $console_write_bool (param i32)))
  (import "console" "write_string" (func $console_write_string (param i32)))
  (import "console" "read_int" (func $console_read_int (result i32)))
  (import "console" "read_float" (func $console_read_float (result f32)))
  (import "console" "read_bool" (func $console_read_bool (result i32)))
  (import "Math" "asin" (func $Math_asin (param f32) (result f32)))
  (import "Math" "abs" (func $Math_abs (param f32) (result f32)))
  (import "Math" "tan" (func $Math_tan (param f32) (result f32)))
  (import "Math" "floor" (func $Math_floor (param f32) (result f32)))
  (import "Math" "atan" (func $Math_atan (param f32) (result f32)))
  (import "Math" "acos" (func $Math_acos (param f32) (result f32)))
  (import "Math" "cos" (func $Math_cos (param f32) (result f32)))
  (import "Math" "log" (func $Math_log (param f32) (result f32)))
  (import "Math" "sin" (func $Math_sin (param f32) (result f32)))
  (import "Math" "exp" (func $Math_exp (param f32) (result f32)))
  (import "Math" "sqrt" (func $Math_sqrt (param f32) (result f32)))
  (import "Math" "ceil" (func $Math_ceil (param f32) (result f32)))
  (import "Math" "pow" (func $Math_pow (param f32) (param f32) (result f32)))
  (memory $memory 1)
  ;; String constants
  (data (i32.const 1) "\"\n\"\00")
  (func $recursion@int_float@int_float
    (param $val1 i32)
    (param $val2 i32)
    local.get $val1
    i32.load
    call $console_write_int
    i32.const 1
    call $console_write_string
    local.get $val2
    f32.load
    call $console_write_float
    i32.const 1
    call $console_write_string
    local.get $val2
    f32.load
    i32.const 5
    f32.convert_i32_s
    f32.gt
    if
        return
    end
    local.get $val2
    local.get $val2
    f32.load
    i32.const 1
    f32.convert_i32_s
    f32.add
    f32.store
    local.get $val2
    local.get $val1
    call $recursion@float_int@float_int
  )
  (func $recursion@float_int@float_int
    (param $val1 i32)
    (param $val2 i32)
    local.get $val1
    f32.load
    call $console_write_float
    i32.const 1
    call $console_write_string
    local.get $val2
    i32.load
    call $console_write_int
    i32.const 1
    call $console_write_string
    local.get $val2
    i32.load
    i32.const 5
    i32.gt_s
    if
        return
    end
    local.get $val2
    local.get $val2
    i32.load
    i32.const 1
    i32.add
    i32.store
    local.get $val2
    local.get $val1
    call $recursion@int_float@int_float
  )
  (func $main
    (local $$temp_2 i32)
    (local $$temp_1 i32)
    i32.const 6
    local.set $$temp_1
    local.get $$temp_1
    f32.const 1.5
    f32.store
    local.get $$temp_1
    i32.const 10
    local.set $$temp_2
    local.get $$temp_2
    i32.const 2
    i32.store
    local.get $$temp_2
    call $recursion@float_int@float_int
  )
  (export "memory" (memory $memory))
  (export "main" (func $main))
)
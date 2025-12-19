(module
  (import "console" "write_int" (func $console_write_int (param i32)))
  (import "console" "write_float" (func $console_write_float (param f32)))
  (import "console" "write_bool" (func $console_write_bool (param i32)))
  (import "console" "write_string" (func $console_write_string (param i32) (param i32)))
  (import "console" "read_int" (func $console_read_int (result i32)))
  (import "console" "read_float" (func $console_read_float (result f32)))
  (import "console" "read_bool" (func $console_read_bool (result i32)))
  (import "Math" "log" (func $Math_log (param f32) (result f32)))
  (import "Math" "cos" (func $Math_cos (param f32) (result f32)))
  (import "Math" "acos" (func $Math_acos (param f32) (result f32)))
  (import "Math" "tan" (func $Math_tan (param f32) (result f32)))
  (import "Math" "abs" (func $Math_abs (param f32) (result f32)))
  (import "Math" "asin" (func $Math_asin (param f32) (result f32)))
  (import "Math" "ceil" (func $Math_ceil (param f32) (result f32)))
  (import "Math" "sqrt" (func $Math_sqrt (param f32) (result f32)))
  (import "Math" "floor" (func $Math_floor (param f32) (result f32)))
  (import "Math" "sin" (func $Math_sin (param f32) (result f32)))
  (import "Math" "atan" (func $Math_atan (param f32) (result f32)))
  (import "Math" "exp" (func $Math_exp (param f32) (result f32)))
  (memory $memory 1)
  (data (i32.const 0) "")
  (func $call_to_templated_sub@int
    (param $val i32)
    (local $i_val i32)
    i32.const 0
    local.set $i_val
    local.get $val
    call $pretty_write@int
    local.get $i_val
    local.get $val
    i32.load
    i32.store
    local.get $i_val
    call $pretty_write@int
    return
  )
  (func $unused_argument@Unused
    return
  )
  (func $pretty_write@float
    (param $a i32)
    i32.const 0
    i32.const 0
    call $console_write_string
    local.get $a
    f32.load
    call $console_write_float
    return
  )
  (func $conflicting_name
    (param $value i32)
    return
  )
  (func $pretty_write@int
    (param $a i32)
    i32.const 0
    i32.const 0
    call $console_write_string
    local.get $a
    i32.load
    call $console_write_int
    return
  )
  (func $explicit_implementation@float
    (param $val i32)
    i32.const 0
    i32.const 0
    call $console_write_string
    local.get $val
    f32.load
    call $console_write_float
    return
  )
  (func $explicit_implementation@int
    (param $val i32)
    i32.const 0
    i32.const 0
    call $console_write_string
    local.get $val
    i32.load
    call $console_write_int
    return
  )
  (func $inner_initialization@float
    (param $result i32)
    (local $intermediate_result i32)
    i32.const 4
    local.set $intermediate_result
    local.get $intermediate_result
    call $console_read_float
    f32.store
    local.get $result
    local.get $intermediate_result
    f32.load
    f32.const 2.0
    f32.mul
    f32.store
    return
  )
  (func $explicit_implementation_without_templated_declaration@int
    (param $val i32)
    i32.const 0
    i32.const 0
    call $console_write_string
    local.get $val
    i32.load
    call $console_write_int
    return
  )
  (func $inner_initialization@int
    (param $result i32)
    (local $intermediate_result i32)
    i32.const 8
    local.set $intermediate_result
    local.get $intermediate_result
    call $console_read_int
    i32.store
    local.get $result
    local.get $intermediate_result
    i32.load
    f32.const 2.0
    f32.trunc
    i32.trunc_f32_s
    i32.mul
    i32.store
    return
  )
  (func $main
    (local $$temp_9 i32)
    (local $$temp_8 i32)
    (local $$temp_7 i32)
    (local $$temp_6 i32)
    (local $$temp_5 i32)
    (local $$temp_4 i32)
    (local $$temp_3 i32)
    (local $$temp_2 i32)
    (local $$temp_1 i32)
    (local $a i32)
    (local $input_float i32)
    i32.const 12
    local.set $input_float
    i32.const 16
    local.set $a
    i32.const 20
    local.set $$temp_1
    local.get $$temp_1
    i32.const 2
    i32.store
    local.get $$temp_1
    call $inner_initialization@T
    i32.const 24
    local.set $$temp_2
    local.get $$temp_2
    f32.const 2.0
    f32.store
    local.get $$temp_2
    call $inner_initialization@T
    i32.const 28
    local.set $$temp_3
    local.get $$temp_3
    i32.const 2
    i32.store
    local.get $$temp_3
    call $explicit_implementation_without_templated_declaration@int
    i32.const 32
    local.set $$temp_4
    local.get $$temp_4
    f32.const 2.0
    f32.store
    local.get $$temp_4
    call $explicit_implementation@T
    i32.const 36
    local.set $$temp_5
    local.get $$temp_5
    i32.const 2
    i32.store
    local.get $$temp_5
    call $call_to_templated_sub@T
    i32.const 40
    local.set $$temp_6
    local.get $$temp_6
    f32.const 2.0
    f32.store
    local.get $$temp_6
    call $call_to_templated_sub@T
    local.get $input_float
    f32.const 0.0
    f32.store
    local.get $a
    call $console_read_float
    f32.trunc
    i32.trunc_f32_s
    i32.store
    i32.const 44
    local.set $$temp_7
    local.get $$temp_7
    i32.const 2
    i32.store
    local.get $$temp_7
    call $inner_initialization@int
    i32.const 48
    local.set $$temp_8
    local.get $$temp_8
    f32.const 2.0
    f32.store
    local.get $$temp_8
    call $inner_initialization@float
    i32.const 52
    local.set $$temp_9
    local.get $$temp_9
    i32.const 2
    i32.store
    local.get $$temp_9
    call $inner_initialization@int
  )
  (export "main" (func $main))
  (start $main)
)
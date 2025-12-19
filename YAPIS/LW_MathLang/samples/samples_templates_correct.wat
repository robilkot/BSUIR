(module
  (import "console" "write_int" (func $console_write_int (param i32)))
  (import "console" "write_float" (func $console_write_float (param f32)))
  (import "console" "write_bool" (func $console_write_bool (param i32)))
  (import "console" "write_string" (func $console_write_string (param i32)))
  (import "console" "read_int" (func $console_read_int (result i32)))
  (import "console" "read_float" (func $console_read_float (result f32)))
  (import "console" "read_bool" (func $console_read_bool (result i32)))
  (import "Math" "sqrt" (func $Math_sqrt (param f32) (result f32)))
  (import "Math" "floor" (func $Math_floor (param f32) (result f32)))
  (import "Math" "tan" (func $Math_tan (param f32) (result f32)))
  (import "Math" "acos" (func $Math_acos (param f32) (result f32)))
  (import "Math" "log" (func $Math_log (param f32) (result f32)))
  (import "Math" "atan" (func $Math_atan (param f32) (result f32)))
  (import "Math" "ceil" (func $Math_ceil (param f32) (result f32)))
  (import "Math" "cos" (func $Math_cos (param f32) (result f32)))
  (import "Math" "asin" (func $Math_asin (param f32) (result f32)))
  (import "Math" "abs" (func $Math_abs (param f32) (result f32)))
  (import "Math" "exp" (func $Math_exp (param f32) (result f32)))
  (import "Math" "sin" (func $Math_sin (param f32) (result f32)))
  (import "Math" "pow" (func $Math_pow (param f32) (param f32) (result f32)))
  (memory $memory 1)
  ;; String constants
  (data (i32.const 1) "\"result before recursion: \"\00")
  (data (i32.const 29) "\"\n\"\00")
  (data (i32.const 34) "\"result after recursion: \"\00")
  (data (i32.const 61) "\"Arbitrary type\"\00")
  (data (i32.const 78) "\"Something pretty\n\"\00")
  (data (i32.const 99) "\"Specifically for int!\"\00")
  (func $double_template@int_bool@int_bool
    (param $key i32)
    (param $value i32)
    (local $key_casted i32)
    i32.const 123
    local.set $key_casted
    local.get $key_casted
    local.get $key
    i32.load
    i32.const 0
    i32.ne
    i32.store
    return
  )
  (func $double_template@bool_bool@bool_bool
    (param $key i32)
    (param $value i32)
    (local $key_casted i32)
    i32.const 127
    local.set $key_casted
    local.get $key_casted
    local.get $key
    i32.load
    i32.store
    return
  )
  (func $explicit_implementation@float@float
    (param $val i32)
    i32.const 61
    call $console_write_string
    local.get $val
    f32.load
    call $console_write_float
    i32.const 29
    call $console_write_string
    return
  )
  (func $double_template@int_float@int_float
    (param $key i32)
    (param $value i32)
    (local $key_casted i32)
    i32.const 131
    local.set $key_casted
    local.get $key_casted
    local.get $key
    i32.load
    f32.convert_i32_s
    f32.store
    return
  )
  (func $recursion@int_int@int
    (param $val i32)
    (param $result i32)
    (local $res i32)
    i32.const 135
    local.set $res
    local.get $res
    local.get $val
    i32.load
    i32.store
    local.get $result
    i32.load
    i32.const 10
    i32.gt_s
    if
        return
    end
    local.get $result
    local.get $result
    i32.load
    i32.const 1
    i32.add
    i32.store
    local.get $val
    local.get $result
    call $recursion@int_int@int
  )
  (func $call_to_templated_sub@int@int
    (param $val i32)
    (local $i_val i32)
    i32.const 139
    local.set $i_val
    local.get $val
    call $pretty_write@int@int
    local.get $i_val
    local.get $val
    i32.load
    i32.store
    local.get $i_val
    call $pretty_write@int@int
    return
  )
  (func $inner_initialization@float@float
    (param $result i32)
    (local $intermediate_result i32)
    i32.const 143
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
  (func $pretty_write@float@float
    (param $a i32)
    i32.const 78
    call $console_write_string
    local.get $a
    f32.load
    call $console_write_float
    i32.const 29
    call $console_write_string
    return
  )
  (func $inner_initialization@int@int
    (param $result i32)
    (local $intermediate_result i32)
    i32.const 147
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
  (func $pretty_write@int@int
    (param $a i32)
    i32.const 78
    call $console_write_string
    local.get $a
    i32.load
    call $console_write_int
    i32.const 29
    call $console_write_string
    return
  )
  (func $call_to_templated_sub@float@float
    (param $val i32)
    (local $i_val i32)
    i32.const 151
    local.set $i_val
    local.get $val
    call $pretty_write@float@float
    local.get $i_val
    local.get $val
    f32.load
    f32.trunc
    i32.trunc_f32_s
    i32.store
    local.get $i_val
    call $pretty_write@int@int
    return
  )
  (func $explicit_implementation@int@int
    (param $val i32)
    i32.const 99
    call $console_write_string
    local.get $val
    i32.load
    call $console_write_int
    i32.const 29
    call $console_write_string
    return
  )
  (func $main
    (local $$temp_16 i32)
    (local $$temp_15 i32)
    (local $$temp_14 i32)
    (local $$temp_13 i32)
    (local $$temp_12 i32)
    (local $$temp_11 i32)
    (local $$temp_10 i32)
    (local $$temp_9 i32)
    (local $$temp_8 i32)
    (local $$temp_7 i32)
    (local $$temp_6 i32)
    (local $$temp_5 i32)
    (local $$temp_4 i32)
    (local $$temp_3 i32)
    (local $$temp_2 i32)
    (local $$temp_1 i32)
    (local $res i32)
    (local $a i32)
    (local $input_float i32)
    i32.const 155
    local.set $input_float
    i32.const 159
    local.set $a
    i32.const 163
    local.set $res
    i32.const 167
    local.set $$temp_1
    local.get $$temp_1
    i32.const 2
    i32.store
    local.get $$temp_1
    call $inner_initialization@int@int
    i32.const 171
    local.set $$temp_2
    local.get $$temp_2
    f32.const 2.0
    f32.store
    local.get $$temp_2
    call $inner_initialization@float@float
    i32.const 175
    local.set $$temp_3
    local.get $$temp_3
    i32.const 2
    i32.store
    local.get $$temp_3
    call $explicit_implementation@int@int
    i32.const 179
    local.set $$temp_4
    local.get $$temp_4
    f32.const 2.0
    f32.store
    local.get $$temp_4
    call $explicit_implementation@float@float
    i32.const 183
    local.set $$temp_5
    local.get $$temp_5
    i32.const 2
    i32.store
    local.get $$temp_5
    call $call_to_templated_sub@int@int
    i32.const 187
    local.set $$temp_6
    local.get $$temp_6
    f32.const 2.0
    f32.store
    local.get $$temp_6
    call $call_to_templated_sub@float@float
    local.get $input_float
    f32.const 0.0
    f32.store
    local.get $a
    call $console_read_float
    f32.trunc
    i32.trunc_f32_s
    i32.store
    i32.const 191
    local.set $$temp_7
    local.get $$temp_7
    i32.const 2
    i32.store
    local.get $$temp_7
    call $inner_initialization@int@int
    i32.const 195
    local.set $$temp_8
    local.get $$temp_8
    f32.const 2.0
    f32.store
    local.get $$temp_8
    call $inner_initialization@float@float
    i32.const 199
    local.set $$temp_9
    local.get $$temp_9
    i32.const 2
    i32.store
    local.get $$temp_9
    call $inner_initialization@int@int
    local.get $res
    i32.const 0
    i32.store
    i32.const 1
    call $console_write_string
    local.get $res
    i32.load
    call $console_write_int
    i32.const 29
    call $console_write_string
    i32.const 203
    local.set $$temp_10
    local.get $$temp_10
    i32.const 2
    i32.store
    local.get $$temp_10
    local.get $res
    call $recursion@int_int@int
    i32.const 34
    call $console_write_string
    local.get $res
    i32.load
    call $console_write_int
    i32.const 29
    call $console_write_string
    i32.const 207
    local.set $$temp_11
    local.get $$temp_11
    i32.const 2
    i32.store
    local.get $$temp_11
    i32.const 211
    local.set $$temp_12
    local.get $$temp_12
    f32.const 4.0
    f32.store
    local.get $$temp_12
    call $double_template@int_float@int_float
    i32.const 215
    local.set $$temp_13
    local.get $$temp_13
    i32.const 2
    i32.store
    local.get $$temp_13
    i32.const 219
    local.set $$temp_14
    local.get $$temp_14
    i32.const 1
    i32.store
    local.get $$temp_14
    call $double_template@int_bool@int_bool
    i32.const 223
    local.set $$temp_15
    local.get $$temp_15
    i32.const 0
    i32.store
    local.get $$temp_15
    i32.const 227
    local.set $$temp_16
    local.get $$temp_16
    i32.const 1
    i32.store
    local.get $$temp_16
    call $double_template@bool_bool@bool_bool
  )
  (export "memory" (memory $memory))
  (export "main" (func $main))
)
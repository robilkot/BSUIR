(module
  (import "console" "write_int" (func $console_write_int (param i32)))
  (import "console" "write_float" (func $console_write_float (param f32)))
  (import "console" "write_bool" (func $console_write_bool (param i32)))
  (import "console" "write_string" (func $console_write_string (param i32)))
  (import "console" "read_int" (func $console_read_int (result i32)))
  (import "console" "read_float" (func $console_read_float (result f32)))
  (import "console" "read_bool" (func $console_read_bool (result i32)))
  (import "Math" "atan" (func $Math_atan (param f32) (result f32)))
  (import "Math" "cos" (func $Math_cos (param f32) (result f32)))
  (import "Math" "abs" (func $Math_abs (param f32) (result f32)))
  (import "Math" "log" (func $Math_log (param f32) (result f32)))
  (import "Math" "acos" (func $Math_acos (param f32) (result f32)))
  (import "Math" "sqrt" (func $Math_sqrt (param f32) (result f32)))
  (import "Math" "floor" (func $Math_floor (param f32) (result f32)))
  (import "Math" "asin" (func $Math_asin (param f32) (result f32)))
  (import "Math" "sin" (func $Math_sin (param f32) (result f32)))
  (import "Math" "ceil" (func $Math_ceil (param f32) (result f32)))
  (import "Math" "exp" (func $Math_exp (param f32) (result f32)))
  (import "Math" "tan" (func $Math_tan (param f32) (result f32)))
  (import "Math" "pow" (func $Math_pow (param f32) (param f32) (result f32)))
  (memory $memory 1)
  ;; String constants
  (data (i32.const 1) "\"\n\"\00")
  (data (i32.const 6) "\"recursive sub:\n\"\00")
  (data (i32.const 25) "\"exiting recursion after c > 100\n\"\00")
  (func $test@float@
    (param $c i32)
    local.get $c
    local.get $c
    f32.load
    f32.const 2.0
    f32.mul
    f32.store
    local.get $c
    f32.load
    call $console_write_float
    i32.const 1
    call $console_write_string
    local.get $c
    f32.load
    f32.const 100.0
    f32.gt
    if
        i32.const 25
        call $console_write_string
        i32.const 100500
        call $console_write_int
        i32.const 1
        call $console_write_string
    else
        local.get $c
        call $test@float@
    end
    return
  )
  (func $main
    (local $$temp_3 i32)
    (local $i i32)
    i32.const 61
    local.set $i
    local.get $i
    i32.const 0
    i32.store
    block $loop_end_2
    loop $loop_start_1
      local.get $i
      i32.load
      i32.const 10
      i32.lt_s
      i32.eqz
      br_if $loop_end_2
        local.get $i
        i32.load
        f32.convert_i32_s
        call $Math_sin
        call $console_write_float
        i32.const 1
        call $console_write_string
      local.get $i
      local.get $i
      i32.load
      i32.const 1
      i32.add
      i32.store
      br $loop_start_1
    end
    end
    i32.const 6
    call $console_write_string
    i32.const 65
    local.set $$temp_3
    local.get $$temp_3
    f32.const 5.0
    f32.store
    local.get $$temp_3
    call $test@float@
  )
  (export "memory" (memory $memory))
  (export "main" (func $main))
)
(module
  (import "console" "write_int" (func $console_write_int (param i32)))
  (import "console" "write_float" (func $console_write_float (param f32)))
  (import "console" "write_bool" (func $console_write_bool (param i32)))
  (import "console" "write_string" (func $console_write_string (param i32) (param i32)))
  (import "console" "read_int" (func $console_read_int (result i32)))
  (import "console" "read_float" (func $console_read_float (result f32)))
  (import "console" "read_bool" (func $console_read_bool (result i32)))
  (import "Math" "log" (func $Math_log (param f32) (result f32)))
  (import "Math" "floor" (func $Math_floor (param f32) (result f32)))
  (import "Math" "abs" (func $Math_abs (param f32) (result f32)))
  (import "Math" "acos" (func $Math_acos (param f32) (result f32)))
  (import "Math" "sqrt" (func $Math_sqrt (param f32) (result f32)))
  (import "Math" "asin" (func $Math_asin (param f32) (result f32)))
  (import "Math" "sin" (func $Math_sin (param f32) (result f32)))
  (import "Math" "exp" (func $Math_exp (param f32) (result f32)))
  (import "Math" "atan" (func $Math_atan (param f32) (result f32)))
  (import "Math" "ceil" (func $Math_ceil (param f32) (result f32)))
  (import "Math" "tan" (func $Math_tan (param f32) (result f32)))
  (import "Math" "cos" (func $Math_cos (param f32) (result f32)))
  (memory $memory 1)
  (data (i32.const 0) "")
  (func $computeWave@float_float@
    (param $x i32)
    (param $result i32)
    local.get $result
    local.get $x
    f32.load
    call $Math_sin
    f32.const 0.5
    f32.const 2.0
    local.get $x
    f32.load
    f32.mul
    f32.const 1.0
    f32.add
    call $Math_sin
    f32.mul
    f32.add
    f32.store
    return
  )
  (func $computeWave@float_float_float@
    (param $x i32)
    (param $amplitude i32)
    (param $result i32)
    local.get $result
    local.get $amplitude
    f32.load
    local.get $x
    f32.load
    call $Math_sin
    f32.mul
    f32.store
    return
  )
  (func $main
    (local $angle i32)
    (local $target i32)
    (local $precision i32)
    (local $x i32)
    (local $result i32)
    i32.const 0
    local.set $result
    i32.const 4
    local.set $x
    i32.const 8
    local.set $precision
    i32.const 12
    local.set $target
    i32.const 0
    i32.const 0
    call $console_write_string
    i32.const 16
    local.set $angle
    local.get $angle
    f32.const 0.0
    f32.store
    block $loop_end_2
    loop $loop_start_1
      local.get $angle
      f32.load
      f32.const 6.28318
      f32.le
      i32.eqz
      br_if $loop_end_2
        local.get $result
        f32.const 0.0
        f32.store
        local.get $angle
        local.get $result
        call $computeWave@float_float@
        i32.const 0
        i32.const 0
        call $console_write_string
        local.get $angle
        f32.load
        call $console_write_float
        i32.const 0
        i32.const 0
        call $console_write_string
        local.get $result
        f32.load
        call $console_write_float
      local.get $angle
      local.get $angle
      f32.load
      f32.const 0.1
      f32.add
      f32.store
      br $loop_start_1
    end
    end
    local.get $x
    f32.const 0.0
    f32.store
    local.get $precision
    f32.const 0.001
    f32.store
    local.get $target
    f32.const 0.5
    f32.store
    i32.const 0
    i32.const 0
    call $console_write_string
    block $loop_end_4
    loop $loop_start_3
      local.get $x
      f32.load
      call $Math_sin
      local.get $target
      f32.load
      f32.sub
      call $Math_abs
      local.get $precision
      f32.load
      f32.gt
      i32.eqz
      br_if $loop_end_4
        local.get $x
        local.get $x
        f32.load
        f32.const 0.01
        f32.add
        f32.store
        local.get $x
        f32.load
        f32.const 10.0
        f32.gt
        if
            br $loop_end_4
        end
      br $loop_start_3
    end
    end
    i32.const 0
    i32.const 0
    call $console_write_string
    local.get $x
    f32.load
    call $console_write_float
    i32.const 0
    i32.const 0
    call $console_write_string
    local.get $x
    f32.load
    call $Math_sin
    call $console_write_float
    local.get $result
    local.get $x
    f32.load
    call $Math_cos
    f32.const 2.0
    f32.mul
    local.get $x
    f32.load
    call $Math_sin
    f32.const 2.0
    f32.mul
    f32.add
    f32.store
    i32.const 0
    i32.const 0
    call $console_write_string
    local.get $result
    f32.load
    call $console_write_float
  )
  (export "main" (func $main))
  (start $main)
)
(module
  (import "console" "write_int" (func $console_write_int (param i32)))
  (import "console" "write_float" (func $console_write_float (param f32)))
  (import "console" "write_bool" (func $console_write_bool (param i32)))
  (import "console" "write_string" (func $console_write_string (param i32)))
  (import "console" "read_int" (func $console_read_int (result i32)))
  (import "console" "read_float" (func $console_read_float (result f32)))
  (import "console" "read_bool" (func $console_read_bool (result i32)))
  (import "Math" "asin" (func $Math_asin (param f32) (result f32)))
  (import "Math" "sin" (func $Math_sin (param f32) (result f32)))
  (import "Math" "sqrt" (func $Math_sqrt (param f32) (result f32)))
  (import "Math" "exp" (func $Math_exp (param f32) (result f32)))
  (import "Math" "floor" (func $Math_floor (param f32) (result f32)))
  (import "Math" "atan" (func $Math_atan (param f32) (result f32)))
  (import "Math" "ceil" (func $Math_ceil (param f32) (result f32)))
  (import "Math" "cos" (func $Math_cos (param f32) (result f32)))
  (import "Math" "log" (func $Math_log (param f32) (result f32)))
  (import "Math" "tan" (func $Math_tan (param f32) (result f32)))
  (import "Math" "abs" (func $Math_abs (param f32) (result f32)))
  (import "Math" "acos" (func $Math_acos (param f32) (result f32)))
  (import "Math" "pow" (func $Math_pow (param f32) (param f32) (result f32)))
  (memory $memory 1)
  ;; String constants
  (data (i32.const 1) "\"Min: \"\00")
  (data (i32.const 9) "\", Max: \"\00")
  (data (i32.const 19) "\"Before swap: num1 = \"\00")
  (data (i32.const 42) "\", num2 = \"\00")
  (data (i32.const 54) "\"After swap: num1 = \"\00")
  (data (i32.const 76) "\"Roots of equation \"\00")
  (data (i32.const 97) "\"x^2 + \"\00")
  (data (i32.const 106) "\"x + \"\00")
  (data (i32.const 113) "\" = 0 are:\"\00")
  (data (i32.const 125) "\"Root 1: \"\00")
  (data (i32.const 136) "\", Root 2: \"\00")
  (data (i32.const 149) "\"Verification (should be close to 0): \"\00")
  (data (i32.const 189) "\" and \"\00")
  (data (i32.const 197) "\"No real roots found\"\00")
  (data (i32.const 219) "\"Both roots are positive: \"\00")
  (func $solveQuadratic@float_float_float_float_float_bool@
    (param $a i32)
    (param $b i32)
    (param $c i32)
    (param $root1 i32)
    (param $root2 i32)
    (param $result i32)
    (local $discriminant i32)
    i32.const 247
    local.set $discriminant
    local.get $discriminant
    local.get $b
    f32.load
    f32.const 2.0
    call $Math_pow
    f32.const 4.0
    local.get $a
    f32.load
    f32.mul
    local.get $c
    f32.load
    f32.mul
    f32.sub
    f32.store
    local.get $discriminant
    f32.load
    f32.const 0.0
    f32.lt
    if
        local.get $result
        i32.const 0
        i32.store
    end
    local.get $root1
    local.get $b
    f32.load
    f32.neg
    local.get $discriminant
    f32.load
    f32.const 0.5
    call $Math_pow
    f32.add
    f32.const 2.0
    local.get $a
    f32.load
    f32.mul
    f32.div
    f32.store
    local.get $root2
    local.get $b
    f32.load
    f32.neg
    local.get $discriminant
    f32.load
    f32.const 0.5
    call $Math_pow
    f32.sub
    f32.const 2.0
    local.get $a
    f32.load
    f32.mul
    f32.div
    f32.store
    local.get $result
    i32.const 1
    i32.store
    return
  )
  (func $findMinMax@float_float_float_float@
    (param $a i32)
    (param $b i32)
    (param $min i32)
    (param $max i32)
    local.get $a
    f32.load
    local.get $b
    f32.load
    f32.lt
    if
        local.get $min
        local.get $a
        f32.load
        f32.store
        local.get $max
        local.get $b
        f32.load
        f32.store
    else
        local.get $min
        local.get $b
        f32.load
        f32.store
        local.get $max
        local.get $a
        f32.load
        f32.store
    end
    return
  )
  (func $swap@float_float@
    (param $x i32)
    (param $y i32)
    (local $temp i32)
    i32.const 251
    local.set $temp
    local.get $temp
    local.get $x
    f32.load
    f32.store
    local.get $x
    local.get $y
    f32.load
    f32.store
    local.get $y
    local.get $temp
    f32.load
    f32.store
    return
  )
  (func $main
            (local $$temp_1 i32)
    (local $isPositive i32)
    (local $check2 i32)
    (local $check1 i32)
    (local $result i32)
    (local $test2 i32)
    (local $test i32)
    (local $root2 i32)
    (local $root1 i32)
    (local $c i32)
    (local $b i32)
    (local $a i32)
    (local $maximum i32)
    (local $minimum i32)
    (local $num2 i32)
    (local $num1 i32)
    i32.const 255
    local.set $num1
    i32.const 259
    local.set $num2
    i32.const 263
    local.set $minimum
    i32.const 267
    local.set $maximum
    i32.const 271
    local.set $a
    i32.const 275
    local.set $b
    i32.const 279
    local.set $c
    i32.const 283
    local.set $root1
    i32.const 287
    local.set $root2
    i32.const 291
    local.set $test
    i32.const 295
    local.set $test2
    i32.const 299
    local.set $result
    i32.const 303
    local.set $check1
    i32.const 307
    local.set $check2
    i32.const 311
    local.set $isPositive
    local.get $num1
    f32.const 1.5
    f32.store
    local.get $num2
    f32.const 8.3
    f32.store
    local.get $minimum
    f32.const 0.0
    f32.store
    local.get $maximum
    f32.const 0.0
    f32.store
          local.get $num1
          local.get $num2
          local.get $minimum
          local.get $maximum
          call $findMinMax@float_float_float_float@
            local.get $num1
            local.get $num2
            local.get $minimum
            i32.const 315
            local.set $$temp_1
            local.get $$temp_1
            local.get $maximum
            f32.load
            call $Math_sin
            f32.store
            local.get $$temp_1
            call $findMinMax@float_float_float_float@
    i32.const 1
    call $console_write_string
    local.get $minimum
    f32.load
    call $console_write_float
    i32.const 9
    call $console_write_string
    local.get $maximum
    f32.load
    call $console_write_float
    i32.const 19
    call $console_write_string
    local.get $num1
    f32.load
    call $console_write_float
    i32.const 42
    call $console_write_string
    local.get $num2
    f32.load
    call $console_write_float
    local.get $num1
    local.get $num2
    f32.load
    f32.store
    local.get $num2
    local.get $num1
    f32.load
    f32.store
    i32.const 54
    call $console_write_string
    local.get $num1
    f32.load
    call $console_write_float
    i32.const 42
    call $console_write_string
    local.get $num2
    f32.load
    call $console_write_float
    local.get $a
    f32.const 1.0
    f32.store
    local.get $b
    f32.const -5.0
    f32.store
    local.get $c
    f32.const 6.0
    f32.store
    local.get $root1
    f32.const 0.0
    f32.store
    local.get $root2
    f32.const 0.0
    f32.store
    local.get $test
    f32.const 0.5
    f32.store
    local.get $test2
    f32.const 0.5
    f32.store
    local.get $result
    i32.const 0
    i32.store
    local.get $a
    local.get $b
    local.get $c
    local.get $root1
    local.get $root2
    local.get $result
    call $solveQuadratic@float_float_float_float_float_bool@
    local.get $result
    i32.load
    if
        i32.const 76
        call $console_write_string
        local.get $a
        f32.load
        call $console_write_float
        i32.const 97
        call $console_write_string
        local.get $b
        f32.load
        call $console_write_float
        i32.const 106
        call $console_write_string
        local.get $c
        f32.load
        call $console_write_float
        i32.const 113
        call $console_write_string
        i32.const 125
        call $console_write_string
        local.get $root1
        f32.load
        call $console_write_float
        i32.const 136
        call $console_write_string
        local.get $root2
        f32.load
        call $console_write_float
        local.get $check1
        local.get $a
        f32.load
        local.get $root1
        f32.load
        f32.const 2.0
        call $Math_pow
        f32.mul
        local.get $b
        f32.load
        local.get $root1
        f32.load
        f32.mul
        f32.add
        local.get $c
        f32.load
        f32.add
        f32.store
        local.get $check2
        local.get $a
        f32.load
        local.get $root2
        f32.load
        f32.const 2.0
        call $Math_pow
        f32.mul
        local.get $b
        f32.load
        local.get $root2
        f32.load
        f32.mul
        f32.add
        local.get $c
        f32.load
        f32.add
        f32.store
        i32.const 149
        call $console_write_string
        local.get $check1
        f32.load
        call $console_write_float
        i32.const 189
        call $console_write_string
        local.get $check2
        f32.load
        call $console_write_float
    else
        i32.const 197
        call $console_write_string
    end
    local.get $isPositive
    local.get $root1
    f32.load
    f32.const 0.0
    f32.gt
    local.get $root2
    f32.load
    f32.const 0.0
    f32.gt
    i32.and
    i32.store
    i32.const 219
    call $console_write_string
    local.get $isPositive
    i32.load
    call $console_write_bool
  )
  (export "memory" (memory $memory))
  (export "main" (func $main))
)
(module
  (import "console" "write_int" (func $console_write_int (param i32)))
  (import "console" "write_float" (func $console_write_float (param f32)))
  (import "console" "write_bool" (func $console_write_bool (param i32)))
  (import "console" "write_string" (func $console_write_string (param i32)))
  (import "console" "read_int" (func $console_read_int (result i32)))
  (import "console" "read_float" (func $console_read_float (result f32)))
  (import "console" "read_bool" (func $console_read_bool (result i32)))
  (import "Math" "sin" (func $Math_sin (param f32) (result f32)))
  (import "Math" "sqrt" (func $Math_sqrt (param f32) (result f32)))
  (import "Math" "tan" (func $Math_tan (param f32) (result f32)))
  (import "Math" "atan" (func $Math_atan (param f32) (result f32)))
  (import "Math" "floor" (func $Math_floor (param f32) (result f32)))
  (import "Math" "log" (func $Math_log (param f32) (result f32)))
  (import "Math" "cos" (func $Math_cos (param f32) (result f32)))
  (import "Math" "ceil" (func $Math_ceil (param f32) (result f32)))
  (import "Math" "abs" (func $Math_abs (param f32) (result f32)))
  (import "Math" "asin" (func $Math_asin (param f32) (result f32)))
  (import "Math" "exp" (func $Math_exp (param f32) (result f32)))
  (import "Math" "acos" (func $Math_acos (param f32) (result f32)))
  (import "Math" "pow" (func $Math_pow (param f32) (param f32) (result f32)))
  (memory $memory 1)
  ;; String constants
  (data (i32.const 1) "\"Enter the first cathetus:\n\"\00")
  (data (i32.const 31) "\"Enter the second cathetus:\n\"\00")
  (data (i32.const 62) "\"Large triangle.\n\"\00")
  (data (i32.const 82) "\"Small triangle.\n\"\00")
  (data (i32.const 102) "\"Area: \"\00")
  (data (i32.const 111) "\", Hypotenuse: \"\00")
  (data (i32.const 128) "\"\n\"\00")
  (data (i32.const 133) "\"Rounded hypotenuse: \"\00")
  (data (i32.const 156) "\"Is right triangle? \"\00")
  (func $isRightTriangle@float_float_float_bool@
    (param $a i32)
    (param $b i32)
    (param $c i32)
    (param $result i32)
    local.get $result
    local.get $a
    f32.load
    f32.const 2.0
    call $Math_pow
    local.get $b
    f32.load
    f32.const 2.0
    call $Math_pow
    f32.add
    local.get $c
    f32.load
    f32.const 2.0
    call $Math_pow
    f32.eq
    local.get $a
    f32.load
    f32.const 2.0
    call $Math_pow
    local.get $c
    f32.load
    f32.const 2.0
    call $Math_pow
    f32.add
    local.get $b
    f32.load
    f32.const 2.0
    call $Math_pow
    f32.eq
    i32.or
    local.get $b
    f32.load
    f32.const 2.0
    call $Math_pow
    local.get $c
    f32.load
    f32.const 2.0
    call $Math_pow
    f32.add
    local.get $a
    f32.load
    f32.const 2.0
    call $Math_pow
    f32.eq
    i32.or
    i32.store
    return
  )
  (func $usingGlobalStuff@@
    (local $global_var3 i32)
    (local $global_var2 i32)
    (local $global_var1 i32)
    i32.const 178
    local.set $global_var1
    i32.const 182
    local.set $global_var2
    i32.const 186
    local.set $global_var3
    local.get $global_var1
    f32.const 2.0
    f32.store
    local.get $global_var2
    f32.const 2.0
    f32.store
    local.get $global_var3
    i32.const 2
    i32.store
    local.get $global_var1
    f32.const 3.0
    f32.store
    local.get $global_var2
    f32.const 3.0
    f32.store
    local.get $global_var3
    i32.load
    call $console_write_int
    i32.const 128
    call $console_write_string
    return
  )
  (func $calculateHypotenuse@float_float_float@
    (param $a i32)
    (param $b i32)
    (param $result i32)
    local.get $result
    local.get $a
    f32.load
    f32.const 2.0
    call $Math_pow
    local.get $b
    f32.load
    f32.const 2.0
    call $Math_pow
    f32.add
    f32.const 0.5
    call $Math_pow
    f32.store
    return
  )
  (func $main
    (local $global_var3 i32)
    (local $global_var2 i32)
    (local $global_var1 i32)
    (local $x i32)
    (local $isRight i32)
    (local $roundedHypotenuse i32)
    (local $hypotenuse i32)
    (local $area i32)
    (local $cathetusB i32)
    (local $cathetusA i32)
    (local $counter i32)
    i32.const 190
    local.set $counter
    i32.const 194
    local.set $cathetusA
    i32.const 198
    local.set $cathetusB
    i32.const 202
    local.set $area
    i32.const 206
    local.set $hypotenuse
    i32.const 210
    local.set $roundedHypotenuse
    i32.const 214
    local.set $isRight
    i32.const 218
    local.set $x
    i32.const 222
    local.set $global_var1
    i32.const 226
    local.set $global_var2
    i32.const 230
    local.set $global_var3
    local.get $counter
    i32.const 0
    i32.store
    local.get $cathetusA
    f32.const 0.0
    f32.store
    local.get $cathetusB
    f32.const 0.0
    f32.store
    i32.const 1
    call $console_write_string
    local.get $cathetusA
    call $console_read_float
    f32.store
    i32.const 31
    call $console_write_string
    local.get $cathetusB
    call $console_read_float
    f32.store
    local.get $area
    f32.const 0.0
    f32.store
    local.get $hypotenuse
    f32.const 0.0
    f32.store
    local.get $area
    local.get $cathetusA
    f32.load
    local.get $cathetusB
    f32.load
    f32.mul
    f32.const 2.0
    f32.div
    f32.store
    local.get $cathetusA
    local.get $cathetusB
    local.get $hypotenuse
    call $calculateHypotenuse@float_float_float@
    local.get $hypotenuse
    f32.load
    f32.const 10.0
    f32.gt
    if
        i32.const 62
        call $console_write_string
    else
        i32.const 82
        call $console_write_string
    end
    i32.const 102
    call $console_write_string
    local.get $area
    f32.load
    call $console_write_float
    i32.const 111
    call $console_write_string
    local.get $hypotenuse
    f32.load
    call $console_write_float
    i32.const 128
    call $console_write_string
    local.get $roundedHypotenuse
    local.get $hypotenuse
    f32.load
    f32.trunc
    i32.trunc_f32_s
    i32.store
    i32.const 133
    call $console_write_string
    local.get $roundedHypotenuse
    i32.load
    call $console_write_int
    i32.const 128
    call $console_write_string
    local.get $isRight
    i32.const 0
    i32.store
    local.get $cathetusA
    local.get $cathetusB
    local.get $hypotenuse
    local.get $isRight
    call $isRightTriangle@float_float_float_bool@
    i32.const 156
    call $console_write_string
    local.get $isRight
    i32.load
    call $console_write_bool
    i32.const 128
    call $console_write_string
    local.get $x
    i32.const 0
    i32.store
    local.get $global_var1
    f32.const 2.0
    f32.store
    local.get $global_var2
    f32.const 2.0
    f32.store
    local.get $global_var3
    f32.const 2.0
    f32.store
    call $usingGlobalStuff@@
    local.get $global_var1
    f32.load
    call $console_write_float
    i32.const 128
    call $console_write_string
    local.get $global_var2
    f32.load
    call $console_write_float
    i32.const 128
    call $console_write_string
  )
  (export "memory" (memory $memory))
  (export "main" (func $main))
)
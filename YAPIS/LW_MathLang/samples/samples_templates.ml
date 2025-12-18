// CORRECT SAMPLES


// Using one template argument
sub pretty_write:(T)(T a)
{
    write("Something pretty")
    write(a)
}

// Using two or more template arguments
sub double_template:(K, V)(K key, V value)
{
    V key_casted = cast:(K, V)(key)
}

// Variables of templated types may be created in subprogram
sub inner_initialization:(T)(T result)
{
    T intermediate_result = read:(T)()
    result = intermediate_result * cast:(float, T)(2.0)
}

sub call_to_templated_sub:(T)(T val)
{
    pretty_write(val)

    // Providing template argument explicitly is allowed in call statement
    int i_val = cast:(T, int)(val)
    pretty_write:(int)(i_val)
}

// When defining templated subprogram, it is possible to manually provide custom implementation for specific types ...
sub explicit_implementation:(T)(T val)
{
    write("Arbitrary type")
    write(val)
}

// ... This requires definition of templated subprogram before
sub explicit_implementation:(int)(int val)
{
    write("Specifically for int!")
    write(val)
}


// INCORRECT SAMPLES
// Syntactically incorrect samples


// Zero template arguments
//sub zero_template_arguments:()() {}

// Using literals or expressions in template arguments
//sub literal_in_template_arguments:(2, 2 + 4)() {}


// Semantically incorrect samples

// Explicit implementation not allowed without previously declared templated subprogram
sub explicit_implementation_without_templated_declaration:(int)(int val)
{
    write("Specifically for int!")
    write(val)
}

// Unused template argument
sub unused_argument:(Unused)() {}
sub unused_argument:(T, K)(T value) {}

// Using template arguments without declaration
// sub unknown_argument(T value) {}
// sub unknown_argument:(T)(K value) {}

// Redefinition of templated subprogram using different template argument identifiers
sub same_name:(T)(T value_one) {}
sub same_name:(K)(K value_two) {}

// Defining non-templated subprogram that conflicts with specific templated subprogram implementation.
// The correct way is to use explicit implementation
sub conflicting_name:(T)(T value) {}
sub conflicting_name(int value) {}

sub test:(T)(T test1, int test2) {}
// sub test2(T test1) {}

sub recursion:(T)(T val, int result)
{
    int res = cast:(K, int)(val)

    if(result > 10)
    {
        return
    }

    result = result + 1

    recursion(cast:(T, K)(val), result)
}

// Sample calling code
inner_initialization(2)
inner_initialization(2.0)

explicit_implementation(2)
explicit_implementation(2.0)

call_to_templated_sub(2)
call_to_templated_sub(2.0)
// call_to_templated_sub("dsd")

float input_float = 0.0
int a = cast:(float, int)(read:(float)())
inner_initialization(2)
inner_initialization(2.0)
// inner_initialization("dsd")
// T a = cast:(int, T)(2)
inner_initialization(2)
// CORRECT SAMPLES


// Using one template argument
sub pretty_write<T>(T a)
{
    write("Something pretty")
    write(a)
}

// Using two or more template arguments
sub double_template<K, V>(K key, V value)
{
    int key_casted = cast(key)
}

// Variables of templated types may be created in subprogram
sub inner_initialization<T>(T result)
{
    T intermediate_result = cast(read())
    result = intermediate_result * 2
}

sub call_to_templated_sub<T>(T val)
{
    // Suitable overload will be found without explicit statement of template argument
    pretty_write(val)

    // Providing template argument explicitly is allowed in call statement
    int i_val = cast(val)
    pretty_write<int>(val)
}

// When defining templated subprogram, it is possible to manually provide custom implementation for specific types ...
sub explicit_implementation<T>(T val)
{
    write("Arbitrary type")
    write(val)
}

// ... This requires definition of templated subprogram before
sub explicit_implementation<int>(int val)
{
    write("Specifically for int!")
    write(val)
}


// INCORRECT SAMPLES
// Syntactically incorrect samples


// Zero template arguments
//sub zero_template_arguments<>() {}

// Using literals or expressions in template arguments
//sub literal_in_template_arguments<2, 2 + 4>() {}


// Semantically incorrect samples

// Explicit implementation not allowed without previously declared templated subprogram
sub explicit_implementation_without_templated_declaration<int>(int val)
{
    write("Specifically for int!")
    write(val)
}

// Unused template argument
sub unused_argument<Unused>() {}
sub unused_argument<T, K>(T value) {}

// Using template arguments without declaration
sub unknown_argument(T value) {}
sub unknown_argument<T>(K value) {}

// Redefinition of templated subprogram using different template argument identifiers
sub same_name<T>(T value_one) {}
sub same_name<K>(K value_two) {}

// Defining non-templated subprogram that conflicts with specific templated subprogram implementation.
// The correct way is to use explicit implementation
sub conflicting_name<T>(T value) {}
sub conflicting_name(int value) {}

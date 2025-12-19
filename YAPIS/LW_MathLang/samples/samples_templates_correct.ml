// CORRECT SAMPLES


// Using one template argument
sub pretty_write:(T)(T a)
{
    write("Something pretty\n")
    write(a)
    write("\n")
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
    write("\n")
}

// ... This requires definition of templated subprogram before
sub explicit_implementation:(int)(int val)
{
    write("Specifically for int!")
    write(val)
    write("\n")
}

sub recursion:(T)(T val, int result)
{
    int res = cast:(T, int)(val)

    if(result > 10)
    {
        return
    }

    result = result + 1

    recursion(val, result)
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
//inner_initialization("dsd")
inner_initialization(2)

int res = 0
write("result before recursion: ")
write(res)
write("\n")
recursion(2, res)
write("result after recursion: ")
write(res)
write("\n")

double_template(2, 4.0)
double_template(2, true)
double_template(false, true)
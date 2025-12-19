sub recursion:(T, K)(T val1, K val2)
{
    write(val1)
    write("\n")
    write(val2)
    write("\n")

    if (val2 > cast:(int, K)(5))
    {
        return
    }

    val2 = val2 + cast:(int, K)(1)

    recursion(val2, val1)
}

recursion(1.5, 2)
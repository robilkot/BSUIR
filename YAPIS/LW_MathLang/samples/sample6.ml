sub test(float c) {
    c = c * 2.0

    write(c)
    write("\n")
    if(c > 100.0)
    {
        write("exiting recursion after c > 100\n")
        write(100500)
        write("\n")
    }
    else
    {
        test(c)
    }
}

for(int i = 0; i < 10; i = i + 1)
{
    write(sin(cast:(int, float)(i)))
    write("\n")
}

write("recursive sub:\n")
test(5.0)

sub test(float c) {
    c = c * 2.0

    write(c)
    if(c > 100.0)
    {
        write(100500)
    }
    else
    {
        test(c)
    }
}

for(int i = 0; i < 10; i = i + 1)
{
    write(sin(cast:(int, float)(i)))
}

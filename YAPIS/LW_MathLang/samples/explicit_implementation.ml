sub expl_impl:(T)(T val)
{
    for(int i = 0; i < 3; i = i + 1)
    {
        write(i)
    }
}

sub expl_impl:(int)(int val)
{
    for(int i = 0; i < 2; i = i + 1)
    {
        write(i)
    }
}

sub expl_impl_incorrect:(float, K)(float float)
{

}

expl_impl(true)
expl_impl(2)
expl_impl_incorrect(2.0)
expl_impl_incorrect(2)
write(2.0)
sin:(int)(2.0)
cast:(int, float, int)(2.0, 2)
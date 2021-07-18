#include <iostream>
#include <chrono>
#include <random>

using std::cout;
using std::endl;

static std::chrono::high_resolution_clock hrc;
static std::mt19937 twister(hrc.now().time_since_epoch().count());

const static int max = 126;
const static int min = 33;

const static unsigned int N_ROWS = 2;
const static unsigned int N_COLS = 2;

void foo(unsigned int& n_spaces, unsigned int& n_stars, unsigned int size, bool direction)
{
    if(!direction)
    {
        n_spaces += 2;
        n_stars -= 2;
    }

    while(1)
    {
        if(direction)
        {
            if(n_spaces < 1)
                break;
        }
        else
        {
            if(n_spaces > size)
                break;
        }

        for(unsigned int i = 0; i < N_COLS; ++i)
        {
            char coc = (twister() % (max - min)) + min;

            for(unsigned int j = 0; j < (n_spaces-1); ++j)
                printf(" ");

            for(unsigned int j = 0; j < n_stars; ++j)
                printf("%c", coc);

            for(unsigned int j = 0; j < (n_stars-1); ++j)
                printf("%c", coc);

            for(unsigned int j = 0; j < n_spaces; ++j)
                printf(" ");
        }
        printf("\n");

        if(direction)
        {
            --n_spaces;
            ++n_stars;
        }
        else
        {
            ++n_spaces;
            --n_stars;
        }
    }
}

int main()
{
    const unsigned int size = 5;

    unsigned int n_spaces = size;
    unsigned int n_stars = 1;
    for(unsigned int i = 0; i < N_ROWS; ++i)
    {
        foo(n_spaces, n_stars, size, true);
        foo(n_spaces, n_stars, size, false);
        for(int j = 0; j < 1; ++j)
        {
            for(unsigned int k = 0; k < N_COLS * size * 2; ++k)
                printf(" ");
            printf("\n");
        }
        n_spaces = size;
        n_stars = 1;
    }
    
    return 0;
}

#include <iostream>

void printBumBac(int limit)
{
    for (int i = 1; i <= limit; i++)
    {
        const bool isDivisibleBy3 = i % 3 == 0; // check if i is divisible by 3
        const bool isDivisibleBy5 = i % 5 == 0; // check if i is divisible by 5

        // if is divisible by 3, print bum
        if (isDivisibleBy3)
            std::cout << "bum";
        // if is divisible by 5, print bác
        if (isDivisibleBy5)
            std::cout << "bác";
        // if is not divisible by 3 or 5, print number
        if (!isDivisibleBy3 && !isDivisibleBy5)
            std::cout << i;
        // separate numbers by commas
        if (i < 100)
            std::cout << "\n";
    }
}

int main()
{
    // print numbers
    printBumBac(100);

    return 0;
}
#include <iostream>
#include <cstdlib>
#include <fstream>
#include "bst.cpp"


int main(int argc, char** argv)
{

    std::ifstream file("input.txt");

    if(!file.is_open()) {
        std::cerr << " -- Failed to open the file -- " << std::endl;
        return EXIT_FAILURE;
    }

    int size; int key; int number;

    while(!file.eof()) {

        file >> size;

        int array[size];

        for(int i = 0; i < size; i++) {
            file >> array[i];
        }

        file >> key;

        int count = 0;

        

        // printArray(array, size);
        // std::cout << " ++ key:\t" << key << std::endl;
        // std::cout << " ~~> result:\t" << result << std::endl;
        std::cout << " --> count:\t" << count << std::endl;

    }

    file.close();

    return EXIT_SUCCESS;
}
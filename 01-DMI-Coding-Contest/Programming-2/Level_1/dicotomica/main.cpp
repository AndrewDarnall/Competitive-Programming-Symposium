#include <iostream>
#include <cstdlib>
#include "bst.cpp"

int main(int argc, char** argv)
{

    BST<int>* tree = new BST<int>();

    for(int i = 0; i < 10; i++) {
        tree->insert(i+1);
    }

    std::cout << " -- Inorder Walk -- " << std::endl;
    tree->inOrder();
    std::cout << " -- Preorder Walk -- " << std::endl;
    tree->preOrder();
    std::cout << " -- Postorder Walk -- " << std::endl;
    tree->postOrder();

    int array[5] = {7, 11, 14, 17, 17};

    BST<int>* nTree = new BST<int>();

    nTree->setRoot(nTree->createTree(array, 5));

    std::cout << " -- Inorder Walk -- " << std::endl;
    nTree->inOrder();


    return EXIT_SUCCESS;
}
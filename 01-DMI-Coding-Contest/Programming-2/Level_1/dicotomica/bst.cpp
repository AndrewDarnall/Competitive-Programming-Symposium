#include <iostream>

template <typename T>
class Node {
    public:

        T key;

        Node<T>* leftChild;
        Node<T>* rightChild;
        Node<T>* parent;
        
        Node<T>(T key) : key(key), leftChild(nullptr), rightChild(nullptr), parent(nullptr) {}
};

template <typename T>
class BST {
    private:
        Node<T>* root;

        void inOrder(Node<T>* p) {
            if (p != nullptr) {
                inOrder(p->leftChild);
                std::cout << p->key << std::endl;;
                inOrder(p->rightChild);
            }
        }

        void preOrder(Node<T>* p) {
            if (p != nullptr) {
                std::cout << p->key << std::endl;
                preOrder(p->leftChild);
                preOrder(p->rightChild);
            }
        }

        void postOrder(Node<T>* p) {
            if (p != nullptr) {
                postOrder(p->leftChild);
                postOrder(p->rightChild);
                std::cout << p->key << std::endl;
            }
        }

    public:
        BST() : root(nullptr) {}

        void insert(T key) {

            Node<T>* newNode = new Node<T>(key);

            if (this->root == nullptr) {
                this->root = newNode;
            } else {
                Node<T>* iter = this->root;
                Node<T>* trace = this->root;

                while(iter != nullptr) {
                    trace = iter;
                    if (key >= iter->key) {
                        iter = iter->rightChild;
                    } else {
                        iter = iter->leftChild;
                    }
                }
                
                if (key >= trace->key) {
                    trace->rightChild = newNode;
                } else {
                    trace->leftChild = newNode;
                }
                
            }
        }

        void setRoot(Node<T>* root) {
            this->root = root;
        }

        Node<T>* getRoot() {
            return this->root;
        }

        void inOrder() {
            inOrder(this->root);
        }

        void preOrder() {
            preOrder(this->root);
        }

        void postOrder() {
            postOrder(this->root);
        }

        Node<T>* createTree(int* array, int size)
        {
            if (size == 0) return nullptr;
            int mid = size / 2;
            Node<T>* newRoot = new Node<T>(array[mid]);
            int left[mid];
            int right[mid];
            for(int i = 0; i < mid; i++) {
                left[i] = array[i];
            }
            for(int j = mid; j < size; j++) {
                right[j] = array[j];
            }
            newRoot->leftChild = createTree(left, mid);
            newRoot->rightChild = createTree(right, mid);
            return newRoot;
        }
};
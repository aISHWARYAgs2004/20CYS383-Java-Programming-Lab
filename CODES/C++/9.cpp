#include <iostream>

using namespace std;

class Test {

int value;

public:

void get_Data() {

cout << "Enter a value : ";

cin >> value;

}

void print_Data() {

cout << value << endl;

}

void operator -() { 

value = -value;

}

};

int main() {

Test t;

t.get_Data();

cout << "Before change the value is : ";

t.print_Data();

-t; // It will call like t.operator -();

cout << "After change the value is : ";

t.print_Data();

}

#include<iostream>
using namespace std;

struct Node{
    int age;
    string name;
    Node * next;
    Node(){
        age=-1;
        name="";
        next=NULL;
    }
    Node (int age_input,string name_input){
        age=age_input;
        name = name_input;
        next=NULL;
    }
};


// delete
// double link list

class Linklist{
    Node * head;
    int length;
    public:
    Linklist(){ 
        head= NULL;
        length=0;
    };
    Linklist(int age,string name){
        head = new Node(age,name);
        length=1;
    }

    void insertAtEnd(int age,string name){

        if (head == NULL){
            
            head = new Node(age,name);
            length=1;
            return ;
        }
       
        Node * temp = head;
        while (temp->next!=NULL){
            temp=temp->next;
        }
        Node * obj = new Node(age,name);
        temp->next = obj;
        length++;
        return ;

    }


    void insertafter(int age,string name, string search){
        Node * obj = new Node(age,name);
        Node * temp = head;
        while(temp->next!=NULL){
            if (temp->name == search){
                Node * temp2 = temp->next;
                temp->next = obj;
                obj->next = temp2;
                length+=1;
                return;
            }
            temp = temp->next;
        }
        temp->next = obj;
        length+=1;
    }

    bool deletet(string name){
        if (head->name == name){
            Node * temp = head->next;
            delete head;
            head = temp;
            length-=1;
            return true;
        }
        if (length==1){
            return false;
        }
        Node * temp2 = head;
        while(temp2->next!=NULL){
            if (temp2->next->name == name){
                Node * temp3 = temp2->next->next;
                delete temp2->next;
                temp2->next = temp3;
                length-=1;
                return true;
            }
            temp2 = temp2->next;
        }
        return false;

    }
    void print(){
        Node * temp = head;
        while(temp!=NULL){
            cout<<"Name: "<<temp->name<<" Age: "<<temp->age <<"  length:  " <<length<<endl;
            temp = temp->next;
        }
    }
};

int main(){
    Linklist my_array = Linklist();
    my_array.insertAtEnd(10,"a");
    my_array.insertAtEnd(20,"b");
    my_array.insertAtEnd(30,"c");
    my_array.insertafter(40,"d","b");
    my_array.insertafter(0,"e","a");
    my_array.print();
    cout<<endl<<endl;
    my_array.deletet("a");
    my_array.print();
     cout<<endl<<endl;
    my_array.deletet("b");
    my_array.print();
     cout<<endl<<endl;
    my_array.deletet("c");
    my_array.print();
     cout<<endl<<endl;
    my_array.deletet("d");
    my_array.print();
     cout<<endl<<endl;
    my_array.deletet("e");
    my_array.print();

    return 0;
}



#Module

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=Node(data)
        if (self.root==None):
            self.root=newnode
            print("Node Succesfully Inserted As Root")
        else:
            temp=self.root
            while(temp is not None):
                par=temp
                if(temp.data>data):
                    temp=temp.left
                else:
                    temp=temp.right
            if(data>par.data):
                par.right=newnode
            else:
                par.left=newnode
            print("Node Inserted Succesfully")
    def findmin(self,root):
        temp=root
        while(temp.left is not None):
             temp=temp.left    
        return temp
        
    def delete(self,temp,val):
        temp=self.root
        rmin=None
        
        while(temp is not None and temp.data is not val  ):
            if(temp.data>val):
                par=temp
                temp=temp.left
            else:
                par=temp
                temp=temp.right
        if temp is None :
            print("Node Is Not Present In The Tree")
        elif(temp.right is None and temp.left is None):
            if par.left is temp:
                par.left=None
            else:
                par.right=None
            del temp
        elif (temp.right is None and temp.left is not None):
            if par.left is temp.left:
                par.left=temp.left
            else:
                par.right=temp.left
            del temp
        elif(temp.right is not None and temp.left is  None):
            if par.left is temp:
                par.left=temp.right
            else:
                par.right=temp.right
            del temp
        elif (temp.right is not None and temp.left is not None):
            rmin=self.findmin(temp.right)
            self.delete(temp,rmin.data)
            temp.data=rmin.data
                    #Added By Vishal Padme


        return self.root
    def inorder(self,temp):
        if(temp is not None):
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)
    def preorder(self,temp):
        if(temp is not None):
            print(temp.data,end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)
    def postorder(self,temp):
        if(temp is not None):
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data,end=" ")
    
    def findmax(self):
        temp=self.root
        while(temp.right is not None):
            temp=temp.right
        print("The MaximumValue In The Binary Search Tree Is =",temp.data)
    
#Call
tree=BST()
print("MENU")
print("1.Insert\n2.Delete\n3.Display inorder\n4.Display  Preorder\n5.Display Postorder\n6.Display Minimum\n7.Display Maximum")
ch=int(input("\nEnter Your Choise-  "))
while ch<9:
    if (ch==1):
        val=int(input("Enter Data To Be Inserted-   "))
        tree.insert(val)
    elif(ch==2):
        val=int(input("Enter Node you Want To Delete   "))
        root=tree.delete(tree.root,val)
        print("Node  ",val," has been deleted")
    elif(ch==3):
        tree.inorder(tree.root)
    elif(ch==4):
        tree.preorder(tree.root)
    elif(ch==5):
        tree.postorder(tree.root)
    elif(ch==6):
        z=tree.findmin(tree.root)
        print("The Minimum Value In The Binary Search Tree Is =",z.data)
    elif(ch==7):
        tree.findmax()

    ch=int(input("\nEnter Your Next Choise-  "))



            
1
**Binary Trees**

**Properties**
* Cannot contain cycles.
* May or may not have links to the parent node.
* A node is called *leaf* if it contains no children.
* Each node has up to 2 children
* If a tree is balanced it's height (levels) is *log n*
* If a tree is balanced the total number of nodes is aprox *2 ^ n*

**Characteristics**
* Complete Tree: Each level filled except leaves. If leaves level is incomplete leaves
must be filled from left to right.
* Full binary tree: Each node has either 2 or 0 childs each.
* Perfect binary tree: Each node has 2 childs.

**Traversal**

Ways to go thorugh each node in a tree.

* Preorder: 
    * Visit (print)
    * Left
    * Right 
* Inorder: 
    * Left
    * Visit (print)
    * Right 
* Postorder: 
    * Left
    * Right
    * Visit (print)

**Binary Search Trees** 

Property:
Let *x* be a node in a binary search tree. If *y* is a node in the left subtree of
*x* then *y.value* <= *x.value*. If *y* is a node in the right subtree of *x* then
*y.value* >= *x.value*

This allow to print all the sorted elements of a Binary Search Tree using the *inorder*
traversal algorithm.

As the name says Binary Search Trees provide the ability to perform a *binary search* in
*O(log n)*

**Tips for solving problems**

1. Use multiple pointers. For example for keeping track of the past, 
for foreseeing the future or one slow and one quicker. If you're using a lot 
of them you can try to keep them labeled in a hashmap.

2. Magic methods that are useful: length, next, iter. For nodes implement equals and
hash. Implement repr for both.
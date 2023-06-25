# Tree - Дерево.
![Tree.png](Tree.png) 


## Структура данных в которой есть несколько основных элементов.
* Root (Parent Node) - Корень. Верхний и главный элемент
* Child Node - Нижестоящий элемент, какого-то элемента.
* Branches - Ветка дерева. Соединяет между собой Ноды.

## Где используется
* **File System**:  This allows for efficient navigation and organization of files.
* **Data Compression**: Huffman coding is a popular technique for data compression that involves constructing a binary tree where the leaves represent characters and their frequency of occurrence. The resulting tree is used to encode the data in a way that minimizes the amount of storage required.
* **Compiler Design**: In compiler design, a syntax tree is used to represent the structure of a program. 
* **Database Indexing**: B-trees and other tree structures are used in database indexing to efficiently search for and retrieve data. 

## Виды деревьев

1. #### Binary Tree. Бинарное дерево - у каждого элемент не более двух дочерних элементов.
   * Основанные на количестве дочерних элементов:
     1. Full BT. У каждого элемента СТРОГО два дочерних
     2. Degenerate or Pathological BT. У каждого элемента только один дочерний 
   * Основанные на количестве уровней:
     1. Complete BT. Одинаковая глубина листьев, кроме последнего
     2. Perfect BT. Одинаковая глубина, одинаковое кол-во дочерних элементов у всех элементов.
     3. Balanced BT. Разница между длинной левого и правого узла не должна быть более, чем в 1 элемент
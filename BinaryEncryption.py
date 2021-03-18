import os


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.rchild = None
        self.lchild = None


class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None
        for chars in encrypt_str:
            if 96 < ord(chars) < 123 or ord(chars) == 32:
                self.insert(chars)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        new_node = Node(ch)
        ascii = ord(ch)
        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
        while (current != None):
            parent = current
            if ascii == ord(current.data):
                return
            if ascii < ord(current.data):
                current = current.lchild
            else:
                current = current.rchild

        # found location now insert node
        if (ascii < ord(parent.data)):
            parent.lchild = new_node
        else:
            parent.rchild = new_node

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        current = self.root
        string = ''
        if ch == self.root.data:
            return '*'
        while (current != None) and (current.data != ch):
            if (ord(ch) < ord(current.data)):
                current = current.lchild
                string += '<'
            else:
                current = current.rchild
                string += '>'
        if current is None:
            return ''
        else:
            return string

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        current = self.root
        string = ''
        for chars in st:
            if current is None:
                return ''
            if chars == '*':
                return self.root.data
            if chars == '<':
                current = current.lchild
            else:
                current = current.rchild
        if current.data is None:
            return ''
        else:
            return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        st.lower()
        string = ''
        for chars in st:
            if 96 < ord(chars) < 123 or ord(chars) == 32:
                string += chars
        encrypted = ''
        for chars in string:
            encrypted += self.search(chars)
            encrypted += '!'
        encrypted = encrypted[:-1]
        return encrypted


    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        current = ''
        decrypted = ''
        for chars in st:
            if chars == '!':
                decrypted += self.traverse(current)
                current = ''
            else:
                current += chars
        decrypted += self.traverse(current)
        return decrypted




def main():
    phrase = 'the quick brown fox jumps over the lazy dog'
    encrypt = 'hey cool this thing works'
    decrypt = '<!<<!>>>><!<<<!<<<>!<><>>!<><>>!<><>><<<!<<<!*!<!<><!<>>>!<<<!*!<!<><!<><>><!<<>>!<<<!>>!<><>>!<>>!<><>!<>>>'
    tree = Tree(phrase)
    print(tree.encrypt(encrypt))
    print(tree.decrypt(decrypt))
    print('Searched: ' + tree.search('t'))
    print('transversed: ' + tree.traverse('<<<<<<<<<<<<'))


    # add your code here


main()
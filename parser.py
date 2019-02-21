# -*- coding: utf-8 -*-

from tree import Tree

#html = open("in.html", "r").read()
html = "<html><body><div>asdasdasd</div><span>oloco meu</span><img /></body></html>"

def tokenizer(html):
    tokens = []
    mytoken = ''
    for i in html:
        if i == '<':
            if mytoken != '':
                tokens.append(mytoken)
            mytoken = i

        elif i == '>':
            if mytoken != '':
                mytoken += i
                tokens.append(mytoken)
                mytoken = ""
        else:
            mytoken += i

    return tokens


def print_tree(tree):
    print("sou", tree, "pai", tree.parent, "tenho ", len(tree.children), " filhos")
    if len(tree.children) > 0:
        for i in tree.children:
            print_tree(i)


def maketree(lt):

    stack = []

    tree = Tree('html')

    for token in lt:
        if "<" in token and ("</" not in token or "/>" in token):
            tag = token.split(" ", 1)[0].replace("<","")
            tag = tag.replace(">","")
            new_node = Tree(token)
            tree.add_child(new_node)
            tree = new_node
            stack.append(tag)

        elif "</" in token:
            tag = token.split(" ", 1)[0].replace("<","")
            tag = tag.replace(">","").replace("/","")
            results = [i for i,x in enumerate(stack) if x==tag]
            if len(results) != 0:
                pos = results[-1]
                del stack[pos]

            tree = tree.parent

        elif "/>" in token:
            new_node = Tree(token)
            tree.add_child(new_node)

        else:
            stack.append(token)
            new_node = Tree(token)
            tree.add_child(new_node)

    return tree


if __name__ == "__main__":
    lt = tokenizer(html)

    tree = maketree(lt)

    print_tree(tree)


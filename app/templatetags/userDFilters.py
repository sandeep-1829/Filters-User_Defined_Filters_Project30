from django import template

register=template.Library()

# @register.filter()
def swap(self):
    return self.swapcase()

register.filter('swapping',swap)


# @register.filter()
def replace_char(self,arg):
    return self.replace(arg,'Z')

register.filter('replace',replace_char)


def count(self,arg):
    c=0
    for i in range(len(self)):
        if arg==self[i:i+len(arg)]:
            c+=1
    return c

register.filter('counting',count) 
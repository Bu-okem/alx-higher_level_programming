#!/usr/bin/python3
'''
A Locked Class
'''


class LockedClass:
    '''
    A class with no class or object attribute, that prevents the user
    from dynamically creating new instance attributes, except if the
    new instance attribute is called first_name
    '''

    def __setattr__(self, attribute, value):
        if attribute == 'first_name':
            object.__setattr__(self, attribute, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '"
                    + attribute + "')

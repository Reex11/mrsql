import os

def wizards():
    prefiles = os.listdir('./wizards')
    __all__ = []
    for file in prefiles:
        if not file.startswith('__') and file.endswith('.py'):
            __all__.append(file[:-3])
    return __all__

__all__ = wizards()

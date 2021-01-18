def lib_info ():
    import tensorflow as tf
    import numpy as np

    print(f'Tensorflow version {tf.__version__}\nNumpy version {np.__version__}')
    return 'Package Imported'

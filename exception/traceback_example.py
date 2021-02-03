import traceback
import os
print(os.getcwd())

def traceback_example():
    try:
        raise Exception("Error occured man !!")

    except:
        errorFile = open(os.path.join(os.getcwd(),'errorInfo.txt', 'w'))
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')
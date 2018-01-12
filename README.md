# pythonpeephole

原理根据 
https://blog.quarkslab.com/building-an-obfuscated-python-interpreter-we-need-more-opcodes.html 

增加了3条指令用于混淆，比较2.7.9源码就可以看到对应改动 

./python test_op.py
  2           0 <148>                    1
              3 COMPARE_OP               4 (>)
              6 POP_JUMP_IF_FALSE       31
              9 LOAD_GLOBAL              0 (fib)
             12 <148>                    1
             15 BINARY_SUBTRACT     
             16 CALL_FUNCTION            1
             19 LOAD_GLOBAL              0 (fib)
             22 <148>                    2
             25 BINARY_SUBTRACT     
             26 CALL_FUNCTION            1
             29 BINARY_ADD          
             30 RETURN_VALUE        
        >>   31 <149>                    0
  6           0 <148>                    1
              3 BINARY_ADD          
              4 STORE_FAST               1 (b)

  8           7 <149>                    1
 11           0 <150>                    0
 14           0 LOAD_GLOBAL              0 (True)
              3 RETURN_VALUE        
              
 看到修改结果





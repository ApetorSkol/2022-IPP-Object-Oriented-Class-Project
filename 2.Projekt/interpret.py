import re                               ## praca s regexami
import argparse                         ## pre argumenty
import xml.etree.ElementTree as ET      ## xml spracovanie
import sys, traceback                   ## pre chybove hlasenie

# return substring count
def is_substr(listok,str):
    count = 0
    for i in listok:
        if i == str:
            count +=1
    return count

# check for correct arguments for arg 1

def check_arg_1(listok):
    if is_substr(listok,"arg1") != 1:
        sys.stderr.write("Invalid argument \n")
        exit(32)
    listok[2] = listok[3]
    listok[3] = listok[4]
    listok.pop()
    return listok

# check for correct arguments for instruction with 2 argumetns
def check_arg_2(listok):
    #check_their count
    if len(listok) != 8:
        sys.stderr.write("Invalid argument \n")
        exit(32)
    if is_substr(listok,'arg1') != 1:
        sys.stderr.write("Invalid argument \n")
        exit(32)

    if is_substr(listok,'arg2') != 1:
        sys.stderr.write("Invalid argument \n")
        exit(32)

    #switch them
    if (listok[2] == 'arg1')&(listok[5] == 'arg2'):
        listok[2] = listok[3]
        listok[3] = listok[4]
        listok[4] = listok[6]
        listok[5] = listok[7]
        listok.pop()
        listok.pop()
        return listok
    else:
        tmp1 = listok[5]
        tmp2 = listok[6]
        tmp3 = listok[7]
        listok[5] = listok[2]
        listok[6] = listok[3]
        listok[7] = listok[4]
        listok[2] = tmp1
        listok[3] = tmp2
        listok[4] = tmp3
        listok[2] = listok[3]
        listok[3] = listok[4]
        listok[4] = listok[6]
        listok[5] = listok[7]
        listok.pop()
        listok.pop()
        return listok

# check for correct arguments
# chcek their count their postion and switch them
def check_arg_3(listok):
    if len(listok) != 11:
        sys.stderr.write("Invalid argument \n")
        exit(32)
    if is_substr(listok,'arg1') != 1:
        sys.stderr.write("Invalid argument \n")
        exit(32)

    if is_substr(listok,'arg2') != 1:
        sys.stderr.write("Invalid argument \n")
        exit(32)

    if is_substr(listok,'arg3') != 1:
        sys.stderr.write("Invalid argument \n")
        exit(32)

    if (listok[2] == 'arg1')&(listok[5] == 'arg2')&(listok[8] == 'arg3'):
        listok[2] = listok[3]
        listok[3] = listok[4]
        listok[4] = listok[6]
        listok[5] = listok[7]
        listok[6] = listok[9]
        listok[7] = listok[10]
        listok.pop()
        listok.pop()
        listok.pop()
        return listok
    elif (listok[8] == 'arg3'):
        tmp1 = listok[5]
        tmp2 = listok[6]
        tmp3 = listok[7]
        listok[5] = listok[2]
        listok[6] = listok[3]
        listok[7] = listok[4]
        listok[2] = tmp1
        listok[3] = tmp2
        listok[4] = tmp3
        listok[2] = listok[3]
        listok[3] = listok[4]
        listok[4] = listok[6]
        listok[5] = listok[7]
        listok[6] = listok[9]
        listok[7] = listok[10]
        listok.pop()
        listok.pop()
        listok.pop()
        return listok
    elif (listok[5] == 'arg2'):
        tmp1 = listok[8]
        tmp2 = listok[9]
        tmp3 = listok[10]
        listok[8] = listok[2]
        listok[9] = listok[3]
        listok[10] = listok[4]
        listok[2] = tmp1
        listok[3] = tmp2
        listok[4] = tmp3
        listok[2] = listok[3]
        listok[3] = listok[4]
        listok[4] = listok[6]
        listok[5] = listok[7]
        listok[6] = listok[9]
        listok[7] = listok[10]
        listok.pop()
        listok.pop()
        listok.pop()
        return listok
    elif (listok[5] == 'arg1'):
        tmp1 = listok[8]
        tmp2 = listok[9]
        tmp3 = listok[10]
        listok[8] = listok[5]
        listok[9] = listok[6]
        listok[10] = listok[7]
        listok[5] = tmp1
        listok[6] = tmp2
        listok[7] = tmp3
        listok[2] = listok[3]
        listok[3] = listok[4]
        listok[4] = listok[6]
        listok[5] = listok[7]
        listok[6] = listok[9]
        listok[7] = listok[10]
        listok.pop()
        listok.pop()
        listok.pop()
        return listok
    else:
        if (listok[2] == 'arg2'):
            tmp1 = listok[5]
            tmp2 = listok[6]
            tmp3 = listok[7]
            tmp4 = listok[8]
            tmp5 = listok[9]
            tmp6 = listok[10]
            listok[5] = listok[2]
            listok[6] = listok[3]
            listok[7] = listok[4]
            listok[2] = tmp4
            listok[3] = tmp5
            listok[4] = tmp6
            listok[8] = tmp1
            listok[9] = tmp2
            listok[10] = tmp3
            listok[2] = listok[3]
            listok[3] = listok[4]
            listok[4] = listok[6]
            listok[5] = listok[7]
            listok[6] = listok[9]
            listok[7] = listok[10]
            listok.pop()
            listok.pop()
            listok.pop()
            return listok
        else:
            if (listok[2] == 'arg3'): #  3  1   2
                tmp1 = listok[5]
                tmp2 = listok[6]
                tmp3 = listok[7]
                tmp4 = listok[2]
                tmp5 = listok[3]
                tmp6 = listok[4]
                listok[8] = listok[2]
                listok[9] = listok[3]
                listok[10] = listok[4]
                listok[2] = tmp1
                listok[3] = tmp2
                listok[4] = tmp3
                listok[8] = tmp4
                listok[9] = tmp5
                listok[10] = tmp6
                listok[2] = listok[3]
                listok[3] = listok[4]
                listok[4] = listok[6]
                listok[5] = listok[7]
                listok[6] = listok[9]
                listok[7] = listok[10]
                listok.pop()
                listok.pop()
                listok.pop()
                return listok
# check if for correct arguments
def check_arg_order(listok):
    if listok[1] == 'DEFVAR':
        return check_arg_1(listok)
    elif listok[1] == 'PUSHS':
        return check_arg_1(listok)
    elif listok[1] == 'POPS':
        return check_arg_1(listok)
    elif listok[1] == 'WRITE':
        return check_arg_1(listok)
    elif listok[1] == 'INT2CHAR':
        return check_arg_2(listok)
    elif listok[1] == 'MOVE':
        return check_arg_2(listok)
    elif listok[1] == 'LABEL':
        return check_arg_1(listok)
    elif listok[1] == 'CALL':
        return check_arg_1(listok)
    elif listok[1] == 'ADD':
        return check_arg_3(listok)
    elif listok[1] == 'SUB':
        return check_arg_3(listok)
    elif listok[1] == 'MUL':
        return check_arg_3(listok)
    elif listok[1] == 'IDIV':
        return check_arg_3(listok)
    elif listok[1] == 'LT':
        return check_arg_3(listok)
    elif listok[1] == 'GT':
        return check_arg_3(listok)
    elif listok[1] == 'EQ':
        return check_arg_3(listok)
    elif listok[1] == 'AND':
        return check_arg_3(listok)
    elif listok[1] == 'OR':
        return check_arg_3(listok)
    elif listok[1] == 'NOT':
        return check_arg_2(listok)
    elif listok[1] == 'STRI2INT':
        return check_arg_3(listok)
    elif listok[1] == 'READ':
        return check_arg_2(listok)
    elif listok[1] == 'CONCAT':
        return check_arg_3(listok)
    elif listok[1] == 'STRLEN':
        return check_arg_2(listok)
    elif listok[1] == 'GETCHAR':
        return check_arg_3(listok)
    elif listok[1] == 'SETCHAR':
        return check_arg_3(listok)
    elif listok[1] == 'JUMP':
        return check_arg_1(listok)
    elif listok[1] == 'EXIT':
        return check_arg_1(listok)
    elif listok[1] == 'TYPE':
        return check_arg_2(listok)
    elif listok[1] == 'JUMPIFEQ':
        return check_arg_3(listok)
    elif listok[1] == 'JUMPIFNEQ':
        return check_arg_3(listok) 
    elif listok[1] == 'DPRINT':
        return check_arg_1(listok)
    else:
        return listok

#assign into var
# open frame. append if var is not initialized
# change if var is initialized
def assign_into_var(value,variable):
    global global_frame,local_frame,temporary_frame
    split_str = variable.split('@')
    if (split_str[0] == 'GF'):
        for i in global_frame:
            if i[0] == split_str[1]:
                if len(i) == 2:
                    i[1] = value
                else:
                    i.append(value)
                return     
    elif (split_str[0] == 'TF'):
        if temporary_frame == 'undefined':
            sys.stderr.write("Working with undefined temporary frame \n")
            exit(55)
        for i in temporary_frame:
            if i[0] == split_str[1]:
                if len(i) == 2:
                    i[1] = value
                else:
                    i.append(value)
                return
    elif (split_str[0] == 'LF'):
        for i in local_frame:
            if i[0] == split_str[1]:
                if len(i) == 2:
                    i[1] = value
                else:
                    i.append(value)
                    return

#check for bool
def check_bool(argum):
    if (argum.get_value() == 'true'):
        return True
    elif (argum.get_value() == 'false'):
        return True
    else:
        sys.stderr.write("Invalid bool \n")
        exit(53)

# check for int
def check_int(argum):
    tmp = argum.get_value()
    for i in str(tmp):
        if ((i < '0')|(i > '9')):
            if i != '-':
                sys.stderr.write("Invalid integer \n")
                exit(32)
    return True

# assign from variable
# open frame. if var is not initialized then break
def assign_from_var(argum):
    global global_frame, local_frame, temporary_frame
    split_str = argum.get_value().split('@')
    if (split_str[0] == 'GF'):
        for i in global_frame:
            if i[0] == split_str[1]:
                if len(i) == 2:
                        return i[1]
                else:
                    sys.stderr.write("Work with uninitialized variable \n")
                    exit(56)
    elif (split_str[0] == 'TF'):
        if temporary_frame == 'undefined':
            sys.stderr.write("Working with undefined temporary frame \n")
            exit(55)
        for i in temporary_frame:
            if i[0] == split_str[1]:
                if len(i) == 2:
                        return i[1]
                else:
                    sys.stderr.write("Work with uninitialized variable \n")
                    exit(56)
    elif (split_str[0] == 'LF'):
        for i in local_frame:
            if i[0] == split_str[1]:
                if len(i) == 2:
                        return i[1]
                else:
                    sys.stderr.write("Work with uninitialized variable \n")
                    exit(56)

# check whther this is variable
def check_var(argument):
    global global_frame, local_frame, temporary_frame
    if (argument.get_typ() == 'var'):
        if (argument.get_value().count("@") != 1):
            sys.stderr.write("Invalid definition of variable \n")
            exit(52)
        split_str = argument.get_value().split('@')
        if (split_str[0] == 'GF'):
            for i in global_frame:
                if i[0] == split_str[1]:
                    return True
            sys.stderr.write("Work with uninitialized variable \n")
            exit(56)
        elif (split_str[0] == 'TF'):
            if temporary_frame == 'undefined':
                sys.stderr.write("Working with undefined temporary frame \n")
                exit(55)
            for i in temporary_frame:
                if i[0] == split_str[1]:
                    return True
            sys.stderr.write("Work with uninitialized variable \n")
            exit(56)
        elif (split_str[0] == 'LF'):
            for i in local_frame:
                if i[0] == split_str[1]:
                    return True
            sys.stderr.write("Work with uninitialized variable \n")
            exit(56)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)
    else:
        return False

# returns number without zeros 
def return_nonzero(arr):
    if ((arr[1] < '0')|(arr[1] > '9')):
        sys.stderr.write("Invalid backslash number \n")
        exit(53)
    if ((arr[2] < '0')|(arr[2] > '9')):
        sys.stderr.write("Invalid backslash number \n")
        exit(53)
    if ((arr[3] < '0')|(arr[3] > '9')):
        sys.stderr.write("Invalid backslash number \n")
        exit(53)
    if arr[1] == '0':
        if arr[2] =='0':
            if arr[3] == '0':
                return 000
            else:
                return arr[3]
        else:
            return arr[2] + arr[3]
    else:
        return arr[1] + arr[2] + arr[3]

# converts list to string
def listToString(s): 
    return "".join(s)

# check whther str is part of list of list
def is_part_of(arr,str):
    for i in arr:
        if str == i[0]:
            sys.stderr.write("Redefinition of variable \n")
            exit(52)

# class instruction

class Instruction:

    def __init__(self, opcode):
        self._opcode = opcode
        self._type: str
    
    def get_opcode(self):
        return self._opcode
    
    def get_num_arg(self):
        return self._num_arg

#class argument

class Argument:

    def __init__(self, order, typ, value):
        self._order = order
        self._typ = typ
        self._value = value

    def get_order(self):
        return self._order

    def get_typ(self):
        return self._typ
    
    def get_value(self):
        return self._value

# class with 0 arguemnts

class Instruct_0_arg(Instruction):
    def __init__(self, arr):
        if ((len(arr)-2 ) != 0 ):
            sys.stderr.write("Invalid number of arguments\n")
            exit(32)
        super().__init__(arr[1])
    
# class with 1 argument

class Instruct_1_arg(Instruction):
    def __init__(self, arr):
        if ((len(arr)-2) != 2):
            sys.stderr.write("Invalid number of arguments\n")
            exit(32)
        super().__init__(arr[1])
        self.Arg1 = Argument(1,arr[2],arr[3])

#class with 2 arguments

class Instruct_2_arg(Instruction):
    def __init__(self, arr):
        if ((len(arr)-2) != 4):
            sys.stderr.write("Invalid number of arguments\n")
            exit(32)
        super().__init__(arr[1])
        self.Arg1 = Argument(1,arr[2],arr[3])
        self.Arg2 = Argument(2,arr[4],arr[5])

#class with 3 arguments

class Instruct_3_arg(Instruction):
    def __init__(self, arr):
        if ((len(arr)-2) != 6):
            sys.stderr.write("Invalid number of arguments\n")
            exit(32)
        super().__init__(arr[1])
        self.Arg1 = Argument(1,arr[2],arr[3])
        self.Arg2 = Argument(2,arr[4],arr[5])
        self.Arg3 = Argument(3,arr[6],arr[7])

#move symbol into var
class Move(Instruct_2_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        #check for symbol in var
        # check if it is int bool or string
        move_value = ['undefined']
        global global_frame, local_frame, temporary_frame
        if (self.Arg2.get_typ() == 'var'):
            if (self.Arg2.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg2.get_value().split('@')
            if (split_str[0] == 'GF'):
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            move_value = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            elif (split_str[0] == 'TF'):
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            move_value = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            elif (split_str[0] == 'LF'):
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            move_value = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        elif (self.Arg2.get_typ() == 'int'):
            for i in self.Arg2.get_value():
                if ((i < '0')|(i > '9')):
                    if i != '-':
                        sys.stderr.write("Invalid integer \n")
                        exit(53)
            move_value = ['int',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'string'):
            move_value = ['string',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'bool'):
            if (self.Arg2.get_value() == 'true'):
                move_value = ['bool',self.Arg2.get_value()]
            elif (self.Arg2.get_value() == 'false'):
                move_value = ['bool',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid work with string \n")
                exit(53)
        elif (self.Arg2.get_typ() == 'nil'):
            if (self.Arg2.get_value() == 'nil'):
                move_value = ['nil',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid work with nil \n")
                exit(53)
        if len(move_value) == 1:
            sys.stderr.write("Invalid work with variable \n")
            exit(58)
        

        # try to find and assign into variable
        if (self.Arg1.get_typ() == 'var'):
            if (self.Arg1.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg1.get_value().split('@')
            if (split_str[0] == 'GF'):
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            i[1] = move_value
                        else:
                            i.append(move_value)
                        return     
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            elif (split_str[0] == 'TF'):
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            i[1] = move_value
                        else:
                            i.append(move_value)
                        return
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            elif (split_str[0] == 'LF'):
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            i[1] = move_value
                        else:
                            i.append(move_value)
                        return
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(53)

# creates empty temporary frame

class Createframe(Instruct_0_arg):

    def __init__(self,arr):
        super().__init__(arr)

    def exe(self):
        global temporary_frame 
        temporary_frame = []

# pushes temporary onto frame stack
# temporary frame is uninitialized

class Pushframe(Instruct_0_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global temporary_frame, frame_stack ,local_frame
        if temporary_frame == 'undefined':
            sys.stderr.write("Working with undefined temporary frame \n")
            exit(55)
        frame_stack.append(temporary_frame)
        local_frame = temporary_frame
        temporary_frame = 'undefined'

# pops frame stack into temporary frame

class Popframe(Instruct_0_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global temporary_frame, frame_stack , local_frame
        if not(local_frame):
            sys.stderr.write("Popframe with empty Local frame\n")
            exit(55)
        temporary_frame = local_frame
        if frame_stack:
            frame_stack.pop()
            local_frame = frame_stack[-1]
        else:
            local_frame = []

# defines new variable in frame
# var is unitialized

class Defvar(Instruct_1_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        if (self.Arg1.get_typ() != 'var'):
            sys.stderr.write("Defining nonvar \n")
            exit(52)
        else:
            if (self.Arg1.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg1.get_value().split('@')
            if (split_str[0] == 'GF'):
                global global_frame
                is_part_of(global_frame,split_str[1])
                global_frame.append([split_str[1]])
            elif (split_str[0] == 'LF'):
                global local_frame
                is_part_of(local_frame,split_str[1])
                local_frame.append([split_str[1]])
            elif (split_str[0] == 'TF'):
                global temporary_frame
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                is_part_of(temporary_frame,split_str[1])
                temporary_frame.append([split_str[1]])
            else:
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)

# jump onto label
# return executes next instruction

class Call_inst(Instruct_1_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global call_stack, instruction_pointer
        call_stack.append(instruction_pointer + 1)
    
        tmp_pointer = 0
        for i in instruction_list:
            if i.get_opcode() == 'LABEL':
                if i.Arg1.get_value() == self.Arg1.get_value():
                    instruction_pointer = tmp_pointer
                    return
            tmp_pointer += 1 
        sys.stderr.write("Undefined label \n")
        exit(52)

# returns back to label

class Return_inst(Instruct_0_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global call_stack, instruction_pointer
        if not call_stack:
            sys.stderr.write("Call stack is empty \n")
            exit(56)
        instruction_pointer = call_stack.pop()

# pushes value onto stack
# var has to be initialized

class Pushs(Instruct_1_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global data_stack
        if self.Arg1.get_typ() == 'var':
            if check_var(self.Arg1) == True:
                data_stack.append(assign_from_var(self.Arg1))
        else:
            data_stack.append([self.Arg1.get_typ(),self.Arg1.get_value()])

# pops value into variable

class Pops(Instruct_1_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global data_stack
        if not(data_stack):
            sys.stderr.write("Poping empty data stack\n")
            exit(56)
        else:
            if (self.Arg1.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg1.get_value().split('@')
            if (split_str[0] == 'GF'):
                global global_frame
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if (len(i)) == 1:
                            i.append(data_stack[-1])
                            data_stack.pop()
                        else:
                            i[1] = data_stack[-1]
                            data_stack.pop()
                        return
                sys.stderr.write("Poping to nonexisting variable \n")
                exit(56)
            elif (split_str[0] == 'LF'):
                global local_frame
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if (len(i)) == 1:
                            i.append(data_stack[-1])
                            data_stack.pop()
                        else:
                            i[1] = data_stack[-1]
                            data_stack.pop()
                        return
                sys.stderr.write("Poping to nonexisting variable \n")
                exit(56)
            elif (split_str[0] == 'TF'):
                global temporary_frame
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if (len(i)) == 1:
                            i.append(data_stack[-1])
                            data_stack.pop()
                        else:
                            i[1] = data_stack[-1]
                            data_stack.pop()
                        return
                sys.stderr.write("Poping to nonexisting variable \n")
                exit(56)
            else:
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)

# calculate add/sub/div/mul of operands
# operands have to be int
# if we are assigning from variable it must be initialized
# also variable that we are assigning into must be initialized

class Aritmetics(Instruct_3_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        global global_frame, local_frame, temporary_frame
        if (self.Arg2.get_typ() == 'var'):
            if (self.Arg2.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg2.get_value().split('@')
            if (split_str[0] == 'GF'):
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            symb1 = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            elif (split_str[0] == 'TF'):
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            symb1 = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            elif (split_str[0] == 'LF'):
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            symb1 = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        elif (self.Arg2.get_typ() == 'int'):
            if check_int(self.Arg2) == True:
                symb1 = ['int',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(56)

        symb2 = ['undefined']
        if (self.Arg3.get_typ() == 'var'):
            if (self.Arg3.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg3.get_value().split('@')
            if (split_str[0] == 'GF'):
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            symb2 = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            elif (split_str[0] == 'TF'):
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            symb2 = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            elif (split_str[0] == 'LF'):
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            symb2 = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        elif (self.Arg3.get_typ() == 'int'):
            if check_int(self.Arg3) == True:
                symb2 = ['int',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(56)

        if ((symb1[0]) != 'int') |  (symb2[0] != 'int'):
            sys.stderr.write("Invalid argument \n")
            exit(53)


        if (self.Arg1.get_typ() == 'var'):
            if (self.Arg1.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg1.get_value().split('@')
            if (split_str[0] == 'GF'):
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            if self.get_opcode() == 'ADD':
                                i[1][1] = int(symb1[1]) + int(symb2[1])
                            elif self.get_opcode() == 'SUB':
                                i[1][1] = int(symb1[1]) - int(symb2[1])
                            elif self.get_opcode() == 'MUL':
                                i[1][1] = int(symb1[1]) * int(symb2[1])
                            elif self.get_opcode() == 'IDIV':
                                if symb2[1] == 0:
                                    sys.stderr.write("Dividing by zero \n")
                                    exit(57)
                                i[1][1] = int(symb1[1]) // int(symb2[1])
                        else:
                            if self.get_opcode() == 'ADD':
                                i.append(['int',int(symb1[1]) + int(symb2[1])])
                            elif self.get_opcode() == 'SUB':
                                i.append(['int',int(symb1[1]) - int(symb2[1])])
                            elif self.get_opcode() == 'MUL':
                                i.append(['int',int(symb1[1]) * int(symb2[1])])
                            elif self.get_opcode() == 'IDIV':
                                if symb2[1] == '0':
                                    sys.stderr.write("Dividing by zero \n")
                                    exit(57)
                                i.append(['int',int(symb1[1]) // int(symb2[1])])
                        return     
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            elif (split_str[0] == 'TF'):
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            if self.get_opcode() == 'ADD':
                                i[1][1] = int(symb1[1]) + int(symb2[1])
                            elif self.get_opcode() == 'SUB':
                                i[1][1] = int(symb1[1]) - int(symb2[1])
                            elif self.get_opcode() == 'MUL':
                                i[1][1] = int(symb1[1]) * int(symb2[1])
                            elif self.get_opcode() == 'IDIV':
                                if symb2[1] == 0:
                                    sys.stderr.write("Dividing by zero \n")
                                    exit(57)
                                i[1][1] = int(symb1[1]) // int(symb2[1])
                        else:
                            if self.get_opcode() == 'ADD':
                                i.append(['int',int(symb1[1]) + int(symb2[1])])
                            elif self.get_opcode() == 'SUB':
                                i.append(['int',int(symb1[1]) - int(symb2[1])])
                            elif self.get_opcode() == 'MUL':
                                i.append(['int',int(symb1[1]) * int(symb2[1])])
                            elif self.get_opcode() == 'IDIV':
                                if symb2[1] == '0':
                                    sys.stderr.write("Dividing by zero \n")
                                    exit(57)
                                i.append(['int',int(symb1[1]) // int(symb2[1])])
                        return  
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            elif (split_str[0] == 'LF'):
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            if self.get_opcode() == 'ADD':
                                i[1][1] = int(symb1[1]) + int(symb2[1])
                            elif self.get_opcode() == 'SUB':
                                i[1][1] = int(symb1[1]) - int(symb2[1])
                            elif self.get_opcode() == 'MUL':
                                i[1][1] = int(symb1[1]) * int(symb2[1])
                            elif self.get_opcode() == 'IDIV':
                                if symb2[1] == 0:
                                    sys.stderr.write("Dividing by zero \n")
                                    exit(57)
                                i[1][1] = int(symb1[1]) // int(symb2[1])
                        else:
                            if self.get_opcode() == 'ADD':
                                i.append(['int',int(symb1[1]) + int(symb2[1])])
                            elif self.get_opcode() == 'SUB':
                                i.append(['int',int(symb1[1]) - int(symb2[1])])
                            elif self.get_opcode() == 'MUL':
                                i.append(['int',int(symb1[1]) * int(symb2[1])])
                            elif self.get_opcode() == 'IDIV':
                                if symb2[1] == '0':
                                    sys.stderr.write("Dividing by zero \n")
                                    exit(57)
                                i.append(['int',int(symb1[1]) // int(symb2[1])])
                        return  
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)

# compares 2 symbols depending
# 

class Comparison(Instruct_3_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        global global_frame, local_frame, temporary_frame
        if (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = assign_from_var(self.Arg2)
        elif (self.Arg2.get_typ() == 'int'):
            if (check_int(self.Arg2) == True):
                symb1 = ['int',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'string'):
            symb1 = ['string',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'bool'):
            if (check_bool(self.Arg2) == True):
                symb1 = ['bool',self.Arg2.get_value()]
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        symb2 = ['undefined']
        if (self.Arg3.get_typ() == 'var'):
            if (check_var(self.Arg3) == True):
                symb2 = assign_from_var(self.Arg3)
        elif (self.Arg3.get_typ() == 'int'):
            if (check_int(self.Arg3) == True):
                symb2 = ['int',self.Arg3.get_value()]
        elif (self.Arg3.get_typ() == 'string'):
            symb2 = ['string',self.Arg3.get_value()]
        elif (self.Arg3.get_typ() == 'bool'):
            if (check_bool(self.Arg3) == True):
                symb2 = ['bool',self.Arg3.get_value()]
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)


        if (type(symb1) != type(symb2)):
            sys.stderr.write("Invalid type of operands \n")
            exit(53)

        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                if self.get_opcode() == 'GT':
                    if ((symb1[1] == 'true' )|( symb1[1] == 'false'))&((symb2[1] == 'true' )|( symb2[1] == 'false')):
                        if (symb1[1] == 'true') & (symb2[1] == 'false'):
                            assign_into_var(['bool','true'],self.Arg1.get_value())
                        else:
                            assign_into_var(['bool','false'],self.Arg1.get_value())
                    elif (symb1[1] > symb2[1]):
                        assign_into_var(['bool','true'],self.Arg1.get_value())
                    else:
                        assign_into_var(['bool','false'],self.Arg1.get_value())
                if self.get_opcode() == 'LT':
                    if ((symb1[1] == 'true' )|( symb1[1] == 'false'))&((symb2[1] == 'true' )|( symb2[1] == 'false')):
                        if (symb1[1] == 'false') & (symb2[1] == 'true'):
                            assign_into_var(['bool','true'],self.Arg1.get_value())
                        else:
                            assign_into_var(['bool','false'],self.Arg1.get_value())
                    elif (symb1[1] < symb2[1]):
                        assign_into_var(['bool','true'],self.Arg1.get_value())
                    else:
                        assign_into_var(['bool','false'],self.Arg1.get_value())
                if self.get_opcode() == 'EQ':
                    if (symb1[1] == symb2[1]):
                        assign_into_var(['bool','true'],self.Arg1.get_value())
                    else:
                        assign_into_var(['bool','false'],self.Arg1.get_value())

# creates logical operation with 2 boolean  values 

class Andor(Instruct_3_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        global global_frame, local_frame, temporary_frame
        if (self.Arg2.get_typ() == 'bool'):
            if (check_bool(self.Arg2) == True):
                symb1 = ['bool',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = assign_from_var(self.Arg2)
                if (symb1 != 'true') &(symb1 != 'false'):
                    sys.stderr.write("Invalid bool \n")
                    exit(58)
        else:
            sys.stderr.write("Invalid bool \n")
            exit(58)

        symb2 = ['undefined']
        if (self.Arg3.get_typ() == 'bool'):
            if (check_bool(self.Arg3) == True):
                symb2 = ['bool',self.Arg3.get_value()]
        elif (self.Arg3.get_typ() == 'var'):
            if (check_var(self.Arg3) == True):
                symb2 = assign_from_var(self.Arg3)
                if (symb2 != 'true') &(symb2 != 'false'):
                    sys.stderr.write("Invalid bool \n")
                    exit(58)
        else:
            sys.stderr.write("Invalid bool \n")
            exit(58)

        if (symb1[0] != 'bool')| (symb2[0] != 'bool'):
            sys.stderr.write("Invalid type of operands \n")
            exit(53)
        
        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                if self.get_opcode() == 'AND':
                    if (symb1[1] == 'true')& (symb1[1] == symb2[1]):
                        assign_into_var(['bool','true'],self.Arg1.get_value())
                    else:
                        assign_into_var(['bool','false'],self.Arg1.get_value())
                else:
                    if (symb1[1] == 'false')& (symb1[1] == symb2[1]):
                        assign_into_var(['bool','false'],self.Arg1.get_value())
                    else:
                        assign_into_var(['bool','true'],self.Arg1.get_value())

# not boolean operation

class Not_inst(Instruct_2_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        global global_frame, local_frame, temporary_frame
        if (self.Arg2.get_typ() == 'bool'):
            if (check_bool(self.Arg2) == True):
                symb1 = ['bool',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = ['bool',assign_from_var(self.Arg2)]
                if (symb1 != 'true') &(symb1 != 'false'):
                    sys.stderr.write("Invalid bool \n")
                    exit(58)
        else:
            sys.stderr.write("Invalid bool \n")
            exit(58)

        if (symb1[0] != 'bool'):
            sys.stderr.write("Invalid type of operands \n")
            exit(53)
        
        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                if symb1[1] == 'true':
                    assign_into_var(['bool','false'],self.Arg1.get_value())
                else:
                    assign_into_var(['bool','true'],self.Arg1.get_value())
            else:
                sys.stderr.write("Invalid variable \n")
                exit(53)

class Int2char(Instruct_2_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        ascii_value = ['undefined']
        global global_frame, local_frame, temporary_frame
        if (self.Arg2.get_typ() == 'var'):
            if (self.Arg2.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg2.get_value().split('@')
            if (split_str[0] == 'GF'):
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            ascii_value = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            elif (split_str[0] == 'TF'):
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            ascii_value = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            elif (split_str[0] == 'LF'):
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            ascii_value = i[1]
                        else:
                            sys.stderr.write("Work with uninitialized variable \n")
                            exit(56)
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        elif (self.Arg2.get_typ() == 'int'):
            check_int(self.Arg2)
            ascii_value = ['int',self.Arg2.get_value()]
        
        if ascii_value[0] != 'int':
            sys.stderr.write("Invalid integer \n")
            exit(58)


        if (self.Arg1.get_typ() == 'var'):
            if (self.Arg1.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg1.get_value().split('@')
            if (split_str[0] == 'GF'):
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            i[1] = ['string',chr(int(ascii_value[1]))]
                        else:
                            i.append(['string',chr(int(ascii_value[1]))])
                        return     
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            elif (split_str[0] == 'TF'):
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            i[1] = ['string',chr(int(ascii_value[1]))]
                        else:
                            i.append(['string',chr(int(ascii_value[1]))])
                        return  
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            elif (split_str[0] == 'LF'):
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            i[1] = ['string',chr(int(ascii_value[1]))]
                        else:
                            i.append(['string',chr(int(ascii_value[1]))])
                        return  
                sys.stderr.write("Using undefined variable \n")
                exit(54)
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)

# converts string on given index into ascii value


class Str2int(Instruct_3_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        global global_frame, local_frame, temporary_frame
        if (self.Arg2.get_typ() == 'string'):
            symb1 = ['string',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = assign_from_var(self.Arg2)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        symb2 = ['undefined']
        if (self.Arg3.get_typ() == 'int'):
            if check_int(self.Arg3) == True:
                symb2 = ['int',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg3.get_typ() == 'var'):
            if (check_var(self.Arg3) == True):
                for i in str(assign_from_var(self.Arg3)):
                    if ((i < '0')|(i > '9')):
                        if i != '-':
                            sys.stderr.write("Invalid integer \n")
                            exit(58)
                    symb2 = assign_from_var(self.Arg3)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if (symb1[0] != 'string')|(symb2[0] != 'int'):
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                if (int(symb2[1]) > len(symb1[1])-1):
                    sys.stderr.write("Invalid index \n")
                    exit(58)
                else:
                    assign_into_var(['int',ord(symb1[1][int(symb2[1])])],self.Arg1.get_value())
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)

# write given value out
# given value does not give \n

class Write(Instruct_1_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        if (self.Arg1.get_typ() == 'var'):
            if (self.Arg1.get_value().count("@") != 1):
                sys.stderr.write("Invalid definition of variable \n")
                exit(52)
            split_str = self.Arg1.get_value().split('@')
            if (split_str[0] == 'GF'):
                global global_frame
                for i in global_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            print(i[1][1],end='')
                            return
                        else:
                            sys.stderr.write("Printing of uninitialized variable \n")
                            exit(56)
                sys.stderr.write("Printing of undefined variable \n")
                exit(54)
            elif (split_str[0] == 'TF'):
                global temporary_frame
                if temporary_frame == 'undefined':
                    sys.stderr.write("Working with undefined temporary frame \n")
                    exit(55)
                for i in temporary_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            print(i[1][1],end='')
                            return
                        else:
                            sys.stderr.write("Printing of uninitialized variable \n")
                            exit(56)
                sys.stderr.write("Printing of undefined variable \n")
                exit(54)
            elif (split_str[0] == 'LF'):
                global local_frame
                for i in local_frame:
                    if i[0] == split_str[1]:
                        if len(i) == 2:
                            print(i[1][1],end='')
                            return
                        else:
                            sys.stderr.write("Printing of uninitialized variable \n")
                            exit(56)
                sys.stderr.write("Printing of undefined variable \n")
                exit(54)
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)    
        elif (self.Arg1.get_typ() == 'int'):
            for i in self.Arg1.get_value():
                if ((i < '0')|(i > '9')):
                    if i != '-':
                        sys.stderr.write("Invalid integer \n")
                        exit(53)
            print(self.Arg1.get_value(),end='')
        elif (self.Arg1.get_typ() == 'bool'):
            if (self.Arg1.get_value() == 'true'):
                print('true',end='')
            elif (self.Arg1.get_value() == 'false'):
                print('false',end='')
            else:
                sys.stderr.write("Invalid bool \n")
                exit(53)
        elif (self.Arg1.get_typ() == 'nil'):
            if (self.Arg1.get_value() == 'nil'):
                print('',end='')
            else:
                sys.stderr.write("Invalid nil \n")
                exit(53)
        elif (self.Arg1.get_typ() == 'string'):
            code_slash=[]
            for i in self.Arg1.get_value():
                if (ord(i) == 92):
                    if (len(code_slash) == 4):
                        print(chr(int(return_nonzero(code_slash))),end='')
                        code_slash=[]
                        code_slash.append(i)
                    else:
                        code_slash.append(i)
                        continue
                elif (len(code_slash) == 4):
                    print(chr(int(return_nonzero(code_slash))),end='')
                    print(i,end='')
                    code_slash=[]
                elif (len(code_slash) != 0):
                    code_slash.append(i)
                    continue
                else:
                    print(i,end='')
                    
        else:
            sys.stderr.write("Invalid type \n")
            exit(52)

# read one line from input 
# save input to the variable

class Read(Instruct_2_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        if (self.Arg2.get_typ() == 'type'):
            if (self.Arg2.get_value() == 'int')|(self.Arg2.get_value() == 'string')|(self.Arg2.get_value() == 'bool'):
                tmp = input_file.readline()
                tmp = list(tmp)
                if (tmp[-1] == '\n'):
                    tmp.pop()
                tmp="".join(tmp)
                symb1 = [self.Arg2.get_value(),tmp]
            else:
                sys.stderr.write("Invalid type \n")
                exit(52)
            if (self.Arg2.get_value() == 'int'):
                for i in symb1[1]:
                    if ((i < '0')|(i > '9')):
                        if i != '-':
                            symb1 = ['nil','nil']
            elif (self.Arg2.get_value() == 'bool'):
                if (symb1[1].upper() == 'TRUE'):
                    symb1 = ['bool','true']
                else:
                    symb1 = ['bool','false']
        else:
            sys.stderr.write("Invalid type \n")
            exit(52)

        global global_frame, local_frame, temporary_frame   
        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                assign_into_var(symb1,self.Arg1.get_value())
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)

# concatenate two symmbols and save it into variable

class Concat(Instruct_3_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        if (self.Arg2.get_typ() == 'string'):
            symb1 = ['string',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = assign_from_var(self.Arg2)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        symb2 = ['undefined']
        if (self.Arg3.get_typ() == 'string'):
            symb2 = ['string',self.Arg3.get_value()]
        elif (self.Arg3.get_typ() == 'var'):
            if (check_var(self.Arg3) == True):
                symb2 = assign_from_var(self.Arg3)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if (symb1[0] == 'string')|(symb2[0] == 'string'):
            sys.stderr.write("Invalid symbol \n")
            exit(58)
        symb3 = str(symb1[1])+str(symb2[1])

        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                assign_into_var(['string',symb3],self.Arg1.get_value())
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)
        
# saves string len into variable

class Str__len(Instruct_2_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        if (self.Arg2.get_typ() == 'string'):
            symb1 = ['string',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = assign_from_var(self.Arg2)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if symb1[0] != 'string':
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                assign_into_var(['int',len(str(symb1[1]))],self.Arg1.get_value())
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)

# get character on given index

class Getchar(Instruct_3_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        symb1 = ['undefined']
        global global_frame, local_frame, temporary_frame
        if (self.Arg2.get_typ() == 'string'):
            symb1 = ['string',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = assign_from_var(self.Arg2)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        symb2 = ['undefined']
        if (self.Arg3.get_typ() == 'int'):
            if check_int(self.Arg3) == True:
                symb2 = ['int',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg3.get_typ() == 'var'):
            if (check_var(self.Arg3) == True):
                for i in str(assign_from_var(self.Arg3)[1]):
                    if ((i < '0')|(i > '9')):
                        if i != '-':
                            sys.stderr.write("Invalid integer \n")
                            exit(58)
                    symb2 = assign_from_var(self.Arg3)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if (symb1[0] != 'string')|(symb2[0] != 'int'):
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                if (int(symb2[1]) > len(symb1[1])-1):
                    sys.stderr.write("Invalid index \n")
                    exit(58)
                else:
                    assign_into_var(symb1[1][int(symb2[1])],self.Arg1.get_value())
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)

# setchar on given index 

class Setchar(Instruct_3_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):

        global global_frame, local_frame, temporary_frame

        symb1 = ['undefined']
        if (self.Arg2.get_typ() == 'int'):
            if check_int(self.Arg2) == True:
                symb1 = ['int',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                for i in str(assign_from_var(self.Arg2)[1]):
                    if ((i < '0')|(i > '9')):
                        if i != '-':
                            sys.stderr.write("Invalid integer \n")
                            exit(58)
                    symb1 = assign_from_var(self.Arg2)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        symb2 = ['undefined']
        if (self.Arg3.get_typ() == 'string'):
            symb2 = ['string',self.Arg3.get_value()]
        elif (self.Arg3.get_typ() == 'var'):
            if (check_var(self.Arg3) == True):
                symb2 = assign_from_var(self.Arg3)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if (symb1[0] !='int')|(symb2[0] != 'string'):
            sys.stderr.write("Invalid symbol \n")
            exit(58)

        if (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                if (int(symb1[1]) > len(assign_from_var(self.Arg1)[1])-1):
                    sys.stderr.write("Invalid index \n")
                    exit(58)
                else:
                    tmp = list(assign_from_var(self.Arg1)[1])
                    if not symb2[1]:
                        sys.stderr.write("Invalid index \n")
                        exit(58)
                    tmp[int(symb1[1])] = symb2[1][0]
                    tmp = "".join(tmp)
                    assign_into_var(['string',tmp],self.Arg1.get_value())
            else:
                sys.stderr.write("Invalid variable \n")
                exit(52)
        else:
            sys.stderr.write("Invalid variable \n")
            exit(52)

# save type into variable of given value

class Type(Instruct_2_arg):
    def __init__(self, arr):
        super().__init__(arr)


    def exe(self):

        check_var(self.Arg1)

        global global_frame,local_frame,temporary_frame
        if (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):          
                split_str = self.Arg2.get_value().split('@')
                if (split_str[0] == 'GF'):
                    for i in global_frame:
                        if i[0] == split_str[1]:
                            if len(i) == 2:
                                assign_into_var(['string',i[1][0]],self.Arg1.get_value())
                            else:
                                assign_into_var(['string',''],self.Arg1.get_value())
                elif (split_str[0] == 'TF'):
                    if temporary_frame == 'undefined':
                        sys.stderr.write("Working with undefined temporary frame \n")
                        exit(55)
                    for i in temporary_frame:
                        if i[0] == split_str[1]:
                            if len(i) == 2:
                                assign_into_var(['string',i[1][0]],self.Arg1.get_value())
                            else:
                                assign_into_var(['string',''],self.Arg1.get_value())
                elif (split_str[0] == 'LF'):
                    for i in local_frame:
                        if i[0] == split_str[1]:
                            if len(i) == 2:
                                assign_into_var(['string',i[1][0]],self.Arg1.get_value())
                            else:
                                assign_into_var(['string',''],self.Arg1.get_value())
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        elif (self.Arg2.get_typ() == 'string'):
            assign_into_var(['string','string'],self.Arg1.get_value())
        elif (self.Arg2.get_typ() == 'bool'):
            assign_into_var(['string','bool'],self.Arg1.get_value())
        elif (self.Arg2.get_typ() == 'int'):
            assign_into_var(['string','int'],self.Arg1.get_value())
        elif (self.Arg2.get_typ() == 'nil'):
            assign_into_var(['string','nil'],self.Arg1.get_value())
        else:
            sys.stderr.write("Invalid type \n")
            exit(52)

# set label to instruction call

class Label(Instruct_1_arg):

    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global instruction_list
        num_of_label = 0
        for i in instruction_list:
            if i.get_opcode() == 'LABEL':
                if i.Arg1.get_typ() != 'label':
                    sys.stderr.write("Invalid argument for label \n")
                    exit(52)
                if (i.Arg1.get_value() == self.Arg1.get_value()):
                    num_of_label += 1
        if num_of_label > 1 :
            sys.stderr.write("Calling 2 same labels \n")
            exit(52)
        
# jump to given label

class Jump(Instruct_1_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        if self.Arg1.get_typ() != 'label':
            sys.stderr.write("Invalid argument for jump \n")
            exit(52)
        global instruction_list, instruction_pointer
        num_of_label = 0
        for i in instruction_list:
            if i.get_opcode() == 'LABEL':
                if (i.Arg1.get_value() == self.Arg1.get_value()):
                    instruction_pointer = num_of_label
                    return
            num_of_label += 1
        sys.stderr.write("Invalid label for jumpifeq \n")
        exit(52)

# jump to given label if two values are equal

class Jumpifeq(Instruct_3_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global global_frame, local_frame, temporary_frame

        symb1 = ['undefined']
        if (self.Arg2.get_typ() == 'int'):
            if check_int(self.Arg2) == True:
                symb1 = ['int',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = assign_from_var(self.Arg2)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        elif (self.Arg2.get_typ() == 'bool'):
            if check_bool(self.Arg2) == True:
                symb1 = ['bool',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid bool \n")
                exit(58)
        elif (self.Arg2.get_typ() == 'string'):
            symb1 = ['string',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'nil'):
            if self.Arg2.get_value() == 'nil':
                symb1 = ['nil',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid nil \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(53)

        symb2 = ['undefine']
        if (self.Arg3.get_typ() == 'int'):
            if check_int(self.Arg3) == True:
                symb2 = ['int',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg3.get_typ() == 'var'):
            if (check_var(self.Arg3) == True):
                symb2 = assign_from_var(self.Arg3)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        elif (self.Arg3.get_typ() == 'bool'):
            if check_bool(self.Arg3) == True:
                symb2 = ['bool',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid bool \n")
                exit(58)
        elif (self.Arg3.get_typ() == 'string'):
            symb2 = ['string',self.Arg3.get_value()]
        elif (self.Arg3.get_typ() == 'nil'):
            if self.Arg3.get_value() == 'nil':
                symb2 = ['nil',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid nil \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(53)

        if (symb1[0] == symb2[0])&(int(symb1[1]) == int(symb2[1])):
            if self.Arg1.get_typ() != 'label':
                sys.stderr.write("Invalid argument for jumpifeq \n")
                exit(52)
            global instruction_list, instruction_pointer
            num_of_label = 0
            for i in instruction_list:
                if i.get_opcode() == 'LABEL':
                    
                    if (i.Arg1.get_value() == self.Arg1.get_value()):
                        instruction_pointer = num_of_label
                        return
                num_of_label += 1
            sys.stderr.write("Invalid label for jumpifeq \n")
            exit(52)

class Jumpifneq(Instruct_3_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global global_frame, local_frame, temporary_frame

        symb1 = ['undefined']
        if (self.Arg2.get_typ() == 'int'):
            if check_int(self.Arg2) == True:
                symb1 = ['int',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg2.get_typ() == 'var'):
            if (check_var(self.Arg2) == True):
                symb1 = assign_from_var(self.Arg2)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        elif (self.Arg2.get_typ() == 'bool'):
            if check_bool(self.Arg2) == True:
                symb1 = ['bool',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid bool \n")
                exit(58)
        elif (self.Arg2.get_typ() == 'string'):
            symb1 = ['string',self.Arg2.get_value()]
        elif (self.Arg2.get_typ() == 'nil'):
            if self.Arg2.get_value() == 'nil':
                symb1 = ['nil',self.Arg2.get_value()]
            else:
                sys.stderr.write("Invalid nil \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(53)

        symb2 = ['undefine']
        if (self.Arg3.get_typ() == 'int'):
            if check_int(self.Arg3) == True:
                symb2 = ['int',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg3.get_typ() == 'var'):
            if (check_var(self.Arg3) == True):
                symb2 = assign_from_var(self.Arg3)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        elif (self.Arg3.get_typ() == 'bool'):
            if check_bool(self.Arg3) == True:
                symb2 = ['bool',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid bool \n")
                exit(58)
        elif (self.Arg3.get_typ() == 'string'):
            symb2 = ['string',self.Arg3.get_value()]
        elif (self.Arg3.get_typ() == 'nil'):
            if self.Arg3.get_value() == 'nil':
                symb2 = ['nil',self.Arg3.get_value()]
            else:
                sys.stderr.write("Invalid nil \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(53)

        if (symb1[0] != symb2[0])|(int(symb1[1]) != int(symb2[1])):
            if self.Arg1.get_typ() != 'label':
                sys.stderr.write("Invalid argument for jumpifeq \n")
                exit(52)
            global instruction_list, instruction_pointer
            num_of_label = 0
            for i in instruction_list:
                if i.get_opcode() == 'LABEL':
                    if (i.Arg1.get_value() == self.Arg1.get_value()):
                        instruction_pointer = num_of_label
                        return
                num_of_label += 1
            sys.stderr.write("Invalid label for jumpifeq \n")
            exit(52)

# exit with exit code

class Exit(Instruct_1_arg):
    def __init__(self, arr):
        super().__init__(arr)
    def exe(self):
        symb1 = ['undefined']
        if (self.Arg1.get_typ() == 'int'):
            if check_int(self.Arg1) == True:
                symb1 = ['int',self.Arg1.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                for i in str(assign_from_var(self.Arg1)[1]):
                    if ((i < '0')|(i > '9')):
                        if i != '-':
                            sys.stderr.write("Invalid integer \n")
                            exit(58)
                    symb1 = assign_from_var(self.Arg1)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(58)
        if (int(symb1[1]) < 0)|(int(symb1[1]) > 49):
            sys.stderr.write("Invalid exit code \n")
            exit(57)
        exit(int(symb1[1]))

# print to stderr

class Dprint(Instruct_1_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global global_frame, local_frame, temporary_frame

        symb1 = ['undefined']
        if (self.Arg1.get_typ() == 'int'):
            if check_int(self.Arg1) == True:
                symb1 = ['int',self.Arg1.get_value()]
            else:
                sys.stderr.write("Invalid integer \n")
                exit(58)
        elif (self.Arg1.get_typ() == 'var'):
            if (check_var(self.Arg1) == True):
                symb1 = assign_from_var(self.Arg1)
            else:
                sys.stderr.write("Invalid symbol \n")
                exit(58)
        elif (self.Arg1.get_typ() == 'bool'):
            if check_bool(self.Arg1) == True:
                symb1 = ['bool',self.Arg1.get_value()]
            else:
                sys.stderr.write("Invalid bool \n")
                exit(58)
        elif (self.Arg1.get_typ() == 'string'):
            symb1 = ['string',self.Arg1.get_value()]
        elif (self.Arg1.get_typ() == 'nil'):
            if self.Arg1.get_value() == 'nil':
                symb1 = ['nil',self.Arg1.get_value()]
            else:
                sys.stderr.write("Invalid nil \n")
                exit(58)
        else:
            sys.stderr.write("Invalid symbol \n")
            exit(53)
        
        sys.stderr.write(symb1[1])

# print frames instructions

class Break(Instruct_0_arg):
    def __init__(self, arr):
        super().__init__(arr)

    def exe(self):
        global global_frame,local_frame,temporary_frame,instruction_list,instruction_pointer,int_order
        if temporary_frame == 'undefined':
            sys.stderr.write("Working with undefined temporary frame \n")
            exit(55)
        print("Global frame:",global_frame)
        print("Local frame:",local_frame)
        print("Temporary frame:",temporary_frame)
        print("Instructions executed so far:",int_order)
        if len(instruction_list)> instruction_pointer+1:
            print("Next instruction executed:",instruction_list[instruction_pointer+1].get_opcode())
        print("Instructions executed so far:",int_order)
        if -1 < instruction_pointer-1:
            print("Previous instruction executed:",instruction_list[instruction_pointer-1].get_opcode())
            
################## SPRACOVANIE ARGUMENTOV ########################
aparser = argparse.ArgumentParser(description="Program interprets XML code")
aparser.add_help=True
aparser.add_argument('--source', type=str,nargs=1, help="source XML file")
aparser.add_argument("--input", type=str,nargs=1, help="file with inputs for interpret") 
args = aparser.parse_args()

if ((args.input == None )&( args.source == None)):
    sys.stderr.write("At least one argument must be given.\nFor more info use --help argument\n")
    exit(10)
elif ((args.input != None )&( args.source == None)):
    #### prevedie si stdin na string a ten posle dalej inputu. 
    #### z toho vznikne root
    str_tmp = ""
    for line in sys.stdin:
        str_tmp = str_tmp + line
    try:
        root = ET.fromstring(str_tmp)
    except:
        traceback.print_exc()
        sys.exit(31)
    root = ET.fromstring(str_tmp)
    try:
        input_file = open(listToString(args.input),"r")
    except:
        traceback.print_exc()
        sys.exit(32)
    input_file = open(listToString(args.input),"r")
elif ((args.input == None )&( args.source != None)):
    #### otvori si subor a z neho vytvori root
    try:
        tree = ET.parse(listToString(args.source))
    except:
        traceback.print_exc()
        sys.exit(31)
    tree = ET.parse(listToString(args.source))
    root = tree.getroot()
    input_file = sys.stdin
elif ((args.input != None )&( args.source != None)):
    try:
        tree = ET.parse(listToString(args.source))
    except:
        traceback.print_exc()
        sys.exit(31)
    tree = ET.parse(listToString(args.source))
    root = tree.getroot()
    try:
        input_file = open(listToString(args.input),"r")
    except:
        traceback.print_exc()
        sys.exit(31)
    input_file = open(listToString(args.input),"r")
################################################################

######################### praca s xml ##########################
### kontrola ci je root program
if (root.tag != "program"):
    sys.stderr.write("Expecting root tag as 'program'.\n")
    exit(32)
if not root.attrib.keys():
    sys.stderr.write("Expecting attributes in 'program'.\n")
    exit(32)
if not root.attrib.get('language'):
    sys.stderr.write("Expecting language attrib in 'program'.\n")
    exit(32)
if root.attrib.get('language') != 'IPPcode22':
    sys.stderr.write("Expecting language IPPcode22 in 'program'.\n")
    exit(32)
### kontrola ci su v programe len instructions
for child in root:
    if (child.tag != "instruction" ):
        sys.stderr.write("Expexting only instructions inside root.\n")
        exit(32)
    atribs = list(child.attrib.keys())
### instructions musia mat spravne atributy
    if not("opcode" in atribs) and not ("order" in atribs) :
        sys.stderr.write("Wrong attributes in instruction.\n")
        exit(32)
### argumenty mozu byt maxximalne 3
    for grandchild in child:
        if not(re.match(r"arg[123]", grandchild.tag)):
            sys.stderr.write("Wrong argument for instruction.\n")
            exit(32)
### atributy argumentu mozu byt len type
        atribs = list(grandchild.attrib.keys())
        if not("type" in atribs) :
            sys.stderr.write("Wrong attributes in instruction.\n")
            exit(32)

# temporary list for help
first_list = []

# data structures we are working with
global_frame = []
local_frame = []
temporary_frame = 'undefined'
frame_stack = []
data_stack = []
call_stack = []

# get all instructions with their order and their arguments
for child in root:
    tmp = []
    if not child.attrib.get('order'):
        sys.stderr.write("No order found.\n")
        exit(32)
    for i in child.attrib.get('order'):
        if (i < '0')|(i > '9'):
            sys.stderr.write("Expecting int as order.\n")
            exit(32)
    tmp.append(child.attrib.get('order'))
    if not child.attrib.get('opcode'):
        sys.stderr.write("No opcode found.\n")
        exit(32)
    tmp.append(child.attrib.get('opcode').upper())
    for grandchild in child: 
        tmp.append(grandchild.tag)
        tmp.append(grandchild.attrib.get('type'))
        tmp.append(grandchild.text)
    first_list.append(tmp)
#sort them by their order
first_list.sort(key=lambda x: int(x[0]))
last_order = -1 
i = 0
while i < len(first_list):
    if int(first_list[i][0]) < 1:
        sys.stderr.write("Wrong order of instruction.\n")
        exit(32)
    if first_list[i][0] == last_order:
        sys.stderr.write("Wrong order of instruction.\n")
        exit(32)
    last_order = first_list[i][0]
    # put them in correct order
    first_list[i] = check_arg_order(first_list[i])
    i += 1


# execute given instruction
# instruction itself checks for correct number of arg
instruction_list= []

for inst in first_list:
    if inst[1] == 'CREATEFRAME':
        i = Createframe(inst)
    elif inst[1] == 'PUSHFRAME':
        i = Pushframe(inst)
    elif inst[1] == 'POPFRAME':
        i = Popframe(inst)
    elif inst[1] == 'DEFVAR':
        i = Defvar(inst)
    elif inst[1] == 'PUSHS':
        i = Pushs(inst)
    elif inst[1] == 'POPS':
        i = Pops(inst)
    elif inst[1] == 'WRITE':
        i = Write(inst)
    elif inst[1] == 'INT2CHAR':
        i = Int2char(inst)
    elif inst[1] == 'MOVE':
        i = Move(inst)
    elif inst[1] == 'LABEL':
        i = Label(inst)
    elif inst[1] == 'CALL':
        i = Call_inst(inst)
    elif inst[1] == 'RETURN':
        i = Return_inst(inst)
    elif inst[1] == 'ADD':
        i = Aritmetics(inst)
    elif inst[1] == 'SUB':
        i = Aritmetics(inst)
    elif inst[1] == 'MUL':
        i = Aritmetics(inst)
    elif inst[1] == 'IDIV':
        i = Aritmetics(inst)
    elif inst[1] == 'LT':
        i = Comparison(inst)
    elif inst[1] == 'GT':
        i = Comparison(inst)
    elif inst[1] == 'EQ':
        i = Comparison(inst)
    elif inst[1] == 'AND':
        i = Andor(inst)
    elif inst[1] == 'OR':
        i = Andor(inst)
    elif inst[1] == 'NOT':
        i = Not_inst(inst)
    elif inst[1] == 'STRI2INT':
        i = Str2int(inst)
    elif inst[1] == 'READ':
        i = Read(inst)
    elif inst[1] == 'CONCAT':
        i = Concat(inst)
    elif inst[1] == 'STRLEN':
        i = Str__len(inst)
    elif inst[1] == 'GETCHAR':
        i = Getchar(inst)
    elif inst[1] == 'SETCHAR':
        i = Setchar(inst)
    elif inst[1] == 'JUMP':
        i = Jump(inst)
    elif inst[1] == 'EXIT':
        i = Exit(inst)
    elif inst[1] == 'TYPE':
        i = Type(inst)
    elif inst[1] == 'JUMPIFEQ':
        i = Jumpifeq(inst)
    elif inst[1] == 'JUMPIFNEQ':
        i = Jumpifneq(inst)   
    elif inst[1] == 'DPRINT':
        i = Dprint(inst)
    elif inst[1] == 'BREAK':
        i = Break(inst)
    else:
        sys.stderr.write("Invalid instruction.\n")
        exit(32) 
    instruction_list.append(i)


# execute through cycle
instruction_pointer = 0
int_order=0
while instruction_pointer < len(instruction_list):
    instruction_list[instruction_pointer].exe()
    instruction_pointer +=1
    int_order += 1

class X:
    def __init__(self, name):
        self.name = name
        print("Object name:", self.name)
        print("Class name:", self.__class__.__name__)

    def execute(self, **kwargs):
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))
        print("Object name:", self.name)
        print("Class name:", self.__class__.__name__)

    def shutdown(self):
        print("Object name:", self.name)
        print("Class name:", self.__class__.__name__)


class A(X):
    obj_count = 0
    class_counter = 0

    def __init__(self, name):
        super(A, self).__init__(name)
        A.class_counter += 1

    def execute(self, **kwargs):
        super(A, self).execute(**kwargs)
        self.obj_count += 1
        print("Object Execute counter:", self.obj_count)


class B(X):
    obj_count = 0
    class_counter = 0

    def __init__(self, name):
        super(B, self).__init__(name)
        B.class_counter += 1

    def execute(self, **kwargs):
        super(B, self).execute(**kwargs)
        self.obj_count += 1
        print("Object Execute counter:", self.obj_count)


class C(X):
    obj_count = 0
    class_counter = 0

    def __init__(self, name):
        super(C, self).__init__(name)
        C.class_counter += 1

    def execute(self, **kwargs):
        super(C, self).execute(**kwargs)
        self.obj_count += 1
        print("Object Execute counter:", self.obj_count)


# c_1 = C('Object C_1')
# c_1.execute(name='chintan', surname='dave')
# c_1.shutdown()
# c_2 = C('Object C_2')
#
# print("Class counter:", C.class_counter)

def obj_name_input_and_checker():
    exist_flag = True
    while exist_flag:
        exist_flag = False
        obj_name = input("Write a name of this object: ")
        # Check if the name collides with ohter names
        for obj in objects_list:
            if obj.name == obj_name:
                print("This name already exists! Please choose a unique name for this object")
                exist_flag = True
                break

        if not exist_flag:
            break

    return obj_name


def create_object(objects_list):
    class_name = input("Choose a Class - ['A','B','C']: ")

    if class_name == 'A':
        obj_name = obj_name_input_and_checker()
        a = A(obj_name)
        objects_list.append(a)
    elif class_name == 'B':
        obj_name = obj_name_input_and_checker()
        b = B(obj_name)
        objects_list.append(b)
    elif class_name == 'C':
        obj_name = obj_name_input_and_checker()
        c = C(obj_name)
        objects_list.append(c)
    else:
        print("Wrong class entered!")

    return objects_list


def delete_object(objects_list):
    obj_name = input("Enter the object name to delete: ")

    del_flag = False
    for i in range(len(objects_list)):
        if objects_list[i].name == obj_name:
            del objects_list[i]
            del_flag = True
            break

    if del_flag:
        print("Object deleted successfully!")
    else:
        print("No Object found with this name!")

    return objects_list


def execute_object(objects_list):
    obj_name = input("Enter the object name to execute: ")
    exe_flag = False
    for i in range(len(objects_list)):
        if objects_list[i].name == obj_name:
            num_params = int(input("Enter the number of parameters to pass: "))
            params = {}
            param_counter = 1
            while param_counter <= num_params:
                param_x = input("Enter the parameter " + str(param_counter) + " value: ")
                params['param_'+str(param_counter)] = param_x
                param_counter += 1
            objects_list[i].execute(**params)
            exe_flag = True
            break

    if exe_flag:
        print("Object executed successfully!")
    else:
        print("No Object found with this name!")

    return objects_list


def get_object_names(objects_list):
    obj_names_str = ''
    for obj in objects_list:
        obj_names_str += obj.name + ', '

    obj_names_str = "Total Objects = " + str(len(objects_list)) + ' -   ' + obj_names_str
    return obj_names_str


if __name__ == '__main__':
    choice = ''
    objects_list = []

    while choice != 'q':
        print("1. Create Object")
        print("2. Delete Object")
        print("3. Execute Object")
        print("4. View all Objects")
        print("q. Quit")

        choice = input()

        if choice == 'q':
            break

        if choice == '1':
            objects_list = create_object(objects_list)
        elif choice == '2':
            objects_list = delete_object(objects_list)
        elif choice == '3':
            objects_list = execute_object(objects_list)
        elif choice == '4':
            obj_names_str = get_object_names(objects_list)
            print(obj_names_str)
